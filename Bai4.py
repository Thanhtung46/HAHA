# 1. Lấy tên file từ người dùng
ten_file = input("Nhập tên file: ")

# 2. Xử lý việc mở và đọc file
try:
    # Mở file trong khối 'with' (để tự động đóng)
    with open(ten_file, 'r') as file:
        
        # Đọc và in ra nội dung
        noi_dung = file.read()
        print("\n--- Nội dung file ---")
        print(noi_dung)
        print("----------------------")

# 3. Xử lý trường hợp file không tồn tại
except FileNotFoundError:
    print(f"\n🚫 Lỗi: File '{ten_file}' không tồn tại.")