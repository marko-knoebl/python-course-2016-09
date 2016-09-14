# stelle dem Benutzer eine Ja/Nein-Frage (mit beliebigem
# Text) und gib True oder False zurueck!

# Programmierer 1
def ask_yes_or_no_question(question_text):
    # frage den Benutzer
    answer = raw_input(question_text)
    if answer.lower() == 'yes' or answer.lower() == 'ja':
        return True
    elif answer.lower() == 'no' or answer.lower() == 'nein':
        return False
    else:
        print 'Ungueltige Eingabe!'
        # frage erneut - rufe die gleiche Funktion wieder auf
        # die Funktion wird im Endeffekt entweder True oder
        #  False zurueckgeben
        answer = ask_yes_or_no_question(question_text)
        return answer

# Programmierer 2
adult = ask_yes_or_no_question('Bist du volljaehrig?')
if adult == True:
    print 'Du darfst Alkohol trinken.'
elif adult == False:
    print 'Du darfst keinen Alkohol trinken'
