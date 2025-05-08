from cartio import CartIO
from menus import (
  LineOption,
)
from files import write_lines

class StoreSelectedCartFileAsVerifiedDefault(LineOption):
  def __init__(self, cart: CartIO):
    self.cart = cart

  def key(self):
    return "store"

  def desc(self):
    msg = "store currently selected cartographer "
    msg += "file as verified default file "
    msg += "for autoloading in future sessions"
    return msg

  def run(self):
    print("")
    if self.cart.selected_file is None:
      print("no cartographer file selected")
      print("please select a file using")
      print("the select option")
      print("")
    else:
      lines = [
        f"cart_file: {self.cart.selected_file}"
      ]
      file_path = self.cart.cfg.verified_cart_file()
      print(f"storing file as {file_path}")
      write_lines(file_path, lines, True)
      print(f"{len(lines)} line(s) written")