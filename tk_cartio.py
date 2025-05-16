import tkinter as tk
from cfg import Config, NwdTestConfig
from cartreg import CartRegistry

class CartIOWindow:
  def __init__(self, master, cfg: Config):
    self.master = master
    self.cfg = cfg
    self.reg = CartRegistry(cfg)
    self.reg.load()
    master.title("CartIO")

    lbltxt = "CartIO Window"
    self.label = tk.Label(master, text=lbltxt)
    self.label.pack(padx=20, pady=20)

    lbltxt = self.cfg.status()
    self.label = tk.Label(master, text=lbltxt)
    self.label.pack(padx=20, pady=20)

    self.listbox = tk.Listbox(self.master)

    for cart in self.reg.carts:
      self.listbox.insert(tk.END, cart["MYRKI"])

    self.listbox.pack()

if __name__ == '__main__':
  root = tk.Tk()
  tcfg = NwdTestConfig()
  window = CartIOWindow(root, tcfg)
  root.mainloop()