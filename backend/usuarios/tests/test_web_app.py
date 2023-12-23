import unittest
from flask import Flask
from app.app_module import app

class TestUsuariosEndpoint(unittest.TestCase):
    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_get_usuarios_all(self):
        # Test GET request to /usuarios without specifying a user
        response = self.app.get('/usuarios')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

if __name__ == '__main__':
    unittest.main()