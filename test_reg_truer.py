import unittest
from cartreg import CartRegistry
from myrreg import MyrkiRegistry
from reg_truer import RegistryTruer

class TestRegistryTruer(unittest.TestCase):
  def test_should_align_registries(self):
    crtrg = CartRegistry()
    cr_loader = crtrg.get_loader()
    cr_loader.load(crtrg)
    myrg = MyrkiRegistry()
    mr_loader = myrg.get_loader()
    mr_loader.load(myrg)
    registry_truer = RegistryTruer()
    is_truedh = registry_truer.true(myrg, self.crtrg)
    self.assertTrue(is_truedh)