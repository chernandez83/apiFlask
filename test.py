# https://github.com/TotallyNotChase/flask-unittest ???
# pip install flask-unittest

import unittest
import json

from app import create_app, db
from config import config


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestAPI, cls).setUpClass()
        environment = config['test']
        cls.app = create_app(environment)

    @classmethod
    def tearDownClass(cls):
        super(TestAPI, cls).tearDownClass()
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()

    def setUp(self):
        self.app = TestAPI.app
        self.client = self.app.test_client()
        self.content_type = 'application/json'
        self.path = 'http://127.0.0.1:5000/api/v1/tasks/'
        print(self)

    def tearDown(self):
        pass

    def test_one_equals_one(self):
        self.assertEqual(1, 1)

    def test_get_all_tasks(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)

    def test_get_all_tasks_size(self):
        response = self.client.get(path=self.path)
        data = json.loads(response.data.decode('utf-8'))
        size = len(data)
        self.assertEqual(size, 2)

    def test_get_first_task(self):
        new_path = self.path + '1'
        response = self.client.get(
            path=new_path, content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode('utf-8'))
        task_id = data['data']['id']
        self.assertEqual(task_id, 1)
    
    def test_not_found(self):
        new_path = self.path + '25'
        response = self.client.get(
            path=new_path, content_type=self.content_type)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
