secret = 10
guess = -1

while secret != guess:
    guess = int(raw_input('Try to guess the number: '))

    if guess == secret:
        print 'Correct!'
    else:
        print 'Wrong!'
