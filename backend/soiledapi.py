# soiled
# Created by Skylar McDermott
#############################

from flask import Flask, abort, request
from flask_restful import Api, Resource, reqparse
import json
# determines soil temp, current weather, future percipitation, and then returns it
import get_data

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument("update", type=str)

# api should only be accessible to localhost
@app.before_request
def block():
    if request.remote_addr != "127.0.0.1":
        abort(403)


class soiledApi(Resource):
    def get(self):
        args = parser.parse_args()
        if args['update'] == 'true':
            return get_data.reader().parse(up="true")
        else:
            return get_data.reader().parse()

    
api.add_resource(soiledApi, "/api")
if __name__ == "__main__":
    pass
    app.run(debug=True)
