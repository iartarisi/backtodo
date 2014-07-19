import unittest

from flask import json

from todo import api

EXAMPLE_TODOS = {'1': {'task': 'brush teeth', 'checked': True},
                 '2': {'task': 'hug trees', 'checked': True},
                 '4': {'task': 'profit!', 'checked': False}}


class ApiTest(unittest.TestCase):
    def setUp(self):
        api.todos.update(EXAMPLE_TODOS)
        self.client = api.app.test_client()

    def tearDown(self):
        api.todos = api.Store()


class ToDoApiTest(ApiTest):
    def test_get_one(self):
        resp = self.client.get('/1')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual({'1': {'checked': True, 'task': 'brush teeth'}},
                         data)

    def test_get_one_404(self):
        resp = self.client.get('/404')
        self.assertEqual(resp.status_code, 404)
        data = json.loads(resp.data)
        self.assertEqual({'message': 'Todo 404 does not exist!'}, data)

    def test_put_new_task(self):
        resp = self.client.put('/3', data=dict(task='do a foo'))
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual({'3': {'checked': False, 'task': 'do a foo'}}, data)

    def test_put_checked_off(self):
        resp = self.client.put('/3', data=dict(task='do a foo', checked=True))
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual({'3': {'checked': 'True', 'task': 'do a foo'}}, data)

    def test_put_check_off_existing(self):
        resp = self.client.put('/4', data=dict(checked=True))
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual({'4': {'checked': 'True',
                                'task': 'profit!'}}, data)

    def test_put_check_off_does_not_exist(self):
        resp = self.client.put('/404', data=dict(checked=True))
        self.assertEqual(resp.status_code, 404)
        data = json.loads(resp.data)
        self.assertEqual({'message':
                          'Task 404 does not exist! Can not check it off.'},
                         data)

    def test_delete_404(self):
        resp = self.client.delete('/404')
        self.assertEqual(resp.status_code, 404)
        data = json.loads(resp.data)
        self.assertEqual({'message':
                          'Could not delete task 404. It does not exist.'},
                         data)

    def test_delete(self):
        resp = self.client.delete('/1')
        self.assertEqual(resp.status_code, 204)
        self.assertEqual('', resp.data.decode('utf-8'))


class ToDoListApiTest(ApiTest):
    def test_list_todos(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual(EXAMPLE_TODOS, data)
