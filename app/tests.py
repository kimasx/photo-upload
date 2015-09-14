import os
import unittest
from app import app


class AppTests(unittest.TestCase):
  def setUp(self):
    self.client = app.test_client()

  def test_img_response(self):
    response = self.client.get('/upload')
    print response.data

if __name__ == '__main__':
  unittest.main()