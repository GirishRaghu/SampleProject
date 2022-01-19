print('How many numbers to be generated? :')
#upper_limit = int(input())
upper_limit = 10
print("The first " + str(upper_limit) + " numbers of the Fibonacci series are ->")
upper_limit -=2

index = 0
num1 = 0
num2 = 1
next = 0


print(num1)
print(num2)

while index < upper_limit:
    next = num1 + num2
    print(next)
    num1 = num2
    num2 = next

    index+=1


