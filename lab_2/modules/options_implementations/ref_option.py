import tkinter as tk

from .option import BaseDropdownOptions


class RefOption(BaseDropdownOptions):
    def __init__(self, root: tk.Misc):
        super().__init__(root, {"Work is done by Yehor Romanov IM-o51": lambda _: None}, ["Work is done by Yehor Romanov IM-o51"])
        self._label = "Reference"
        self.button = tk.Button(root, text=self._label, command=lambda: self._menu.post(root.winfo_rootx() + 10, root.winfo_rooty() + 30))

    def render(self, parent: tk.Misc | None = None) -> None:
        target = parent if parent is not None else self.root
        self.button.pack(in_=target, side=tk.LEFT, padx=(0, 8), pady=4)

    def refresh(self, *args, **kwargs):
        return None
