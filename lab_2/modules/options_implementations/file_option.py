import tkinter as tk

from .option import BaseDropdownOptions


class FileOption(BaseDropdownOptions):
    def __init__(self, root: tk.Misc):
        super().__init__(root, {"Close": lambda _: root.destroy()}, ["Close"])
        self._label = "File"
        self.button = tk.Button(root, text=self._label, command=lambda: self._menu.post(root.winfo_rootx() + 10, root.winfo_rooty() + 30))

    def render(self, parent: tk.Misc | None = None) -> None:
        target = parent if parent is not None else self.root
        self.button.pack(in_=target, side=tk.LEFT, padx=(0, 8), pady=4)

    def open_file(self, *args, **kwargs):
        return None
