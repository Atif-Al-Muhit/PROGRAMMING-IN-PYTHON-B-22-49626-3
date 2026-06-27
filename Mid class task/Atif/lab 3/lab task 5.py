
N = int(input("Enter a number: "))

a, b = 0, 1

print("Fibonacci numbers below", N, ":")


while a < N:
    print(a, end=" ")
    a, b = b, a + b