# Q10: File Reading with Finally Block

def read_file(filename):
    file = None
    try:
        file = open(filename, "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("File not found.")
    finally:
        if file:
            file.close()

read_file("hello.txt")
read_file("missing.txt")
