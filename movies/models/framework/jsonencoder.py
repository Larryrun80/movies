from bson import ObjectId
from flask import json


class FlaskJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        # override default flask json encoder if necessary
        # see example http://flask.pocoo.org/snippets/119/

        # write your code here:
        # for example:
        # if isinstance(obj, decimal.Decimal):
        #     # Convert decimal instances to strings.
        #     return str(obj)
        if isinstance(obj, ObjectId):
            return str(obj)

        return super(FlaskJSONEncoder, self).default(obj)
