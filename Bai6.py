text = "Hôm nay trời đẹp."
with open("output.txt", "wb") as f:
    f.write(text.encode("utf-8"))
with open("output.txt", "rb") as f:
    data = f.read()
    print("Đã ghi (bytes):", data)
    print("Đã ghi (decode):", data.decode("utf-8"))
