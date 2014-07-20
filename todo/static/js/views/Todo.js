define(['backbone', "text!templates/todo.html"],
  function(Backbone, html) {
    var TodoView = Backbone.View.extend({
      tagName: "tr",

      initialize: function() {
        this.listenTo(this.model, 'change', this.render);
      },
      events: {
        "click input": "toggleDone"
      },
      render: function() {
        var template = _.template(html, {todo: this.model});
        this.$el.html(template);
        this.$el.toggleClass('checked', this.model.get('checked'));
        return this;
      },
      toggleDone: function() {
        this.model.toggle();
      }
    });
    return TodoView;
});