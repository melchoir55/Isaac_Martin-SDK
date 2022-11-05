import requests
import sdk_config


class ResourceBase:
    endpoint: str
    auth_header = True
    default_headers = {'Content-Type': 'application/json'}

    def build_auth_header(self):
        return {'Authorization': f'Bearer {sdk_config.AUTHENTICATION_TOKEN}'}

    def list(self):
        full_path = f'{sdk_config.API_URL}{self.endpoint}'
        if self.auth_header:
            response = requests.get(full_path, headers=self.default_headers | self.build_auth_header())
        else:
            response = requests.get(full_path, headers=self.default_headers)

        if response.ok:
            return response
        else:
            raise Exception(f'{response.status_code}: {response.content}')
