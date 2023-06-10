from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QTimer
import sys

r=255      #works as pointer for red values and initial state
g=0        #works as pointer for green values and initial state       
b=255      #works as pointer for blue values and initial state

red=[]                                  #list of red values in hexadecimal
for i in range(256):
    redhex=hex(i).split('0x')           #convert to hexadecimal
    redhex[1] = redhex[1].zfill(2)      #convert to 2 digits value
    red.append(redhex[1])               #adds a new list value
    #print(red[i])

green=[]                                #list of green values in hexadecimal
for i in range(256):
    greenhex=hex(i).split('0x')
    greenhex[1]=greenhex[1].zfill(2)
    green.append(greenhex[1])
    #print(green[i])
        
blue=[]                                 #list of blue values in hexadecimal
for i in range(256):
    bluehex=hex(i).split('0x')
    bluehex[1] = bluehex[1].zfill(2)
    blue.append(bluehex[1])
    #print(blue[i])

class colors(QMainWindow):                              #creates the window for the app                 
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)                       #timer to loop function refreshcolor    
        self.timer.timeout.connect(self.refreshcolor)  

        self.setGeometry(200,200,400,400)               #size and position of the window
        self.setWindowTitle("COL - Colors Of Light")

        self.labelcorHex = QLabel("Cor HEX: ", self)    #title 
        self.labelcorHex.move(20,300)
        self.labelcorRGB = QLabel("Cor RGB: ", self)    #title
        self.labelcorRGB.move(20,330)
        self.labelnomecorhex = QLabel("", self)         #label which saves correspondent value in hex of the color
        self.labelnomecorhex.move(100,300)
        self.labelnomecorrgb = QLabel("", self)         #label which saves correspondent value in RGB of the color
        self.labelnomecorrgb.move(100,330)

        self.fundocor = QLabel("", self)
        self.fundocor.setStyleSheet("background-color: #FFFFFF;") #starts the initial color of the window as white
        self.fundocor.setGeometry(0,0,400,250)                    #defines the size of color field to be shown inside window

    
        self.refreshcolor()                     #runs function 
        
    def refreshcolor(self):                    #function to refresh the color in window 
        global r,g,b
        
        cor=red[r]+green[g]+blue[b]            #creates the string for the color with the 3 values (RGB) in hexadecimal
        #print(cor, r,g,b)
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
    window = colors()
    window.show()
    sys.exit(app.exec_())