import datetime

def getDayName(a,b):
        day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
        return day[datetime.date(2016,a,b).weekday()]

print(getDayName(5,24))
