import tempfile
from pathlib import Path
from sqlalchemy import Integer, String, create_engine, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Device(Base):
    __tablename__ = "devices"

    id: Mapped[int] = mapped_column(primary_key=True)
    hostname: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    power_watt: Mapped[int] = mapped_column(Integer, default=15)


with tempfile.TemporaryDirectory() as tmp_dir:
    db_file = Path(tmp_dir) / "c03_schema.db"
    engine = create_engine(f"sqlite:///{db_file}", connect_args={"check_same_thread": False})
    try:
        Base.metadata.create_all(engine)
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        cols = [c["name"] for c in inspector.get_columns("devices")]
        print("Tabel terbentuk :", tables)
        print("Kolom devices   :", cols)
    finally:
        engine.dispose()
