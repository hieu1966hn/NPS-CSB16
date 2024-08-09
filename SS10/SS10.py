# car = {
#     "brand": "Toyota",
#     "year": 2010,
#     "price": 400.45,
#     "color": ["grey", "red", "blue"],
# }


#### In ra toàn bộ dict này
# print(car)

### Lấy ra năm sản xuất và in ra màn hình terminal
# print(car["year"])

### lấy ra 1 màu bất kỳ của xe và in ra nó
# print(car["color"][2])


###### Các thuộc tính đi kèm với Dictionary
### Xóa 1 khóa: Sử dụng từ khóa del
# del car["price"]
# print(car) ### Không còn khóa "price"

### Đếm số lượng khóa đang có trong dict: len()
# print(len(car))

### Xóa toàn bộ dictionary: dict.clear()
# car.clear()
# print(car)


### Tìm kiếm key trong dict
# if "brand" in car:
#     print("True")


### Sao chép một Dict: Sử dụng phương thức copy().
# car1 = car.copy() ### Thay đổi car1 cũng sẽ không thay đổi car


#### In ra toàn bộ khóa bên trong 1 dict
# for key in car:
# print(key) # brand, year, ...
# print(car[key])

## Kiểm tra xem key - value có tồn tại bên trong dict khong?
# for ("brand", "Toyota") in car.items:


#### Chữa bài I ý 3:
mindX_shop = {
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,
    "ASUS": 30,
}

inp = input("Mời người dùng nhập vào hãng máy tính: ")

### Kiểm tra xem Hãng này có là key bên trong mindX_shop không
if inp in mindX_shop:
    print(f"Số lượng {inp} trong kho là: {mindX_shop[inp]}")
else:
    print(f"Không tồn tại hãng {inp} trong kho")


#### Chữa bài II
ninja_adventure = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2,
}

## Thêm 50 golde cho nhân vật này;
# ninja_adventure["Gold"] += 50
ninja_adventure["Gold"] = ninja_adventure["Gold"] + 50
print(ninja_adventure["Gold"])

## thêm khóa poket 
ninja_adventure["Pocket"] = ["MonsterDex", "Flashlight"]
print(ninja_adventure["Pocket"])
