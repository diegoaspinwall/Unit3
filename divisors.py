#Diego Aspinwall
#9-29-17
#divisors.py

num = int(input('Enter a number: '))

i=0
while i<=num:
    i+=1
    if num%i==0:
        print(num/i)
