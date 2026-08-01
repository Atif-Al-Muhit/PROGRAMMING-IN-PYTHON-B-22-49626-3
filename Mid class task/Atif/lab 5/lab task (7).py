words = ['aca', 'xyz', 'aba', '1221']

count = 0

for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1

print("Count =", count)