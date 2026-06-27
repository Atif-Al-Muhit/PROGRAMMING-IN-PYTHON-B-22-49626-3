def palindrome(text):
    text = text.lower()

    if text == text[::-1]:
        return True
    else:
        return False


word = input("Enter a string: ")

if palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")