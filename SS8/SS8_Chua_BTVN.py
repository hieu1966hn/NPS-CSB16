##### Chữa Phần 2  - Bài 1:
colors = ["blue", "teal", "green", "orange"]

## Người dùng nhập vị trí và in ra màn hình tên màu ở vị trí đó. Đếm thứ tự từ 1.
inp = input("Mời người dùng nhập vị trí phần tử muốn xem")
print(f"Phần tử ở vị trí số {int(inp)} là {colors[int(inp) - 1]}")  ### 3 => "green"

removeItem = input("Người dùng muốn xóa gì trong danh sách")  ### số || Chữ
## Kiểm tra chữ
if removeItem.isalpha() == True:
    colors.remove(removeItem)

## Kiểm tra số =>  xóa vị trí
elif removeItem.isdigit() == True:
    colors.remove(colors[int(removeItem) - 1])
    print(colors)
else:
    print("không tồn tại giá trị để xóa")
