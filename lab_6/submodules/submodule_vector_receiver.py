import json
import math
import queue
import threading
import tkinter as tk
from tkinter import messagebox, ttk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sorted Vector")
        self._commands = queue.Queue()

        frame = ttk.Frame(self, padding=8)
        frame.pack(fill=tk.BOTH, expand=True)
        self._table = ttk.Treeview(frame, columns=("value",), show="headings")
        self._table.heading("value", text="Values")
        self._table.column("value", anchor=tk.W, width=150)
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self._table.yview)
        self._table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self._table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self._refresh_from_clipboard()

        threading.Thread(target=self._read_commands, daemon=True).start()
        self.after(100, self._process_commands)

    def _read_commands(self):
        while True:
            try:
                command = input(f"Enter command: ").strip().lower()
            except EOFError:
                return
            self._commands.put(command)

    def _process_commands(self):
        while not self._commands.empty():
            command = self._commands.get_nowait()
            if command == "refresh":
                self._refresh_from_clipboard()
            elif command:
                print("Unknown command. Use 'refresh' to read the clipboard.", flush=True)
        self.after(100, self._process_commands)

    def _refresh_from_clipboard(self):
        try:
            values = json.loads(self.clipboard_get())
            if not isinstance(values, list) or any(
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                for value in values
            ):
                raise ValueError("Clipboard must contain a JSON array of finite numbers.")
            vector = sorted(float(value) for value in values)
        except (tk.TclError, json.JSONDecodeError, ValueError, OverflowError) as error:
            messagebox.showerror("Invalid clipboard", str(error), parent=self)
            return

        self._table.delete(*self._table.get_children())
        for value in vector:
            self._table.insert("", "end", values=(value,))


if __name__ == "__main__":
    Window().mainloop()
