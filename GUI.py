from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QPixmap
from img2braille import *


class Stats:

    def __init__(self):
        # 从文件中加载UI定义
        self.ui = QUiLoader().load('transformGUI.ui')

        # 选择图像
        self.ui.button_selectPic.clicked.connect(self.openimage)
        self.ui.button_start.clicked.connect(self.start)

    def openimage(self):
        # getOpenFileName第一个参数为父类名，直接用最大的父类 self.ui
        imgName, imgType = QFileDialog.getOpenFileName(self.ui, "打开图片", "", "*.png;;*.jpg;;All Files(*)")
        # 文本输出
        self.ui.text_selectPic.setText(imgName)
        jpg = QPixmap(imgName).scaled(self.ui.showImage.width(), self.ui.showImage.height())
        self.ui.showImage.setPixmap(jpg)

    def start(self):
        if self.ui.text_selectPic.text():
            filename = self.ui.text_selectPic.text()
            print(filename)
            disable_smoothing = False
            no_resize = False
            width = int(self.ui.text_width.text())
            height = None
            invert = self.ui.button_invert.isChecked()

            if no_resize:
                resize_size = size_max
            elif width and not height:
                resize_size = size_from_width_ratio(width)
            elif height and not width:
                resize_size = size_from_height_ratio(height)
            else:
                resize_size = size_from_width_ratio(30)  # ！！！设置宽度，
            print(self.ui.spin_bsize.value())
            result = img2braille(
                filename=filename,
                bsize=int(self.ui.spin_bsize.value()),
                resize_size=resize_size,
                smoothing=not disable_smoothing,
                invert=invert
            )
            try:
                res = ""
                for c in result:
                    res += c
                self.ui.text_ouput.setPlainText(res)
            except BrokenPipeError:
                pass
        else:
            # 输出文本框
            QMessageBox.about(self.ui,
                              'error',
                              'select image first!'
                              )


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()