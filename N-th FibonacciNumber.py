# Fibonacci:A string of numbers that are created by calculating the sum of the previous two numbers.Except(1,0)
# Formula: n={0,1,1,2,3,4,5,....}   F1=F2=1   n>2    Fn=F(n-1)+F(n-2)
# For example: n=6   F6=F5+F4    F5=4    F4=3    F6=7   -----> the sixth Fibonacci number is 13


# print N-min number Fibonacci
def find_number_fibonacci(n):
    # If the entered number is (1,2) it returns 1 because the first two members of the Fibonacci sequence are 1
    if n == 1 or n == 2:
        return 1
    first_number = 1
    second_number = 2
    for number in range(3, n+1):
        new_number = first_number + second_number
        first_number = second_number
        second_number = new_number
    return second_number


number_user = int(input("Please enter the desired number: "))
result = find_number_fibonacci(number_user)
print("The Nth number of the Fibonacci series: ", result)

# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali
