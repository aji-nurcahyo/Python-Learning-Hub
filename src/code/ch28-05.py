"""Chapter 28 Example 05: HTTP Status Codes & Error Handling
Python Learning Hub - Professional Python Engineering
"""


class HttpError(Exception):
    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(f"HTTP {status_code}: {message}")
        self.status_code = status_code


def handle_http_response(status_code: int) -> str:
    """Memetakan kode status HTTP ke tindakan yang sesuai."""
    if 200 <= status_code < 300:
        return f"OK ({status_code}): Permintaan sukses diproses"
    elif status_code == 400:
        raise HttpError(400, "Bad Request - Format parameter salah")
    elif status_code == 401:
        raise HttpError(401, "Unauthorized - Token autentikasi hilang atau kedaluwarsa")
    elif status_code == 404:
        raise HttpError(404, "Not Found - Sumber daya tidak ditemukan")
    elif status_code == 429:
        raise HttpError(429, "Too Many Requests - Melebihi kuota rate limit")
    elif 500 <= status_code < 600:
        raise HttpError(status_code, "Internal Server Error - Kegagalan pada server remote")
    else:
        raise HttpError(status_code, "Unhandled Status Code")


def main() -> None:
    test_codes = [200, 201, 401, 404, 500]
    print("Pengujian Pemetaan Status Code HTTP:")
    for code in test_codes:
        try:
            res = handle_http_response(code)
            print(f" -> {code}: {res}")
        except HttpError as err:
            print(f" -> {code}: Tertangkap HttpError -> {err}")


if __name__ == "__main__":
    main()
