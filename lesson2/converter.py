print 'Welcome to the unit converter - convert km to miles'

# wir verwenden eine "unendliche Schleife", die nur durch "break" verlassen wird
while True:

    # Frage nach Anzahl an km und wandle in Meilen um
    len_km = float(raw_input('Enter number of kilometers: '))
    len_miles = len_km / 1.06
    print len_km, 'km are', len_miles, 'miles'

    # setze 'answer' auf irgendetwas ausser 'y' oder 'n'
    answer = 'blabla'
    # frage den Benutzer so lange, bis seine Antwort 'y' oder 'n' ist
    while answer != 'y' and answer != 'n':
        answer = raw_input('Do you want to convert another number? (y/n)')
    # hier ist die Schleife zu Ende - das heisst der Benutzer hat entweder
    # 'y' oder 'n' geantwortet!
    if answer == 'n':
        # wenn er 'n' geantwortet hat, hoere auf
        break
    # wenn er 'y' geantwortet hat, beginnt jetzt die while-Schleife erneut (bei Zeile 6)
