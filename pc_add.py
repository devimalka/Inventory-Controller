from PyQt5.QtWidgets import QWidget,QVBoxLayout,QComboBox,QLineEdit,QPushButton,QLabel,QMessageBox,QListWidget,QListView
from pip import main

from sql import dbc

class addPc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Computer")
        self.seriallist = []
        
        self.layout = QVBoxLayout()
        

        self.machinetypecb = QComboBox()
     
        self.machinetypes = dbc.execute("select * from computer_type;")
        self.machinetypes = self.machinetypes.fetchall()
        
        
        #add computer types to combobox
        for i in self.machinetypes:
            self.machinetypecb.addItem(i[0])
            
        self.layout.addWidget(self.machinetypecb)
        
        # qlinedit to get serial of item
        self.itemserial = QLineEdit()
        self.layout.addWidget(self.itemserial)
        
        
        self.findbtn = QPushButton("find data")
        self.findbtn.clicked.connect(self.findComponent)
        self.layout.addWidget(self.findbtn)
        
        self.list = QListWidget()
        
        self.layout.addWidget(self.list)
        
        self.setLayout(self.layout)
        
    
    
    def findComponent(self):
        
        serial = self.itemserial.text()
        if serial not in self.seriallist:
            data = dbc.execute("select serial,description,in_date from componentdata where serial='%s'"%(serial))
            data = data.fetchall()
            data = [element for sublist in data for element in sublist]
            mainstring = ''
            for i in data:
                mainstring = mainstring + " " + str(i)
                
            if serial in data:
                self.list.addItem(str(mainstring))
                self.seriallist.append(serial)
            else:
                self.showNoItem("ITEM NOT FOUND")
        else:
            self.showNoItem("ITEM ALREADY ADDED")
            
    def showNoItem(self,message):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("item status")
        self.msg.setText(message)
        self.msg.show()
        
        
    def additemtoshow(self,data):
        self.label = QLabel(str(data))
        self.layout.addWidget(self.label)