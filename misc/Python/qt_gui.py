import sys
from PyQt5 import QtWidgets,QtGui,QtCore,Qt
from PyQt5.QtWidgets import QTextEdit,QTextBrowser
import NAR 

class GUI(QtWidgets.QWidget):
    def __init__(self):
        #初始化————init__
        super().__init__()
        self.initGUI()
        self.last_info = ''

    def initGUI(self):
        #设置窗口大小
        self.resize(1400,900)
        #设置窗口位置(下面配置的是居于屏幕中间)
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        #设置窗口标题和图标
        self.setWindowTitle('窗口标题')
        self.setWindowIcon(QtGui.QIcon('2.png'))
        #设置窗口提示
        self.setToolTip('窗口提示')
        #设置label信息

        #self.label = QtWidgets.QLabel(self)
        #self.label.setGeometry(QtCore.QRect(100, 10, 900, 1000))
        #self.label.setText('这是lable信息')
        #self.label.setObjectName('label')
        ## 设置label提示
        #self.label.setToolTip('label提示')

        #self.outputTextEdit = Qt.QTextEdit(self)
        #self.outputTextEdit.resize(900, 600)
        #self.outputTextEdit.move(50, 10)

        #self.history_text_browser = QTextBrowser(self)
        #self.history_text_browser.resize(900, 300)
        #self.history_text_browser.move(50, 10)
        
        self.text_browser = QTextBrowser(self)
        self.text_browser.resize(1300, 600)
        self.text_browser.move(50, 10)



        
        self.inputLine = Qt.QLineEdit(self)
        self.inputLine.resize(900, 20)
        self.inputLine.move(100, 620)
        self.inputLine.editingFinished.connect(self.enterPress)

        #设置按钮
        self.btn =QtWidgets.QPushButton('concepts',self)
        self.btn.resize(80,20)
        self.btn.move(120,650)
        self.btn.clicked.connect(lambda : self.clickbtn(self.btn))

        self.reset_btn =QtWidgets.QPushButton('reset',self)
        self.reset_btn.resize(80,20)
        self.reset_btn.move(200,650)
        self.reset_btn.clicked.connect(lambda : self.clickbtn(self.reset_btn))
        self.i_btn =QtWidgets.QPushButton('inverted_atom_index',self)
        self.i_btn.resize(160,20)
        self.i_btn.move(280,650)
        self.i_btn.clicked.connect(lambda : self.clickbtn(self.i_btn))


        # 设置按钮样式
        #self.btn.setStyleSheet("background-color: rgb(164, 185, 255);"
        #                  "border-color: rgb(170, 150, 163);"
        #                  "font: 75 12pt \"Arial Narrow\";"
        #                  "color: rgb(126, 255, 46);")
        # 设置按钮提示
        #self.btn.setToolTip('按钮提示')
        #点击鼠标触发事件


        #设置输入框
        self.inputTextEdit = Qt.QTextEdit(self)
        self.inputTextEdit.resize(900, 150)
        self.inputTextEdit.move(30, 680)
        ## 设置输入框提示
        #self.inputTextEdit.setToolTip('输入框提示')

        self.send_btn =QtWidgets.QPushButton('send',self)
        self.send_btn.resize(200,40)
        self.send_btn.move(60,830)
        self.send_btn.clicked.connect(self.clickbtn_send)

        #展示窗口
        self.show();

    def show_history():
        #p = self.text_browser.toPlainText()
        #if len(p) > 6:
        #    p = p[:-6]
        #max_len = 4*1024
        #if len(p) > max_len:
        #    p = p[int(len(p)/2):]
        pass

    def add_nars(self, s):
        r = NAR.AddInput(s)
        p = "\n==>> " + s
        if 'raw' in r:
            p += "\n<< " + r['raw']
        else:
            p += "\n<< " + str(r)

        now_info = p
        p += self.last_info + "\n" + "#"*90 + "\n" + p
        self.last_info = now_info
        print(p)
        p += '\n' * 6

        self.text_browser.setPlainText(p)
        self.text_browser.moveCursor(Qt.QTextCursor.End)

        #max_len = 4*1024
        #h = self.history_text_browser.toPlainText()
        #if h > max_len:
        #    h = h[len(h)/2:]
        #self.history_text_browser.setPlainText(h + p)
        #self.history_text_browser.moveCursor(Qt.QTextCursor.End)

    def enterPress(self):
        s = self.inputLine.text()
        if s == '':
            return
        #self.outputTextEdit.setPlainText(s)
        if s.isdigit() or s.startswith("*") or s.startswith('<'):
            pass
        else:
            s = '<%s>. :|:'%s
        print("enterPress [%s]" %s)
        self.add_nars(s)
        self.inputLine.setText('')
      
    def clickbtn_send(self):
        ss = self.inputTextEdit.toPlainText()
        for s in ss.split('\n'):
            if s.startswith('//'):
                continue
            if s.strip() == "":
                continue
            print('add ' + s)
            self.add_nars(s)

    def clickbtn(self, btn):
        #print('btn %s'%btn)
        #if btn.text() == "inverted_atom_index":
        #    self.add_nars("*inverted_atom_index")
        self.add_nars("*" + btn.text())


    def reset_clickbtn(self):
        self.add_nars("*reset")

    #点击鼠标触发函数
    #def clickbtn(self):
        #self.add_nars("*concepts")
        #打印出输入框的信息
        #inputTextEditValue = self.inputTextEdit.toPlainText()
        #inputTextEdit = self.inputLine.text()
        #self.outputTextEdit.setPlainText(inputTextEditValue)
        #QtWidgets.QMessageBox.question(self, "信息", '你输入的输入框内容为:' + inputTextEditValue,QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
        #清空输入框信息
        #self.inputTextEdit.setPlainText('')

    #关闭窗口事件重写
    #def closeEvent(self, QCloseEvent):
    #    reply = QtWidgets.QMessageBox.question(self, '警告',"确定关闭当前窗口?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
    #    if reply == QtWidgets.QMessageBox.Yes:
    #        QCloseEvent.accept()
    #    else:
    #        QCloseEvent.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())
