import tempfile
from pathlib import Path
from typing import Generator

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.testclient import TestClient
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


class Base(DeclarativeBase):
    pass


class RouterAsset(Base):
    __tablename__ = "router_assets"
    id: Mapped[int] = mapped_column(primary_key=True)
    hostname: Mapped[str] = mapped_column(String(40), unique=True)
    site: Mapped[str] = mapped_column(String(40))


class AssetIn(BaseModel):
    hostname: str = Field(min_length=3)
    site: str = Field(min_length=2)


class AssetOut(AssetIn):
    id: int
    model_config = ConfigDict(from_attributes=True)


def create_db_app(db_url: str):
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    Base.metadata.create_all(engine)

    def get_db() -> Generator[Session, None, None]:
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    app = FastAPI(title="Persistent Assets API")

    @app.post("/assets", response_model=AssetOut, status_code=status.HTTP_201_CREATED)
    def create_asset(payload: AssetIn, db: Session = Depends(get_db)) -> RouterAsset:
        existing = db.scalars(select(RouterAsset).where(RouterAsset.hostname == payload.hostname)).first()
        if existing:
            raise HTTPException(status_code=409, detail="Hostname sudah terdaftar")
        record = RouterAsset(**payload.model_dump())
        db.add(record)
        db.commit()
        db.refresh(record)
        return record

    @app.get("/assets", response_model=list[AssetOut])
    def list_assets(db: Session = Depends(get_db)) -> list[RouterAsset]:
        return list(db.scalars(select(RouterAsset).order_by(RouterAsset.id)).all())

    return app, engine


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp_dir:
        app, engine = create_db_app(f"sqlite:///{Path(tmp_dir) / 'app.db'}")
        try:
            client = TestClient(app)
            r1 = client.post("/assets", json={"hostname": "ITERA-CORE-01", "site": "Lampung"})
            r_dup = client.post("/assets", json={"hostname": "ITERA-CORE-01", "site": "Lampung"})
            r_list = client.get("/assets")
            print("POST baru   :", r1.status_code, r1.json())
            print("POST duplikat:", r_dup.status_code, r_dup.json())
            print("GET list    :", r_list.status_code, r_list.json())
        finally:
            engine.dispose()
