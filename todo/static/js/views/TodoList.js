define(['backbone',
        'collections/Todos',
        'views/Todo',
        'text!templates/footer.html'],
  function(Backbone, Todos, TodoView, footer_temp) {
    var TodoList = Backbone.View.extend({
      el: '#content',
      initialize: function() {
        this.input = this.$("#new-task-input");
        this.tasks = this.$("#todo-tbody");
        this.footer = this.$("#footer");

        this.listenTo(Todos, 'add', this.addOne);
        this.listenTo(Todos, 'all', this.render);

        Todos.fetch();
      },
      events: {
        'click #mark-all': 'markAllComplete',
        'submit #new-task-form': 'createTodo'
      },
      render: function() {
        var remaining = Todos.remaining().length;
        this.footer.html(_.template(footer_temp, {remaining: remaining}));
      },
      createTodo: function (ev) {
        Todos.create({task: this.input.val()});
        this.input.val('');

        return false;
      },
      addOne: function(todo) {
        var view = new TodoView({model: todo});
        this.$("#todo-tbody").append(view.render().el);
      },
      markAllComplete: function() {
        Todos.each(function (todo) {
          if ( !todo.attributes['checked'] ) {
            todo.save({'checked': true});
          }
        });
        return false;
      }
    });
    return TodoList;
});