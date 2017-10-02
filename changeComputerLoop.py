#Diego Aspinwall
#10-2-17
#changeComputerLoop.py

centtotal = int(input('Input number of cents: '))
quarters = centtotal//25
dimes = (centtotal-quarters*25)//10
nickles = (centtotal-(dimes*10+quarters*25))//5
pennies = (centtotal-(nickles*5+dimes*10+quarters*25))

print('Quarters: ', quarters)
print('Dimes: ', dimes)
print('Nickles: ', nickles)
print('Pennies: ', pennies)

