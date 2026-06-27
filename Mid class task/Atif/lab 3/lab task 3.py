base = int(input("Enter base: "))
power = int(input("Enter exponent: "))

result = 1

for _ in range(power):
    result *= base

print("Result:", result)