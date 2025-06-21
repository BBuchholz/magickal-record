from cartio import CartIO
from constants import CART_TEST_FILE_SOME_CARDS
from menus import (
  LineOption,
)
from cfg import NwdTestConfig

class AuditMyrkisOp(LineOption):
  def __init__(self, cart: CartIO):
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
    if len(self.cart.selected_files) < 1:
      print("no cartographer file selected")
      print("please select a file using")
      print("the select option")
      print("")
    else:
      myrkis = self.cart.get_unconnected_myrkis()
      if len(myrkis) > 0:
        for myrki in myrkis:
          print(myrki)
        print("myrkis: ")
        print(self.cart.get_myrkis())
        print("related myrkis: ")
        print(self.cart.get_related_myrkis())
      else:
        print("no missing myrkis found")

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  cart = CartIO(tcfg)
  cart.select_file(CART_TEST_FILE_SOME_CARDS)
  main = AuditMyrkisOp(cart)
  main.run()