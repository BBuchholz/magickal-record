
from menus import (
  # LineOption,
  Menu,
  # SubMenu,
)
from cli_cart import CartMenu
from cartio import CartIO
from cfg import Config, NwdConfig, NwdTestConfig
from cli_obsid import ObsidMenu
from cli_gardiner import GarDinErMenu
from cli_reg import RegistryMenu
from obsidio import ObsidIO
from cli_sql import SqliteMenu
from cli_crsl import MyrCarouselMenu
from cli_test import TestMenu
from cli_git import GitIOMenu

class MainMenu(Menu):
  def __init__(self, cfg: Config):
    self.cfg = cfg
    self.obio = ObsidIO(cfg)
    self.cart = CartIO(cfg)

  def get_ops(self):
    ops = []
    ops.append(CartMenu(self.cart))
    ops.append(ObsidMenu(self.obio))
    ops.append(GarDinErMenu(self.cfg, self.obio))
    ops.append(RegistryMenu(self.cfg))
    ops.append(SqliteMenu(self.cfg))
    ops.append(MyrCarouselMenu(self.cfg))
    ops.append(GitIOMenu(self.cfg))
    # TestMenu uses its own test config
    tcfg = NwdTestConfig()
    ops.append(TestMenu(tcfg))
    return ops

if __name__ == "__main__":
  ncfg = NwdConfig()
  main = MainMenu(ncfg)
  main.show_menu()