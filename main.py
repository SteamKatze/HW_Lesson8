import random

def find_min_sum_position(number):
    if len(number) < 10:
        return None

    min_sum = sum(number[:10])
    min_sum_start = 0

    for i in range(1, len(number) - 9):
        current_sum = sum(number[i:i + 10])
        if current_sum < min_sum:
            min_sum = current_sum
            min_sum_start = i

    return min_sum_start


def print_sequence_info(number, start):
    for i in range(start, start + 10):
        print(f"arr[{i}] = {number[i]}", end=", ")
    print(f"Sum = {sum(number[start:start + 10])}")


random_numbers = [random.randint(1, 100) for _ in range(100)]

position = find_min_sum_position(random_numbers)

if position is not None:
    print(f"Result: {position}")
    print_sequence_info(random_numbers, position)
else:
    print("Array is too short")