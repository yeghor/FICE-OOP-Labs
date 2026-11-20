from abc import ABC, abstractmethod
from math import ceil
from pathlib import Path
from typing import Any, Callable, Dict, List
import tkinter as tk


class BaseOption(ABC):
    _ICON_SIZE = 16
    _ICONS_DIR = Path(__file__).parent / "icons"

    def __init__(self, root: tk.Misc, icon_size: int | None = None):
        self._root = root
        self._icon_size = self._ICON_SIZE if icon_size is None else icon_size
        self._images: List[tk.PhotoImage] = []

    def _load_icon(self, icon_name: str | None) -> tk.PhotoImage | None:
        if icon_name is None:
            return None

        icon_path = self._ICONS_DIR / icon_name
        if not icon_path.exists():
            return None

        image = tk.PhotoImage(master=self._root, file=str(icon_path))
        factor = max(1, ceil(max(image.width(), image.height()) / self._icon_size))
        image = image.subsample(factor, factor)
        self._images.append(image)
        return image

    def _create_button(
        self,
        icon_name: str | None,
        command: Callable[[], None],
        text: str | None = None,
    ) -> tk.Button:
        image = self._load_icon(icon_name)
        if image is None:
            return tk.Button(self._root, text=text or "", command=command)

        return tk.Button(
            self._root,
            image=image,
            width=self._icon_size,
            height=self._icon_size,
            text=text,
            command=command,
        )

    def _render_buttons(
        self, buttons: List[tk.Button], parent: tk.Misc | None, padx: tuple[int, int]
    ) -> None:
        target = parent if parent is not None else self._root
        for button in buttons:
            button.pack(in_=target, side=tk.LEFT, padx=padx, pady=4)

    @abstractmethod
    def render(self, parent: tk.Misc | None = None) -> None:
        ...


class BaseDropdownOptions(BaseOption):
    def __init__(
        self,
        root: tk.Misc,
        options_cbs: Dict[str, Callable[[Any], None]],
        readable_options: List[str] | None = None,
    ):
        super().__init__(root)
        self._label = "Menu"
        self._options = (
            list(options_cbs.keys()) if readable_options is None else readable_options
        )
        self._options_cbs = options_cbs
        self._menu = tk.Menu(root, tearoff=0)
        self._attach_menu_items()

    def _attach_menu_items(self) -> None:
        for option in self._options:
            self._menu.add_command(
                label=option, command=lambda value=option: self._select_option(value)
            )

    def _select_option(self, option: str) -> None:
        callback = self._options_cbs.get(option)
        if callback is not None:
            callback(option)

    @property
    def chosen_option(self) -> str:
        return self._label
    