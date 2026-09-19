import tkinter as tk
from .module_abstract import InputModuleAbstract
from typing import Callable

class InputModule(InputModuleAbstract):
    def __init__(self, root: tk.Tk, cb: Callable[[str], None] | None):
        super().__init__(root, "input_module", align_buttons=True)

        self._top.geometry("200x100")

        self._cb = cb

        self._input_val = tk.StringVar()
        self._input = tk.Entry(self._top, textvariable=self._input_val)

        if self._using_grid:
            self._input.grid(
                row=0,
                columnspan=self._n_initial_columns+1,
                sticky="ew"
            )
        else:
            self._input.pack()

    def _submit(self) -> None:
        if self._cb:
            self._cb(self._input_val.get())

        self._top.destroy()

    def _cancel(self) -> None:
        self._top.destroy()
