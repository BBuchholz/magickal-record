from menus import SubMenu
from op_gar_report import GenerateGarDinErReport
from cfg import Config
from gardiner import GarDinEr
from obsidio import ObsidIO

class GarDinErMenu(SubMenu):
  def __init__(self, cfg: Config, obio: ObsidIO):
    self.gar = GarDinEr(cfg, obio)

  def key(self):
    return "gar"
  
  def desc(self):
    return "tha ConStanT GarDinEr"
  
  def get_ops(self):
    ops = []
    ops.append(GenerateGarDinErReport(self.gar))
    return ops
  