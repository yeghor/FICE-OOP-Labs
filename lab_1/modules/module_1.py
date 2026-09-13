"""Dropdown module with five selectable options."""

import tkinter as tk
from typing import Any, Callable

from .module_abstract import ModuleAbstract


class ListboxModule(ModuleAbstract):
    def __init__(
        self,
        root: tk.Tk,
        apply_new_label_text_cb: Callable[[str], None] | None,
    ):
        super().__init__(root, apply_new_label_text_cb)

        self._top = tk.Toplevel(self._root, name="listbox_module")

        self._options = ("Apple", "Banana", "Cherry", "Orange", "Strawberry")
        self._selected_value = tk.StringVar(self._top, value=self._options[0])
        # self._selected_value.trace_add(mode="write", callback=self.update_current_value)

        self._dropdown = tk.OptionMenu(self._top, self._selected_value, *self._options)
        self._dropdown.pack()

        self._submit_button = tk.Button(self._top, text="Submit", command=self.submit)
        self._submit_button.pack()

    def submit(self) -> None:
        if self._apply_label_cb:
            self._apply_label_cb(self._selected_value.get())

        self._top.destroy()