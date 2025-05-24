from menus import LineOption
from myrreg import MyrkiRegistry

class ListMyrKisOp(LineOption):
  def __init__(self, myrreg: MyrkiRegistry):
    self.myrreg = myrreg

  def key(self):
    return "lmk"
  
  def desc(self):
    return "List Myrkis"
  
  def run(self):
    total = len(self.myrreg.myrkis)
    print(f"Listing Myrkis({total}): ")
    count = 0
    for myrki in self.myrreg.myrkis:
      count += 1
      print(f"Myrki {count} of {total}: {myrki}")
    print(f"Finished Listing Myrkis({total})") 
    