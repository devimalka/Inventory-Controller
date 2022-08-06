from operator import index
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QGridLayout,
    QHBoxLayout,
    QMessageBox,
    QComboBox,
    QErrorMessage,
    QTableWidget,
    QTableWidgetItem
    )

import sys
from QmultiThreading import Worker,WorkerSignals

from sql import DBConnector

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Controller")
        self.setFixedSize(500,500)
        self.mainwidget = QWidget()
        
        
        self.setCentralWidget(self.mainwidget)
        
        
        self.layout = QGridLayout()
        self.button = QPushButton("click me")  
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.clickbtn)
        self.showdata = QPushButton("show data")
        self.showdata.clicked.connect(self.showd)
        self.layout.addWidget(self.showdata)
        self.mainwidget.setLayout(self.layout) 

    
    def clickbtn(self):
        self.window = SubWindow("test")
        self.window.show()
        
    def showd(self):
        self.window2 = tableview()
        self.window2.show()

 



class SubWindow(QWidget):
    def __init__(self,windowtitle):
        super().__init__()
        self.setWindowTitle(windowtitle)

        self.mainLayout = QVBoxLayout()
        
       
        self.serial = myLayout(QHBoxLayout,'Serial')
        self.description = myLayout(QHBoxLayout,'Description')  
        self.cb = QComboBox(self)

        self.mainLayout.addWidget(self.cb)
        self.mainLayout.addLayout(self.serial.layout)
        self.mainLayout.addLayout(self.description.layout)
        
        self.dbc = DBConnector()
        self.combo = self.dbc.execute("select * from component")
        self.combolist = self.combo.fetchall()
        for i in self.combolist:
            self.cb.addItem(i[1])
        self.savebutton = QPushButton("SAVE")
        self.savebutton.clicked.connect(self.save)
        self.mainLayout.addWidget(self.savebutton)
        
        self.setLayout(self.mainLayout)        
        


    def save(self):
        ComponentID = self.dbc.execute("select componentID from component where component_name='%s'"%(self.cb.currentText())).fetchall()
        ComponentID = ComponentID[0][0]
        self.kwargs = {'query':"insert into componentdata(serial,description,componentID) values('%s','%s',%d)"%(self.serial.layoutLine.text(),self.description.layoutLine.text(),ComponentID)}
        self.worker = Worker(self.dbc.execute,**self.kwargs)
        self.worker.finished.connect(self.succesmsg)
        self.worker.finished.connect(self.close)
        self.worker.start()
        
    def succesmsg(self):
       msg= QErrorMessage()
       
    
       msg.exec_()

class myLayout():
    def __init__(self,Layout,labelname):
        super().__init__()
        self.ly = Layout
        
        self.layout = self.ly()
        self.layoutLable = QLabel(labelname)
        self.layoutLine = QLineEdit()
        self.layoutLine.move(0,50)
        self.layout.addWidget(self.layoutLable)
        self.layout.addWidget(self.layoutLine)
        
        

class tableview(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Show data")
        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.databasec = DBConnector()
        self.results = self.databasec.execute('select serial,description,component_name from componentdata inner join  component on  componentdata.componentID=component.componentID;')
        self.rows = self.results.fetchall()
        self.table.setColumnCount(len(self.rows[0]))
        self.table.setRowCount(len(self.rows))
        self.columns = [i[0] for i in self.results.description]
        print(self.columns)
        for row in self.rows:
           print(row)
        count = 0

        self.table.setHorizontalHeaderLabels(self.columns)
        for row in self.rows:

            x = 0
            for i in row:
                self.table.setItem(count,x,QTableWidgetItem(str(i)))
                x+=1
            count+=1
        # self.table.setItem(count,0,QTableWidgetItem("HELLO"))
        # self.table.setItem(count,1,QTableWidgetItem("HELLO"))

        self.table
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)
        






app = QApplication([])


window = Mainwindow()

window.show()


app.exec()