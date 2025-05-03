import unittest
from cartreg import CartRegistry
from cfg import NwdTestConfig

class TestCartRegistry(unittest.TestCase):
  def setUp(self):
    self.crtrg = CartRegistry()

  def test_should_have_class(self):
    self.assertIsNotNone(self.crtrg)

  def test_should_get_loader(self):
    self.assertEqual(len(self.crtrg.carts), 0)
    cr_loader = self.crtrg.get_loader(NwdTestConfig())
    cr_loader.load(self.crtrg)
    self.assertTrue(len(self.crtrg.carts) > 0)