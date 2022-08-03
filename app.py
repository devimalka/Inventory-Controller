from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QVBoxLayout,QPushButton,QLineEdit

import sys







class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Controller")
        self.setFixedSize(500,500)
        self.mainwidget = QWidget()
        
        
        self.setCentralWidget(self.mainwidget)
        
        
        self.layout = QVBoxLayout()
        self.button = QPushButton("click me")  
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.clickbtn)
        
        
        self.mainwidget.setLayout(self.layout) 

    
    def clickbtn(self):
        self.window = SubWindow("test")
        self.window.show()






class SubWindow(QWidget):
    def __init__(self,windowtitle):
        super().__init__()
        self.setWindowTitle(windowtitle)
        self.layout = QVBoxLayout()
        self.input = QLineEdit()
        self.layout.addWidget(self.input)
        
        self.setLayout(self.layout)
        
        















app = QApplication([])


window = Mainwindow()

window.show()


app.exec()