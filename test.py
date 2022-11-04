import unittest
import requests

class ApiTest(unittest.TestCase):
   BASE_URL = "http://localhost:3000"
   TEST_IP = {
      "data": '8.8.8.8'
   }
   
   def test_home(self):
      r = requests.get(ApiTest.BASE_URL)
      self.assertEqual(r.status_code, 200)
      
   def test_get_ip_info(self):
      r = requests.post(f'{ApiTest.BASE_URL}/ip/info', json=ApiTest.TEST_IP)
      self.assertEqual(r.status_code, 200)
   
   def test_get_backlog(self):
      r = requests.get(f'{ApiTest.BASE_URL}/ip/backlog')
      self.assertEqual(r.status_code, 200)
      

if __name__ == '__main__':
   unittest.main()