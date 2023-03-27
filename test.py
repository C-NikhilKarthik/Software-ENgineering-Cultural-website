import unittest
from app import app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Cultural Destination</title>', response.data)

    def test_about_route(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>About Us | Cultural Destination</title>', response.data)

    def test_events_route(self):
        response = self.client.get('/events')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Events | My Website</title>', response.data)

    def test_artists_route(self):
        response = self.client.get('/artists')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Artists | My Website</title>', response.data)

if __name__ == '__main__':
    unittest.main()
