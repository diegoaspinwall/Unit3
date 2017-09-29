#Diego Aspinwall
#9-29-17
#perfectNumber.py

guess = int(input('Enter a number: '))
total = 0

i=0
while i<num:
    i+=1
    if num%i==0:
        total+=i
    if total==guess:
        print('Perfect')
    else:
        print('Not Perfect')