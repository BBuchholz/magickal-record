from gdp import GarDinPlot
from cetar import CetAR

class GarDinPlotAR:
  """
  Represents a GarDinPlot Audit Report
  """
  def __init__(self, gdp: GarDinPlot):
    self.gdp = gdp
    self.repos = []
    self.lines = []

  def add_repos(self, lst: list):
    for repo in lst:
      if repo not in self.repos:
        self.repos.append(repo)

  def get_repos(self) -> list:
    return self.repos
  
  def add_report_line(self, line: str):
    self.lines.append(line)

  def get_report_lines(self):
    return self.lines
  
  def append_heading(self, heading):
    self.add_report_line("")
    self.add_report_line("# " + heading)
    self.add_report_line("")

  def add_audit_report(self, short_name, ar: CetAR):
    self.append_heading(short_name)
    for line in ar.to_lines():
      self.add_report_line(line)
