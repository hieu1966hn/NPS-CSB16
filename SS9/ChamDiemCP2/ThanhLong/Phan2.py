# 1
nk=int(input("nhap vao so nguyen n: "))
k=1
while nk>1:
    k=k*nk
    nk=nk-1
print(k)

# 2
list1=[1,2,34,5,57,-34,-14,-53,4]
list1.sort(reverse=False)
print(list1, end=" ")
#___________________________________________
print("""
""")
#___________________________________________
# 3
mk=int(input("nhap vao so nguyen n: "))
def print_fibo(n):
    a=1
    b=1
    for i in range(n):
        print(a,end=" ")
        temp=a
        a=b
        b=temp+b

print(print_fibo(mk))


















































































