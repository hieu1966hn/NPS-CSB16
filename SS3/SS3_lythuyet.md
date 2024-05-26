Buổi 2:
- KDL: String & Number (int & float)
- Tách 1 String: "Hello World!"
+ str1 = string[0;5]


Buổi 3:
- Giới thiệu về Kiểu dữ liệu: Boolean (True/False)
- các phép toán có thể trả về Boolean: Toán tử so sánh: >, <, >=, <=, !=, ==

- Cách sử dụng câu lệnh điều kiện: if ....
- Cú pháp:
if condition:
    statement if true
else
    statement if false

Toán tử logic: and, or, not
- VD1: Tôi gầy hoặc béo (được lựa chọn và chọn gì cũng đúng).
- VD2: Tôi gầy và mập (Bắt buộc phải lấy cả 2 trường hợp).
- VD3: Con chó có lông vàng hoặc lông xanh lá và 3 chân.
(con chó màu lông nào cũng đúng và đều phải có 3 chân)

+ and: Toán tử tìm kiếm giá trị trả về là False, nếu không có đk sai => True. 
+ or: Toán tử tìm kiếm giá trị trả về là True, nếu không có đk đúng => False. 
+ not: Toán tử kiểm tra giá trị khác với giá trị so sánh.


Bài tập thực hành;
1. Viết chương trình tìm số lớn hơn trong 3 số nhập từ người dùng
2. Viết chương trình tính chỉ số BMI, in ra tình trạng sức khỏe của người dùng biết: 
BMI = trọng lượng/chiều_cao^2 (kg/m^2). 
3. Viết chương trình tính nghiệm của phương trình bậc 2
4. Viết chương trình kiểm tra số người dùng nhập vào là: số dương, âm, số 0
5. Viết chương trình kiểm tra năm nhuận hay không biết:
+ Năm nhuận là năm chia hết cho 4
+ Năm chia hết cho 100 thì đồng thời phải chia hết cho 400.

import math
a= 4
print(math.sqrt(a)) # tính căn bậc 2.

Quy đổi sức khỏe: 
BMI < 18.5: Gầy
18.5 <= BMI < 24.9 : Bình thường
BMI >= 25: Thừa cân
25 < BMI < 29.9: Tiền béo phì 
30 <= BMI < 34.9: Béo phì độ I
35 <= BMI < 39.9: Béo phì độ II
40 <= BMI: Béo phì độ III