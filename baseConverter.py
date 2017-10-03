#Diego Aspinwall
#10-2-17
#baseConverter.py

from math import log10

base10 = int(input('Enter a base-10 number: '))
base = int(input('What base would you like to convert it to: '))

totaldig = log10(base10)/log10(base)+1

power = 0
ans = ''
while totaldig>=0:
    ans += (base10//base**power)%base
    base10= base10%base
    totaldig=totaldig-1
    power+=1
print(ans)
print(base10, 'in base-',base, 'is', )
print(totaldig)