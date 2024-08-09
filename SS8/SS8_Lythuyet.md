Nội dung:
Phần I: chữa BTVN
Phần II: Hàm & Module

- Cách viết hàm và mục đích sử dụng hàm
- Phân biệt hàm print và hàm return
- Cách viết hàm thành module và import module để tái sử dụng.

Hàm: Là một đoạn code (chương trình con) dùng để thực hiện một việc nào đó. Trong Python có 2 loại:

- Hàm built-in: Hàm có sẵn trong Python: print, input, append, remove, min, max, range.
- Hàm do người dùng viết..

Cú pháp khai báo hàm:
def <ten_ham>(a, b, c):
    .....
    return
    ....

- a,b,c: Tham số truyền vào hàm
- gọi hàm <ten_ham>(1, 2 ,3 ): 1, 2, 3 => được gọi là đối số.
- return: Cú pháp trả về giá trị khi thực thi hàm (Chú ý: khi câu lệnh return chạy xong -> kết thúc hàm luôn).


Phạm vi của Biến: 
- Global: Là biến được tạo ra ngoài hàm, được duy trì trong toàn bộ chương trình code.
- Local: Là biến được tạo trong hàm. Có tác dụng trong hàm đó và biến mất sau khi hàm kết thúc.


Module: 
- Tách hàm ra file để có thể sử dụng ở nhiều chương trình khác nhau.
- File hàm phải ở cùng folder với file chương trình.
- Cách import hàm như nào?


Bài tập thực hành: 
1. Viết hàm kiểm tra năm nhập vào xem năm đó có phải là năm nhuận hay không (nhuận: True, không nhuận: False).
- Năm nhuận là năm chia hết cho 4 nhưng không chia hết cho 100.
- Năm chia hết cho 400.

2. Viết hàm tính tổng một LIST cho trước. Nếu trong List đó tồn tại phần tử không phải là số thì bỏ qua nó. [1, 2, 3, "hi"] => 6

3. Viết một chương trình chấp nhận chuỗi do người dùng nhập vào, phân tách nhau bởi dấu ",". và in những từ đó thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.