"""Chapter 28 Example 02: URL Query Parameters & Encoding
Python Learning Hub - Professional Python Engineering
"""

from urllib.parse import urlencode, urljoin


def build_api_endpoint(base_url: str, path: str, params: dict[str, str | int]) -> str:
    """Membangun URL lengkap yang aman dengan query parameters terenkodasi."""
    full_path = urljoin(base_url, path)
    encoded_query = urlencode(params)
    return f"{full_path}?{encoded_query}"


def main() -> None:
    base = "https://api.telecom.internal/"
    endpoint = "v2/bts/metrics"
    query_params = {
        "region": "Jawa Tengah & DIY",  # Karakter khusus & spasi akan di-encode otomatis
        "min_rsrp": -95,
        "limit": 50,
    }

    url = build_api_endpoint(base, endpoint, query_params)
    print("Membangun Endpoint API dengan Query Parameters:")
    print(f"URL Hasil: {url}")


if __name__ == "__main__":
    main()
