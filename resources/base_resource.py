import dataclasses

import requests
import sdk_config
from dataclasses_json import dataclass_json
import json


@dataclass_json
@dataclasses.dataclass
class ResourceBase:
    _default_headers = {'Content-Type': 'application/json'}

    @staticmethod
    def get_endpoint():
        raise Exception('Implement Me')

    @staticmethod
    def requires_auth():
        return True

    @classmethod
    def _process_response(cls, response: requests.Response):
        if not response.ok:
            raise Exception(f'{response.status_code}: {response.content}')

        loaded = []
        content = json.loads(response.content)
        for obj in content['docs']:
            loaded.append(cls.from_dict(obj))
        return loaded


    @staticmethod
    def _build_auth_header():
        return {'Authorization': f'Bearer {sdk_config.AUTHENTICATION_TOKEN}'}

    @classmethod
    def make_request(cls, full_path:str):
        if cls.requires_auth():
            response = requests.get(full_path, headers=cls._default_headers | cls._build_auth_header())
        else:
            response = requests.get(full_path, headers=cls._default_headers)
        return response

    @classmethod
    def list(cls):
        full_path = f'{sdk_config.API_URL}{cls.get_endpoint()}'
        response = cls.make_request(full_path)
        return cls._process_response(response)

    @classmethod
    def index(cls, id:str):
        full_path = f'{sdk_config.API_URL}{cls.get_endpoint()}/{id}'
        response = cls.make_request(full_path)
        return cls._process_response(response)[0]