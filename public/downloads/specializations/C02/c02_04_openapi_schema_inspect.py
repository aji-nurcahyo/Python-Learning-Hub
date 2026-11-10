from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Telecom Device Catalog", version="2.0.0")


class DeviceSchema(BaseModel):
    hostname: str
    uptime_hours: int


@app.post("/devices", response_model=DeviceSchema, tags=["Devices"])
def register_device(device: DeviceSchema) -> DeviceSchema:
    return device


schema = app.openapi()
print("OpenAPI Title   :", schema["info"]["title"])
print("OpenAPI Version :", schema["info"]["version"])
print("Registered Paths:", list(schema["paths"].keys()))
print("Schemas Listed  :", sorted(schema["components"]["schemas"].keys()))
