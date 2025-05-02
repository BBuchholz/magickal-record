import tkinter as tk

def add_btn(txt, cmd):
  button = tk.Button(root, text=txt, command=cmd)
  button.pack(padx=20, pady=20)

def button_click():
  print("button was clicked!")

def open_info():
  new_window = tk.Toplevel()
  new_window.title("Info")
  msg = "This is the info window for 'the Remote'.\n"
  msg += "Each window should have one that explains\n"
  msg += "its function and planning.\n"
  msg += "This window launches all the others."
  label = tk.Label(new_window, text=msg)
  label.pack(padx=20, pady=20)


def open_mdio():
  new_window = tk.Toplevel()
  new_window.title("MDIO")
  msg = "MDIO (MarkDown IO)\n"
  msg += ""
  label = tk.Label(new_window, text=msg)
  label.pack(padx=20, pady=20)

root = tk.Tk()
root.title("My first GUI")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(padx=20, pady=20)

add_btn("Click Here", button_click)

add_btn("?", open_info)

add_btn("MDIO", open_mdio)



root.mainloop()