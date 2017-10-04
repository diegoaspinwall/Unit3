#Diego Aspinwall
#10-2-17
#baseConverter.py

from math import log10

num = int(input('Enter a base-10 number: '))
base = int(input('What base would you like to convert it to: '))
"""
totaldig = log10(num)/log10(base)+1"""

power = 0
ans = 0
while num>0:
    ans += (num//base**power)%base
    totaldig=totaldig-1
    power+=1
    print(ans)

print(ans)
print(num, 'in base-',base, 'is', )
print(totaldig)