import tkinter as tk
import tkinter.ttk as ttk


class TkinterResizeDemoApp:
    """App that creates a window with elements, that resize with the window."""

    def __init__(
        self,
        window: tk.Tk | None = None,
        grid_size: tuple[int, int] = (10, 10)
    ) -> None:
        """
        Create a new instance of `TkinterResizeDemoApp`.

        :param window: If you want, you can provide a custom `Tk` here. Be \
        aware that if you do so, no settings will be applied to `tk` by \
        `__init__()` (this may cause the window to not resize as intended).

        :param grid_size: Defines how many elements will be put on the \
        screen. Defaults to `(10, 10)`. Enter by pattern `(x, y)`.
        """

        # SETUP WINDOW
        # Create a window is None was provided
        user_provided_window = window is not None
        self.tk = window if user_provided_window else tk.Tk()
        # Apply required settings for resizing to the window
        # TODO: Add option to let __init__ configure
        #       the Tk, even if window is None
        if not user_provided_window:
            self.tk.title("Tkinter Resize Demo")
            # The next two lines get explained later in the code
            self.tk.columnconfigure(0, weight=1)  # <- IMPORTANT
            self.tk.rowconfigure(0, weight=1)  # <- IMPORTANT

        # ROOT LEVEL FRAME
        # The root level frame should be the only child of the window
        self.button_grid = ttk.Frame(self.tk, padding=2)
        # sticky="nesw" tells Tk that the Frame should stick to all borders
        # n = NORTH ; e = EAST ; s = SOUTH ; w = WEST
        self.button_grid.grid(column=0, row=0, sticky="nesw")

        # CREATE AND DISPLAY BUTTONS
        # Store the size of the grid
        self.grid_size = grid_size
        # Store the elements in the grid
        self.buttons: list[list[ttk.Button]] = []
        # Create the elements in the grid
        # First for loop is for y, because the list if row-major
        for y in range(self.grid_size[1]):
            # Append row and create elements in columns
            self.buttons.append([])
            for x in range(self.grid_size[0]):
                # Set the weight value of the grid elements to 1, so they can
                # expand. If they were 0 nothing would happen when resizing.
                self.button_grid.columnconfigure(x, weight=1)  # <- IMPORTANT
                self.button_grid.rowconfigure(y, weight=1)  # <- IMPORTANT
                # Create a new button
                self.buttons[y].append(ttk.Button(
                    master=self.button_grid,
                    text=f"x/col={x}\ny/row={y}",
                    command=lambda: print(f"\nx/col={x}\ny/row={y}"),
                    padding=2))
                # Display the button on the screen. Make sure to set sticky.
                self.buttons[y][x].grid(column=x, row=y, sticky="nesw")

    def mainloop(self, n: int = 0) -> None:
        """Starts the application."""
        self.tk.mainloop(n)


if __name__ == "__main__":
    app = TkinterResizeDemoApp()
    app.mainloop()
