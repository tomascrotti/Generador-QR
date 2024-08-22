import tkinter as tk

class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("420x180")

if __name__ == '__main__':
    app = Ventana()
    app.mainloop()