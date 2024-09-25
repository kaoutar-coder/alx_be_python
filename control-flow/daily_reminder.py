task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        reminder = f"'{task}' is a {priority} task"
    case "medium":
        reminder = f"'{task}' is a {priority} task"
    case "low":
        reminder = f"'{task}' is a {priority} task"
    case _:
        reminder = f"⚠️ '{task}' has no priority level"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print("Reminder: " + reminder)
else:
    reminder += ". Consider completing it when you have free time."
    print("Note: " + reminder)


