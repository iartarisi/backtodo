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

require(['jquery', 'backbone', 'views/TodoList'],
  function($, Backbone, TodoList) {
    var Router = Backbone.Router.extend({
      routes: {
        '': 'index'
      },
      index: function() {
        var todoList = new TodoList();
      }
    });

    var router = new Router();
    Backbone.history.start();
  });

