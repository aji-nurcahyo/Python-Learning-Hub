import tempfile
from pathlib import Path
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


class Base(DeclarativeBase):
    pass


class TelemetryNode(Base):
    __tablename__ = "telemetry_nodes"

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(24), unique=True, index=True)
    region: Mapped[str] = mapped_column(String(32))
    status: Mapped[str] = mapped_column(String(20), default="online")


class NodeRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(self, node_id: int) -> TelemetryNode | None:
        return self.db.get(TelemetryNode, node_id)

    def get_by_code(self, code: str) -> TelemetryNode | None:
        return self.db.scalars(select(TelemetryNode).where(TelemetryNode.code == code)).first()

    def list_all(self, region: str | None = None) -> list[TelemetryNode]:
        stmt = select(TelemetryNode).order_by(TelemetryNode.id)
        if region:
            stmt = stmt.where(TelemetryNode.region == region)
        return list(self.db.scalars(stmt).all())

    def create(self, code: str, region: str, status: str) -> TelemetryNode:
        node = TelemetryNode(code=code, region=region, status=status)
        self.db.add(node)
        self.db.commit()
        self.db.refresh(node)
        return node

    def update(self, node: TelemetryNode, region: str, status: str) -> TelemetryNode:
        node.region = region
        node.status = status
        self.db.commit()
        self.db.refresh(node)
        return node

    def delete(self, node: TelemetryNode) -> None:
        self.db.delete(node)
        self.db.commit()


def init_db_factory(db_url: str):
    engine = create_engine(db_url, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    return engine, sessionmaker(bind=engine, autoflush=False, autocommit=False)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as td:
        engine, SessionLocal = init_db_factory(f"sqlite:///{Path(td) / 'repo_demo.db'}")
        try:
            with SessionLocal() as db:
                repo = NodeRepository(db)
                created = repo.create("LPG-01", "Sumatera", "online")
                print("Created node via Repository:", (created.id, created.code, created.status))
        finally:
            engine.dispose()
