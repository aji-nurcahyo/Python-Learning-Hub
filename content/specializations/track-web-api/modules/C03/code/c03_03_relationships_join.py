import tempfile
from pathlib import Path
from sqlalchemy import ForeignKey, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Region(Base):
    __tablename__ = "regions"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=True)
    nodes: Mapped[list["Node"]] = relationship(back_populates="region")


class Node(Base):
    __tablename__ = "nodes"
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(20), unique=True)
    region_id: Mapped[int] = mapped_column(ForeignKey("regions.id"))
    region: Mapped[Region] = relationship(back_populates="nodes")


with tempfile.TemporaryDirectory() as tmp_dir:
    engine = create_engine(f"sqlite:///{Path(tmp_dir) / 'rel.db'}")
    try:
        Base.metadata.create_all(engine)
        with Session(engine) as session:
            sumatera = Region(name="Sumatera")
            jawa = Region(name="Jawa")
            sumatera.nodes.extend([Node(code="LPG-01"), Node(code="PLG-02")])
            jawa.nodes.append(Node(code="BDG-01"))
            session.add_all([sumatera, jawa])
            session.commit()

            rows = session.scalars(select(Node).join(Node.region).where(Region.name == "Sumatera")).all()
            print("Node di Region Sumatera:", [n.code for n in rows])
    finally:
        engine.dispose()

