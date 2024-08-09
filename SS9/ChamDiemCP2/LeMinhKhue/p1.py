# n=int(input("Insert a number: "))
# def kiem_tra_chan_le(n):
#     n=n
#     if n%2 == 0:
#         return "This number is even"
#     else:
#         return "This number is not even"
# print (kiem_tra_chan_le(n))

n=int(input("Insert radius: "))
def cal_area(n):
    n=n
    area=(n^2)*3.14
    return(area)
print(cal_area(n))

def reverse_str(s):
    reverse_s = ""
    for char in s:
        reverse_s = char + reverse_s
    return reverse_s

print(reverse_str("mindX"))