from cfg import Config
from os import path
from cartio import CartIO
from files import (
  get_lines_from,
)

class CartRegistry:
  def __init__(self, cfg: Config):
    self.carts = []
    self.cartio = CartIO(cfg)

  def get_myrkis(self):
    myrkis = []
    for cart in self.carts:
      if "MYRKI" in cart:
        myrkis.append(cart["MYRKI"])
    return myrkis

  def load(self):
    msg = "attempting to load CartRegistry from "
    msg += "stored configuation"
    print(msg)
    # check if stored configuration exists
    verified_file = self.cartio.cfg.verified_cart_file()
    if path.exists(verified_file):
      print("verified file found")
      cart_file = self.load_cart_file_from(verified_file)
      print(f"selecting file {cart_file}")
      self.cartio.select_file(cart_file)
      print("loading registry from CartIO")
      for card in self.cartio.cards.values():
        self.carts.append(card)
        print(f"loaded card {card}")
      print(f"{len(self.carts)} cards loaded")
      
    else:
      print("verified file not found")
      msg = "autoloading is disabled until a verified "
      msg += "cartographer file is stored using the "
      msg += "store option in the cart ops menu"
      print(msg)
      
  def load_cart_file_from(self, verified_file):
    print(f"loading verified file: {verified_file}")
    # TODO: load from that file
    # mimic obsidio.load vaults
    lines = get_lines_from(verified_file)
    print("reading from verified file")
    print("if verified file has multiple lines")
    print("only last line will be used")
    print(f"found {len(lines)} line(s)")
    found = ""
    for line in lines:
      found = self.process_verified_file_line(line)
    return found
  
  def process_verified_file_line(self, line):
    found = ""
    if line.lower().startswith("cart_file: "):
      found = line[11:]
      print(f"found cart_file: {found}")
    return found