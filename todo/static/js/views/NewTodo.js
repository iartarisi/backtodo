define(['backbone', 'collections/Todos'],
  function(Backbone, Todos) {
    var NewTodo = Backbone.View.extend({
      el: '#new-task',
      events: {
        'submit #new-task-form': 'createTodo'
      },
      createTodo: function (ev) {
        var newTask = {task: $('#new-task-input').val()};
        Todos.create(newTask);
        $('#new-task-input').val('');

        return false;
      }
    });
    return NewTodo;
});