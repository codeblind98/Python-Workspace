num = (int)(input("Enter a number of your choice : "))
check=(num//2)+1
i=2
if num < 2:
    print('Not a prime number')
if num==2:
    print('Prime number')
if num>2:
    while i != check:
        if num % i==0:
            print('Not a prime number')
            break
        i += 1
    else:
        print('Prime Number')


        

