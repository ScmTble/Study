```python
from PySide2.QtWidgets import QApplication,QMainWindow
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)

        # 使用界面定义的控件，也是从ui里面访问
        self.ui.web.load('http://www.baidu.com/')


app = QApplication([])
mainw = MainWindow()
mainw.show()
app.exec_()

# 将ui文件转为py文件使用
```





--------------------------

```python
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('main.ui')


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()

# 动态链接ui文件
```

