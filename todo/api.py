from flask import Flask, request
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)


class Store(dict):
    """In-memory dictionary wrapper store for ToDo items"""
    def index(self):
        """Returns a list of all the todo items as a list of dicts"""
        return [{'order': order,
                 'checked': todo['checked'],
                 'task': todo['task']}
                for order, todo in self.items()]

    def append(self, task):
        """Add a new ToDO item to the list

        :task: a string name/description of a task

        A new ToDo item will be created. It will be unchecked by default
        ('checked': False) and will have a generated task_id.

        """
        todo_id = self._next()
        self.__setitem__(todo_id, {'checked': False, 'task': task})
        return todo_id

    def _next(self):
        """Returns an unused task_id as a string"""
        if self.keys():
            return str(int(max(self.keys())) + 1)
        else:
            return '1'

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
todos.update({
    '1': {'task': 'Discuss report with John', 'checked': False},
    '2': {'task': 'Get a haircut', 'checked': True},
    '3': {'task': 'Pay electricity bill', 'checked': True},
    '4': {'task': 'Check gym hours', 'checked': False}
})

@app.route('/')
def root():
    return app.send_static_file('index.html')

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


class ToDoList(restful.Resource):
    def get(self):
        return todos.index()

    def post(self):
        todo_id = todos.append(request.form.get('task'))
        return {todo_id: todos[todo_id]}, 201

api.add_resource(ToDoList, '/todos/')
api.add_resource(ToDo, '/todos/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)
