text = input("Enter a string: ")

words = text.split()

result = []

for word in words:
    result.append(word[::-1])

print("Reversed String:", " ".join(result))