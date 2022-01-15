from os import environ


class _BaseConfig:
    YOUR_SHIT: str = "HEER"

    def __init__(self):
        self._load_environment_variables()

    def _load_environment_variables(self):
        [
            setattr(self, k, environ.get(k, v))
            for k, v in vars(_BaseConfig).items()
            if not k.startswith("__")
        ]


config = _BaseConfig()
