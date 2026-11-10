from pydantic import BaseModel, Field, ValidationError


class TelemetryReading(BaseModel):
    device_id: str = Field(min_length=3)
    temp_c: float = Field(ge=-40.0, le=120.0)
    battery_pct: int = Field(ge=0, le=100)


valid_payload = {"device_id": "NODE-01", "temp_c": 31.5, "battery_pct": 88}
record = TelemetryReading.model_validate(valid_payload)
print("Model tervalidasi :", record.model_dump())

invalid_payload = {"device_id": "X", "temp_c": 250.0, "battery_pct": 110}
try:
    TelemetryReading.model_validate(invalid_payload)
except ValidationError as exc:
    print("Jumlah error validasi tertangkap:", len(exc.errors()))
    for err in exc.errors():
        print(f" - field={err['loc'][0]}: {err['msg']}")

