#Diego Aspinwall
#10-2-17
#baseConverter.py

num = int(input('Enter a base-10 number: '))
base = int(input('What base would you like to convert it to: '))

num2=num
power = 0
ans = 0
ans2= ''
while num>0:
    ans += (num//base**power)%base
    num = num-ans*base**power
    power += 1
    if ans == 10:
        ans2='A'+ans2
    elif ans == 11:
        ans2='B'+ans2
    elif ans == 12:
        ans2='C'+ans2
    elif ans == 13:
        ans2='D'+ans2
    elif ans == 14:
        ans2='E'+ans2
    elif ans == 15:
        ans2='F'+ans2
    else:
        ans2= str(ans)+ans2
    ans=0
    

print(num2, 'in base-',base, 'is', ans2)
