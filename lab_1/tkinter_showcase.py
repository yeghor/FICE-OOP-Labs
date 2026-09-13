import tkinter as tk
from string import Template

"""
screenName (opt) - name of the display for UNIX systems
baseName (opt) - base name of the application, default - scrpipt name
className (opt) - Defines the name of the window class (used for styling and window manager settings)
useTk (optional): A boolean that tells whether to initialize the Tk subsystem (usually left as default 1)
"""
root = tk.Tk(
    screenName=None,
    baseName=None,
    className="Tk",
    useTk=1,
)
root.geometry("900x450")
root.minsize(100, 100)
root.maxsize(1920, 1080)

"""
Label used for displaying text of images
"""
label = tk.Label(root, text="Hello World!")
label.pack()


"""
Buttons!
"""
def counter_decorator(func: callable) -> callable:
    counter_template = Template("Count: $counter")
    counter = 0

    counter_label = tk.Label(root, text=counter_template.substitute({"counter": counter}))
    counter_label.pack()

    def wrapper(*args, **kwargs): 
        nonlocal counter

        counter += 1
        func(counter_label, counter_template, counter, *args, **kwargs)

    return wrapper

@counter_decorator
def button_counter_callback(label: tk.Label, counter_template: Template, counter: int) -> None:
    label.configure(text=counter_template.substitute({"counter": counter}))

counter_button = tk.Button(root, text="Hello!", width=25, command=button_counter_callback)
counter_button.pack()

kill_buttom = tk.Button(root, text="KILL", width=25, command=root.destroy)
kill_buttom.pack()

"""Entry"""

# # cannot use grid if pack is already used
# tk.Label(root, text="First Name").grid(row=0, column=0)
# tk.Label(root, text="Last Name").grid(row=1, column=0)

# entry1 = tk.Entry(root)
# entry2 = tk.Entry(root)

# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)

# TopLevel external windows

def open_context_window_cb(name: str):
    toplevel_window = tk.Toplevel(root)
    tk.Label(toplevel_window, text=name).pack()
    tk.Button(toplevel_window, text="Close", command=toplevel_window.destroy).pack()


context_window_button = tk.Button(root, text="Open context window", command=lambda: open_context_window_cb("Context window №1"))
context_window_button.pack()

if __name__ == "__main__":
    # starts event loop, window will accept user commands until the window is closed
    tk.mainloop()
