from resources.base_resource import ResourceBase
from dataclasses import dataclass
import sdk_config


@dataclass
class Book(ResourceBase):
    _id: str
    name: str

    @staticmethod
    def get_endpoint():
        '''
        Override the superclass method to return this class's specific endpoint.
        :return:
        '''
        return '/book/'

    @staticmethod
    def requires_auth():
        return False

    @classmethod
    def chapters(cls, book_id: str):
        full_path = f'{sdk_config.API_URL}{cls.get_endpoint()}/{book_id}/chapter'
        response = cls.make_request(full_path)
        return Chapter._process_response(response)

@dataclass
class Chapter(ResourceBase):
    _id: str
    chapterName: str

    @classmethod
    def list(cls):
        raise Exception("Chapters don't have lists")

    @classmethod
    def index(cls, id:str):
        raise Exception("Chapters don't have indexes")
