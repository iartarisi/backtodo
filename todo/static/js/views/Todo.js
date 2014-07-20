define(['backbone', "text!templates/todo.html"],
  function(Backbone, html) {
    var TodoView = Backbone.View.extend({
      tagName: "tr",

      render: function() {
        var template = _.template(html, {todo: this.model});
        this.$el.html(template);
        return this;
      }
    });
    return TodoView;
});