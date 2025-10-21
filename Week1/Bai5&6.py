with open("output.txt", "w", encoding="utf-8") as f:
    f.write("I'm a student.\n")
    f.write(f"{1/7:.5f}\n")
    a = 1
    b = 1
    f.write(f"The sum of {a} and {b} is: {a + b}\n")

with open("output.txt", "ab") as f:
    text = "Hôm nay trời đẹp."
    f.write(text.encode("utf-8"))
