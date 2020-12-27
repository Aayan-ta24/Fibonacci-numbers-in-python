# Enter number of terms needed
num=int(input("Enter the number of terms you require: "))
a=0                                         #element 1
s=1                                         #element 2
while a<=num:
    print(a, )
    fib = a + s
    a = s
    s = fib
