Quan = ["BĐ", "BTL", "CG", "ĐĐ", "HBT"]
Danso = [247100, 333300, 266800, 420900, 318000]


# Quan_va_danso = {}
# index = 0
# for i in Quan:
#     Quan_va_danso[i] = Danso[index]
#     index +=1
# print(Quan_va_danso)

### Sắp xếp Dân số tăng dần


def main():
    ten_quan = ["BD", "BTL", "CG", "ĐĐ", "HBT"]
    dan_so = [247100, 333300, 266800, 420900, 318000]
    vi_tri_dan_so_cao_nhat = dan_so.index(max(dan_so))# index: tim vi tri: 3
    vi_tri_dan_so_thap_nhat = dan_so.index(min(dan_so)) # 0
    print(f"Vi tri quan co dan so cao nhat: {vi_tri_dan_so_cao_nhat}")
    print(f"Vi tri quan co dan so thap nhat: {vi_tri_dan_so_thap_nhat}")
    print(f"Quan co dan so cao nhat: {ten_quan[vi_tri_dan_so_cao_nhat]}")
    print(f"Quan co dan so thap nhat: {ten_quan[vi_tri_dan_so_thap_nhat]}")
if __name__ == "__main__":
  main()