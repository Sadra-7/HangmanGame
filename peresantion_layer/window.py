from ttkbootstrap import *

class Window(Window):
    def __init__(self , weight = 300 , height = 700):
        super().__init__(themename="cyborg" , title='Hangman')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0 , weight=1)


        self.geometry(f"{weight}x{height}")

    def show(self):
        self.mainloop()