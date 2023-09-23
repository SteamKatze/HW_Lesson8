def my_pow(number, degree):
    if degree <= 1:
        return number

    result = number * my_pow(number, degree - 1)
    print(f"my_pow({number}, {degree}) -> {number} * my_pow({number}, {degree - 1}) => {result}")
    return result

number = 2
degree = 3
result = my_pow(number, degree)
print(f"my_pow({number}, {degree}) -> {result}")
