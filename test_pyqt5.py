from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import sys
import sqlite3
import uuid


from config_app import name_app
#import warnings
#warnings.filterwarnings("ignore")
#import multitimer
#import random
#import queue
import time
import datetime
#from numpy import convolve
#import numpy as np
#import copy

from functools import partial

class Stock(QMainWindow):
   def __init__(self):
      super().__init__()
      self.width=850
      self.height=600
      self.set=0
      self.cart=0
      self.cart_price=0
      
      self.x=0
      self.y=0
      self.x2=0
      self.y2=0
      
      self.list_x=[]
      self.list_butt=[]
      
      self.list_x2=[]
      self.list_butt2=[]
      
      self.w_size_b=100
      self.h_size_b=100
      self.icon_size=80
      self.app_name=name_app
      self.low=10
      # this will hide the title bar
      #self.setWindowFlag(Qt.FramelessWindowHint)
      self.offset = None
      self.setGeometry(100,100,self.width,self.height)
      self.setWindowTitle('GESTION DE STOCK PRODUITS')
      self.setStyleSheet("""
                        QMainWindow{ background-color:#000;color:#fff;
                             background-image: url("assets/background2.jpg"); 
                             background-repeat: no-repeat; 
                             background-position: center;}
                          QMessageBox{ background-color:#fff}
                         """)
      #self.setFixedSize(self.width,self.height)
      self.setWindowOpacity(1)

      self.button_boisson1={}
      self.lab_boisson1={}
      self.button_boisson2={}
      self.lab_boisson2={}   
      
      self.widgets()
      #self.boissons_page()
      #self.refresh_all()
      #self.refresh_cat()
      #self.showMaximized()


   def widgets(self):

      self.list_boisson=QListWidget(self)
      self.list_boisson.setGeometry(50,50,425,510)
      self.list_boisson.setStyleSheet("""
                            background-color:#00f;color:#000

                            QListWidget::item:selected{border-style:solid;border-width:1px;border-color:#000;
                            background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                            font-weight:bold;border-style:solid;border-size:20px;border-color:#fff;border-radius:0px}
                            
                            QListWidget::item:!selected{border-style:solid;border-width:1px;border-color:#000;
                            background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                            font-weight:bold;border-radius:0px}
                            """)
      

      #_________BOISSON PAGE 1
      self.boisson1=QFrame()
      self.boisson1.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)

      self.boisson1.move(5,5)
      self.boisson1.resize(400,400)
      #_________BOISSON PAGE 2
      self.boisson2=QWidget()
      self.boisson2.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)

      self.boisson2.move(5,400)
      self.boisson2.resize(400,400)

      self.style_button="""
                   QToolButton::pressed{background-color :#1b1b1c;color:#fff;border-style:solid;
                   border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:8pt;
                   font-weight:bold;border-radius:10px}
                   QToolButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                   background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                   font-weight:bold;border-radius:10px}
                   QToolButton::focus{background-color :#1b1b1c;color:#fff;border-style:solid;
                   border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                   font-weight:bold;border-radius:10px}
                   QToolButton::hover{background-color :#1b1b1c;color:#fff;border-style:solid;
                   border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                   font-weight:bold;border-radius:10px}
                   
                 """
      
      for i in range(5):
         for j in range(4):

            #================# BOISSON PAGE 1
            
            self.button_boisson1[(i,j)]=QToolButton(self.boisson1)
            self.button_boisson1[(i,j)].setStyleSheet(self.style_button)
            self.button_boisson1[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            self.button_boisson1[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
            self.button_boisson1[(i,j)].resize(100,100)
            self.button_boisson1[(i,j)].setText('{}-{}'.format(i,j))

            self.lab_boisson1[(i,j)]=QLabel(self.boisson1)
            self.lab_boisson1[(i,j)].setStyleSheet(""" 
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                """)
            self.lab_boisson1[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
            self.lab_boisson1[(i,j)].adjustSize()
            
            self.button_boisson1[(i,j)].move(self.x,self.y)
            self.lab_boisson1[(i,j)].move(self.x,self.y)    
            self.x+=100
            self.list_x.append(0)
            self.list_butt.append(str(i)+'-'+str(j))
            if len(self.list_x)==4:
               self.list_x.clear()
               self.x=0
               self.y+=100
            self.button_boisson1[(i,j)].clicked.connect(self.page1)

            #================# BOISSON PAGE 2
            
            self.button_boisson2[(i,j)]=QToolButton(self.boisson2)
            self.button_boisson2[(i,j)].setStyleSheet(self.style_button)
            self.button_boisson2[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            self.button_boisson2[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
            self.button_boisson2[(i,j)].resize(100,100)
            self.button_boisson2[(i,j)].setText('{}-{}'.format(i,j))

            self.lab_boisson2[(i,j)]=QLabel(self.boisson2)
            self.lab_boisson2[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                """)
            self.lab_boisson2[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
            self.lab_boisson2[(i,j)].adjustSize()
            
            self.button_boisson2[(i,j)].move(self.x2,self.y2)
            self.lab_boisson2[(i,j)].move(self.x2,self.y2)      
            self.x2+=100
            self.list_x2.append(0)
            self.list_butt2.append(str(i)+'-'+str(j))
            if len(self.list_x2)==4:
               self.list_x2.clear()
               self.x2=0
               self.y2+=100
            self.button_boisson2[(i,j)].clicked.connect(self.page2)

            #==============================================================================================#

      self.data = [self.boisson1,self.boisson2]
      
      for i in self.data:
          
         self.item = QListWidgetItem(self.list_boisson)
         self.item.setSizeHint(QSize(0,1000))
         
         self.list_boisson.addItem(self.item)
         self.list_boisson.setItemWidget(self.item,i)

   def page1(self):
      sending_button = self.sender()
      for i in range(5):
         for j in range(4):
            if sending_button==self.button_boisson1[(i,j)]:
               for index,value in enumerate(self.list_butt):
                  if value==str(i)+'-'+str(j):                     
                     print("You pressed button {0} in page1".format(index+1))
                     self.button_boisson1[(i,j)].setFocus()
   def page2(self):
      sending_button = self.sender()
      for i in range(5):
         for j in range(4):
            if sending_button==self.button_boisson2[(i,j)]:
               for index,value in enumerate(self.list_butt):
                  if value==str(i)+'-'+str(j):                     
                     print("You pressed button {0} in page2".format(index+1))
                     self.button_boisson2[(i,j)].setFocus()
      


if __name__=='__main__':
   app=QApplication(sys.argv)
   app.setStyle('plastique')
   screen=Stock()   
   screen.show()
   sys.exit(app.exec_())
