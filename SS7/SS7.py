##### Số nguyên tố: Chỉ chia hết cho 1 và chính nó.
# soChan = int(input("Mời người dùng nhập vào số chẵn")) ##10

# if soChan%2 ==0:
#     ## kiểm tra số nguyên tố
#     for k in range(1, soChan+1): # 1 - 10
#         dem = 0
#         ### Code kiểm tra số nguyên tố K:
#         for i in range(1, k + 1):
#             if k % i == 0:
#                 dem = dem + 1
#         if dem == 2:
#             print(k)


#### Phần 4: 
# start_number = 2
# stop_number = 20
# i = start_number ## 2
# while i<= stop_number:
#     if i %2 ==0:
#         print(i)
#     # Tăng i lên một đơn vị sau mỗi lần lặp.
#     i = i +1


### Tính tổng từ  1 - 100: 1 + 2 + 3 + 4 + ... + 99 + 100
# tong = 0
# for i in range(1 , 101):
#     tong = tong + i
# print(tong)


#### Code phần  vẽ hình tam giác
# import turtle
# t = turtle.Turtle()
# t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
# t.forward(200)
# t.left(120)
# t.forward(200)
# t.left(120)
# t.forward(200)
# t.left(120)


#### Bài nâng cao với list
int_list = [5, 1, 8, 92, -1, 30]
input_number = int(input("Mời người dùng nhập vào một số nguyên")) ## 8
if input_number in int_list:
    print(int_list.index(input_number)) ## list.index sử dụng để tìm kiếm và trả về vị trí phần tử trong list
