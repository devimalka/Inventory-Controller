import barcode
from sql import dbc
from barcode import PROVIDED_BARCODES
from barcode.writer import ImageWriter
import string    
import random 




#generate random barcode
def generateBarcodeSerial():
        barcodeserial = ''.join(random.choices(string.digits,k=13))
        return barcodeserial
    
    

#cheking the barcode serial if barcode serial is in database the generateBarCodeSerial is called again in recursion checkBarCodeSerial    
def checkBarcodeSerial(barocodeSerialinput):
        barcodeSerial = barocodeSerialinput
        barcodeSerialData = dbc.execute('select computer_barcode from computer;')
        barcodeSerialData = barcodeSerialData.fetchall()
        barcodeSerialData = [item for sublist in barcodeSerialData for item in sublist]
        print("len of barcode data is %d"%(len(barcodeSerialData)))
        if barcodeSerial not in barcodeSerialData:
            return barcodeSerial
        elif barcodeSerial in barcodeSerialData:
            checkBarcodeSerial(generateBarcodeSerial())
            
            
        
