from menus import LineOption
from myrreg import MyrkiRegistry

class ListCartFileEntriesOp(LineOption):
  def __init__(self, myrreg: MyrkiRegistry):
    self.myrreg = myrreg

  def key(self):
    return "lcf"
  
  def desc(self):
    return "List Card File Entries"
  
  def run(self):
    total = len(self.myrreg.cartrg.carts)
    print(f"Listing Card File Entries({total}): ")
    count = 0
    for cart in self.myrreg.cartrg.carts:
      count += 1
      print(f"Cart {count} of {total}: {cart}")
    print(f"Finished Listing Card File Entries({total})")
