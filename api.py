from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


todos = {}


class TdoSimple(Resource):
    def get(self, todo_id):
        # return {todo_id: todos[todo_id]}
        return {todo_id: todos.get(todo_id)}

    def put(self, todo_id):
        todos[todo_id] = request.form["data"]
        return {todo_id: todos.get(todo_id)}

api.add_resource(HelloWorld, "/")


if __name__ == "__main__":
    # access api by
    # localhost:5000
    # e.g. curl http://localhost:5000
    app.run(debug=True)