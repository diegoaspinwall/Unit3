#Diego Aspinwall
#10-2-17
#changeComputerLoop.py

centtotal = int(input('Input number of cents: '))

quarters = 0
while centtotal-25>=25:
    quarters+=1
    centtotal=centtotal-25
"""
dimes = d
(centtotal-quarters*25)//10

nickles = n
(centtotal-(dimes*10+quarters*25))//5

pennies = p
(centtotal-(nickles*5+dimes*10+quarters*25))
"""
print('Quarters: ', quarters)
"""print('Dimes: ', dimes)
print('Nickles: ', nickles)
print('Pennies: ', pennies)"""

