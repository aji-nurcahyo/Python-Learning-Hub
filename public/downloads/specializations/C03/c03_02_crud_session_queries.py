import tempfile
from pathlib import Path
from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Sensor(Base):
    __tablename__ = "sensors"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(20), unique=True)
    status: Mapped[str] = mapped_column(String(20), default="active")


with tempfile.TemporaryDirectory() as tmp_dir:
    engine = create_engine(f"sqlite:///{Path(tmp_dir) / 'crud.db'}")
    try:
        Base.metadata.create_all(engine)
        with Session(engine) as session:
            session.add_all([Sensor(code="S-01"), Sensor(code="S-02", status="standby")])
            session.commit()

            # Update S-02 -> active
            target = session.scalars(select(Sensor).where(Sensor.code == "S-02")).one()
            target.status = "active"
            session.commit()

            # Delete S-01
            to_del = session.scalars(select(Sensor).where(Sensor.code == "S-01")).one()
            session.delete(to_del)
            session.commit()

            remaining = session.scalars(select(Sensor)).all()
            print("Sensor tersisa:", [(s.code, s.status) for s in remaining])
    finally:
        engine.dispose()
