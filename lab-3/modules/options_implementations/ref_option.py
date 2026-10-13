from pathlib import Path
import tkinter as tk

from .option import BaseDropdownOptions


class RefOption(BaseDropdownOptions):
    def __init__(self, root: tk.Misc):
        super().__init__(root, {"Work is done by Yehor Romanov IM-o51": lambda _: None}, ["Work is done by Yehor Romanov IM-o51"])
        self._label = "Reference"
        self._image = tk.PhotoImage(
            master=root,
            file=str(Path(__file__).parent / "icons" / "ref_option.png"),
        ).subsample(3, 3)
        self.button = tk.Button(root, image=self._image, width=16, height=16, text=self._label, command=lambda: self._menu.post(root.winfo_rootx() + 10, root.winfo_rooty() + 30))

    def render(self, parent: tk.Misc | None = None) -> None:
        target = parent if parent is not None else self.root
        self.button.pack(in_=target, side=tk.LEFT, padx=(0, 8), pady=4)

    def refresh(self, *args, **kwargs):
        return None
