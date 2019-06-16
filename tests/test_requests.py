import unittest 
import requests
from movies import app

class MyTestClass(unittest.TestCase): 

  def setUp(self):
    self.app = app.test_client()
        # propagate the exceptions to the test client
    self.app.testing = True

  # clean up logic
  # code that is executed after each test
  def test_search(self):
    

    # test method
    result = self.app.get('/search/subreddit') 

        # assert the status code of the response
    self.assertEqual(result.status_code, 200) 

  def test_search(self):
    

  # test method
    result = self.app.get('/login') 

        # assert the status code of the response
    self.assertEqual(result.status_code, 200) 

  def test_home_data(self):
    

  # test method
    result = self.app.get('/') 

        # assert the status code of the response
    self.assertEqual(result.status_code, 200) 

  def test_home_data_1(self):
    

  # test method
    result = self.app.get('/home') 

        # assert the status code of the response
    self.assertEqual(result.status_code, 200) 
  
  def test_home_posts_1(self):
    

  # test method
    result = self.app.get('/history') 

        # assert the status code of the response
    self.assertEqual(result.status_code, 200) 
  def test_collections(self):
    

  # test method
    result = self.app.get('/collections') 

        # assert the status code of the response
    self.assertEqual(result.status_code, 200) 

  def test_comments(self):
    

  # test method
    result = self.app.get('/comments') 

        # assert the status code of the response
    self.assertEqual(result.status_code, 200) 
  
  
  

# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()