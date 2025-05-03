import unittest
from myrreg import MyrkiRegistry
from cfg import NwdTestConfig

class TestMyrkiRegistry(unittest.TestCase):
  def setUp(self):
    self.myrg = MyrkiRegistry()

  def test_should_have_class(self):
    self.assertIsNotNone(self.myrg)

  def test_should_get_loader(self):
    self.assertEqual(len(self.myrg.myrkis), 0)
    cr_loader = self.myrg.get_loader(NwdTestConfig())
    cr_loader.load(self.myrg)
    self.assertTrue(len(self.myrg.myrkis) > 0)