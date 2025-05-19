
from menus import (
  # LineOption,
  Menu,
  # SubMenu,
)
from cli_cart import CartMenu
from cfg import Config, NwdConfig
from cli_obsid import ObsidMenu
from cli_gardiner import GarDinErMenu


class MainMenu(Menu):
  def __init__(self, cfg: Config):
    self.cfg = cfg

  def get_ops(self):
    ops = []
    ops.append(CartMenu(self.cfg))
    ops.append(ObsidMenu(self.cfg))
    ops.append(GarDinErMenu(self.cfg))
    return ops

if __name__ == "__main__":
  ncfg = NwdConfig()
  main = MainMenu(ncfg)
  main.show_menu()