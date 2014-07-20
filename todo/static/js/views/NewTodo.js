define(['backbone', 'models/Todo', 'views/TodoList'],
  function(Backbone, Todo, TodoList) {
    var NewTodo = Backbone.View.extend({
      el: '#new-task',
      events: {
        'submit #new-task-form': 'createTodo'
      },
      createTodo: function (ev) {
        var newTask = {task: $('#new-task-input').val()};

        var todo = new Todo();
        todo.save(newTask, {
          success: function (todo) {
            $('#new-task-input').val('');
            var todoList = new TodoList();
            todoList.render();
          }
        });
        return false;
      }
    });
    return NewTodo;
});