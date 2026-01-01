from gdp import GarDinPlot

class GarDinPlotAR:
  """
  Represents a GarDinPlot Audit Report
  """
  def __init__(self, gdp: GarDinPlot):
    self.gdp = gdp
    self.repos = []

  def add_repos(self, lst: list):
    for repo in lst:
      if repo not in self.repos:
        self.repos.append(repo)

  def get_repos(self) -> list:
    return self.repos