Task=input("enter your task: ")
Priority=input("priority high/medium/low: ")
Time_Bound=input("it is time-bound ? (yes/no): ")
match Priority:
    case "high":
        reminder=f"Finish"'{task}'" is a high priority task"
    case "medium":
        reminder=f"reminder:Finish"'{task}'" is a medium priority task"
    case "low":
        reminder=f"Note:" '{task}'"is a low priority task."

        exit()  # Stop the script if an invalid priority is entered

# Add the time-bound condition
if Time_Bound == "yes":
    reminder += " that requires immediate attention today!"
    print(reminder)
elif Time_Bound == "no":
    reminder += " Consider completing it when you have free time."
    print(reminder)


    

