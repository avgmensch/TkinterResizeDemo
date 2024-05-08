import tkinter as tk
import tkinter.ttk as ttk


class TkinterResizeDemoApp:
    def __init__(self, window: tk.Tk | None = None) -> None:
        user_provided_window = window is not None
        self.tk = window if user_provided_window else tk.Tk()
        if not user_provided_window:
            self.tk.title("Tkinter Resize Demo")

    def mainloop(self, n: int = 0) -> None:
        self.tk.mainloop(n)


if __name__ == "__main__":
    app = TkinterResizeDemoApp()
    app.mainloop()
