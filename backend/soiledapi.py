from flask import Flask, abort, request
from flask_restful import Api, Resource, reqparse
import json
# determines soil temp, current weather, future percipitation, and then returns it
import get_data
app = Flask(__name__)
api = Api(app)

class soiledApi(Resource):
    class get(self):
        help(len)