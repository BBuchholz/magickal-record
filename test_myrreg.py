import unittest
from myrreg import MyrkiRegistry
from cfg import NwdTestConfig

class TestMyrkiRegistry(unittest.TestCase):
  def setUp(self):
    self.myrg = MyrkiRegistry(NwdTestConfig())

  def test_should_have_class(self):
    self.assertIsNotNone(self.myrg)

  def test_should_load(self):
    self.assertEqual(len(self.myrg.myrkis), 0)
    self.myrg.load()
    self.assertTrue(len(self.myrg.myrkis) > 0)