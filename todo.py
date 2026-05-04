tasks = []
while True:
    print("\n1. Add a Task")
    print("2. View Tasks")
    print("3. Remove Tasks")
    print("4. Exit")
    choice = input("Enter your choice:")
   
   # Add a Task

    if choice == "1":
        task = input("Enter your task:")
        tasks.append(task)
        print("task added successfully!")
        
    # View Task

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            for i, task in enumerate(tasks):
                print(i,task)

    # Remove Tasks

    elif choice == "3":
        index = int(input("Enter task number to remove: "))
        if index < len(tasks):
            removed = tasks.pop(index)
            print("Removed:", removed)
        else:
            print("Invalid index")

    # Exit Program

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again!")