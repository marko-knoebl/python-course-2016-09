# addiere Zwei Zahlen (int)
print 2 + 3
# fuege zwei Texte zusammen (str)
print '2' + '3'

# frage nach der Rechenoperation: + oder -
operation = raw_input('Welche Operation willst du durchfuehren? (+, -, * oder /)')

# frage nach zwei Zahlen
zahl1 = raw_input('Gib die erste Zahl ein:')
zahl2 = raw_input('Gib die zweite Zahl ein:')

# wandle den Text (der hoffentlich Zahlen enthaelt) in Zahlen (int) um
zahl1_int = int(zahl1)
zahl2_int = int(zahl2)

# Ueberpruefe die einzelnen Faelle:
# Was hat der Benutzer als Operation angegeben?
if operation == '+':
    print 'Du hast + gewaehlt'
    print 'Das Ergebnis lautet', zahl1_int + zahl2_int
elif operation == '-':
    print 'Du hast - gewaehlt'
    print 'Das Ergebnis lautet', zahl1_int - zahl2_int
elif operation == '*':
    print 'Du hast * gewaehlt'
    print 'Das Ergebnis lautet', zahl1_int * zahl2_int
elif operation == '/':
    print 'Du hast / gewaehlt'
    print 'Das Ergebnis lautet', zahl1_int * zahl2_int
else:
    print 'Ungueltige Operation. Waehle +, -, * oder /'
