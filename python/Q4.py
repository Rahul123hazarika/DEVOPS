# Read from a file

file = open("new.txt", "r")

content = file.read()

print("File Content:\n")
print(content)

file.close()