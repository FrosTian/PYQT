# 0.导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1.创建一个应用程序对象
app = QApplication(sys.argv)

t = 1
# 2.控件的操作
# 2.1创建控件
window = QWidget()
# 2.2设置控件
window.setWindowTitle('定时器')
window.resize(500, 500)

'''定时器执行的timerEvent继承自父类，所以我们要求改timerEvent，就可以创建一个新的类继承自QLabel'''
class MQLabel(QLabel):

    """把定时器放在了初始化里面，这样方便传递time_id"""
    def __init__(self, *args, **kwargs):  # 这里是要传递参数的，这个表达是通用适配所有的类型
        super().__init__(*args, **kwargs)  # 先执行父类的方法
        self.move(200, 200)
        self.setStyleSheet("font-size:72px")

    """保持了封装灵活性"""
    def start_sec(self, sec):
        self.setText(str(sec))

    def timer_ms(self, ms):
        self.time_id = self.startTimer(ms) # 每隔1000豪秒执行父类里面的timeEvent, 加上一个self. 把局部变量变成了全局变量

    """重写定时器事件部分,这里传的参数是自动补全的，是类方法的参数写法，不明白的话也可以写*args, **kwargs"""
    def timerEvent(self, a0: 'QTimerEvent'):
        # print('wer')
        # 获取当前标签内容
        curunt_sec = int(self.text())
        curunt_sec -= 1
        self.setText(str(curunt_sec))
        if curunt_sec == 0:
            print('停止了')
            self.killTimer(self.time_id)  # 这里是要转递定时器的id的


lab = MQLabel(window)
lab.start_sec(5)  # 设定起始数字
lab.timer_ms(500)  # 设定定时器间隔
# 2.3展示控件
window.show()
# 3.应用程序的执行，进入循环消息
sys.exit(app.exec_())