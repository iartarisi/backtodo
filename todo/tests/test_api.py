import unittest

from flask import json

from todo.api import app


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_one(self):
        resp = self.client.get('/1')
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual({'1': {'checked': False, 'task': 'foo'}},
                         data)

    def test_get_one_404(self):
        resp = self.client.get('/404')
        self.assertEqual(resp.status_code, 404)
        data = json.loads(resp.data)
        self.assertEqual({'message': 'Todo 404 does not exist!'}, data)

    def test_post_new_task(self):
        resp = self.client.put('/3', data=dict(task='do a foo'))
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual({'3': {'checked': False, 'task': 'do a foo'}}, data)

    def test_post_checked_off(self):
        resp = self.client.put('/3', data=dict(task='do a foo', checked=True))
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual({'3': {'checked': 'True', 'task': 'do a foo'}}, data)
