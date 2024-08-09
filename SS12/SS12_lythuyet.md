File: Là đơn vị lưu trữ thông tin trong hệ thống máy tính. File có thể chứa nhiều loại dữ liệu khác nhau gồm: video, hình ảnh, văn bản, âm thanh ,... Các file được tổ chức và lưu trữ trong các thư mục (folder).

Liệt kê các đuôi file cơ bản: 
- .doc/.pdf/.pptx: tài liệu
- .png/.jpg: file hình ảnh
- .xlxs: file bảng tính
- .exe: file thực thi
- .inf: file thông tin ()
- .mp3: file âm thanh
- .mp4: file video


File path: Đường dẫn file được lưu trữ bên trong máy tính.

Mode file: Chế độ xử lý file trong Python
r: read only, Báo lỗi nếu không có file
- read(): đọc toàn bộ nội dung trong file
- read(n): đọc n ký tự đầu tiên
- readline(): Đọc theo từng dòng.

a: Thêm nội dung vào cuối file, Tạo file nếu chưa có file đó.
w: Ghi đè file, tạo file nếu chưa có file đó
x: Tạo file

Xóa file: 
- import module os
- hàm remove
- hàm rmdir()


Bài tập thực hành: 

Đề bài: Bài 1a: Ghi dữ liệu vào file
- tạo 1 file văn bản có tên là example.txt
- Ghi dòng chữ "Hello World!!" vào file này.


Bài 1b: Đọc dữ liệu từ file
- Mở file example.txt đã tạo ở bài tập 1a
- Đọc và in ra nội dung của file này?

Bài 2: Đếm số dòng trong file example.txt

Bài 3a: Đọc số nguyên từ file
- Tạo một file có tên là numbers.txt và ghi vào file này các số nguyên, mỗi số nằm trên một dòng.
- Viết chương trình để đọc các số từ file và tính tổng của chúng.

Bài 3b: Tính giá trị trung bình 
- Sử dụng file numbers.txt từ bài tập 3a. Viết chương trình để tính và in ra giá trị trung bình của các số.

Bài 4: Tìm và thay thế từ trong file
- Đọc nội dung của một file văn bản (sample.txt) có nội dung là "Hello World".
- Tìm và thay thế một từ cụ thể trong nội dung. Thay thế "Hello World" "Hi".
- Ghi nội dung đã thay thế vào một file mới.
- Viết dưới dạng hàm thay thế nội dung: replace_word_in_file(input_file, output_file, target_word, replacement_word)

Bài 5: Gộp nội dung từ nhiều file thành một file.
- Có 3 file văn bản (file1.txt, file2.txt, file3.txt).
- Đọc nội dung từ cả 3 file và gộp lại thành một file merged.txt.
- Hiển thị toàn bộ nội dung file merged.txt ra terminal.