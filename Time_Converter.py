import math

def Time_Converter(time):
    Seconds = time % 60
    Minutes = time / 60
    Minutes = math.trunc(Minutes)
    Hours = Minutes / 60
    Hours = math.trunc(Hours)
    Minutes = Minutes % 60
    Days = Hours / 24
    Days = math.trunc(Days)
    Hours = Hours % 24
    Weeks = Days / 7
    Weeks = math.trunc(Weeks)
    Days = Days % 7
    print(f'Total Time: {Weeks} week(s), {Days} day(s), {Hours}:{Minutes}:{Seconds}')