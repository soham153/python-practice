# fibonacci series

n = int(input("Enter size of series"))

number1 = 0
number2 = 1 
while(n!=0):
    number3 = number1+number2
    print(number3)
    number1 = number2
    number2 = number3
    n= n-1