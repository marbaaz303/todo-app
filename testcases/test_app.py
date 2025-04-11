import unittest
import sys
import os

# Fix path to import app.py from parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, tasks  # Import the app and the global tasks list

class TodoAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        tasks.clear()  # Reset the tasks list before each test

    def test_homepage_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'My To-Do List', response.data)

    def test_add_task(self):
        response = self.app.post('/add', data={'task': 'Test Task'}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Task', response.data)

    def test_delete_task(self):
        self.app.post('/add', data={'task': 'Temp Task'}, follow_redirects=True)
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Temp Task', response.data)

    def test_bva_empty_task(self):
        response = self.app.post('/add', data={'task': ''}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'<li></li>', response.data)

    def test_ecp_invalid_delete(self):
        response = self.app.get('/delete/99', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
