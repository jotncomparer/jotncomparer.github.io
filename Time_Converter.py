import math

#Pass in time in seconds
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
    if Weeks > 4:
        Months = Weeks / 4
        Months = math.trunc(Months)
        Weeks = Weeks % 4
        if Months > 12:
            Years = Months / 12
            Years = math.trunc(Years)
            Months = Months % 12
            return f'{Years} years(s) {Months} month(s) {Weeks} week(s), {Days} day(s), {Hours}:{Minutes}:{Seconds}'
        else:
            pass
        return f'{Months} month(s) {Weeks} week(s), {Days} day(s), {Hours}:{Minutes}:{Seconds}'
    else:
        return f'{Weeks} week(s), {Days} day(s), {Hours}:{Minutes}:{Seconds}'

