from cartio import CartIO
from cfg import NwdTestConfig
from menus import LineOption

class SelectFileOp(LineOption):
  def __init__(self, file_mgr, key, file_name):
    self.file_mgr = file_mgr
    self.key_value = key
    self.file_name = file_name

  def key(self):
    return self.key_value

  def desc(self):
    return self.file_name

  def run(self):
    print("")
    print(f"selecting file: {self.file_name}")
    self.file_mgr.select_file(self.file_name)
    print("")

if __name__ == "__main__":
  tcfg = NwdTestConfig()
  cart = CartIO(tcfg)
  cart.print_selected_files()
  main = SelectFileOp(cart, 1, tcfg.cart_test_file_some_cards())
  main.run()
  cart.print_selected_files()

