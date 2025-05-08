from cfg import Config
from os import path
from cartio import CartIO

class CartRegistry:
  def __init__(self, cfg: Config):
    self.carts = []
    self.cartio = CartIO(cfg)

  def load(self):
    msg = "attempting to load CartRegistry from "
    msg += "stored configuation"
    print(msg)
    # TODO: check if stored configuration exists
    if path.exists(self.cartio.cfg.verified_cart_file()):
      print("verified file found")
      # TODO: load from that file
    else:
      print("verified file not found")
      msg = "autoloading is disabled until a verified "
      msg += "cartographer file is stored using the "
      msg += "store option in the cart ops menu"
      print(msg)
      