from isaac_martin_sdk.sdk import TheOneSDK
import unittest


class TestTheOneSDK(unittest.TestCase):
    def test_initialization(self):
        url = 'https://the-one-api.dev/v2'
        token = 'One ring to rule them all, one ring to find them, One ring to bring them all, and in the darkness bind them; In the Land of Mordor where the shadows lie.'
        TheOneSDK(url=url, authentication_token=token)

        from isaac_martin_sdk.sdk_config import API_URL
        self.assertEquals(url, API_URL)

        from isaac_martin_sdk.sdk_config import AUTHENTICATION_TOKEN
        self.assertEquals(token, AUTHENTICATION_TOKEN)

