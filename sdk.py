import sdk_config


class TheOneSDK:
    def __init__(self, url: str, authentication_token: str):
        sdk_config.API_URL = url
        sdk_config.AUTHENTICATION_TOKEN = authentication_token
