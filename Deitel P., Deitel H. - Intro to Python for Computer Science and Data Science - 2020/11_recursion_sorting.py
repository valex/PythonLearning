# ----------------------------------------------------
# Linear Search
# ----------------------------------------------------





# ----------------------------------------------------
# Recursive Fibonacci Series
# ----------------------------------------------------

# # Function fibonacci 
# def fibonacci(n):
#     if n in (0, 1):  # base cases
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
    
# # Testing Function fibonacci
# for n in range(41):
#     print(f'Fibonacci({n}) = {fibonacci(n)}')

# # Self Check Exercise 3
# def iterative_fibonacci(n):
#     result = 0
#     temp = 1
#     for j in range(0, n):
#         temp, result = result, result + temp
#     return result

# # %timeit fibonacci(30)
# # 807 ms ± 787 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)

# # %timeit iterative_fibonacci(30)
# # 5.11 µs ± 36 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


# ----------------------------------------------------
# Recursive Factorial
# ----------------------------------------------------

# def factorial(number):
#     """Return factorial of number."""
#     if number <= 1:
#         return 1
#     return number * factorial(number - 1)  # recursive call
    
# for i in range(11):
#     print(f'{i}! = {factorial(i)}')


# print(factorial(50))

# ----------------------------------------------------
# Factorial
# ----------------------------------------------------

# factorial = 1

# for number in range(5,0,-1):
#     factorial *= number

# # 5!
# print(factorial)
# # 120