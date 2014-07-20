requirejs.config({
   baseUrl: "static/js/",
   paths: {
     app: 'app',
     backbone: 'libs/backbone',
     underscore: 'libs/underscore',
     jquery: 'libs/jquery-1.11.1'
   }
});

require(['jquery', 'backbone', 'views/TodoList'],
  function($, Backbone, TodoList) {
    var Router = Backbone.Router.extend({
      routes: {
        '': 'index'
      },
      index: function() {
        var todoList = new TodoList();
        todoList.render();
      }
    });

    var router = new Router();
    Backbone.history.start();
  });

