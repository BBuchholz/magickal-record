from menus import LineOption
from obsidio import ObsidIO

class IsolateObsidIOFileOp(LineOption):
  def __init__(self, obsid: ObsidIO):
    self.obsid = obsid

  def key(self):
    return "iso"
  
  def desc(self):
    return "Isolate ObsidIO File"
  
  def run(self):
    print("not yet implemented")
    