#Diego Aspinwall
#9-28-17
#converter2.py

while True:
    print('1) Kilometers to Miles')
    print('2) Kilograms to Pounds')
    print('3) Liters to Gallons')
    print('4) Celsius to Fahrenheit')
    print('5) "quit"')
    print(' ')

    num = input('Choose an option: ')


    if num=='4':
        cel = float(input('Enter Degrees in Celsius: '))
        print(cel, 'degrees Celsius is', cel*9/5 + 32, 'degrees in Fahrenheit')
        print(' ')
        print(' ')
    elif num=='3':
        lit = float(input('Enter Volume in Liters: '))
        print(lit, 'Liters is', lit*0.264172, 'Gallons')
        print(' ')
        print(' ')
    elif num=='2':
        mass = float(input('Enter Mass in Kilograms: '))
        print(mass, 'Kilograms is', mass*2.20462, 'Pounds')
        print(' ')
        print(' ')
    elif num=='1':
        kilo = float(input('Enter Distance in Kilometers: '))
        print(kilo, 'Kilometers is', kilo*0.621371, 'Miles')
        print(' ')
        print(' ')
    elif num=='quit':
        break
    else:
        print('Please check spelling BOI. You cant even spell a number.')
        print(' ')
        print(' ')
