import tkinter as tk
root = tk.Tk()
root.title("My first GUI")


def button_click():
  print("button was clicked!")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(padx=20, pady=20)
button = tk.Button(root, text="Click Me!", command=button_click)
button.pack(padx=20, pady=20)

def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("New Window")
    
    label = tk.Label(new_window, text="This is a new window")
    label.pack(padx=20, pady=20)


button2 = tk.Button(root, text="Open New Window", command=open_new_window)
button2.pack(pady=20)


root.mainloop()