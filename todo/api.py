from flask import Flask, request
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)


class Store(dict):
    """In-memory dictionary wrapper store for ToDo items"""
    def __setitem__(self, task_id, value):
        """Create or update a Todo Task

        :task_id: the id of an existing task or a new one
        :value: a dictionary with the following items:
           - checked(required) - the boolean status of a task
           - task - a string name/description of a task. Only required
             for new tasks (will raise a 404 if missing)

        """
        if 'task' not in value or not value['task']:
            if task_id not in self:
                restful.abort(404, message="Task {} does not exist! "
                              "Can not check it off.".format(task_id))
            else:
                value['task'] = self[task_id]['task']
        super().__setitem__(task_id, value)

    def __getitem__(self, name):
        try:
            return super().__getitem__(name)
        except KeyError:
            restful.abort(404, message="Todo {} does not exist!".format(name))

    def __delitem__(self, task_id):
        try:
            return super().__delitem__(task_id)
        except KeyError:
            restful.abort(404, message="Could not delete task {}. "
                          "It does not exist.".format(task_id))

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

    def delete(self, todo_id):
        del todos[todo_id]
        return '', 204

api.add_resource(ToDo, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
