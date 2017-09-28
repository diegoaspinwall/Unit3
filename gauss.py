#Diego Aspinwall
#9-28-17
#gauss.py

lower = int(input('Enter lower number: '))
higher = int(input('Enter upper number: '))
dist = int(input('Enter the difference between each number: '))

total = 0

for i in range(lower,higher+1,dist):
    total = total + i
print('The sum of the numbers from', lower, 'to', higher, 'with a difference of',dist, 'is', total)
