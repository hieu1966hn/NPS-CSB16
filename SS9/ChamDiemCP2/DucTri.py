#bài 3:
def print_fibo(n):
    a=1
    b=1
    for i in range (n):
        print(a,end=" ")
        temp=a
        a=b
        b=b+temp

print(print_fibo(10))