#Diego Aspinwall
#10-2-17
#baseConverter.py

num = int(input('Enter a base-10 number: '))
base = int(input('What base would you like to convert it to: '))

num2=num
power = 0
ans = 0
while num>0:
    ans += (num//base**power)%base
    num = num-(ans//10)%10
    power += 1
    if ans == 10:
        print('A')
    elif ans == 11:
        print('B')
    elif ans == 12:
        print('C')
    elif ans == 13:
        print('D')
    elif ans == 14:
        print('E')
    elif ans == 15:
        print('F')
    else:
        print(ans)
    ans=0
    

print(num2, 'in base-',base, 'is', )