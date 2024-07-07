## Viết hàm tìm số lớn hơn trong 2 số
def max1(a, b):
    if a > b:
        return a
    else: 
        return b


## Định nghĩa hàm có thể chấp nhận input là số nguyên và in "Đây là số chẵn" nếu nó chẵn và ngược lại.
def kiem_tra_chan_le(n):   
        if n%2 == 0:
            return "Đây là số chẵn"
        else:
            return "Đây là số lẻ"

    