import tkinter as tk
from modules import Canvas, Options
from typing import List, Any

class App(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self._canvas = Canvas(self)
        self._options = Options(self)

    def shape_select_cb():
        pass

    def shape_created():
        pass

    def file_action():
        pass



if __name__ == "__main__":
    App(screenName="canvas", baseName="lab-2").mainloop()