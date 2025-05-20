from chronio import ChronIO
from cfg import Config
from obsidio import ObsidIO
from files import path_exists

class GarDinEr:
  def __init__(self, cfg: Config, obio: ObsidIO):
    self.greeting = "Welcome toTha GarDin..."
    self.chron = ChronIO()
    self.cfg = cfg
    self.obio = obio

  def load(self):
    pass # TODO: loading functionality goes here

  def get_practice_lines(self):
    practices = [
      "breath meditations",
      "mind meditations",
      "ritual work",
      "card work",
    ]
    # TODO: load these from Obsidian using ObsidIO and latest verified vault and configuration
    return practices

  def get_timestamp_lines(self):
    timestamp_lines = [
      f"- {self.chron.get_timestamp()}",
      "timestamp_lines",
      "go_here"
    ]
    return timestamp_lines
  
  def get_config_lines(self):
    config_lines = [
      f"- Status: {self.cfg.status()}",
      f"- NWD FOLDER: {self.cfg.nwd_folder()}",
      f"- OBSIDIO FOLDER: {self.cfg.obsidio_folder()}",
      f"- CARTIO FOLDER: {self.cfg.cartio_folder()}",
    ]
    return config_lines
  
  def get_cet_lines(self):
    cet_lines = []
    if not self.obio.last_loaded_vault:
      msg = "no vault loaded at time of report generation"
      print("no vault loaded at time of report generation")
      cet_lines.append(msg)
      return cet_lines
    year = 24
    codes = self.chron.get_all_sabbat_codes()
    cet_file_names = []
    while year < 27:
      for code in codes:
        look_for = code + str(year)
        vault_path = self.obio.get_src_md_file_path(look_for)
        if path_exists(vault_path):
          cet_file_names.append(look_for)
      year += 1
    for fname in cet_file_names:
      link = "[[" + fname + "]]"
      cet_lines.append(link)
    return cet_lines
  
  def get_place_lines(self):
    place_lines = [
      "place_lines",
      "go_here"
    ]
    return place_lines

  def report(self):
    report_lines = []
    # Greeting
    report_lines.append(self.greeting)
    report_lines.append("")
    # TimeStamp
    report_lines.append("# TimeStamp")
    for line in self.get_timestamp_lines():
      report_lines.append(line)
    # Configuration
    report_lines.append("# Configuration")
    for line in self.get_config_lines():
      report_lines.append(line)
    # Cets
    report_lines.append("# Cets")
    for line in self.get_cet_lines():
      report_lines.append(line)
    # Practices
    report_lines.append("# Practices")
    for line in self.get_practice_lines():
      report_lines.append(line)
    # Places
    report_lines.append("# Places")
    for line in self.get_place_lines():
      report_lines.append(line)
    return report_lines