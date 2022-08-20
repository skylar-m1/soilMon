from flask import Flask, abort, request
from flask_restful import Api, Resource, reqparse
import json
# determines soil temp, current weather, future percipitation, and then returns it
import get_data
app = Flask(__name__)
api = Api(app)

# get data will create dict
class soiledApi(Resource):
    def get(self):
        return get_data.parse().json()
    
if __name__ == "__main__":
    api.add_resource(soiledApi)