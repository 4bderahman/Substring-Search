txt = input("Enter a string: ")
x = input("Enter the substring to search for: ")

c = txt.find(x)

if c >= 0:
    print(x,"is found at position:" c)
else:
    print(f"The substring '{x}' was not found.")
