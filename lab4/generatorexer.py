#1
def squares_generator(N):
    for i in range(N):
        yield i ** 2

# Example usage
N = 5
squares = squares_generator(N)
for square in squares:
    print(square)

#2
def even_numbers_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Example usage
n = int(input("Enter a number: "))
even_numbers = even_numbers_generator(n)
print("Even numbers:", ", ".join(map(str, even_numbers)))

#3
def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage
n = int(input("Enter a number: "))
divisible_numbers = divisible_by_3_and_4_generator(n)
for num in divisible_numbers:
    print(num)

#4
def squares_generator(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Example usage
a = 3
b = 7
for square in squares_generator(a, b):
    print(square)

#5
def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1

# Example usage
n = 5
countdown = countdown_generator(n)
for num in countdown:
    print(num)
