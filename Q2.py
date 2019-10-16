# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys
import random

# 1.创建一个应用程序对象
app = QApplication(sys.argv)
 
# 2.控件的操作
# 2.1创建控件    
window = QWidget()
# 2.2设置控件
window.setWindowTitle('随机数')
# window.resize(200,200)
# window.move(200,0)
label1 = QLabel(window)
name = random.randint(0, 99)
label1.setText(str(name))
label1.move(50, 20)
label1.setStyleSheet('background-color:red')


def add():
    newTest = random.randint(0, 99)
    label1.setText(str(newTest))
    label1.adjustSize()

btn1 = QPushButton(window)
btn1.setText('reset')
btn1.move(20,40)
btn1.clicked.connect(add)
# 2.3展示控件
window.show()

# window.setGeometry(500,500,400,400)
print('-'*20)
print(window.geometry())
# 3.应用程序的执行，进入循环消息
sys.exit(app.exec_())