def print_stars(N):
    if N <= 0:
        return
    print("*", end=" ")
    print_stars(N - 1)

N = int(input("Enter the number of stars: "))
print_stars(N)