import unittest
class ForVideo(unittest.TextCase):
  def setUp(self):
    print 'first text'
  def test_search_in_python_org(self):
    print 'second text'
  def tearDown(self):
    print 'third text'
    
if __name__ == "__main__":
  unittest.main()
