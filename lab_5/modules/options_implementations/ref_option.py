import tkinter as tk

from .option import BaseDropdownOptions


class RefOption(BaseDropdownOptions):
    _ICON_SIZE = 24

    def __init__(self, root: tk.Misc):
        super().__init__(
            root,
            {"Work is done by Yehor Romanov IM-o51": lambda _: None},
            ["Work is done by Yehor Romanov IM-o51"],
        )
        self._label = "Reference"
        self.button = self._create_button(
            "ref_option.png",
            lambda: self._menu.post(root.winfo_rootx() + 10, root.winfo_rooty() + 30),
            self._label,
        )

    def render(self, parent: tk.Misc | None = None) -> None:
        self._render_buttons([self.button], parent, (0, 8))

    def refresh(self, *args, **kwargs):
        return None
