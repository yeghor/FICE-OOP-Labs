import tkinter as tk
from modules import *

root = tk.Tk(screenName="main", baseName="lab-1")

def create_popup(module: ModuleAbstract, *args, **kwargs):
    module(*args, **kwargs)

showcase_text = tk.Label(text="")
showcase_text.pack()

def showcase_apply(val: str) -> None:
    showcase_text.config(text=val)
    showcase_text.update()

module_1_button = tk.Button(root, text="List", command=lambda: create_popup(ListboxModule, root, showcase_apply))
module_2_button = tk.Button(root, text="Input", command=lambda: create_popup(InputModule, root, showcase_apply))

module_1_button.pack()
module_2_button.pack()

if __name__ == "__main__":
    root.mainloop()
