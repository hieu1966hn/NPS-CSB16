#### Muốn sử dụng hàm từ file hàm thì phải import
import SS8_DEF


### Khai báo một hàm
# def sayHello():
#     print("Hello World!!!")


### Gọi hàm
# sayHello()


### Khai báo một hàm có tham số:
# def sum1(a, b):
#     print(a + b)


### Gọi hàm có tham số
# sum1(3, 2)  ### 5


### Khai báo hàm diện tích tam giác
# def StamGiac(width, height):
#     return width * height / 2

# print(StamGiac(5, 10))


### Gọi hàm tìm số lớn nhất
print(SS8_DEF.max1(1, 10)) #### ?

### Gọi hàm kiểm tra số nguyên và chẵn lẻ
print(SS8_DEF.kiem_tra_chan_le(11))


### Gọi hàm kiểm tra năm nhuận
print(SS8_DEF.kiem_tra_nam_nhuan(2022))

#### Gọi hàm tính tổng danh sách
# a = "1"
# print(a.isdigit())
# print(SS8_DEF.sum_list([1, 2, 3, 4.0 ,"Hello"])) ###