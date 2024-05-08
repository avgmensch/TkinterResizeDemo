import tkinter as tk
import tkinter.ttk as ttk


class TkinterResizeDemoApp:
    def __init__(
            self,
            window: tk.Tk | None = None,
            grid_size: tuple[int, int] = (10, 10)
    ) -> None:

        # Setup window
        user_provided_window = window is not None
        self.tk = window if user_provided_window else tk.Tk()
        if not user_provided_window:
            self.tk.title("Tkinter Resize Demo")
            self.tk.columnconfigure(0, weight=1)
            self.tk.rowconfigure(0, weight=1)

        # Root level frame
        self.button_grid = ttk.Frame(self.tk, padding=2)
        self.button_grid.grid(column=0, row=0, sticky="nesw")

        # Create buttons
        self.grid_size = grid_size
        self.buttons: list[list[ttk.Button]] = []
        for y in range(self.grid_size[1]):
            self.buttons.append([])
            for x in range(self.grid_size[0]):
                self.button_grid.columnconfigure(x, weight=1)
                self.button_grid.rowconfigure(y, weight=1)
                self.buttons[y].append(ttk.Button(
                    master=self.button_grid,
                    text=f"x/col={x}\ny/row={y}",
                    command=lambda: print(f"\nx/col={x}\ny/row={y}"),
                    padding=2))
                self.buttons[y][x].grid(column=x, row=y, sticky="nesw")

    def mainloop(self, n: int = 0) -> None:
        self.tk.mainloop(n)


if __name__ == "__main__":
    app = TkinterResizeDemoApp()
    app.mainloop()
