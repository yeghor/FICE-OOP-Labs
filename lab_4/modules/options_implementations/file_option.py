import tkinter as tk

from .option import BaseDropdownOptions


class FileOption(BaseDropdownOptions):
    _ICON_SIZE = 24

    def __init__(self, root: tk.Misc):
        super().__init__(root, {"Close": lambda _: root.destroy()}, ["Close"])
        self.button = self._create_button(
            "file_option.png",
            lambda: self._menu.post(root.winfo_rootx() + 10, root.winfo_rooty() + 30),
        )

    def render(self, parent: tk.Misc | None = None) -> None:
        self._render_buttons([self.button], parent, (0, 8))

    def open_file(self, *args, **kwargs):
        return None
