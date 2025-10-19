import tkinter as tk
from cfg import Config, NwdTestConfig
from obsidio import ObsidIO

class CRSLWindow:
  def __init__(self, master, cfg: Config):
    self.master = master
    self.cfg = cfg
    self.obio = ObsidIO(self.cfg)
    master.title("CRSL")

    lbltxt = "CRSL Window"
    self.label = tk.Label(master, text=lbltxt)
    self.label.pack(padx=20, pady=20)

    lbltxt = self.cfg.status()
    self.label = tk.Label(master, text=lbltxt)
    self.label.pack(padx=20, pady=20)

    self.listbox = tk.Listbox(self.master)

    for cf_name in self.obio.get_crsl_file_names():
      self.listbox.insert(tk.END, cf_name)

    self.listbox.pack()

if __name__ == '__main__':
  root = tk.Tk()
  tcfg = NwdTestConfig()
  window = CRSLWindow(root, tcfg)
  root.mainloop()