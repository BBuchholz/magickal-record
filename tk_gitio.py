import tkinter as tk
from tkinter import filedialog
from cfg import Config, NwdTestConfig

class GitIOWindow:
  def __init__(self, root: tk.Tk, cfg: Config):
    self.root = root
    self.cfg = cfg
    root.title("GitIO")

    lbltxt = "GitIO Window"
    self.label = tk.Label(root, text=lbltxt)
    self.label.pack(padx=20, pady=20)

    lbltxt = self.cfg.status()
    self.label = tk.Label(root, text=lbltxt)
    self.label.pack(padx=20, pady=20)

    self.btn_folder = tk.Button(
        root, 
        text="Select Folder", 
        command=self.open_folder
        )
    self.btn_folder.pack(padx=20, pady=20)

  def open_folder(self):
    # self.root.withdraw() # hide the main window
    folder_path = filedialog.askdirectory(initialdir=self.cfg.nwd_folder())
    if folder_path:
      print(f"Selected folder: {folder_path}")
    else:
      print("No folder selected")

if __name__ == '__main__':
  root = tk.Tk()
  tcfg = NwdTestConfig()
  window = GitIOWindow(root, tcfg)
  root.mainloop()