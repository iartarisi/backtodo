define(['backbone', 'collections/Todos', 'text!templates/todolist.html'],
  function(Backbone, Todos, html) {
    var TodoList = Backbone.View.extend({
      el: '#tasks',
      render: function () {
        var that = this;
        var todos = new Todos();
        todos.fetch({
          success: function () {
            var template = _.template(html, {todos: todos.models});
            that.$el.html(template);
          }
        });
      }
    });
    return TodoList;
});