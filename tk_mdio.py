import tkinter as tk
from cfg import Config, NwdTestConfig

class MdioWindow:
  def __init__(self, master, cfg: Config):
    self.master = master
    self.cfg = cfg
    master.title("MDIO")

    lbltxt = "MDIO Window"
    self.label = tk.Label(master, text=lbltxt)
    self.label.pack(padx=20, pady=20)

    lbltxt = self.cfg.status()
    self.label = tk.Label(master, text=lbltxt)
    self.label.pack(padx=20, pady=20)


if __name__ == '__main__':
  root = tk.Tk()
  tcfg = NwdTestConfig()
  window = MdioWindow(root, tcfg)
  root.mainloop()