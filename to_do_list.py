def get_menu():
	print('''
		1. Add a task
		2. View all tasks
		3. Mark a task as complete
		4. Delete a task
		5. Exit
		''')


def get_add_task(task:str)->str:
	if task == " ":
		return 'invalid input'
	return 'valid input'

def get_view_task():
	view_display = []
	return view_display

def main():
	
	display = get_view_task()
	while True:

		get_menu()
		enter_choice = input('enter choice between 1-5: ')
	
		if enter_choice == '1':
			while True:
				enter_task = input('Enter task: ')
				tasks = get_add_task(enter_task)
				if tasks == 'valid input':
					break
				print('invalid input. please try again')
			displays = {'task':enter_task}
			display.append(displays)
			print('expenses added succesfully')
	
		if enter_choice == '2':
				for task in display:
					print(task['task'])

		if enter_choice == '3':
				mark_tasks = input('mark task: ')
				for task in display:
					if num[task] == mark_tasks:
						print(num['task*'])



















main()