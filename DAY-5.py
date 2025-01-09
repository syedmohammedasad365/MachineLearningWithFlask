# Ask the user to enter a positive integer n
n = int(input("Enter a positive integer: "))
# Use a for loop to print all numbers from 1 to n on separate lines
for i in range(1, n + 1):
    print(i)
# Use a while loop to calculate the sum of all numbers from 1 to n and print the result
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(f"The sum of all numbers from 1 to {n} is {sum}")

##TASK-2

# Define a function named calculate_square that takes a single argument n and returns the square of n
def calculate_square(n):
    return n * n
# In the main program, ask the user to input a positive integer
n = int(input("Enter a positive integer: "))
# Call the calculate_square function with the user-provided number and display the result
result = calculate_square(n)
print(f"The square of {n} is {result}")