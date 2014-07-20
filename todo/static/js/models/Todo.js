define(['backbone'],
  function(Backbone) {
    var Todo = Backbone.Model.extend({
      urlRoot: '/todos'
    });
    return Todo;
});