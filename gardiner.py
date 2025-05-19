from chronio import ChronIO
from cfg import Config

class GarDinEr:
  def __init__(self, cfg: Config):
    self.greeting = "Welcome toTha GarDin..."
    self.chron = ChronIO()
    self.cfg = cfg

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
      "config_lines",
      "go_here"
    ]
    return config_lines
  
  def get_cet_lines(self):
    cet_lines = [
      "cet_lines",
      "go_here"
    ]
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