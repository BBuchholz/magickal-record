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
    config_header = "# GarDinPlot"
    self.assertIn(config_header, full_report)

  def test_full_report_should_include_cet_list(self):
    full_report = self.gard.report()
    cet_list_header = "# Cets"
    self.assertIn(cet_list_header, full_report)

  def test_full_report_should_include_activities(self):
    full_report = self.gard.report()
    activities_header = "# Activities"
    self.assertIn(activities_header, full_report)

  def test_full_report_should_include_places(self):
    full_report = self.gard.report()
    places_header = "# Zhones"
    self.assertIn(places_header, full_report)

  def test_full_report_should_not_include_vhales_as_seperate_section(self):
    # we want them listed in parenthesis next to the activities as links
    full_report = self.gard.report()
    vhales_header = "# Vhales"
    self.assertNotIn(vhales_header, full_report)