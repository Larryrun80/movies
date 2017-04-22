from pymongo import MongoClient

from ... import app
from .error import AppError


class Mongo():
    def __init__(self, mongo_tag=''):
        if not isinstance(mongo_tag, str):
            raise AppError('TYPE_ERROR', param='mongo_tag', expect_type='str')

        params = {
            'host': '',
            'port': 27017,
            'user': '',
            'password': '',
            'database': '',
        }
        db_str = ''
        prefix = 'MONGO_'

        if mongo_tag != '':
            prefix += mongo_tag + '_'

        for param in params.keys():
            params[param] = app.config.get(
                '{}{}'.format(prefix.upper(), param.upper()), params[param])

        for param in ('host', 'database'):  # host and database is necessary
            if params[param] == '':
                raise AppError(
                    'DB_INIT_ERROR',
                    reason='param {} not found in settings'
                    ''.format(prefix.upper()+param.upper()))

        if params['user'] == '':  # login without auth
            db_str = 'mongodb://{}:{}/{}'.format(params['host'],
                                                 params['port'],
                                                 params['database'])
        else:
            db_str = 'mongodb://{}:{}@{}:{}/{}'.format(params['user'],
                                                       params['password'],
                                                       params['host'],
                                                       params['port'],
                                                       params['database'])

        self.database = params['database']
        self.mongo_cnx = MongoClient(db_str)

    def get_collection(self, coll_name):
        return self.mongo_cnx[self.database][coll_name]

    def __del__(self):
        self.mongo_cnx.close()
