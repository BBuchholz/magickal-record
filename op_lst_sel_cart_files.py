from cartio import CartIO
from cfg import NwdTestConfig, Config
from menus import LineOption

class ListSelectedCartFilesOp(LineOption):
  def __init__(self, cart: CartIO):
    self.cart = cart

  def key(self):
    return "lst"
  
  def desc(self):
    msg = "list currently selected "
    msg += "cartographer files"
    return msg
  
  def run(self):
    if len(self.cart.selected_files) > 0:
      print("selected files:")
      for file in self.cart.selected_files:
        print(file)
    else:
      print("no files selected")


if __name__ == "__main__":
  tcfg = NwdTestConfig()
  cart = CartIO(tcfg)
  cart.select_file(tcfg.cart_test_file_current_cards())
  main = ListSelectedCartFilesOp(cart)
  main.run()