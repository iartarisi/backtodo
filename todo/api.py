from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

todos = {'1': 'foo'}


class ToDo(restful.Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}


api.add_resource(ToDo, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
