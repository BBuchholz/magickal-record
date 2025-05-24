from menus import LineOption
from cartio import CartIO

class ClearSelectedVerifiedCartFiles(LineOption):
  def __init__(self, cart: CartIO):
    self.cart = cart

  def key(self):
    return "clear"

  def desc(self):
    msg = "clear selected cartographer "
    msg += "spreadsheet files"
    return msg

  def run(self):
    print("")
    count = len(self.cart.selected_files)
    print(f"clearing {count} selected files...")
    card_count = len(self.cart.cards)
    print(f"current card count is {card_count}")
    self.cart.selected_files.clear()
    print(f"cleared {count} selected files")
    count = len(self.cart.selected_files)
    self.cart.cards.clear()
    print(f"{count} files selected")
    card_count = len(self.cart.cards)
    print(f"current card count is {card_count}")
    print("")
