from operator import itemgetter
import unittest

from flask import json

from todo import api

EXAMPLE_TODOS = {'1': {'task': 'brush teeth', 'checked': True},
                 '2': {'task': 'hug trees', 'checked': True},
                 '4': {'task': 'profit!', 'checked': False}}


class ApiTest(unittest.TestCase):
    def setUp(self):
        api.todos = api.Store()
        api.todos.update(EXAMPLE_TODOS)
        self.client = api.app.test_client()

    def json_post(self, *args, **kwargs):
        kwargs['content_type'] = 'application/json'
        kwargs['data'] = json.dumps(kwargs['data'])
        return self.client.post(*args, **kwargs)

    def json_put(self, *args, **kwargs):
        kwargs['content_type'] = 'application/json'
        kwargs['data'] = json.dumps(kwargs['data'])
        return self.client.put(*args, **kwargs)


class ToDoApiTest(ApiTest):
    def test_get_one(self):
        resp = self.client.get('/todos/1')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual({'1': {'checked': True, 'task': 'brush teeth'}},
                         data)

    def test_get_one_404(self):
        resp = self.client.get('/todos/404')
        self.assertEqual(resp.status_code, 404)
        data = json.loads(resp.data)
        self.assertEqual({'message': 'Todo 404 does not exist!'}, data)

    def test_put_new_task(self):
        resp = self.json_put('/todos/3', data=dict(task='do a foo'))
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual({'3': {'checked': False, 'task': 'do a foo'}}, data)

    def test_put_checked_off(self):
        resp = self.json_put('/todos/3',
                             data={'task': 'do a foo', 'checked': True})
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual({'3': {'checked': True, 'task': 'do a foo'}}, data)

    def test_put_check_off_existing(self):
        resp = self.json_put('/todos/4', data=dict(checked=True))
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual({'4': {'checked': True, 'task': 'profit!'}}, data)

    def test_put_check_off_does_not_exist(self):
        resp = self.json_put('/todos/404', data=dict(checked=True))
        self.assertEqual(resp.status_code, 404)
        data = json.loads(resp.data)
        self.assertEqual({'message':
                          'Task 404 does not exist! Can not check it off.'},
                         data)

    def test_delete_404(self):
        resp = self.client.delete('/todos/404')
        self.assertEqual(resp.status_code, 404)
        data = json.loads(resp.data)
        self.assertEqual({'message':
                          'Could not delete task 404. It does not exist.'},
                         data)

    def test_delete(self):
        resp = self.client.delete('/todos/1')
        self.assertEqual(resp.status_code, 204)
        self.assertEqual('', resp.data.decode('utf-8'))


class ToDoListApiTest(ApiTest):
    def test_list_todos(self):
        resp = self.client.get('/todos')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual([{'order': '1',
                           'task': 'brush teeth',
                           'checked': True},
                          {'order': '2',
                           'task': 'hug trees',
                           'checked': True},
                          {'order': '4',
                           'task': 'profit!',
                           'checked': False}],
                         data)

    def test_post_todo(self):
        resp = self.json_post('/todos', data={'task': 'win the internet'})
        self.assertEqual(resp.status_code, 201)
        data = json.loads(resp.data)
        self.assertEqual({'5': {'checked': False, 'task': 'win the internet'}},
                         data)

    def test_post_todo_first_time(self):
        api.todos = api.Store()
        resp = self.json_post('/todos', data={'task': 'win the internet'})
        self.assertEqual(resp.status_code, 201)
        data = json.loads(resp.data)
        self.assertEqual({'1': {'checked': False, 'task': 'win the internet'}},
                         data)

    def test_delete_from_the_middle_then_post(self):
        resp = self.client.delete('/todos/2')
        self.assertEqual(resp.status_code, 204)

        resp = self.json_post('/todos', data={'task': 'win the internet'})
        self.assertEqual(resp.status_code, 201)
        data = json.loads(resp.data)
        self.assertEqual({'5': {'checked': False, 'task': 'win the internet'}},
                         data)

    def test_post_returns_next_after_10(self):
        self.json_put('/todos/9', data={'task': 'last task'})
        self.json_post('/todos', data={'task': 'a new task'})
        self.json_post('/todos', data={'task': 'another new task'})
        resp = self.client.get('/todos')
        data = json.loads(resp.data)
        self.assertEqual(6, len(data))
