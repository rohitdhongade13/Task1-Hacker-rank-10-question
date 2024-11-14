# find the year is leap year or not 
def is_leap(year):
    leap = True
    noLeap = False
    if (year % 4 == 0) and (year % 400 == 0 or year % 100 !=0 ):
        return leap
    else:
        return noLeap
    
year = int(input())
print(is_leap(year))