
def recursion(num):
    if num == 1:
        return 1
    else:
        return num * recursion(num-1)

num = int(input('Enter number of your choice : '))
print("Factorial of ",num," is ",recursion(num))
