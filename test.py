try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: 'example.txt' not found.")
