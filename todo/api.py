from flask import Flask, request
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)


class Store(dict):
    """In-memory dictionary wrapper store for ToDo items"""
    def __setitem__(self, name, value):
        if 'checked' not in value:
            value.update(checked=False)

        super().__setitem__(name, value)

    def __getitem__(self, name):
        try:
            return super().__getitem__(name)
        except KeyError:
            restful.abort(404, message="Todo {} does not exist!".format(name))

todos = Store()
todos['1'] = {'task': 'foo'}


class ToDo(restful.Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = {'task': request.form['data']}
        return {todo_id: todos[todo_id]}


api.add_resource(ToDo, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
