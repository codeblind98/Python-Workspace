import math

lst = []
num = (int)(input("Enter total number of data : "))
for n in range(num):
     numbers = (float)(input("\nEnter number : "))
     lst.append(numbers)

mean = sum(lst)/num
for n in range(num):
    tmp = abs(lst[n]-mean)     
    lst[n] = tmp*tmp

std_dev = math.sqrt(sum(lst)/num)
print("\nThe standard deviation is : ",std_dev)    