import unittest
from crsl_crtr import CarouselCreator
from cfg import NwdTestConfig
from myr_file import MyrFile

class TestCarouselCreator(unittest.TestCase):
  def setUp(self):
    tcfg = NwdTestConfig()
    self.crtr = CarouselCreator(tcfg)
    self.crtr.load_registries()

  def test_should_load_registries(self):
    self.assertIsNotNone(self.crtr.myrreg)
    self.assertIsNotNone(self.crtr.cartreg)

  def test_should_create_myrki_myr_file(self):
    myrki_lines = [
      "THIS SHOULD BE A MOCKUP OF",
      "WHAT WE WANT TO SEE",
    ]
    mf = MyrFile()
    mf.load_from_lines_arr(myrki_lines)
    created_mf = self.crtr.create_myrki_file("SERPENT")
    self.assertEquals(created_mf, mf) 

  def test_should_create_myrki_instance_myr_file(self):
    pass