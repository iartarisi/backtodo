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

todos = Store()
todos['1'] = {'text': 'foo'}


class ToDo(restful.Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = {'text': request.form['data']}
        return {todo_id: todos[todo_id]}


api.add_resource(ToDo, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
