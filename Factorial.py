num = (int)(input("Enter a number of your choioce :"))
fact = 1
if num==0:
    print('Factorial is 1')
elif num<0:
    print('Factorial does not exist')
else:
    for i in range(1,num+1):
        fact *= i 
if num>0:
    print('Factorial of ',num,' is ',fact)