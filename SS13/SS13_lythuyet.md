Buổi 13: Làm game với Python
- Làm quen với thư viện pygame
- Cú pháp sử dụng thư viện:  import pygame
- Hàm init
- Cách vẽ các khối: Hàm Rect()
- Hàm display()

Thư viện Pygame: là bộ thư viện sử dụng để phát triển trò chơi trong Python. Nó cung cấp các chức năng để làm việc với đồ họa, âm thanh và các yếu tố khác của một trò chơi.


Để vẽ các khối, chúng ta cần cửa sổ để hiển thị chúng
- Tạo cửa sổ bằng hàm: display.set_model():
screen = pygame.display.setmodel((width, height))

Vẽ các khối với hàm: draw.rect() || x,y là tọa độ góc bên trái trên của HCN. 
rect = pygame.Rect(x, y, width, height)

Để hiển thị những gì vừa vẽ, chúng ta cần cập nhật map chơi (màn hình) bằng hàm:
display.flip() hoặc display.update()

import sys: Là module cung cấp các hàm và biến để tương tác với hệ thống Python.