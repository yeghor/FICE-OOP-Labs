import tkinter as tk
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List


class BaseDropdownOptions(ABC):
    def __init__(self, root: tk.Misc, options_cbs: Dict[str, Callable[[Any], None]], readable_options: List[str] | None = None):
        self.root = root
        self._label = "Menu"
        self._options = list(options_cbs.keys()) if readable_options is None else readable_options
        self._options_cbs = options_cbs
        self._menu = tk.Menu(root, tearoff=0)
        self._attach_menu_items()

    def _attach_menu_items(self) -> None:
        for option in self._options:
            callback = self._options_cbs.get(option)
            self._menu.add_command(label=option, command=lambda value=option: self._select_option(value))

    def _select_option(self, option: str) -> None:
        callback = self._options_cbs.get(option)
        if callback is not None:
            callback(option)

    @property
    def chosen_option(self) -> str:
        return self._label

    @abstractmethod
    def render(self, parent: tk.Misc | None = None) -> None:
        ...
    