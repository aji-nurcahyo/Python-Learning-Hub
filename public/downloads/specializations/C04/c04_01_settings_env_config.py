from dataclasses import dataclass


@dataclass(frozen=True)
class AppSettings:
    app_env: str
    api_secret: str
    token_ttl_seconds: int = 3600
    debug: bool = False

    @classmethod
    def from_mapping(cls, env: dict[str, str]) -> "AppSettings":
        app_env = env.get("APP_ENV", "development").strip().lower()
        secret = env.get("API_SECRET", "").strip()
        if len(secret) < 16:
            raise ValueError("API_SECRET wajib disediakan minimal 16 karakter.")
        ttl = int(env.get("TOKEN_TTL_SECONDS", "3600"))
        debug = env.get("APP_DEBUG", "false").lower() == "true"
        return cls(app_env=app_env, api_secret=secret, token_ttl_seconds=ttl, debug=debug)


simulated_env = {
    "APP_ENV": "staging",
    "API_SECRET": "local-dev-signing-key-999",
    "TOKEN_TTL_SECONDS": "1800",
    "APP_DEBUG": "false",
}
cfg = AppSettings.from_mapping(simulated_env)
print("Env aktif      :", cfg.app_env)
print("Token TTL (det):", cfg.token_ttl_seconds)
print("Panjang secret :", len(cfg.api_secret), "karakter (nilai dirahasiakan)")
