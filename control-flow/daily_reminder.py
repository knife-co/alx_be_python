Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
Time_bound = input("Is it time_bound? (yes/no): ")

match priority:
    case "high": 
        if Time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today! ")
        else:
            print(f"Reminder: {task} is a high priority task that can be done later ")
    case "medium":
        if Time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires attention today! ")
        else:
            print(f"Reminder: {task} is a medium priority that can be done later ")
    case "low":
        if Time_bound == "yes":
            print(f"Reminder: {task} is a low priority task that requires immediate attention today! ")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time")
    case _:
        print("Wrong priority input")

