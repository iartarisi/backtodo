define(['backbone', 'collections/Todos', 'views/Todo'],
  function(Backbone, Todos, TodoView) {
    var TodoList = Backbone.View.extend({
      el: '#todo-tbody',
      initialize: function() {
        this.listenTo(Todos, 'add', this.addOne);
        Todos.fetch();
      },
      addOne: function(todo) {
        var view = new TodoView({model: todo});
        this.$el.append(view.render().el);
      }
    });
    return TodoList;
});