"""Starter code Tugas C03: REST API Inventaris Persisten SQLAlchemy 2.0."""

from __future__ import annotations

from fastapi import FastAPI
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class LocationModel(Base):
    __tablename__ = "locations"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    assets: Mapped[list["AssetModel"]] = relationship(back_populates="location")


class AssetModel(Base):
    __tablename__ = "assets"
    id: Mapped[int] = mapped_column(primary_key=True)
    hostname: Mapped[str] = mapped_column(String(50), unique=True)
    status: Mapped[str] = mapped_column(String(20), default="active")
    location_id: Mapped[int] = mapped_column(ForeignKey("locations.id"))
    location: Mapped[LocationModel] = relationship(back_populates="assets")


def build_db_app(db_url: str) -> tuple[FastAPI, object]:
    """Membuat aplikasi FastAPI + SQLAlchemy engine dan SessionLocal dependency."""
    # TODO: Buat engine, SessionLocal, get_db generator, dan endpoint CRUD /locations & /assets
    raise NotImplementedError("Implementasikan build_db_app")


if __name__ == "__main__":
    print("Starter C03 siap diuji dengan SQLite temp DB dan FastAPI TestClient.")

