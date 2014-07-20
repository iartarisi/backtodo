define(['backbone'],
  function(Backbone) {
    var Todos = Backbone.Collection.extend({
      url: '/todos'
    });
    return Todos;
});