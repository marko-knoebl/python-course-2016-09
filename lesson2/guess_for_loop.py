secret = 10
guess = -1

for i in range(4):
    guess = int(raw_input('Try to guess the number: '))

    if guess == secret:
        print 'Correct!'
        break
    else:
        print 'Wrong!'
