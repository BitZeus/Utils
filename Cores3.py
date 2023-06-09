from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QTimer
import sys

r=255
g=0
b=255

red=[]
for i in range(256):
    redhex=hex(i).split('0x')
    redhex[1] = redhex[1].zfill(2)
    red.append(redhex[1])
    print(red[i])

green=[]
for i in range(256):
    greenhex=hex(i).split('0x')
    greenhex[1]=greenhex[1].zfill(2)
    green.append(greenhex[1])
    print(green[i])
        
blue=[]
for i in range(256):
    bluehex=hex(i).split('0x')
    bluehex[1] = bluehex[1].zfill(2)
    blue.append(bluehex[1])
    print(blue[i])

class WindowCores(QMainWindow):
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.atualizacor)  

        self.setGeometry(200,200,400,400)
        self.setWindowTitle("COL - Colors Of Light")

        self.labelcorHex = QLabel("Cor HEX: ", self)
        self.labelcorHex.move(20,300)
        self.labelcorRGB = QLabel("Cor RGB: ", self)
        self.labelcorRGB.move(20,330)
        self.labelnomecorhex = QLabel("", self)
        self.labelnomecorhex.move(100,300)
        self.labelnomecorrgb = QLabel("", self)
        self.labelnomecorrgb.move(100,330)

        self.fundocor = QLabel("", self)
        self.fundocor.setStyleSheet("background-color: #FFFFFF;")
        self.fundocor.setGeometry(0,0,400,250)

    
        self.atualizacor()  
        
    def atualizacor(self):
        global r,g,b
        
        cor=red[r]+green[g]+blue[b]
        print(cor, r,g,b)
        self.fundocor.setStyleSheet(f"background-color: #{cor};")
        self.labelnomecorhex.setText(f"#{cor}")
        self.labelnomecorrgb.setText(f"{r,g,b}")
        if r>0 and r<256 and g==0 and b==255:
            r-=1
            self.timer.start(100)
        elif r==0 and g>=0 and g<=254 and b==255:
            g+=1
            self.timer.start(100)
        elif r==0 and g==255 and b>=1 and b<256:
            b-=1
        elif r>=0 and r<255 and g==255 and b==0:
            r+=1
            self.timer.start(100)
        elif r==255 and g>=1 and g<256 and b==0:
            g-=1
            self.timer.start(100)
        elif r>=1 and r<256 and g==0 and b==0:
            r-=1
            self.timer.start(100)
        else:
            self.timer.stop()            
            
      
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WindowCores()
    window.show()
    sys.exit(app.exec_())