from resources.base_resource import ResourceBase
from dataclasses import dataclass
import sdk_config
from resources.quote import Quote


@dataclass
class Movie(ResourceBase):
    _id: str
    name: str
    runtimeInMinutes: int
    budgetInMillions: int
    boxOfficeRevenueInMillions: int
    academyAwardNominations: int
    academyAwardWins: int
    rottenTomatoesScore: int

    @staticmethod
    def get_endpoint():
        '''
        Override the superclass method to return this class's specific endpoint.
        :return:
        '''
        return '/movie/'

    @classmethod
    def quotes(cls, movie_id: str):
        full_path = f'{sdk_config.API_URL}{cls.get_endpoint()}/{movie_id}/quote'
        response = cls.make_request(full_path)
        return Quote._process_response(response)

