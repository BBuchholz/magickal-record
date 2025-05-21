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
    # test vault is vaultone and should only have SERPENT and STAR
    # other files are in there to make sure we are filtering
    self.assertEqual(len(self.myrg.myrkis), 2)
    # test vault is vaultone and should only have SERPENT(2) and STAR(1)
    # other files are in there to make sure we are filtering
    self.assertEqual(len(self.myrg.myrki_instances), 3)