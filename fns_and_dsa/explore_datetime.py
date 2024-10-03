from datetime import datetime

def display_current_datetime():
    current_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted date and time:", current_date)
display_current_datetime()

def calculate_future_date():
    current_date= datetime.datetime.now()

    days=int(input("Enter the number of days to add to the current date:"))

    future_date = current_date + datetime.timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S") 

    print(" future date :",formatted_future_date )

calculate_future_date()


