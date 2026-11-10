from dataclasses import dataclass
from pydantic import BaseModel, ConfigDict, Field


@dataclass(frozen=True)
class ServiceConfig:
    service_name: str
    db_url: str
    api_secret: str


class NodeCreate(BaseModel):
    code: str = Field(min_length=3, max_length=24)
    region: str = Field(min_length=2, max_length=32)
    status: str = Field(default="online", pattern="^(online|maintenance|offline)$")


class NodeUpdate(BaseModel):
    region: str = Field(min_length=2, max_length=32)
    status: str = Field(pattern="^(online|maintenance|offline)$")


class NodeOut(NodeCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


if __name__ == "__main__":
    sample = NodeCreate(code="NODE-ITERA-01", region="Sumatera", status="online")
    print("Schema NodeCreate valid :", sample.model_dump())
    cfg = ServiceConfig("telemetry-api", "sqlite:///local.db", "demo-service-secret-1234")
    print("ServiceConfig siap      :", cfg.service_name)
