"""Variant 0 ((12 + 1) mod 4 = 3)"""
import tkinter as tk
from .module_abstract import ModuleAbstract
from typing import Callable

class InputModule(ModuleAbstract):
    def __init__(self, root: tk.Tk, apply_new_label_text_cb: Callable[[str], None] | None):
        super().__init__(root, apply_new_label_text_cb)

        self._top = tk.Toplevel(self._root, name="input_module")

        self._input_val = tk.StringVar()
        # self._input_val.trace_add(mode="write", callback=self.update_current_value)
        self._input = tk.Entry(self._top, textvariable=self._input_val)
        self._input.pack()

        self._submit_button = tk.Button(self._top, command=self.submit)
        self._submit_button.pack()
        
    def submit(self) -> None:
        if self._apply_label_cb:
            self._apply_label_cb(self._input_val.get())

        self._top.destroy()
