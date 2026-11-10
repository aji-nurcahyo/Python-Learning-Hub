import base64
import hashlib
import hmac
import json
import secrets


def hash_password(password: str, salt: str | None = None) -> str:
    salt_val = salt or secrets.token_hex(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt_val.encode("utf-8"), 100_000)
    return f"pbkdf2_sha256${salt_val}${dk.hex()}"


def verify_password(password: str, stored_hash: str) -> bool:
    _, salt_val, expected_hex = stored_hash.split("$")
    recomputed = hash_password(password, salt=salt_val).split("$")[2]
    return hmac.compare_digest(expected_hex, recomputed)


def create_signed_token(subject: str, exp_epoch: int, secret: str) -> str:
    payload = json.dumps({"sub": subject, "exp": exp_epoch}, separators=(",", ":"), sort_keys=True)
    body_b64 = base64.urlsafe_b64encode(payload.encode("utf-8")).decode("ascii").rstrip("=")
    sig = hmac.new(secret.encode("utf-8"), body_b64.encode("ascii"), hashlib.sha256).hexdigest()
    return f"{body_b64}.{sig}"


def verify_signed_token(token: str, secret: str, now_epoch: int) -> dict | None:
    if "." not in token:
        return None
    body_b64, sig = token.split(".", 1)
    expected_sig = hmac.new(secret.encode("utf-8"), body_b64.encode("ascii"), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(sig, expected_sig):
        return None
    padded = body_b64 + "=" * (-len(body_b64) % 4)
    data = json.loads(base64.urlsafe_b64decode(padded.encode("ascii")).decode("utf-8"))
    if int(data["exp"]) < now_epoch:
        return None
    return data


if __name__ == "__main__":
    stored = hash_password("SandiAman#2025", salt="fixed-demo-salt-01")
    print("Password cocok   :", verify_password("SandiAman#2025", stored))
    print("Password salah   :", verify_password("TebakanSalah", stored))

    tok = create_signed_token("operator-01", exp_epoch=2000, secret="demo-hmac-secret-key")
    print("Token valid (t=1500):", verify_signed_token(tok, "demo-hmac-secret-key", now_epoch=1500))
    print("Token kedaluwarsa   :", verify_signed_token(tok, "demo-hmac-secret-key", now_epoch=2500))
