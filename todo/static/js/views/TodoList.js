define(['backbone'],
  function(Backbone) {
    var TodoList = Backbone.View.extend({
      el: '#tasks',
      render: function () {
        this.$el.html("placeholder!");
      }
    });
    return TodoList;
});