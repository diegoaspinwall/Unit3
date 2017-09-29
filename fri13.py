#Diego Aspinwall
#9-29-17
#fri13.py

from calendar import weekday
from datetime import date

yNow = date.today().year
mNow = date.today().month
dNow = date.today().day
wdnow = weekday(yNow,mNow,dNow)

y = 0
m = 0
i=0
while i<=10:
    if weekday(yNow,mNow,13)==4:
        print(mNow, '13', yNow)
        i+=1
    while m<=12:
        m+=1
        if weekday(yNow, mNow+m,13)==4:
            print(mNow+m, '13', yNow)
            

print(yNow, mNow, dNow, wdnow)