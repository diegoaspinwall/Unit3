#Diego Aspinwall
#10-2-17
#changeComputerLoop.py

centtotal = int(input('Input number of cents: '))

quarters = 0
while centtotal>=25:
    quarters+=1
    centtotal=centtotal-25

dimes = 0
while centtotal>=10:
    dimes+=1
    centtotal=centtotal-10

nickles = 0
while centtotal>=5:
    nickles+=1
    centtotal=centtotal-5

pennies = 0
while centtotal>0:
    pennies+=1
    centtotal=centtotal-1

print('Quarters: ', quarters)
print('Dimes: ', dimes)
print('Nickles: ', nickles)
print('Pennies: ', pennies)
