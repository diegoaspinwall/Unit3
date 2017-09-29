#Diego Aspinwall
#9-29-17
#perfectNumber.py

guess = int(input('Enter a number: '))
total = 0
"""
i=1
while i<=guess:
    i+=1
    if guess%i==0:
        total+=i
"""
for i in range(2,guess):
    if guess%i==0:
        total+=i
if total==guess:
    print('Perfect')
else:
    print('Not Perfect')
