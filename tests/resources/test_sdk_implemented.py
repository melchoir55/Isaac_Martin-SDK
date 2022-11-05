from isaac_martin_sdk.resources.book import ResourceBase
import unittest
from isaac_martin_sdk.resources.base_resource import SDKNotImplemented, AuthTokenNotProvided
import isaac_martin_sdk

class TestForgotToInstantiateSdk(unittest.TestCase):
    def test_forget_to_instantiate_sdk_with_token(self):
        full_path = 'https://the-one-api.dev/v2/movie/'
        isaac_martin_sdk.sdk_config.AUTHENTICATION_TOKEN = None
        ResourceBase.requires_auth = lambda: True
        with self.assertRaises(AuthTokenNotProvided) as context:
            ResourceBase.make_request(full_path)

    def test_forget_to_instantiate_sdk(self):
        full_path = 'None/v2/movie/'
        ResourceBase.requires_auth = lambda: True
        with self.assertRaises(SDKNotImplemented) as context:
            ResourceBase.make_request(full_path)










