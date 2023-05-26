from datetime import datetime, timedelta

def check_date_difference():
    from_date = input("Enter the 'from' date (yy-mm-dd): ")
    to_date = input("Enter the 'to' date (yy-mm-dd): ")
    difference = int(input("Enter the difference in days: "))
    
    date_format = '%y-%m-%d'
    date1 = datetime.strptime(from_date, date_format)
    date2 = datetime.strptime(to_date, date_format)
    delta = date2 - date1
    
    if delta < timedelta(days=difference):
        return True
    else:
        return False
result = check_date_difference()
print(result)
