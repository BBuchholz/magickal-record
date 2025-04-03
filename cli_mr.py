
from menus import (
  # LineOption,
  Menu,
  # SubMenu,
)
from cli_cart import CartMenu


class MainMenu(Menu):
  def get_ops(self):
    ops = []
    ops.append(CartMenu())
    return ops

if __name__ == "__main__":
  main = MainMenu()
  main.show_menu()