import unittest
class ForVideo(unittest.TestCase):
  def setUp(self):
    print("first")
  def test_search_in_python_org(self):
    print("second")
  def tearDown(self):
    print("third")
    
if __name__ == "__main__":
  unittest.main()
