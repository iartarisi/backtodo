define(['backbone', 'collections/Todos'],
  function(Backbone, Todos) {
    var TodoList = Backbone.View.extend({
      el: '#tasks',
      render: function () {
        var that = this;
        var todos = new Todos();
        todos.fetch({
          success: function () {
            that.$el.html("placeholder!");
          }
        });
      }
    });
    return TodoList;
});