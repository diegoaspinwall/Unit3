#Diego Aspinwall
#10-2-17
#warmup8.py

total=0
i=0
while i<100000:
    if i%3==0 or i%10==0 or i%17==0:
        total+=i
    i+=1
print(total)
