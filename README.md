# ToDo #

This is a ToDo app written with Backbone.js, Require.js and Flask-RESTful using python3.3.

A JSON API is used on the backend, which supports all the basic CRUD operations on ToDo items. E.g.

* `POST 'todos'`
* `GET 'todos'`
* `GET 'todos/42'`
* `PUT 'todos/42'`
* `DELETE 'todos/42'`

The backend store is just a python dictionary, it does not offer any persistence between server restarts.

The webUI has only been tested in Firefox and Chromium.

## Installation ##

```bash
$ git clone https://github.com/mapleoin/backtodo
$ cd backtodo
$ pip install -r requirements.txt
$ cd todo
$ python3 api.py
```
Then point your browser to `http://localhost:5000`.

## Tests ##

There are no extra requirements for the unit tests.

```bash
$ cd backtodo
$ python3 -m unittest discover
```