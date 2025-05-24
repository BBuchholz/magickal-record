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
    total = len(self.myrreg.myrki_instances)
    print(f"Listing Myrki Instances({total}): ")
    count = 0
    for mi in self.myrreg.myrki_instances:
      count += 1
      print(f"Myrki Instance {count} of {total}: {mi}")
    print(f"Finished Listing Myrki Instances({total}): ")