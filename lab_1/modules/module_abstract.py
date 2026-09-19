from abc import ABC, abstractmethod
import tkinter as tk
from typing import Tuple

class InputModuleAbstract(ABC):
    """
    Contains basic contents for a generic modal input field \n
    `Submit` and `Cancel` buttons are not compiled initially 
    """

    @staticmethod
    def _align_buttons_between(top: tk.Toplevel, *buttons: tk.Button) -> int:
        """Switches items aligning to grid!"""

        for i, button in enumerate(buttons, start=0):
            top.columnconfigure(i, weight=1) # horizontal center

            button.grid(row=1, column=i, sticky="ew") # align to left and right to simulate grow effect

        return i

    def __init__(self, root: tk.Tk, module_name: str, align_buttons: bool = False):
        """`align_buttons=True` align buttons via grid to second row otherwise via pack"""
        self._root = root
        self._top = tk.Toplevel(self._root, name=module_name)

        self._submit_button = tk.Button(self._top, text="Submit", command=self._submit)
        self._cancel_button = tk.Button(self._top, text="Cancel", command=self._cancel)

        self._n_initial_columns: int | None = None
        self._using_grid = False

        if align_buttons:
            self._n_initial_columns = self._align_buttons_between(self._top, self._submit_button, self._cancel_button)
            self._using_grid = True
        else:
            self._submit_button.pack()
            self._cancel_button.pack()

    @abstractmethod
    def _submit(self) -> None:
        raise NotImplementedError("Not implemented!")

    @abstractmethod
    def _cancel(self) -> None:
        raise NotImplementedError("Not implemented!")
