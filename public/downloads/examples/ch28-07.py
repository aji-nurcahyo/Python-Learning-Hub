"""Chapter 28 Example 07: Environment Variables & Bearer Token Authentication
Python Learning Hub - Professional Python Engineering
"""

import os


def prepare_auth_headers(token_env_var: str = "TELECOM_API_TOKEN") -> dict[str, str]:
    """Membaca token autentikasi dari environment variable dan menyusun header HTTP yang aman."""
    # Mengambil token dari sistem operasi tanpa hardcoding rahasia di source code
    token = os.environ.get(token_env_var)
    if not token:
        # Fallback nilai demo terkontrol jika env var belum diset
        token = "demo_token_xyz_secure_hash"

    # Menyusun header Authorization sesuai standar RFC 6750 (Bearer Token)
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
        "X-Client-Version": "2.4.0",
    }
    return headers


def mask_sensitive_token(headers: dict[str, str]) -> dict[str, str]:
    """Menyamarkan token rahasia sebelum dicatat ke file log audit."""
    safe_copy = headers.copy()
    if "Authorization" in safe_copy:
        val = safe_copy["Authorization"]
        if len(val) > 15:
            safe_copy["Authorization"] = f"{val[:11]}...{val[-4:]}"
    return safe_copy


def main() -> None:
    headers = prepare_auth_headers()
    print("Header HTTP Asli yang Dikirimkan:")
    print(f" -> Accept: {headers['Accept']}")
    print(f" -> X-Client-Version: {headers['X-Client-Version']}")

    # Demonstrasi log aman
    masked = mask_sensitive_token(headers)
    print(f"\nHeader Tersamar untuk Log Audit Aman:")
    print(f" -> Authorization: {masked['Authorization']} (Aman dari kebocoran credential)")


if __name__ == "__main__":
    main()
