from tkinter import * 
import serial 
from ActionResult import *
from decimal import *
import time

class application: 
    baseProductCount = 5
    baseProductWeight = 0.00
    scaleWeight = 0.00
    tareWeight = 0.00
    netWeight = 0.00
    productCount = 0.00

    def onClickbuttonTare(self):
        result = self.getScaleWeight()
        if (result.errorId == 0):
            self.tareWeight = result.Obj
            self.netWeight = 0.00

    def onClickbuttonProductCount(self):
        result = self.getScaleWeight()
        if (result.errorId == 0):
            self.baseProductWeight = Decimal((Decimal(result.Obj) - Decimal(self.tareWeight)) / Decimal(self.baseProductCount))


    def onClickbuttonPlus(self):
        if (self.baseProductCount > 9):
            self.baseProductCount = 1
        elif (self.baseProductCount < 1):
            self.baseProductCount = 10
        else:
            self.baseProductCount = self.baseProductCount  + 1
        self.buttonProductCount.config(text = str(self.baseProductCount))
    def onClickbuttonMinus(self):
        if (self.baseProductCount > 10):
            self.baseProductCount = 1
        elif (self.baseProductCount < 1):
            self.baseProductCount = 10
        else:
            self.baseProductCount = self.baseProductCount  - 1
        self.buttonProductCount.config(text = str(self.baseProductCount))

    def updateFormObjects(self):
        try:
            if (self.baseProductWeight == 0):return 
            result = self.getScaleWeight()
            if (result.errorId == 0):
                self.netWeight = Decimal(result.Obj) - Decimal(self.tareWeight)
                self.productCount = round(Decimal(self.netWeight) / Decimal(self.baseProductWeight))

                self.labelNetWeight.config(text = "Net Ağırlık \n" + str(round(self.netWeight,4)))
                self.labelProductWeight.config(text = "Ürün Ağırlığı \n" + str(round(self.baseProductWeight,4)))
                self.labelProductCount.config(text = "Ürün Adeti \n" + str(self.productCount))

        except Exception as e:
            a=1
        finally:
            self.root.after(500, self.updateFormObjects)


    

    def __init__(self, window):

        self.root = window
        self.root.attributes("-fullscreen", True)
        self.root.geometry("500x500")
        
        self.weightScaleSerial = serial.Serial(port="/dev/ttyUSB0", baudrate=9600,bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=1)

        self.buttonTare = Button(self.root, text="Kasa Boşken Tıkla", bg="#709fba", command=self.onClickbuttonTare, font="Verdana 24 bold", fg="white",wraplength=150)
        self.buttonTare.place(relx = 0.01, rely = 0.01, relwidth=0.4, relheight=0.2)


        self.buttonProductCount = Button(self.root, text="5", bg="#709fba", command=self.onClickbuttonProductCount, font="Verdana 36 bold", fg="white")
        self.buttonProductCount.place(relx=0.01, rely = 0.21, relwidth=0.3, relheight=0.2)


        self.buttonPlus = Button(self.root, text="+", bg="#709fba", command=self.onClickbuttonPlus, font="Verdana 24 bold", fg="white")
        self.buttonPlus.place(relx=0.31, rely = 0.21, relwidth=0.1, relheight=0.1)


        self.buttonMinus = Button(self.root, text="-", bg="#709fba", command=self.onClickbuttonMinus, font="Verdana 24 bold", fg="white")
        self.buttonMinus.place(relx=0.31, rely = 0.31, relwidth=0.1, relheight=0.1)

        self.frameNetWeight = Frame(self.root, bg='#0097A7')
        self.frameNetWeight.place(relx=0.41, rely = 0.01, relwidth=0.4, relheight=0.2)
        self.labelNetWeight = Label(self.frameNetWeight, bg="#0097A7", text = "Net Ağırlık \n0.00", font="Verdana 24 bold", fg="white")
        self.labelNetWeight.place(relx = 0.5,rely = 0.5,anchor = 'center')
   
        self.frameProductWeight = Frame(self.root, bg='#6610f2')
        self.frameProductWeight.place(relx=0.41, rely = 0.21, relwidth=0.4, relheight=0.2)
        self.labelProductWeight = Label(self.frameProductWeight, bg="#6610f2", text = "Ürün Ağırlığı \n0.00", font="Verdana 24 bold", fg="white")
        self.labelProductWeight.place(relx = 0.5,rely = 0.5,anchor = 'center')

        self.frameProductCount = Frame(self.root, bg='#1565C0')
        self.frameProductCount.place(relx=0.41, rely = 0.41, relwidth=0.4, relheight=0.2)
        self.labelProductCount = Label(self.frameProductCount, bg="#1565C0", text = "Ürün Adeti \n0", font="Verdana 24 bold", fg="white")
        self.labelProductCount.place(relx = 0.5,rely = 0.5,anchor = 'center')
        self.root.after(500, self.updateFormObjects)
    def getScaleWeight(self):
        result = ActionResult(0, "", 0)
        currentScaleWeight = 0.00
        tryScale = 0
        try:
            if (self.weightScaleSerial.isOpen() != 0):
                self.weightScaleSerial.close();

            self.weightScaleSerial = serial.Serial(port="/dev/ttyUSB0", baudrate=9600,bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=1)
            while(True):
                currentRead =""
                tryScale = tryScale +1
                if (currentScaleWeight != 0 or tryScale > 3):
                    result.errorId = 1
                    result.errorMessage = "Tartıdan veri alınamıyor. "
                    return result
                timerStart = time.time()
                while(self.weightScaleSerial.inWaiting() ==0):
                    elapasedTime = time.time() -timerStart
                    if(elapasedTime > 2):
                        break
                while self.weightScaleSerial.inWaiting() > 0:
                    currentRead = str(self.weightScaleSerial.readline().decode('utf-8').rstrip()).split(',')
                    if currentRead:
                        if (currentRead[0] == 'ST'):
                            if (currentRead[2][0] == '+'):
                                result.errorId = 0
                                result.Obj = Decimal(currentRead[2].replace('kg', '', 1).replace('+','',1).lstrip().rstrip())
                                return result
                            else:
                                result.errorId = 3
                                result.Obj = Decimal(currentRead[2].replace('kg', '', 1).replace('-','',1).lstrip().rstrip())
                                return result
                        elif (currentRead[0] == 'US'):
                            if (currentRead[2][0] == '+'):
                                result.errorId = 3
                                result.Obj = Decimal( currentRead[2].replace('kg', '', 1).replace('+','',1).lstrip().rstrip())
                                return result
                            else:
                                result.errorId = 3
                                result.Obj = Decimal( currentRead[2].replace('kg', '', 1).replace('-','',1).lstrip().rstrip()) * (-1)
                                return result
                        else:
                            result.errorId=1
                            result.Obj = 0
                            return result
        except Exception as e: 
            result.errorId = 1
            result.errorMessage = "Hata oluştu. [" + str(e) + "]"
            result.Obj = 0
            return result
        
if __name__ == '__main__':
    window = Tk()
    app = application(window)
    
    window.mainloop()

