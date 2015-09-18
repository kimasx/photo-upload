import os
import unittest
from app import app
from StringIO import StringIO


class AppTests(unittest.TestCase):
  def setUp(self):
    self.app = app
    self.app.config['TESTING'] = True    
    self.client = app.test_client()

  def test_img_upload(self):
    with self.client as client:
      client.post('/upload',
                  data=dict(image=(StringIO('./test.png'), 'test.png')),
                  follow_redirects=True)


  def test_img_response(self):
    self.test_img_upload()
    res = self.client.get('/display/test.png', follow_redirects=True)
    self.assertEqual(res.status_code, 200)
  
    

if __name__ == '__main__':
  unittest.main()