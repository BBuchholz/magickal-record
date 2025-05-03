import unittest
from myrreg import MyrkiRegistry

class TestMyrkiRegistry(unittest.TestCase):
  def setUp(self):
    self.myrg = MyrkiRegistry()

  def test_should_have_class(self):
    self.assertIsNotNone(self.myrg)