
def sort_arr(arr):
    for i in range(len(arr) - 1):
        min_pos = i ## find i - th max element
        for j in range(i + 1, len(arr)): 
            if arr[j] < arr[min_pos]:
                min_pos = j
       ## Cách 1: arr[i], arr[min_pos]  = arr[min_pos], arr[i] ## swap to current position

       ## Cách 2:
                # Sau khi đã tìm được vị trí có giá trị nhỏ nhất (min_pos), hoán đổi giá trị giữa arr[i] và arr[min_pos]
                temp = arr[i]          # Lưu giá trị hiện tại của arr[i] vào một biến tạm thời
                arr[i] = arr[min_pos]  # Gán giá trị của arr[min_pos] vào vị trí arr[i]
                arr[min_pos] = temp    # Gán giá trị tạm thời (ban đầu là arr[i]) vào vị trí arr[min_pos]
    return arr


arr = [5, 1, 8, 92, -1, 30] ## 6
print("Original list: " )
for el in arr:
    print(el, end=" ")

arr_sorted = sort_arr(arr)
print("sorted list", arr_sorted)



