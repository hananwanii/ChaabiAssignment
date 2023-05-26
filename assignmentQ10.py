from datetime import datetime, timedelta

def get_previous_date():
    date = input("Enter the date (yy-mm-dd): ")
    n = int(input("Enter the number of days: "))
    
    date_format = '%y-%m-%d'
    current_date = datetime.strptime(date, date_format)
    previous_date = current_date - timedelta(days=n)
    
    return previous_date.strftime(date_format)
result = get_previous_date()
print(result)
