from abc import ABC, abstractmethod
import tkinter as tk
from typing import Callable, Any

class ModuleAbstract(ABC):
    def __init__(self, root: tk.Tk,  apply_new_label_text_cb: Callable[[str], None]):
        self._root = root
        self._apply_label_cb = apply_new_label_text_cb

    @abstractmethod
    def submit(self) -> None:
        pass
