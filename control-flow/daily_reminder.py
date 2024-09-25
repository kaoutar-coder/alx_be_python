
Task = input("enter your task: ")
Priority = input("priority (high/medium/low): ")
time_bound = input("it is time-bound ? (yes/no): ")   

match Priority:
    case "high":
        reminder=f"Finish"'{Task}'" is a high priority task"
    case "medium":
        reminder=f"reminder:Finish"'{task}'" is a medium priority task"
    case "low":
        reminder=f"Note:" '{Task}'"is a low priority task."
    case _:
        reminder = f"⚠️ '{Task}' has no priority level"

# Add the time-bound condition
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(reminder)
elif time_bound == "no":
    reminder += " Consider completing it when you have free time."
    print(reminder)


    

