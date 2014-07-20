define(['backbone', 'models/Todo'],
  function(Backbone, Todo) {
    var TodoCol = Backbone.Collection.extend({
      url: '/todos',
      model: Todo,
      comparator: 'id',
      remaining: function() {
        return this.filter(
          function(todo) {
            return todo.attributes['checked'] != true;
          });
      }
    });
    var Todos = new TodoCol();
    return Todos;
});