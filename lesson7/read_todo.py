class Task(object):
    # Initialisiert ein Objekt der Klasse 'Task'
    # Hier koennen Name, Status und Datum 'uebergeben' werden
    def __init__(self, task_name, status, due_date):
        # Speichere die Daten ins Objekt
        #   (das Objekt heisst immer 'self')
        self.task_name = task_name
        self.status = status
        self.due_date = due_date
    
    # Verwandelt das Objekt in einen String
    # (wird bei print automatisch aufgerufen)
    def __str__(self):
        return 'Task: ' + self.task_name

def main():
    todo_file = open('toy-company-todo.txt', 'r+')

    task_list = []

    for line in todo_file:
        task_name, status, due_date = line.split(';')
        task = Task(task_name, status, due_date)
        task_list.append(task)

    list_of_tasks(task_list)
    update_tasks(task_list)
    todo_file.close()

def list_of_tasks(task_list):
    # gibt Tasks formatiert aus:
    for index, task in enumerate(task_list):
        print index, ':', task.task_name
        print task.status
        print task.due_date

def update_tasks(tasks):
    list_of_tasks(tasks)
    
    task_index = int(raw_input('Which task do you want to edit?'))
    print 'You are editing task', task_index
    
    new_name = raw_input('Enter a new name: ')
    tasks[task_index].task_name = new_name
    print 'Your task has been changed'
    list_of_tasks(tasks)

if __name__ == '__main__':
    main()
