# importiere aus der Datei "ask_yes_or_no_question.py" die
# gleichnamige Funktion - die andere Datei muss im gleichen
# Verzeichnis abgespeichert sein
from ask_yes_or_no_question import ask_yes_or_no_question

license = ask_yes_or_no_question('Hast du einen Fuehrerschein?')
if license == True:
    print 'Gute Fahrt!'
elif license == False:
    print 'Stop!'
