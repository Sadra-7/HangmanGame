from ttkbootstrap import *
from ttkbootstrap.dialogs import Messagebox
from common_layer.hangman_create import Char_H
import time

from business_layer.business import Business
class Game (Frame):
    def __init__(self , view , window):
        super().__init__(window)

        self.business = Business()
        self.char_hangman = Char_H()
        self.current_list = []
        self.wrong_letters = []
        self.grid_columnconfigure(0 , weight=1)
        self.grid_columnconfigure(1 , weight=1)

        self.view = view

        self.title = Label(self , text="Find current name!")
        self.title.grid(row = 0 , column = 0 , padx = 10 , pady = 10 , columnspan = 2)

        self.current_word = Label(self , text=self.word_len())
        self.current_word.grid(row=1, column=0, pady=10 , padx = 10 , columnspan = 2)

        self.word_label = Label(self , text="Guess a word : ")
        self.word_label.grid(row=2, column=0, pady=10 , padx = 10 ,sticky = 'w')

        self.word_entry = Entry(self , width=2 , style="info")
        self.word_entry.grid(row = 2 , column = 1 , padx = 10 , pady = 10, sticky = 'nsew')

        self.word_entry.bind("<Return>" , self.guess_check)

        self.submit_button = Button(self , text="Submit" , style="info")
        self.submit_button.grid(row = 3 , column = 0 , padx = 10 , pady = 10 ,sticky = 'nsew' , columnspan = 2)

        self.submit_button.bind("<Button-1>", self.guess_check)

        self.wrong_label = Label(self, text="Wrong Answers : ")
        self.wrong_label.grid(row=4, column=0, pady=10, padx=10, sticky = 'w')

        self.hangman_label = Label(self, text=self.char_hangman.character()[0])
        self.hangman_label.grid(row=5, column=0, pady=10, padx=10, columnspan=2)

        self.restart_button = Button(self , text="Restart" , command=self.restart_game , style = "secondary")
        self.restart_button.grid(row=7, column=0, pady=10, padx=10, columnspan=2 , sticky = "nsew")

        self.back_button = Button(self , text="Back" , command = self.back , style="danger")
        self.back_button.grid(row=8, column=0, pady=10, padx=10, columnspan=2 , sticky = "nsew")

        self.answer_button = Button(self , text="Show Answer" , style="warning" , command=self.answer)
        self.answer_button.grid(row = 9 , column = 0 , padx = 10 , pady = 10 ,sticky = 'nsew' , columnspan = 2)


    def word_len(self):
        self.word = self.business.get_random_name()
        self.letter_len = []

        len_word = len(self.word)
        for i in range(len_word):
            self.letter_len.append("_")

        return self.letter_len

    def guess_check(self  ,event):
        list_letters = self.business.letter_list

        guess = self.word_entry.get().upper()
        if len(guess) >= 2 or guess not in list_letters:
            self.word_entry.delete(0 , END)
            Messagebox.show_error(message="You should use one letter!")
        else:

            if guess in self.word:
                counter = 0
                for i in self.word:
                    if self.letter_len[counter] == "_":
                        if guess == i:

                                self.letter_len[counter] = i

                        else:
                            self.letter_len[counter] = "_"

                    counter+=1
                self.current_word.destroy()
                self.current_word = Label(self, text=self.letter_len)
                self.current_word.grid(row=1, column=0, pady=10, padx=10, columnspan=2)

                current_name = (''.join(self.letter_len))
                if current_name == self.word:
                    self.word_entry.delete(0, END)
                    self.letter_len.clear()

                    Messagebox.show_info(message="Congratulation!\nYou Win!")
                    self.restart_game()



                else:
                    self.word_entry.delete(0, END)
            else:
                if guess in self.wrong_letters:
                    Messagebox.show_error(message="You wrote this letter!")
                    self.word_entry.delete(0, END)
                else:
                    self.wrong_letters.append(guess)

                    self.wrong = Label(self, text=self.wrong_letters)
                    self.wrong.grid(row=4, column=1, pady=10, padx=10, columnspan=2, sticky = 'nsew')

                    self.hangman_label2 = Label(self, text=self.char_hangman.character()[len(self.wrong_letters)])
                    self.hangman_label2.grid(row=5, column=0, pady=10, padx=10, columnspan=2)
                    self.word_entry.delete(0, END)
                    if len(self.wrong_letters) == 7:
                        Messagebox.show_error(message=f"You lose!\n{self.char_hangman.character()[7]}")
                        self.restart_game()


    def restart_game(self):
        try:
            self.current_word.destroy()
            self.current_word = Label(self, text=self.word_len())
            self.current_word.grid(row=1, column=0, pady=10, padx=10, columnspan=2)

            self.wrong_letters.clear()
            self.hangman_label = Label(self, text=self.char_hangman.character()[0])
            self.hangman_label.grid(row=5, column=0, pady=10, padx=10, columnspan=2)

            self.wrong.destroy()
            self.wrong = Label(self, text=self.wrong_letters)
            self.wrong.grid(row=4, column=1, pady=10, padx=10, columnspan=2, sticky='nsew')
            self.word_answer.destroy()


        except:

            Messagebox.show_info(message="The name changed")
            self.answer()
            self.word_answer.destroy()


    def back(self):
        self.view.switch("start")

    def answer(self):
        self.word_answer = Label(self , text=f'Answer : {self.word}')
        self.word_answer.grid(row=10, column=0, pady=10, padx=10, columnspan=2)
