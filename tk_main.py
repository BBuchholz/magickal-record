import tkinter as tk
from tk_mdio import MdIOWindow
from tk_crsl import CRSLWindow
from tk_obio import ObsidIOWindow
from tk_cartio import CartIOWindow
from tk_gitio import GitIOWindow
from cfg import Config, NwdConfig

class MainWindow:
  def __init__(self, master, cfg: Config):
    self.master = master
    self.cfg = cfg
    master.title("Main Window")

    self.label = tk.Label(
       master, 
       text="Master Control Window"
       )
    self.label.pack(padx=20, pady=20)

    self.btn_crsl = tk.Button(
        master, 
        text="CRSL", 
        command=self.open_crsl
        )
    self.btn_crsl.pack(padx=20, pady=20)

    self.btn_mdio = tk.Button(
        master, 
        text="MDIO", 
        command=self.open_mdio
        )
    self.btn_mdio.pack(padx=20, pady=20)

    self.btn_obio = tk.Button(
        master, 
        text="ObsidIO", 
        command=self.open_obio
        )
    self.btn_obio.pack(padx=20, pady=20)

    self.btn_cartio = tk.Button(
        master, 
        text="CartIO", 
        command=self.open_cartio
        )
    self.btn_cartio.pack(padx=20, pady=20)

    self.btn_gitio = tk.Button(
        master, 
        text="GitIO", 
        command=self.open_gitio
        )
    self.btn_gitio.pack(padx=20, pady=20)

  def open_mdio(self):
    self.new_window = tk.Toplevel(self.master)
    MdIOWindow(self.new_window, self.cfg)

  def open_crsl(self):
    self.new_window = tk.Toplevel(self.master)
    CRSLWindow(self.new_window, self.cfg)

  def open_obio(self):
    self.new_window = tk.Toplevel(self.master)
    ObsidIOWindow(self.new_window, self.cfg)

  def open_cartio(self):
    self.new_window = tk.Toplevel(self.master)
    CartIOWindow(self.new_window, self.cfg)

  def open_gitio(self):
    self.new_window = tk.Toplevel(self.master)
    GitIOWindow(self.new_window, self.cfg)

if __name__ == '__main__':
    root = tk.Tk()
    ncfg = NwdConfig()
    main_window = MainWindow(root, ncfg)
    root.mainloop()