def sum_range(a, b):
    if a == b:
        print(f"sum_range({a}, {b}) -> {a}")
        return a

    print(f"sum_range({a}, {b}) -> {a} + sum_range({a + 1}, {b})")
    return a + sum_range(a + 1, b)

a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

result = sum_range(a, b)
print(f"The sum of numbers in the range from {a} to {b} is {result}.")