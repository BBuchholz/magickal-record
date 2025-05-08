import unittest
from cartreg import CartRegistry
from cfg import NwdTestConfig

class TestCartRegistry(unittest.TestCase):
  def setUp(self):
    self.crtrg = CartRegistry(NwdTestConfig())

  def test_should_have_class(self):
    self.assertIsNotNone(self.crtrg)

  def test_should_load(self):
    self.assertEqual(len(self.crtrg.carts), 0)
    self.crtrg.load()
    self.assertTrue(len(self.crtrg.carts) > 0)