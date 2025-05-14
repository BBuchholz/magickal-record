from menus import LineOption
from obsidio import ObsidIO
from cfg import NwdConfig
import tkinter as tk
# TODO: replace with tk_obio when created (this is a placeholder)
from tk_main import MainWindow

class LaunchVaultBrowserGUI(LineOption):
  def __init__(self, obio: ObsidIO):
    self.obio = obio

  def key(self):
    return "gui"
  
  def desc(self):
    return "Launch Vault Browser GUI"
  
  def run(self):
    root = tk.Tk()
    ncfg = NwdConfig()
    MainWindow(root, ncfg)
    root.mainloop()