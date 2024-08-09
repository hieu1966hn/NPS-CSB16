# #######phần 1 bài 1
# num = int(input("Input a number: "))
# if num%2==0:
#     print("This number is even")
# else:
#     print("This number is not even")


######phần 1 bài 2
# def cal_area(radius):
#     area = 3.14 * radius**2
#     return area
# radius = float(input("Input a number: "))
# print("Circle’s area:", cal_area(radius))


#####phần 1 bài 3
# def reverse_str(s):
#     reverse_s = ""
#     for char in s:
#         reverse_s = char + reverse_s
#     return reverse_s
# print(reverse_str("mindx"))

#####phần 1 bài 4
# def is_palindrome(s):
#     str = ""
#     for char in s:
#         str = char + str
#     return str
# print(is_palindrome("hannah"))

#####phần 2 bài 1
# def giai_thua(n):
#     gt =1
#     for i in range(1, n+1):
#         gt = gt*i
#     return gt
# n = int(input("Input a number: "))
# print(giai_thua(n))

#####phần 2 bài 2
# def sap_xep():
#     min=1
#     for i in range(len(list1)):
#         list1 =[5, 1, 8, 92, -1, 30]


#####phần 2 bài 3
def print_fibo(n):
    a = 1
    b = 1
    for i in range(n):
        print(a, end="")
        temp = a
        a=b
        b = temp +b
print(print_fibo(5))