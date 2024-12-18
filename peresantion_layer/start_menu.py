from ttkbootstrap import *



class Start_frame(Frame):
    def __init__(self ,view , window):
        super().__init__(window)

        self.grid_columnconfigure(0, weight=1)

        self.view = view



        self.welcome = Label(self , text='Welcome to HANGMAN')
        self.welcome.grid(row = 0 , column = 0 , padx = 10 , pady = 10 )

        self.start_b =Button(self ,text='Start Game' , command=self.start_clicked, style = "success")
        self.start_b.grid(row = 1 , column = 0 , padx = 10 , pady = 10 , sticky = "nsew")

        self.exit_b =Button(self ,text='Exit Game' , command=self.exit , style = "danger")
        self.exit_b.grid(row = 2 , column = 0 , padx = 10 , pady = 10 , sticky = "nsew")

    def start_clicked(self):
        self.view.switch('game')

    def exit(self):
        self.view.window.destroy()



