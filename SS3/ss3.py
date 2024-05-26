### Ôn tập buổi 2
# str1 ="Hello World!"
# str2 = 123

# Tach chuỗi
# str2 = str1[0:5]
# print(str2)
# print(str1 + str2)


#### code buổi 3: Toán tử so sánh
# print(1 < 2)  # True
# print(1 > 2)  # False
# print(2 == 2)  # True
# print(3 <= 4)  # True
# print(3 >= 4)  # False

### Ví dụ với if:
# tuoi = 19
# if tuoi >= 18:
#     print("ok")
#     print("Đây là câu lệnh thứ 2")
#     print("Đây là câu lệnh thứ 3")
# print("Đây là câu lệnh thứ 4")

a = 500
b = 1000
# print(a>b)
if a > b:
    print("a is greater than b")
elif a == 500:
    print("a have value is: 500")
else:
    print("b is greater than a")

### Toán tử logic: and, or, not


#### Bài toán xếp loại học sinh:
# Giỏi (>= 8.0)
# khá (8.0 > x >= 6.5)
# trung bình (6.5 > x >= 5.0)
# yếu (5.0 > x >= 2.5)
# kém (2.5 > x)

# diem = float(input("Mời người dùng nhập điểm"))
# if diem >= 8.0:
#     print("Đạt học sinh giỏi")
# elif diem < 8.0 and diem >= 6.5:
#     print("Đạt học sinh khá")
# elif 6.5 > diem and diem >= 5.0:
#     print("Đạt học sinh trung bình")
# elif 5.0 > diem and diem >= 2.5:
#     print("Đạt học sinh yếu")
# else:
#     print("Đạt học sinh kém")

import math
a= 4
print(math.sqrt(a)) # tính căn bậc 2.