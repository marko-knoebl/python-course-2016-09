from random import randint

# Diese Funktion erstellt eine Liste von
# Zufallszahlen von 1 bis 45.
# Der Parameter 'anzahl' gibt die Laenge der Liste an.
def generate_random_numbers(anzahl):
    random_numbers = []
    # fuelle die Liste mit Zufallszahlen
    for i in range(anzahl):
        rand_num = randint(1, 45)
        random_numbers.append(rand_num)
    # gib die Liste zurueck
    return random_numbers

def test_generate_random_numbers():
    # erstelle neue Liste von Zufallszahlen der Laenge 5
    numbers = generate_random_numbers(5)
    # hat der Befehl das richtige gemacht?
    if len(numbers) != 5:
        print 'Error: wrong length'
    if numbers[0] > 45:
        print 'Error: first number is too high'

test_generate_random_numbers()

print 'Welcome to the Lottery numbers generator.'
anzahl = int(raw_input('Please enter how many random numbers would you like to have:'))

numbers = generate_random_numbers(anzahl)
print numbers
