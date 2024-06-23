#### Khai báo List
# a = []

#### Khai báo List có giá trị:
# shoppingList = ["Snack", "fish", "Đậu", "Nước ngọt", "Xì dầu", "sữa"]


#### Phương thức đếm số thứ tự danh sách: len()
# print(len(shoppingList)) #### 6

#### Vị trí bắt đầu của item trong list là:
# print(shoppingList[1]) ### 0


### Thêm một phần tử vào cuối list: append()
# shoppingList.append("banana")
# print(shoppingList) ###

### Xóa một phần tử trong list:
# shoppingList.remove("Snack")
# print(shoppingList) ###


#### Xóa toàn bộ phần tử trong List:
# shoppingList.clear()
# print(shoppingList) ###


#### Tìm kiếm trong danh sách:
# print("sữa" in shoppingList)


#### Sao chép mảng
# a = [1,2,3]
# b = a.copy()
# b[0] = 100
# print(a) ## giữ nguyên.

#### Gộp 2 danh sách:
# a = [1, 2, 3]
# b = [4, 5, 6]
#####C1: gộp 2 danh sách
# c = a + b
# print(c)

#####C2: extend(): mở rộng danh ban đầu.
# b.extend(a)
# print(b)


############ Duyệt danh sách với vòng lặp:
##### in ra toàn bộ phần tử có trong danh sách shoppingList(mỗi phần tử một dòng)
# for item in shoppingList:
#     print(item) # Snack, fish, ...., sữa. (in ra giá trị...)

##### In ra toàn bộ list, tuy nhiên item/i đại diện cho vị trí phần tử trong list.
# for i in range(len(shoppingList)): # 0 - 5 => 6 phần tử
#     print(i)  # 0,1,2, ... 5



########## Khai báo một tuple
const1 = (3.14, "123")


##### Số lượng phần tử có trong Tuple
print(len(const1))

##### Tìm kiếm phần tử trong Tuple
print(3.14 in const1)