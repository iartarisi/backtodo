define(['backbone'],
  function(Backbone) {
    var Todo = Backbone.Model.extend({
      urlRoot: '/todos',
      toggle: function() {
        this.save({checked: !this.get('checked')});
      }
    });
    return Todo;
});