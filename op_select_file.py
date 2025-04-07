from cartographer import Cartographer
from menus import LineOption

class SelectFileOp(LineOption):
  def __init__(self, cart, key, file_name):
    self.cart = cart
    self.key = key
    self.file_name = file_name

  def key(self):
    return self.key

  def desc(self):
    return self.file_name

  def run(self):
    print("")
    self.cart.selected_file = self.file_name
    print(f"selecting file: {self.file_name}")
    print("")

if __name__ == "__main__":
  cart = Cartographer()
  print(f"Selected file is: {cart.selected_file}")
  main = SelectFileOp(cart, 1, "EXAMPLE.xlsx")
  main.run()
  print(f"Selected file is: {cart.selected_file}")

