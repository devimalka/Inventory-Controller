from PyQt5.QtCore import (
    QThread,
    QObject,
    pyqtSignal,
    pyqtSlot
)


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)

    
class Worker(QThread):
    def __init__(self,fn,**kwargs):
        super(Worker,self).__init__()
        self.signals = WorkerSignals()
        self.fn = fn
        self.kwargs = kwargs
        

    @pyqtSlot()
    def run(self):
        try:
            self.fn(**self.kwargs)
        except:
            print("Something went wrong with the Qthread worker class")