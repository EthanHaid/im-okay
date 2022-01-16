from os import environ


class _BaseConfig:
    TWILIO_ACCOUNT_SID: str = "ACfa91146369a012b0e912cd3719cb04d8"
    TWILIO_AUTH_TOKEN: str = "bbf8c32367b2783e998dc080fe5926f7"
    TWILIO_PHONE_NUMBER: str = "+19377644868"
    FRONTEND_URL: str = "https://imokay.tech/"

    def __init__(self):
        self._load_environment_variables()

    def _load_environment_variables(self):
        [
            setattr(self, k, environ.get(k, v))
            for k, v in vars(_BaseConfig).items()
            if not k.startswith("__")
        ]


config = _BaseConfig()
