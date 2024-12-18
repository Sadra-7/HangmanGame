from peresantion_layer.window import Window
from .start_menu import Start_frame
from .game import Game

class View:
    def __init__(self):
        self.window = Window()

        self.frames = {}

        self.frame('game' , Game(self , self.window))
        self.frame('start' , Start_frame(self , self.window))


        self.window.show()


    def frame(self , name , frame):
        self.frames[name] = frame
        self.frames[name].grid(row = 0 , column = 0 , sticky = "nsew")

    def switch(self , frame_name):
        self.frames[frame_name].tkraise()
        return self.frames[frame_name]

    def reset (self):
        Game(self , self.window)