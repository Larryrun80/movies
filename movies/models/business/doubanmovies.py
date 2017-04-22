from ..framework.mongo import Mongo


class DoubanMovies():
    """docstring for DoubanMovies"""

    def __init__(self):
        self.source = Mongo()

    def get_movie_by_id(self, movie_id):
        collection = self.source.get_collection('films')
        return collection.find_one({'id': movie_id})
