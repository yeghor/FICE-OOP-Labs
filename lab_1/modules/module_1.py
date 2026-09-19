"""Dropdown module with five selectable options."""

import tkinter as tk
from typing import List, Callable

from .module_abstract import InputModuleAbstract


class ListboxModule(InputModuleAbstract):
    def __init__(
        self,
        root: tk.Tk,
        cb: Callable[[str], None],
        options: List[str] = None,
    ):
        super().__init__(root, "listbox_module", align_buttons=True)

        self._top.geometry("200x100")

        self._cb = cb

        self._options = ("Apple", "Banana", "Cherry", "Orange", "Strawberry")
        self._selected_value = tk.StringVar(self._top, value=self._options[0])

        self._dropdown = tk.OptionMenu(self._top, self._selected_value, *self._options)

        if self._using_grid:
            self._dropdown.grid(
                row=0,
                columnspan=self._n_initial_columns+1,
                sticky="ew"
            )
        else:
            self._dropdown.pack()

    def _submit(self) -> None:
        if self._cb:
            self._cb(self._selected_value.get())
        self._top.destroy()

    def _cancel(self) -> None:
        self._top.destroy()
