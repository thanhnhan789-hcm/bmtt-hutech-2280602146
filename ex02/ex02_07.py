# Nhập các dòng từ người dùng 
print("Nhập các dòng văn bản (Nhập 'done để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    line.append(line)
# Chuyển các dòng thành chữ in hoa và in ra màn hình
print("\nCac dòng đã nhập sau khi chuyển thành chữ i hoa:")    
for line in lines:
    print(line.upper())