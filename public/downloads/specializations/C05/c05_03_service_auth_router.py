import hashlib
import hmac
import sys
from pathlib import Path
from typing import Callable, Generator

from fastapi import APIRouter, Depends, Header, HTTPException, Response, status
from sqlalchemy.orm import Session

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from c05_01_domain_schemas import NodeCreate, NodeOut, NodeUpdate
from c05_02_repository_db import NodeRepository


def make_hmac_token(subject: str, api_secret: str) -> str:
    sig = hmac.new(api_secret.encode("utf-8"), subject.encode("utf-8"), hashlib.sha256).hexdigest()
    return f"{subject}.{sig}"


def verify_hmac_token(token: str, api_secret: str) -> str | None:
    if "." not in token:
        return None
    subject, sig = token.split(".", 1)
    expected = hmac.new(api_secret.encode("utf-8"), subject.encode("utf-8"), hashlib.sha256).hexdigest()
    return subject if hmac.compare_digest(sig, expected) else None


def build_nodes_router(
    get_db_dep: Callable[[], Generator[Session, None, None]],
    api_secret: str,
) -> APIRouter:
    router = APIRouter(prefix="/api/v1/nodes", tags=["Telemetry Nodes"])

    def require_auth(authorization: str | None = Header(default=None)) -> str:
        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Autentikasi Bearer diperlukan",
                headers={"WWW-Authenticate": "Bearer"},
            )
        subject = verify_hmac_token(authorization.removeprefix("Bearer ").strip(), api_secret)
        if not subject:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token tidak valid")
        return subject

    @router.post("", response_model=NodeOut, status_code=status.HTTP_201_CREATED)
    def create_node(
        payload: NodeCreate,
        db: Session = Depends(get_db_dep),
        _actor: str = Depends(require_auth),
    ):
        repo = NodeRepository(db)
        if repo.get_by_code(payload.code):
            raise HTTPException(status_code=409, detail="Kode node sudah terdaftar")
        return repo.create(payload.code, payload.region, payload.status)

    @router.get("", response_model=list[NodeOut])
    def list_nodes(region: str | None = None, db: Session = Depends(get_db_dep)):
        return NodeRepository(db).list_all(region=region)

    @router.put("/{node_id}", response_model=NodeOut)
    def update_node(
        node_id: int,
        payload: NodeUpdate,
        db: Session = Depends(get_db_dep),
        _actor: str = Depends(require_auth),
    ):
        repo = NodeRepository(db)
        node = repo.get_by_id(node_id)
        if not node:
            raise HTTPException(status_code=404, detail="Node tidak ditemukan")
        return repo.update(node, payload.region, payload.status)

    @router.delete("/{node_id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_node(
        node_id: int,
        db: Session = Depends(get_db_dep),
        _actor: str = Depends(require_auth),
    ) -> Response:
        repo = NodeRepository(db)
        node = repo.get_by_id(node_id)
        if not node:
            raise HTTPException(status_code=404, detail="Node tidak ditemukan")
        repo.delete(node)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return router


if __name__ == "__main__":
    tok = make_hmac_token("service-admin", "demo-capstone-secret-key-01")
    print("Subjek terverifikasi:", verify_hmac_token(tok, "demo-capstone-secret-key-01"))
