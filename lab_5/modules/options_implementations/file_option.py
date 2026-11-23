import json
import tkinter as tk
from tkinter import filedialog, messagebox

from .option import BaseDropdownOptions
from ..shapes_implementations import ShapesFileDataCb


class FileOption(BaseDropdownOptions):
    _ICON_SIZE = 24

    def __init__(self, root: tk.Misc, get_shapes_for_save_cb: ShapesFileDataCb):
        super().__init__(
            root,
            {
                "Save": lambda _: self.save_file(),
                "Close": lambda _: root.destroy(),
            },
            ["Save", "Close"],
        )
        self._get_shapes_for_save_cb = get_shapes_for_save_cb
        self.button = self._create_button(
            "file_option.png",
            lambda: self._menu.post(root.winfo_rootx() + 10, root.winfo_rooty() + 30),
        )

    def render(self, parent: tk.Misc | None = None) -> None:
        self._render_buttons([self.button], parent, (0, 8))

    def open_file(self, *args, **kwargs):
        return None

    def save_file(self) -> None:
        file_path = filedialog.asksaveasfilename(
            parent=self._root,
            title="Save drawing",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
        )
        if not file_path:
            return

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(
                    {"shapes": self._get_shapes_for_save_cb()},
                    file,
                    indent=2,
                )
                file.write("\n")
        except OSError as error:
            messagebox.showerror(
                "Save failed",
                f"Could not save the drawing:\n{error}",
                parent=self._root,
            )
