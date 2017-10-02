#Diego Aspinwall
#10-2-17
#baseConverter.py

base10 = int(input('Enter a base-10 number: '))
base? = int(input('What base would you like to convert it to: '))

dig1 = base10%16
dig2 = (base10//16)%16

print(base10, 'in base-'+base?, 'is', dig2, dig1)
