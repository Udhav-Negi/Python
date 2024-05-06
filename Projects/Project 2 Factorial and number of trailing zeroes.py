# Part 1 - Calculate the factorial of a given number
# Pat 2- Find the number of trailing zeroes in that factorial


# def factorial(n):
#     if n <= 1:
#         return n
#     return n * factorial(n-1)

n = int(input("Enter a number to find its factorial : "))
# ans = factorial(n)
# print(f"Factorial is {ans}")

# count = 0
# while n > 0:
#     rem = n % 10
#     if rem != 0:
#         break
#     count += 1
#     n = n // 10


def factorialTrailingZeroes(number):
    # This is the logic by Code With Harry to calculate no of trailing zeroes in a number
    # 100! = 100//5 + 100//5*5 + 100/5*5*5 -> This is the formula to calculate no of trailing zeroes in a number 
    count = 0
    i = 5
    while number/i != 0:
        count += int(number/i)
        i = i * 5
    return count


print(f"Number of trailing zeroes are {factorialTrailingZeroes(n)}")