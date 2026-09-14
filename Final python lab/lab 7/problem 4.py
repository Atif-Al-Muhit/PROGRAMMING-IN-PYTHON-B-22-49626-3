filename = "sample.txt"

try:

   
    with open(filename, "w") as file:
        file.write("Hello Python!\n")
        file.write("This is Lab 07.\n")

    print("File written successfully.")

    with open(filename, "r") as file:
        data = file.read()

    print("\nFile Content:")
    print(data)

       with open(filename, "a") as file:
        file.write("This line was added using append mode.\n")

    print("Data appended successfully.")

       with open(filename, "r") as file:
        data = file.read()

    print("\nUpdated File Content:")
    print(data)

except FileNotFoundError:
    print("Error: File or directory not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected Error:", e)