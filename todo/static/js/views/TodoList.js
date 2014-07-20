define(['backbone', 'collections/Todos', 'views/Todo'],
  function(Backbone, Todos, TodoView) {
    var TodoList = Backbone.View.extend({
      el: '#content',
      initialize: function() {
        this.input = this.$("#new-task-input");
        this.tasks = this.$("#todo-tbody");
        this.listenTo(Todos, 'add', this.addOne);
        Todos.fetch();
      },
      events: {
        'submit #new-task-form': 'createTodo'
      },
      createTodo: function (ev) {
        var newTask = {task: this.input.val()};
        Todos.create(newTask);
        this.input.val('');

        return false;
      },
      addOne: function(todo) {
        var view = new TodoView({model: todo});
        this.$("#todo-tbody").append(view.render().el);
      }
    });
    return TodoList;
});