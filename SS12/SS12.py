# f = open("./SS12/example.txt","x")
# # Thêm nội dung vào trong file
# f.write("Hello World!!!")
# f.close()


## Đọc nội dung trong file
# f = open("./SS12/example.txt","r")
# print(f.read())
# f.close()


##### Bài 2
# f = open("./SS12/example.txt","r")
## Dùng vòng lặp để line by line
# i = 0
# for x in f:
#     print(x)
#     i+=1
# f.close()
# print(f"Số dòng trong file example.txt là: {i}")

## C2
# f = open("./SS12/example.txt", "r")
# a = f.readlines()
# b = len(a)
# f.close()
# print(b)


# ### Chữa bài 3a/b
# f = open('./SS12/numbers.txt', "w")
# ## đoạn code thêm nội dung vào từng dòng 1 trong file
# f.write("1\n2\n3\n4\n5")
# f.close()

# ### Đọc các số từ file và tính tổng của chúng
# f = open('./SS12/numbers.txt', "r")
# total = 0
# line = 0
# for i in f:
#     i = int(i) ## ép kiểu dữ liệu thành kiểu int
#     total = total + i
#     line += 1
# print(f"Tổng của các số trong file numbers.txt là: {total}")
# print(f"Giá trị trung fình của các số trong file numbers.txt là: {total/line} ")
# f.close()


### Chữa bài 4: 
## Khởi tạo hàm
def replace_word_in_file(input_file, output_file, target_word, replacement_word):
    try:
        ## Đọc nội dung từ file đầu vào
        with open(input_file, "r") as file:
            content = file.read()
        
        ## thay thế từ mục tiêu bằng từ khóa thay thế
        new_content = content.replace(target_word, replacement_word)

        ## Ghi nội dung mới vào file đầu ra
        with open(output_file, "w") as file:
            file.write(new_content)
        
        print(f'đã thay thế {target_word} bằng {replacement_word} trong file {output_file}.')

    except FileNotFoundError:
        print(f"{input_file} không tồn tại.")
    except Exception as e:
        print(f"Có lỗi xảy ra {e}")

## Sử dụng hàm với các thông số cụ thể 
replace_word_in_file('./SS12/sample.txt', "./SS12/sample_modified.txt", "mẫu", "ví dụ")