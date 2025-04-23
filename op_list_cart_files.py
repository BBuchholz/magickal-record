from cartio import Cartographer
from menus import (
  LineOption,
)

class ListCartFilesOp(LineOption):
  def __init__(self, cart):
    self.cart = cart

  def key(self):
    return "files"

  def desc(self):
    msg = "list cartographer "
    msg += "spreadsheet files in "
    msg += "cartographer folder"
    return msg

  def run(self):
    print("")
    print("these are the files found:")
    files_found = self.cart.get_cart_files()
    if len(files_found) > 0:
      for file in files_found:
        print(file)
    else:
      print("no files found")
    print("")


if __name__ == "__main__":
  cart = Cartographer()
  main = ListCartFilesOp(cart)
  main.run()