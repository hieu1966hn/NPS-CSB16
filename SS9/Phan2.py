### Chữa bài 3


def print_fibo(n):
    ### khởi tạo 2 phần tử đầu của dãy:
    a = 1
    b = 1
    ### In ra các phần tử 
    for i in range(n): # 0 - n
        print(a, end=" ")    ## 1,1,2,3,5,8,13,..
        temp = a ## Lưu giá trị hiện tại của biến a vào biến tạm
        a = b ## Gán giá trị của b cho a
        b = temp + b ## Tính tổng của giá trị cũ của a và b, gán cho b.

print(print_fibo(5))