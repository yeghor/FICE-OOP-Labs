import tkinter as tk
from typing import Type
from modules import *

root = tk.Tk(screenName="main", baseName="lab-1")
root.geometry("500x400")

toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X)

def create_popup(module: Type[InputModuleAbstract], *args, **kwargs) -> None:
    module(*args, **kwargs)

def showcase_apply(val: str) -> None:
    showcase_text.config(text=val)
    showcase_text.update()

module_1_button = tk.Button(toolbar, text="List", command=lambda: create_popup(ListboxModule, root, showcase_apply))
module_1_button.pack(side=tk.LEFT)

module_2_button = tk.Button(toolbar, text="Input", command=lambda: create_popup(InputModule, root, showcase_apply))
module_2_button.pack(side=tk.LEFT)
    
showcase_text = tk.Label(root, text="No options were chosen")
showcase_text.pack(side=tk.TOP, pady=10) 

if __name__ == "__main__":
    root.mainloop()