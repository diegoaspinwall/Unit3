#Diego Aspinwall
#10-2-17
#baseConverter.py

from math import log10

num = int(input('Enter a base-10 number: '))
base = int(input('What base would you like to convert it to: '))

num2=num
power = 0
ans = 0
while num>0:
    ans += (num//base**power)%base
    num += -ans
    power += 1
    print(ans)
    ans=0

print(num2, 'in base-',base, 'is', )