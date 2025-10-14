# print("I'm a student.")

# value = 1/7
# print(f"{value:.5f}")

# a = int(input("Enter the first integer: "))
# b = int(input("Enter the second integer: "))
# print("The sum of the two numbers is:", a + b)

# filename = input("Enter the file name: ")
# try:
#     with open(filename, "r", encoding="utf-8") as f:
#         content = f.read()
#         print("File content:")
#         print(content)
# except FileNotFoundError:
#     print("Error: File does not exist.")

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("I'm a student.\n")
    f.write(f"{1/7:.5f}\n")
    a = 3
    b = 4
    f.write(f"The sum of {a} and {b} is: {a + b}\n")

# with open("output.txt", "ab") as f:
#     text = "Hôm nay trời đẹp."
#     f.write(text.encode("utf-8"))
