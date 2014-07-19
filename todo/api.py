from flask import Flask, request
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)


class Store(dict):
    """In-memory dictionary wrapper store for ToDo items"""
    def __setitem__(self, name, value):
        if 'task' not in value or not value['task']:
            if name not in self:
                restful.abort(404, message="Task {} does not exist! "
                              "Can not check it off.".format(name))
            else:
                value['task'] = self[name]['task']
        super().__setitem__(name, value)

    def __getitem__(self, name):
        try:
            return super().__getitem__(name)
        except KeyError:
            restful.abort(404, message="Todo {} does not exist!".format(name))

todos = Store()


class ToDo(restful.Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = {
            'task': request.form.get('task'),
            'checked': request.form.get('checked', False)
        }
        return {todo_id: todos[todo_id]}


api.add_resource(ToDo, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
