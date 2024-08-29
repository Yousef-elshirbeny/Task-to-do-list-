import datetime

def add_task(tasks):
    """Add a new task."""
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            task_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            print("Incorrect date format, please try again.")
            continue  # Request the date again
        
        today = datetime.date.today()
        if task_date < today:
            print("The date must be today or later.")
            continue  # Request the date again
        
        break  # Exit the loop when the date is valid

    task_day = task_date.strftime('%A')  # Get the day of the week from the date
    
    while True:
        task_description = input("Enter task description: ").strip()
        if not task_description:
            print("You must enter a description for the task.")
            continue  # Request the description again
        break  # Exit the loop when the description is valid

    task = {
        'date': task_date.isoformat(),
        'day': task_day,
        'description': task_description
    }
    tasks.append(task)
    print("Task added successfully!")

    # Prompt user to return to the menu
    return_to_menu()

def view_tasks(tasks):
    """View tasks for today."""
    today = datetime.date.today().isoformat()
    print(f"\nTasks for today {today}:")
    tasks_for_today = [task for task in tasks if task['date'] == today]
    if not tasks_for_today:
        print("No tasks for today.")
    else:
        for task in tasks_for_today:
            print(f"{task['day']}: {task['description']}")

    # Prompt user to return to the menu
    return_to_menu()

def view_all_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print("No tasks available.")
        return

    sorted_tasks = sorted(tasks, key=lambda x: x['date'])  # Sort tasks by date
   
    print("\nList of all tasks:")
    current_date = None
    for task in sorted_tasks:
        if task['date'] != current_date:
            if current_date is not None:
                print()  # Separator between dates
            current_date = task['date']
            print(f"\n{current_date} ({task['day']}):")
        print(f"  - {task['description']}")

    # Prompt user to return to the menu
    return_to_menu()

def delete_task(tasks):
    """Delete tasks for a specific date or all tasks."""
    while True:
        print("1. Delete tasks for a specific date")
        print("2. Delete all tasks")
        print("3. Return to menu")
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            while True:
                date_str = input("Enter the date (YYYY-MM-DD) of tasks to delete: ")
                try:
                    delete_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                except ValueError:
                    print("Incorrect date format, please try again.")
                    continue  # Request the date again if format is incorrect

                # Check if there are tasks for the given date
                tasks_for_date = [task for task in tasks if task['date'] == delete_date.isoformat()]
                
                if not tasks_for_date:
                    print("No tasks found for the specified date. Please enter a different date.")
                    continue  # Request the date again if no tasks are found
                
                # If tasks are found, proceed with deletion
                tasks_before_deletion = len(tasks)
                
                tasks[:] = [task for task in tasks if task['date'] != delete_date.isoformat()]

                if len(tasks) == tasks_before_deletion:
                    print("No tasks found for the specified date.")
                else:
                    print(f"Tasks for {delete_date} have been deleted.")
                break  # Exit the loop once the task deletion is done

        elif choice == '2':
            tasks.clear()
            print("All tasks have been deleted.")
            break  # Exit the loop once all tasks are deleted

        elif choice == '3':
            break  # Return to menu

        else:
            print("Invalid choice, please select a valid option.")

    # Prompt user to return to the menu
    return_to_menu()

def return_to_menu():
    """Prompt user to return to the menu."""
    while True:
        return_choice = input("\n1. Return to previous step\n2. Return to main menu\nChoose an option: ").strip()
        if return_choice == '1':
            return  # Go back to the previous step
        elif return_choice == '2':
            return  # Exit to main menu
        else:
            print("Invalid choice, please select a valid option.")

def print_menu():
    """Print the list of options."""
    print("\n1. Add Task")
    print("2. View Tasks for Today")
    print("3. View All Tasks")
    print("4. Delete Tasks")
    print("5. Exit")

def main():
    """Main function for interacting with the user."""
    tasks = []  # Define tasks list

    while True:
        print_menu()
        choice = input("Choose an action: ").strip()
        
        if choice == '1':
            while True:
                add_task(tasks)
                if input("\nDo you want to add another task? (y/n): ").strip().lower() != 'y':
                    break  # Return to main menu
        elif choice == '2':
            while True:
                view_tasks(tasks)
                if input("\nDo you want to view today's tasks again? (y/n): ").strip().lower() != 'y':
                    break  # Return to main menu
        elif choice == '3':
            while True:
                view_all_tasks(tasks)
                if input("\nDo you want to view all tasks again? (y/n): ").strip().lower() != 'y':
                    break  # Return to main menu
        elif choice == '4':
            while True:
                delete_task(tasks)
                if input("\nDo you want to delete more tasks? (y/n): ").strip().lower() != 'y':
                    break  # Return to main menu
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()





