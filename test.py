import unittest
from server import app

class ApiTest(unittest.TestCase):
   BASE_URL = "http://localhost:3000"
   TEST_IP = {
      "data": '8.8.8.8'
   }
   
   def setUp(self):
        app.testing = True
        self.app = app.test_client()
        
   def test_home(self):
      rv = self.app.get('/')
      self.assertEqual(rv.status, '200 OK')

   def test_get_ip_info(self):
      rv = self.app.post('/ip/info', json={
         "data": '8.8.8.8'
      })
      if(rv.status == '429 TOO MANY REQUESTS'):
         self.assertEqual(rv.status, '429 TOO MANY REQUESTS')
         return
      self.assertEqual(rv.status, '200 OK')
      
   def test_get_backlog(self):
      rv = self.app.get('/ip/backlog')
      self.assertEqual(rv.status, '200 OK')


if __name__ == '__main__':
   unittest.main()