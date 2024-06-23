### Ví dụ về vòng lặp for: Bài toán in ra các số từ 1 - 10;
# for i in range(1, 11 ,1):
#     print(i) # 1, 2 , 3, ...10


# for i in range(11):
#     print(i) #  0, 1, ... , 10


#### Ví dụ về vòng lặp while: Bài toán in ra các số từ 0 - 10
# i = 0
# while i < 11:
#     print(i)  # 0, 1, 2,...., 10
#     i = i + 1 # ,11


### Ví dụ while với vòng lặp while
# n = 1
# while n<5:
#     print("Hi")
#     n += 1 # Cách viết khác = n + 1


### Chữa Bài tập thực hành 2
# for i in range(0, 21):
#     if i%3 == 0:
#         print(i)


### Chữa bài 4:
# n = int(input("Mời người dùng nhập vào số nguyên từ bàn phím: "))
# n = 1470
# so_chu_so = 0 ## đây sẽ là biến đếm số.
# while n > 0:
#     n = n // 10 ## //: Phép chia lấy phần nguyên. (147,14, 1,0)
#     so_chu_so += 1

# print(so_chu_so)

### Chữa bài 6:
# n = int(input("Mời người dùng nhập vào số nguyên từ bàn phím: "))
# dem = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         dem += 1

# if dem == 2: #Chỉ chia hết đúng 2 lần trong phạm vi từ 1 đến n+1
#     print(f"{n} là số nguyên tố")
# else:
#     print(f"{n} là không số nguyên tố")


## Chữa bài 5: 
# n = int(input("Mời người dùng nhập vào số nguyên từ bàn phím: "))
# giai_thua = 1
# for i in range(1, n+1):
#     giai_thua = giai_thua*i

# print(giai_thua)