import random

import Tkinter
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text='Guess the secret number!')
greeting.pack()

secret = random.randint(1, 100)

guess = Tkinter.Entry(window)
guess.pack()

def check_guess():
    try:
        user_guess = int(guess.get())
    except ValueError:
        result_text = 'Enter a number!'
    else:
        if user_guess == secret:
            result_text = 'Correct!'
        elif user_guess > secret:
            result_text = 'Wrong! Your guess is too high!'
        else:
            result_text = 'Wrong! Your guess is too low!'

    tkMessageBox.showinfo('Result', result_text)

submit = Tkinter.Button(window, text='submit', command=check_guess)
submit.pack()


window.mainloop()
