requirejs.config({
   baseUrl: "static/js/",
   paths: {
     app: 'app',
     backbone: 'libs/backbone',
     jquery: 'libs/jquery-1.11.1',
     text: 'libs/text',
     underscore: 'libs/underscore'
   }
});

require(['jquery', 'backbone', 'views/TodoList', 'views/NewTodo'],
  function($, Backbone, TodoList, NewTodo) {
    var Router = Backbone.Router.extend({
      routes: {
        '': 'index'
      },
      index: function() {
        new NewTodo();
        var todoList = new TodoList();
        todoList.render();
      }
    });

    var router = new Router();
    Backbone.history.start();
  });

