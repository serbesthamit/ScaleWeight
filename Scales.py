from ActionResult import *
import serial
from tkinter import *
import tkinter as tk
import time
import math
from decimal import *
# pack
# place
# grid


class application:
    scaleWeight = 0.00
    oldWeight = 0.00
    oldScaleWeight = 0.00
    tareWeight = 0.00
    netWeight = 0.00
    productWeight = 0.00
    productCount = 0.00

    def __init__(self, window):
        # root.overrideredirect(1) 
        #self.root.attributes("-topmost", 1)
        self.root = window
        self.root.attributes("-fullscreen", True)
        self.root.geometry("500x500")
        self.weightScaleSerial = serial.Serial(
            port="/dev/ttyUSB0", baudrate=9600, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=1)

        #self.scaleWeight = StringVar(self.root)
        # self.scaleWeight.set("0.00")

        # -------SCALE WEIGHT------------------------------------------------------------------------------------------------------------------------------------

        self.frameScaleWeight = Frame(self.root, bg='#68e365')
        #self.frameScaleWeight.bind("<Button-1>", ConnectToScale)
        self.frameScaleWeight.place(
            relx=0.01, rely=0.01, relwidth=0.98, relheight=0.20)

        self.labelScaleWeightName = Label(
            self.frameScaleWeight, bg="#68e365", text="Tartı Ağırlık", font="Verdana 24 bold", fg="white")
        #self.labelScaleWeightHint.bind("<Button-1>", ConnectToScale)
        self.labelScaleWeightName.place(relx=0.01, rely=0.5, anchor='w')

        self.labelScaleWeightHint = Label(
            self.frameScaleWeight, bg="#68e365", text="Şu an ki tartı ağırlığı", font="Verdana 12 bold", fg="white")
        #self.labelScaleWeightHint.bind("<Button-1>", ConnectToScale)
        self.labelScaleWeightHint.place(relx=0.01, rely=1.0, anchor='sw')

        self.labelScaleWeight = Label(
            self.frameScaleWeight, bg="#68e365", text="0.00", font="Verdana 24 bold", fg="white")
        #labelScaleWeight.bind("<Button-1>", ConnectToScale)
        self.labelScaleWeight.place(relx=0.98, rely=0.2, anchor='ne')

        # -------TARE WEIGHT-----------------------------------------------------------------------------------------------------------------------------------

        self.frameTareWeight = Frame(self.root, bg='#68e365')
        self.frameTareWeight.place(
            relx=0.01, rely=0.22, relwidth=0.80, relheight=0.20)

        self.labelTareWeightName = Label(
            self.frameTareWeight, bg="#68e365", text="Dara Ağırlık", font="Verdana 24 bold", fg="white")
        #self.labelScaleWeightHint.bind("<Button-1>", ConnectToScale)
        self.labelTareWeightName.place(relx=0.01, rely=0.5, anchor='w')

        self.labelTareWeightHint = Label(self.frameTareWeight, bg="#68e365",
                                         text="Koliyi tartının üzerine koyduğunuzda DARA AL butonuna tıklayınız.", font="Verdana 12 bold", fg="white")
        self.labelTareWeightHint.place(relx=0.01, rely=1.0, anchor='sw')

        self.labelTareWeight = Label(
            self.frameTareWeight, bg="#68e365", text="0.00", font="Verdana 24 bold", fg="white")
        self.labelTareWeight.place(relx=0.98, rely=0.2, anchor='ne')

        self.buttonTare = Button(
            self.root, text="Dara Al", bg="#ffa755", command=self.setTareScale)
        self.buttonTare.place(relx=0.81, rely=0.22,
                              relwidth=0.18, relheight=0.20)

        # ---NET WEIGHT---------------------------------------------------------------------------------------------------------------------------------------

        self.frameNetWeight = Frame(self.root, bg='#68e365')
        self.frameNetWeight.place(
            relx=0.01, rely=0.44, relwidth=0.80, relheight=0.20)

        self.labelNetWeightName = Label(
            self.frameNetWeight, bg="#68e365", text="Net Ağırlık", font="Verdana 24 bold", fg="white")
        self.labelNetWeightName.place(relx=0.01, rely=0.5, anchor='w')

        self.labelNetWeightHint = Label(self.frameNetWeight, bg="#68e365",
                                        text="Dara ağırlığı düşüldükten sonraki net ağırlık", font="Verdana 12 bold", fg="white")
        self.labelNetWeightHint.place(relx=0.01, rely=1.0, anchor='sw')

        self.labelNetWeight = Label(
            self.frameNetWeight, bg="#68e365", text="0.00", font="Verdana 24 bold", fg="white")
        self.labelNetWeight.place(relx=0.98, rely=0.2, anchor='ne')

        self.buttonNet = Button(
            self.root, text="Net Ağr.", bg="#6610f2", fg="white", command=self.setNetWeight)
        self.buttonNet.place(relx=0.81, rely=0.44,
                             relwidth=0.18, relheight=0.20)

        # ----PRODUCT WEIGHT & PRODUCT COUNT--------------------------------------------------------------------------------------------------------------------------------------

        self.frameProductWeight = Frame(self.root, bg='#68e365')
        self.frameProductWeight.place(
            relx=0.01, rely=0.66, relwidth=0.48, relheight=0.20)

        self.labelProductWeightName = Label(
            self.frameProductWeight, bg="#68e365", text="Ürün Ağırlığı", font="Verdana 24 bold", fg="white")
        self.labelProductWeightName.place(relx=0.01, rely=0.5, anchor='w')

        self.labelProductWeightHint = Label(self.frameProductWeight, bg="#68e365",
                                            text="Tüm ürünleri kolinin içine koyduktan sonra üründen bir adet çıkarın.", font="Verdana 12 bold", fg="white")
        self.labelProductWeightHint.place(relx=0.01, rely=1.0, anchor='sw')

        self.labelProductWeight = Label(
            self.frameProductWeight, bg="#68e365", text="0.00", font="Verdana 24 bold", fg="white")
        self.labelProductWeight.place(relx=0.98, rely=0.2, anchor='ne')

        # ------------------------------------------------------------------------------------------------------------------------------------------

        self.frameProductCount = Frame(self.root, bg='#68e365')
        self.frameProductCount.place(
            relx=0.50, rely=0.66, relwidth=0.48, relheight=0.20)

        self.labelProductCountName = Label(
            self.frameProductCount, bg="#68e365", text="Ürün Adeti", font="Verdana 24 bold", fg="white")
        self.labelProductCountName.place(relx=0.01, rely=0.5, anchor='w')

        self.labelProductCountHint = Label(self.frameProductCount, bg="#68e365",
                                           text="Ürün ağırlığı ve Adeti hesaplanacaktır.", font="Verdana 12 bold", fg="white")
        self.labelProductCountHint.place(relx=0.01, rely=1.0, anchor='sw')

        self.labelProductCount = Label(
            self.frameProductCount, bg="#68e365", text="0.00", font="Verdana 24 bold", fg="white")
        self.labelProductCount.place(relx=0.98, rely=0.2, anchor='ne')

        # ------------------------------------------------------------------------------------------------------------------------------------------

        self.frameMessage = Frame(self.root, bg='#68e365')
        self.frameMessage.place(
            relx=0.01, rely=0.88, relwidth=0.98, relheight=0.10)
        self.labelMessage = Label(self.frameMessage, bg="#68e365",
                                           text="", font="Verdana 12 bold", fg="white")
        self.labelMessage.place(relx=0.5, rely=0.5, anchor='center')

        self.root.after(2000, self.updateFormObjects)

    def setTareScale(self):
        try:
            self.tareWeight = self.scaleWeight
            self.netWeight = 0
            self.productWeight = 0
            self.productCount = 0
        except Exception as e:
            a = 1
        finally:
            self.updateFormObjects()

    def setNetWeight(self):
        try:
            self.netWeight = self.scaleWeight - self.tareWeight
            self.productWeight = 0
            self.productCount = 0
        except Exception as e:
            a = 1
        finally:
            self.updateFormObjects()

    def getScaleWeight(self):
        result = ActionResult(0, "", 0)
        global scaleWeight

        currentScaleWeight = 0.00
        tryScale = 0
        try:
            if (self.weightScaleSerial.isOpen() != 0):
                self.weightScaleSerial.close()

            #self.weightScaleSerial = serial.Serial(port="COM22", baudrate=9600,bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=1)
            self.weightScaleSerial = serial.Serial(
                port="/dev/ttyUSB0", baudrate=9600, bytesize=serial.SEVENBITS, parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=1)
            while(True):
                currentRead = ""
                tryScale = tryScale + 1
                if (currentScaleWeight != 0 or tryScale > 3):
                    result.errorId = 1
                    result.errorMessage = "Tartıdan veri alınamıyor. "
                    return result
                #self.weightScaleSerial.write(bytes("P", "utf-8"))
                ##currentRead = str(self.weightScaleSerial.readline().decode('utf-8').rstrip()).split(',')
                # self.weightScaleSerial.flush()
                timerStart = time.time()
                while(self.weightScaleSerial.inWaiting() == 0):
                    elapasedTime = time.time() - timerStart
                    if(elapasedTime > 2):
                        #result.errorId = 1
                        #result.errorMessage = "Terazi ya kapalı ya kablosu çıkmış lutfen kontrol edin !"
                        break
                while self.weightScaleSerial.inWaiting() > 0:
                    currentRead = str(self.weightScaleSerial.readline().decode(
                        'utf-8').rstrip()).split(',')
                    if currentRead:
                        if (currentRead[0] == 'ST'):
                            # return str(Decimal( currentRead.replace('ST,NT,+', '', 1).lstrip().rstrip().replace('kg','')))
                            if (currentRead[2][0] == '+'):
                                result.errorId = 0
                                result.Obj = Decimal(currentRead[2].replace(
                                    'kg', '', 1).replace('+', '', 1).lstrip().rstrip())
                                return result
                                #currentScaleWeight = Decimal( currentRead[2].replace('kg', '', 1).replace('+','',1).lstrip().rstrip())
                                break
                                # //return str(Decimal( currentRead[2].replace('kg', '', 1).replace('+','',1).lstrip().rstrip()))
                            else:
                                result.errorId = 3
                                result.Obj = Decimal(currentRead[2].replace(
                                    'kg', '', 1).replace('-', '', 1).lstrip().rstrip())
                                return result
                                #currentScaleWeight = Decimal( currentRead[2].replace('kg', '', 1).replace('-','',1).lstrip().rstrip()) * (-1)
                                # return str(Decimal( currentRead[2].replace('kg', '', 1).replace('-','',1).lstrip().rstrip()) * (-1))

                        elif (currentRead[0] == 'US'):
                            if (currentRead[2][0] == '+'):
                                result.errorId = 3
                                result.Obj = Decimal(currentRead[2].replace(
                                    'kg', '', 1).replace('+', '', 1).lstrip().rstrip())
                                return result
                                #currentScaleWeight = Decimal( currentRead[2].replace('kg', '', 1).replace('+','',1).lstrip().rstrip())
                            else:
                                result.errorId = 3
                                result.Obj = Decimal(currentRead[2].replace(
                                    'kg', '', 1).replace('-', '', 1).lstrip().rstrip()) * (-1)
                                return result
                                #currentScaleWeight = Decimal( currentRead[2].replace('kg', '', 1).replace('-','',1).lstrip().rstrip()) * (-1)
                        else:
                            result.errorId = 1
                            result.Obj = 0
                            return result
                            # return str(Decimal( currentRead[2].replace('kg', '', 1).lstrip().rstrip()))
                            # return str(Decimal( currentRead.replace('UT,NT,+', '', 1).lstrip().rstrip().replace('kg','')))
        except Exception as e:
            #result.errorId = 1
            #result.errorMessage = "Hata Oluştu [GetScaleWeight try, except]" + str(e)
            #scaleWeight = "- 0.00"
            #self.scaleWeight = "-0.00"
            result.errorId = 1
            result.errorMessage = "Hata oluştu. [" + str(e) + "]"
            result.Obj = 0
            return result
        # finally:

            #self.scaleWeight = currentScaleWeight
            # self.updateFormLabels()
            #self.root.after(1000, self.getScaleWeight)
    def updateFormObjects(self):
        try:
            resultScaleWeight = self.getScaleWeight()
            if (resultScaleWeight.errorId != 0):
                self.UpdateFormObjects() 
                return 
            bgColor = "#68e365"
            if (resultScaleWeight.errorId != 0):
                bgColor = "#dc3545"

            self.scaleWeight = resultScaleWeight.Obj
            if (self.oldScaleWeight > 0):
                change =  self.scaleWeight- self.oldScaleWeight
                if  (abs(change) <= 0.002):
                    self.updateFormObjects()
                    return 
                    #self.productWeight = (self.oldScaleWeight - self.scaleWeight)
                    #self.productCount = math.ceil((self.oldScaleWeight - self.tareWeight) / self.productWeight)
                #else:
                #a=1
            self.currentProductWeight = (self.netWeight - (self.scaleWeight - self.tareWeight))

            if ((self.productCount == 0 or self.currentProductWeight != self.productWeight)

                and resultScaleWeight.errorId == 0):
                if (self.tareWeight > 0):
                    change = self.scaleWeight - self.tareWeight
                    if(abs(change) > 0.0021):
                        self.oldScaleWeight = change
                if (self.netWeight > 0 and self.tareWeight > 0 and self.scaleWeight > 0 and self.netWeight > self.oldScaleWeight):
                    self.productWeight = (self.netWeight - self.oldScaleWeight)
                    self.productCount = round((
                        self.netWeight / self.productWeight), 0)

            #self.oldScaleWeight = self.scaleWeight
            self.labelScaleWeight.config(text=str(self.scaleWeight))
            self.frameScaleWeight.config(bg=bgColor)
            self.labelScaleWeightName.config(bg=bgColor)
            self.labelScaleWeightHint.config(bg=bgColor)
            self.labelScaleWeight.config(bg=bgColor)

            self.frameTareWeight.config(bg=bgColor)
            self.labelTareWeight.config(text=str(self.tareWeight))
            self.labelTareWeightName.config(bg=bgColor)
            self.labelTareWeightHint.config(bg=bgColor)
            self.labelTareWeight.config(bg=bgColor)

            self.frameNetWeight.config(bg=bgColor)
            self.labelNetWeight.config(text=str(self.netWeight))
            self.labelNetWeightName.config(bg=bgColor)
            self.labelNetWeightHint.config(bg=bgColor)
            self.labelNetWeight.config(bg=bgColor)

            self.frameProductWeight.config(bg=bgColor)
            self.labelProductWeight.config(text=str(self.productWeight))
            self.labelProductWeightName.config(bg=bgColor)
            self.labelProductWeightHint.config(bg=bgColor)
            self.labelProductWeight.config(bg=bgColor)

            self.frameProductCount.config(bg=bgColor)
            self.labelProductCount.config(text=str(self.productCount))
            self.labelProductCountName.config(bg=bgColor)
            self.labelProductCountHint.config(bg=bgColor)
            self.labelProductCount.config(bg=bgColor)

            message = ""
            if (self.tareWeight == 0):
                message = "Önce boş koli yerleştirip Dara Al tuşuna basın."
            elif (self.netWeight == 0):
                message = "Tüm ürünleri koliye doldurduktan sonra Net Ağr. tuşuna basın."
            elif (self.productCount == 0):
                message = "Şimdi koliden bir adet ürün alarak ürün sayısının hesaplanmasını bekleyin."
            else:
                message = "Ürün sayısı hesaplanmıştır. İşleme yeniden başlamak için Dara Al tuşuna basın. "

            self.labelMessage.config(text= message)
            
            #self.labelNetWeight.config(text=str(self.scaleWeight - self.tareWeight))
            #self.labelNetWeight.config(bg = bgColor)
        except Exception as e:
            a = 1
        finally:
            self.root.after(1000, self.updateFormObjects)

    # def updateScaleWeight(self):
    #    try:
    #        currentRead =""
    #        while self.weightScaleSerial.inWaiting() > 0:
    #            currentRead = str(self.weightScaleSerial.readline().decode('utf-8').rstrip()).split(',')
    #            #currentRead = str(self.weightScaleSerial.readline().decode('utf-8').rstrip())
    #            if currentRead:
    #                if (currentRead[0] == 'ST'):
    #                    if (currentRead[2][0] == '+'):
    #                        self.labelTareWeight.config(text = str(Decimal( currentRead[2].replace('kg', '', 1).replace('+','',1).lstrip().rstrip())))
    #                    else:
    #                        self.labelTareWeight.config(text = str(Decimal( currentRead[2].replace('kg', '', 1).replace('-','',1).lstrip().rstrip()) * (-1)))

    #                elif (currentRead[0] == 'UT'):
    #                    if (currentRead[2][0] == '+'):
    #                        self.labelTareWeight.config(text = str(Decimal( currentRead[2].replace('kg', '', 1).replace('+','',1).lstrip().rstrip())))
    #                    else:
    #                        self.labelTareWeight.config(text = str(Decimal( currentRead[2].replace('kg', '', 1).replace('-','',1).lstrip().rstrip()) * (-1)))
    #                    #self.labelTareWeight.config(text = str(Decimal( currentRead[2].replace('kg', '', 1).lstrip().rstrip())))
    #    except Exception as e:
    #        #result.errorId = 1
    #        #result.errorMessage = "Hata Oluştu [GetScaleWeight try, except]" + str(e)
    #        #scaleWeight = "- 0.00"
    #        self.labelTareWeight.config(text = "-0.00")
    #    finally:
    #        self.labelTareWeight.after(1000, self.updateScaleWeight)


def ConnectToScale(event):
    # labelScaleWeightHint.config(text='Ok')
    print('Ok')


#button = RoundedButton(root, 200, 100, 50, 2, 'red', 'white', command=ConnectToScale)

#button.place(relx=.1, rely=.1)
# frameLeft = Frame(root, bg="#add8e6")
#frameLeft.place(relx=0.1, rely=0.21, relwidth=0.23, relheight=0.5)

# frameRight = Frame(root, bg="#add8e6")
#frameRight.place(relx=0.34, rely=0.21, relwidth=0.56, relheight=0.5)

# labelTitle = Label(frameTop, bg="#add8e6", text = "Terazi Uygulaması", font="Verdana 12 bold")
#labelTitle.pack(padx=10, pady=10,side=LEFT)

# textServerIpAddress = Text(frameTop, height=9, width=40)#, value="192.168.1.117", name="serverAddress")
#textServerIpAddress.pack(padx=10, pady=10, side=LEFT)

#buttonConnect = Button(frameTop, text="Connect", command=ConnectToScale)
#buttonConnect.pack(padx=10, pady=10)
def CalibratePCEInstrumentsScale():
    ClearExistingDataToReadFromScale()
    result = ActionResult(0, "", None)
    shortDataResult = GetShortWeightDataFromPCEScale()
    if(shortDataResult.errorId == 0):
        if(shortDataResult.Obj.status == "US"):
            result.errorId = 1
            result.errorMessage = "TERAZI veya uzerindeki obje hareket ediyor , sabitleyin"
            return result
        if(shortDataResult.Obj.status == "OL"):
            result.errorId = 1
            result.errorMessage = "TERAZI kapasitesinin uzerinde YUKLU !!!"
            return result
        if(shortDataResult.Obj.status == "ST"):
            if(shortDataResult.Obj.mode == "GS"):
                SetPceInstrumentsWeightToZero()
                CalibratePCEInstrumentsScale()
            elif(shortDataResult.Obj.mode == "NT"):
                if(shortDataResult.Obj.weight != 0):
                    SetPceInstrumentsWeightToZero()
                    CalibratePCEInstrumentsScale()
                else:
                    return result
            else:
                result.errorId = 1
                result.errorMessage = "TERAZI'den gelen SHORT DATA'da Status KISMINDA HATALI VERI GELIYOR"
                return result
        else:
            result.errorId = 1
            result.errorMessage = "TERAZI'den gelen SHORT DATA'da Status KISMINDA HATALI VERI GELIYOR"
            return result

    else:
        return shortDataResult


if __name__ == '__main__':
    window = Tk()
    app = application(window)

    window.mainloop()
