import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)  # sys.argv 是通过命令行传参数

window = QWidget()
window.resize(500, 500)
window.move(300, 300)
# print(window.width())
window.show()  # 展示的是父控件

geshu = 100
# 每行的数量
colum_num = 3

# 计算一个空间的宽度
widget_width = window.width()/colum_num
# 计算行数
height_num = (geshu - 1) // colum_num + 1

#计算高度
widget_high = window.height()/height_num

for i in range(0, geshu):
    w = QWidget(window)

    Wid_x = i % colum_num * widget_width
    Wid_y = i // colum_num * widget_high
    w.resize(widget_width, widget_high)

    w.setStyleSheet('background-color:red;border:1px solid yellow')
    w.move(Wid_x, Wid_y)
    w.show()

sys.exit(app.exec())