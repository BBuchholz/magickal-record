from cartio import CartIO
from menus import LineOption

class SelectFileOp(LineOption):
  def __init__(self, cart, key, file_name):
    self.cart = cart
    self.key_value = key
    self.file_name = file_name

  def key(self):
    return self.key_value

  def desc(self):
    return self.file_name

  def run(self):
    print("")
    self.cart.select_file(self.file_name)
    print(f"selecting file: {self.file_name}")
    print("")

if __name__ == "__main__":
  cart = CartIO()
  print(f"Selected file is: {cart.selected_file}")
  main = SelectFileOp(cart, 1, "EXAMPLE.xlsx")
  main.run()
  print(f"Selected file is: {cart.selected_file}")

