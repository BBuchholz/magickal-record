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
    print(f"Card File Entries({len(self.myrreg.cartrg.carts)}): ")
    for cart in self.myrreg.cartrg.carts:
      print("Cart: ")
      print(cart)
