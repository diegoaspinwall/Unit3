#Diego Aspinwall
#9-29-17
#perfectNumber.py

guess = int(input('Enter a number: '))
total = 0

i=0
while i<guess:
    i+=1
    if guess%i==0:
        total+=i
    if total==guess:
        print('Perfect')
    else:
        print('Not Perfect')