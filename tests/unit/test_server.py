import unittest
import server


class ServerTest(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def test_server_up(self):
        rv = self.app.get('/')
        assert 'Unbelievable.  No entries here so far' in rv.data
