#Diego Aspinwall
#9-29-17
#fri13.py

from calendar import weekday
from datetime import date

yNow = date.today().year
mNow = date.today().month
dNow = date.today().day
wdnow = weekday(year,month,day)

i=0

while i<=10:
    
print(yNow, mNow, dNow, wdnow)