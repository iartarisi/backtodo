define(['backbone'],
  function(Backbone) {
    var NewTodo = Backbone.View.extend({
      el: '#new-task',
      events: {
        'submit #new-task-form': 'createTodo'
      },
      createTodo: function (ev) {
        var newTask = {task: $('#new-task-form').val()};
        console.log(newTask);
        return false;
      }
    });
    return NewTodo;
});