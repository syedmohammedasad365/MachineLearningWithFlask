## PYTHON PROGRAM TO CALCULATE THE SUM OF ALL EVEN NUMBERS FROM 1 TO N NUMBERS
def sum_of_even_numbers(n):
    sum_even = 0
    for i in range(2, n + 1, 2):
        sum_even += i
    return sum_even
n = int(input("Enter a positive integer: "))
print("Sum of all even numbers between 1 and", n, "is:", sum_of_even_numbers(n))