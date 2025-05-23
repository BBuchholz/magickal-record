from menus import LineOption
from myrreg import MyrkiRegistry

class ListMyrkiInstancesOp(LineOption):
  def __init__(self, myrreg: MyrkiRegistry):
    self.myrreg = myrreg

  def key(self):
    return "lmi"
  
  def desc(self):
    return "List Myrki Instances"
  
  def run(self):
    print(f"Myrki Instances({len(self.myrreg.myrki_instances)}): ")
    for mi in self.myrreg.myrki_instances:
      print("Myrki Instance: ")
      print(mi)