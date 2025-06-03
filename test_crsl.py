import unittest
from crsl import MyrCarousel
from myrreg import MyrkiRegistry
from cfg import NwdTestConfig

class TestMyrCarousel(unittest.TestCase):
  def setUp(self):
    self.crsl = MyrCarousel()
    tcfg = NwdTestConfig()
    mreg = MyrkiRegistry(tcfg)
    mreg.load()
    mis = []
    for mi in mreg.myrki_instances:
      if mi.startswith("TCTKL-"):
        print(f"mi found: {mi}")
        mis.append(mi)
    self.crsl.load_list(mis)

  def test_should_have_class_loaded(self):
    self.assertIsNotNone(self.crsl)
    self.assertEqual(len(self.crsl.lst), 16)

  def test_should_get_next(self):
    # should get first if no argument supplied
    next = self.crsl.get_next()
    self.assertEqual(next, "TCTKL-0-6c4b")
    # should get next
    next = self.crsl.get_next(next)
    self.assertEqual(next, "TCTKL-1-da")
    # should loop at last one
    next = self.crsl.get_next("TCTKL-MATRIX-0fe4")
    self.assertEqual(next, "TCTKL-0-6c4b")
