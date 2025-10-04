import unittest
from gardiner import GarDinEr
from cfg import NwdTestConfig
from obsidio import ObsidIO

class TestGarDinEr(unittest.TestCase):
  def setUp(self):
    tcfg = NwdTestConfig()
    obio = ObsidIO(tcfg)
    self.gard = GarDinEr(tcfg, obio)

  def test_should_have_class(self):
    self.assertIsNotNone(self.gard)

  def test_should_have_welcome_greeting(self):
    self.assertIn("Welcome", self.gard.greeting)

  def test_full_report_should_include_timestamp(self):
    full_report = self.gard.report()
    time_header = "# TimeStamp"
    self.assertIn(time_header, full_report)

  def test_full_report_should_include_greeting(self):
    full_report = self.gard.report()
    greeting = self.gard.greeting
    self.assertIn(greeting, full_report)

  def test_full_report_should_include_config(self):
    full_report = self.gard.report()
    config_header = "# Configuration"
    self.assertIn(config_header, full_report)

  def test_full_report_should_include_cet_list(self):
    full_report = self.gard.report()
    cet_list_header = "# Cets"
    self.assertIn(cet_list_header, full_report)

  def test_full_report_should_include_practices(self):
    full_report = self.gard.report()
    practices_header = "# Practices"
    self.assertIn(practices_header, full_report)

  def test_full_report_should_include_places(self):
    full_report = self.gard.report()
    places_header = "# Places"
    self.assertIn(places_header, full_report)

  def test_full_report_should_include_vhales(self):
    full_report = self.gard.report()
    vhales_header = "# Vhales"
    self.assertIn(vhales_header, full_report)