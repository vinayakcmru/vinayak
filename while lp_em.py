i=1
print("1st")
while(i<=10):
    print(i)
    i=i+1

print("2nd")
for i in(1,2,3,4,5):
    if(i==3):
      continue
    print(i)

print("3rd")
for i in(1,2,3,4,5):
    if(i==2):
       break
    print(i)
