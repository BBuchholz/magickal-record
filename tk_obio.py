import tkinter as tk
from cfg import Config, NwdTestConfig

class ObsidIOWindow:
  def __init__(self, master, cfg: Config):
    self.master = master
    self.cfg = cfg
    master.title("ObsidIO")

    lbltxt = "ObsidIO Window"
    self.label = tk.Label(master, text=lbltxt)
    self.label.pack(padx=20, pady=20)

    lbltxt = self.cfg.status()
    self.label = tk.Label(master, text=lbltxt)
    self.label.pack(padx=20, pady=20)


if __name__ == '__main__':
  root = tk.Tk()
  tcfg = NwdTestConfig()
  window = ObsidIOWindow(root, tcfg)
  root.mainloop()