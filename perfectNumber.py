#Diego Aspinwall
#9-29-17
#perfectNumber.py

guess = int(input('Enter a number: '))
total = 1

for i in range(1,guess):
    if guess%i==0:
        total+=i
if total==guess:
    print('Perfect')
else:
    print('Not Perfect')
print(total)