def create_name(first: str, last: str):
    return first + last
    
def day_of_creation(day: str, month: str, year: str):
    if len(day == 1):
        day = "0" + day
    if len(month==1):
        month = "0" + month
    if len(year==2):
        year = "20"