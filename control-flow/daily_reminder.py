task=input("enter your task: ")
priority=input("priority high/medium/low: ")
time_bound=input("it is time-bound ? (yes/no): ")
match priority:
    case "high":
        reminder=f"Finish"+task+" is a high priority task"
    case "medium":
        reminder=f"reminder:Finish"+task+" is a medium priority task"
    case "low":
        reminder=f"Note:"+ task + "is a low priority task."

        exit()  # Stop the script if an invalid priority is entered

# Add the time-bound condition
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(reminder)
elif time_bound == "no":
    reminder += " Consider completing it when you have free time."
    print(reminder)


    

