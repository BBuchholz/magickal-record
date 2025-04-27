from cartio import CartIO
from constants import CART_TEST_FILE_SOME_CARDS
from menus import (
  LineOption,
)

class AuditMyrkisOp(LineOption):
  def __init__(self, cart):
    self.cart = cart

  def key(self):
    return "audit"

  def desc(self):
    msg = "find unconnected myrkis "
    msg += "in currently selected "
    msg += "cartographer file"
    return msg

  def run(self):
    print("")
    if self.cart.selected_file is None:
      print("no cartographer file selected")
      print("please select a file using")
      print("the select option")
      print("")
    else:
      myrkis = self.cart.get_unconnected_myrkis()
      if len(myrkis) > 0:
        for myrki in myrkis:
          print(myrki)
      else:
        print("no missing myrkis found")

if __name__ == "__main__":
  cart = CartIO()
  cart.select_file(CART_TEST_FILE_SOME_CARDS)
  main = AuditMyrkisOp(cart)
  main.run()