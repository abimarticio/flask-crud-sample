from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


todos = {}


class TdoSimple(Resource):
    def get(self):
        return {"Hello": "World"}

api.add_resource(HelloWorld, "/")


if __name__ == "__main__":
    # access api by
    # localhost:5000
    # e.g. curl http://localhost:5000
    app.run(debug=True)