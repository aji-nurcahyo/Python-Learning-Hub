"""Starter code Capstone C05: Production-Ready Telemetry Nodes Microservice."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field


class NodeCreate(BaseModel):
    code: str = Field(min_length=3, max_length=24)
    region: str = Field(min_length=2, max_length=32)
    status: str = Field(default="online", pattern="^(online|maintenance|offline)$")


class NodeOut(NodeCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


def create_microservice_app(db_url: str, api_secret: str) -> tuple[FastAPI, object]:
    """Merakit aplikasi FastAPI modular dengan SQLAlchemy repository, auth guard, dan middleware."""
    # TODO: Implementasikan engine/SessionLocal, NodeRepository, APIRouter, dan timing middleware
    raise NotImplementedError("Implementasikan create_microservice_app")


if __name__ == "__main__":
    print("Starter Capstone C05 siap diuji via TestClient dan pytest.")

