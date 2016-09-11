expenses = []

while True:
    expense_type = raw_input('Gib die Art der Ausgabe ein (exit zum Beenden): ')
    if expense_type == 'exit':
        break
    amount = float(raw_input('Gib den Batrag ein: '))
    
    expenses.append({'type': expense_type, 'amount': amount})

for expense in expenses:
    print expense
