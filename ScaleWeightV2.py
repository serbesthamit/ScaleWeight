from tkinter import * 
import serial 
from ActionResult import *
from decimal import *
import time

class application: 
    baseProductCount = 10
    baseProductWeight = 0.00
    scaleWeight = 0.00
    tareWeight = 0.00
    netWeight = 0.00
    productCount = 0.00
    #serialPort ="COM7"
    serialPort ="/dev/ttyUSB0"
    def onClickbuttonTare(self):
        result = self.getScaleWeight()
        if (result.errorId == 0):
            self.tareWeight = result.Obj
            self.netWeight = 0.00
            self.baseProductWeight =0
            self.productCount = 0
            self.frameEmptyTare.config(bg="#429A0A")
            self.labelEmptyTareName.config(bg="#429A0A")
            self.labelEmptyTareValue.config(bg="#429A0A")
            self.frameProductCount.config(bg="#A00A30")
            self.labelProductCountName.config(bg="#A00A30")
            self.labelProductCountValue.config(bg="#A00A30")
            self.buttonProductCount.config(bg="#041948")
        else:
            self.buttonTare.config(bg="#A00A30")
            self.buttonProductCount.config(bg="#A00A30")


    def onClickbuttonProductCount(self):
        result = self.getScaleWeight()
        if (result.errorId == 0):
            self.baseProductWeight = Decimal((Decimal(result.Obj) - Decimal(self.tareWeight)) / Decimal(self.baseProductCount))
            # self.buttonTare.config(bg="#3B5798")
            if (self.baseProductWeight <= 0.002): return
            self.frameProductCount.config(bg="#429A0A")
            self.labelProductCountName.config(bg="#429A0A")
            self.labelProductCountValue.config(bg="#429A0A")
            #self.buttonProductCount.config(bg="#429A0A")



    def onClickbuttonPlus(self):
        if (self.baseProductCount >= 10 and self.baseProductCount <50):
            self.baseProductCount = self.baseProductCount+5
        elif (self.baseProductCount >= 50):
            self.baseProductCount = self.baseProductCount+10
        else:
            self.baseProductCount = self.baseProductCount  + 1
        self.buttonProductCount.config(text = str(self.baseProductCount))
    def onClickbuttonMinus(self):
        if (self.baseProductCount ==1):
            a=1
        elif (self.baseProductCount >= 15 and self.baseProductCount <=50):
            self.baseProductCount = self.baseProductCount-5
        elif (self.baseProductCount >= 60):
            self.baseProductCount = self.baseProductCount-10
        else:
            self.baseProductCount = self.baseProductCount  - 1
        self.buttonProductCount.config(text = str(self.baseProductCount))

    def updateFormObjects(self):
        try:
            #if (self.baseProductWeight == 0):return 
            result = self.getScaleWeight()
            if (result.errorId == 0):
                self.netWeight = Decimal(result.Obj) - Decimal(self.tareWeight)
                if (self.baseProductWeight > 0):
                    self.productCount = round(Decimal(self.netWeight) / Decimal(self.baseProductWeight),2)
                    if(self.productCount <=0 ):
                        self.tareWeight =0
                        self.netWeight =0
                        # self.baseProductCount =0
                        self.productCount =0
                        self.baseProductWeight =0
                        self.frameEmptyTare.config(bg="#A00A30")
                        self.labelEmptyTareName.config(bg="#A00A30")
                        self.labelEmptyTareValue.config(bg="#A00A30")
                        self.frameProductCount.config(bg="#A00A30")
                        self.labelProductCountName.config(bg="#A00A30")
                        self.labelProductCountValue.config(bg="#A00A30")

                self.labelEmptyTareValue.config(text = str(round(self.tareWeight,3))+ " Kg." )
                self.labelNetWeightValue.config(text = str(round(self.netWeight,3)) + " Kg.")
                
                self.labelProductWeightKgValue.config(text = str(round(self.baseProductWeight,3)) + " Kg.")
                self.labelProductWeightGrValue.config(text = str(round((self.baseProductWeight * 1000),1)) + " Gr.")
                self.labelProductCountValue.config(text = str(round(self.productCount)))

        except Exception as e:
            a=1
        finally:
            self.root.after(100, self.updateFormObjects)


    
 
    def __init__(self, window):
 #github test1
 
        self.root = window 
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-topmost", 1)
        self.root.geometry("800x480")
        
        self.weightScaleSerial = serial.Serial(port=self.serialPort, baudrate=9600,bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=1)
        #self.weightScaleSerial = serial.Serial(port="/dev/ttyUSB0", baudrate=9600,bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=1)

        self.frameEmptyTare = Frame(self.root, bg='#A00A30')
        self.frameEmptyTare.place(relx=0, rely = 0, relwidth=0.5, relheight=0.25)
        self.labelEmptyTareName = Label(self.frameEmptyTare, bg="#A00A30", text = "Boş Kasa", font="Verdana 16 bold", fg="white")
        self.labelEmptyTareName.place(relx = 0.5,rely = 0.3,anchor = 'center')
        self.labelEmptyTareValue = Label(self.frameEmptyTare, bg="#A00A30", text = "0.00", font="Verdana 30 bold", fg="white")
        self.labelEmptyTareValue.place(relx = 0.5,rely = 0.6,anchor = 'center')

        self.frameNetWeight = Frame(self.root, bg='#20418E')
        self.frameNetWeight.place(relx=0.50, rely = 0, relwidth=0.5, relheight=0.25)
        self.labelNetWeightName = Label(self.frameNetWeight, bg="#20418E", text = "Net Ağırlık", font="Verdana 16 bold", fg="white")
        self.labelNetWeightName.place(relx = 0.5,rely = 0.3,anchor = 'center')
        self.labelNetWeightValue = Label(self.frameNetWeight, bg="#20418E", text = "0.00", font="Verdana 30 bold", fg="white")
        self.labelNetWeightValue.place(relx = 0.5,rely = 0.6,anchor = 'center')



        self.frameProductWeightKg = Frame(self.root, bg='#092461')
        self.frameProductWeightKg.place(relx=0, rely = 0.25, relwidth=0.5, relheight=0.25)
        self.labelProductWeightKgName = Label(self.frameProductWeightKg, bg="#092461", text = "Ürün Ağırlığı", font="Verdana 16 bold", fg="white")
        self.labelProductWeightKgName.place(relx = 0.5,rely = 0.3,anchor = 'center')
        self.labelProductWeightKgValue = Label(self.frameProductWeightKg, bg="#092461", text = "0.00 Kg", font="Verdana 30 bold", fg="white")
        self.labelProductWeightKgValue.place(relx = 0.5,rely = 0.6,anchor = 'center')


        self.frameProductWeightGr = Frame(self.root, bg='#041948')
        self.frameProductWeightGr.place(relx=0.50, rely = 0.25, relwidth=0.50, relheight=0.25)
        self.labelProductWeightGrName = Label(self.frameProductWeightGr, bg="#041948", text = "Ürün Ağırlığı", font="Verdana 16 bold", fg="white")
        self.labelProductWeightGrName.place(relx = 0.5,rely = 0.3,anchor = 'center')
        self.labelProductWeightGrValue = Label(self.frameProductWeightGr, bg="#041948", text = "0.00 Gr", font="Verdana 30 bold", fg="white")
        self.labelProductWeightGrValue.place(relx = 0.5,rely = 0.6,anchor = 'center')

        #self.frameProductCount = Frame(self.root, bg='#FF7043')
        self.frameProductCount = Frame(self.root, bg='#A00A30')
        self.frameProductCount.place(relx=0, rely = 0.50, relwidth=1, relheight=0.25)
        self.labelProductCountName = Label(self.frameProductCount, bg="#A00A30", text = "Ürün Adeti", font="Verdana 16 bold", fg="white")
        self.labelProductCountName.place(relx = 0.5,rely = 0.3,anchor = 'center')
        self.labelProductCountValue = Label(self.frameProductCount, bg="#A00A30", text = "0.00", font="Verdana 30 bold", fg="white")
        self.labelProductCountValue.place(relx = 0.5,rely = 0.6,anchor = 'center')




        self.buttonTare = Button(self.root, text="1-Boş Kasa Ağırlık AL", bg="#3B5798", command=self.onClickbuttonTare, font="Verdana 18 bold", fg="white")
        self.buttonTare.place(relx = 0, rely = 0.75, relwidth=0.5, relheight=0.25)


        self.buttonProductCount = Button(self.root, text=str(self.baseProductCount), bg="#041948", command=self.onClickbuttonProductCount, font="Verdana 18 bold", fg="white")
        self.buttonProductCount.place(relx=0.5, rely = 0.75, relwidth=0.30, relheight=0.25)


        self.buttonPlus = Button(self.root, text="+", bg="#20418E", command=self.onClickbuttonPlus, font="Verdana 18 bold", fg="white")
        self.buttonPlus.place(relx=0.80, rely = 0.75, relwidth=0.20, relheight=0.125)


        self.buttonMinus = Button(self.root, text="-", bg="#3B5798", command=self.onClickbuttonMinus, font="Verdana 18 bold", fg="white")
        self.buttonMinus.place(relx=0.80, rely = 0.875, relwidth=0.20, relheight=0.125)



        self.root.after(100, self.updateFormObjects)
    def getScaleWeight(self):
        result = ActionResult(0, "", 0)
        currentScaleWeight = 0.00
        tryScale = 0
        try:
            if (self.weightScaleSerial.isOpen() != 0):
                self.weightScaleSerial.close();

            self.weightScaleSerial = serial.Serial(port=self.serialPort, baudrate=9600,bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=1)
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

