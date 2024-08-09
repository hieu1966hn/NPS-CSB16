## Viết hàm tìm số lớn hơn trong 2 số
def max1(a, b):
    if a > b:
        return a
    else:
        return b


## Định nghĩa hàm có thể chấp nhận input là số nguyên và in "Đây là số chẵn" nếu nó chẵn và ngược lại.
def kiem_tra_chan_le(n):
    if n % 2 == 0:
        return "Đây là số chẵn"
    else:
        return "Đây là số lẻ"


#### Định nghĩa hàm kiểm tra năm nhuận
def kiem_tra_nam_nhuan(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year %400 ==0:
        return True
    else:
        return False
    
#### Định nghĩa hàm tính tổng danh sách
def sum_list(list): ### Làm lại
    tong = 0
    for i in list:
        i = str(i)
        print(i)
        if i.isdigit(): 
            tong = tong + float(i)
            print(tong)
    return tong

