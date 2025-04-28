# Q9: Generator Function for Efficient Iteration
# python
# Copy
# Edit
def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# The yield keyword is used to return a list of values from a function.

# Unlike the return keyword which stops further execution of the function, the yield keyword continues to the end of the function.

for num in generate_numbers(5):
    print(num)
