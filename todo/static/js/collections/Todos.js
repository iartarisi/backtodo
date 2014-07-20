define(['backbone', 'models/Todo'],
  function(Backbone, Todo) {
    var TodoCol = Backbone.Collection.extend({
      url: '/todos',
      model: Todo
    });
    var Todos = new TodoCol();
    return Todos;
});