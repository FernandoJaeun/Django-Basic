import sys, os
import calendar
import datetime

folderPath = "C:/Users/leeja/OneDrive/바탕 화면/하루일기/2020/9"
fileContext = "전 날 가장 행복했던 일:\n전 날 가장 우울했던 일:\n앞으로 다짐:"

thisYear = datetime.datetime.today().year
thisMonth =  datetime.datetime.today().month

startDayOfThisMonth = int(calendar.monthrange(thisYear,thisMonth)[0])
endDayOfThisMonth = int(calendar.monthrange(thisYear,thisMonth)[1])+1

day = 2

for day in range(endDayOfThisMonth):
    try:
        file = open(f"{folderPath}/{day}.txt","w")
        file.write(fileContext)
        file.close()
    except:
        pass