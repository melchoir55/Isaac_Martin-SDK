from resources.base_resource import ResourceBase
from dataclasses import dataclass
import sdk_config


@dataclass
class Quote(ResourceBase):
    _id: str
    dialog: str
    movie: str
    character: str

    @staticmethod
    def get_endpoint():
        '''
        Override the superclass method to return this class's specific endpoint.
        :return:
        '''
        return '/quote/'
