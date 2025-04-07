from cartographer import Cartographer
from constants import CART_TEST_FILE_SOME_CARDS
from menus import (
  LineOption,
)


class ListRelatedMyrkisOp(LineOption):
  def __init__(self, cart):
    self.cart = cart

  def key(self):
    return "related"

  def desc(self):
    msg = "list related myrkis "
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
      myrkis = self.cart.get_related_myrkis()
      if len(myrkis) > 0:
        for myrki in myrkis:
          print(myrki)
      else:
        print("no related myrkis found")


if __name__ == "__main__":
  cart = Cartographer()
  cart.selected_file = CART_TEST_FILE_SOME_CARDS
  main = ListRelatedMyrkisOp(cart)
  main.run()