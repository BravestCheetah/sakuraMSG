import tkinter as tk

class main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.add_widgets()
        self.geometry("800x1200")

    def add_widgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.rowconfigure(0, weight=9)
        self.rowconfigure(1, weight=1)

        

if __name__ == "__main__":
    app = main()
    app.mainloop()