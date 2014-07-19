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
        self.assertEqual({"1": "foo"}, data)
