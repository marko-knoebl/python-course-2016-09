# Frage den Benutzer wiederholt, ob er ein todo-item hinzufuegen will
# schreibe die items in eine liste

task_list = []

while True:
    new_item_name = raw_input('Gib ein neues TODO-item ein:')
    new_item_done = raw_input('Ist es erledigt? (J)')
    if new_item_done == 'J':
        new_item = {'name': new_item_name, 'done': True}
    else:
        new_item = {'name': new_item_name, 'done': False}
    task_list.append(new_item)
    
    cancel = raw_input('Willst du abbrechen? (J)')
    if cancel == 'J':
        break

# greife auf das 0-te Element zu
#print task_list[0]

# kompliziertere Version:
#for i in range(len(task_list)):
#    print task_list[i]

# einfacher:

print 'Du hast folgende TODOs angelegt:'
for task in task_list:
    print 'Todo:', task['name']
    print 'erledigt:', task['done']
