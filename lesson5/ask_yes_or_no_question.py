# stelle dem Benutzer eine Ja/Nein-Frage (mit beliebigem
# Text) und gib True oder False zurueck!
# Das ist die Version, die wir in der Einheit erstellt haben
#  - siehe ask_yes_or_no_question_advanced.py fuer eine
#    noch etwas verbesserte Version

# Dies ist eine Funktion - sie kann zB in anderen Python-Skripten
# importiert und verwendet werden.
def ask_yes_or_no_question(question_text):
    # frage den Benutzer
    answer = raw_input(question_text)
    if answer.lower() == 'yes' or answer.lower() == 'ja':
        return True
    elif answer.lower() == 'no' or answer.lower() == 'nein':
        return False
    else:
        print 'Ungueltige Eingabe!'

# Programmierer 2
#adult = ask_yes_or_no_question('Bist du volljaehrig?')
#if adult == True:
#    print 'Du darfst Alkohol trinken.'
#elif adult == False:
#    print 'Du darfst keinen Alkohol trinken'
