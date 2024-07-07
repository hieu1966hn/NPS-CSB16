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
1. 