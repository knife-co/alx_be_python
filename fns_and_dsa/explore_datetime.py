from datetime import datetime,timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_format_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"current date and time: {current_format_date}")


def  calculate_future_date():
    display_current_datetime()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    formatted_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_date} ")

calculate_future_date()






