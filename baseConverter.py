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
    num += -num//base**power
    power+=1
    print(ans)
    a=0

#print(ans)
print(num2, 'in base-',base, 'is', )
print(totaldig)