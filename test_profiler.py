import unittest
from profiler import Profiler
from profile_examples import ProfileExample
from myr_file import MyrFile

class TestProfiler(unittest.TestCase):
  def test_should_profile_md_file(self):
    prof = Profiler()
    exams = ProfileExample()
    md_file = exams.example_md_file()
    result = prof.profile(md_file)
    self.assertIn("MyrFile", result)
    self.assertNotIn("MyrkiInstance", result)

  def test_should_profile_myrki_instance(self):
    prof = Profiler()
    exams = ProfileExample()
    mi_file = exams.example_myrki_instance_file()
    result = prof.profile(mi_file)
    self.assertIn("MyrFile", result)
    self.assertIn("MyrkiInstance", result)

  def test_should_profile_folder(self):
    prof = Profiler()
    exams = ProfileExample()
    fldr = exams.example_folder()
    result = prof.profile(fldr)
    self.assertIn("Folder", result)
    self.assertNotIn("MyrFile", result)

  def test_should_parse_ufu(self):
    prof = Profiler()
    exams = ProfileExample()

    # NON UFU FILE
    md_file = exams.example_md_file()
    mf = MyrFile()
    mf.load_from_string_path(md_file)
    analysis_report = prof.parse_ufu(mf)
    ar_wxrd_type = analysis_report["wxrd_type"]
    ar_match_count = analysis_report["match_count"]
    ar_total_count = analysis_report["total_count"]
    self.assertEqual("MyrFile", ar_wxrd_type)
    self.assertEqual(0, ar_match_count)
    self.assertEqual(2, ar_total_count)

    # UFU FILE
    md_file = exams.example_ufu_md_file()
    mf = MyrFile()
    mf.load_from_string_path(md_file)
    analysis_report = prof.parse_ufu(mf)
    ar_wxrd_type = analysis_report["wxrd_type"]
    ar_match_count = analysis_report["match_count"]
    ar_total_count = analysis_report["total_count"]
    self.assertEqual("UfuMyrFile", ar_wxrd_type)
    self.assertEqual(1, ar_match_count)
    self.assertEqual(1, ar_total_count)