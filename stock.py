#####################################
# IZI TOC V1.0 by Edan_Zoung
#####################################

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

class Stock(QMainWindow):
   def __init__(self):
      super().__init__()
      self.width=1200
      self.height=600
      self.set=0
      self.cart=0
      self.cart_price=0
      self.x=0
      self.y=0
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

      self.list_boisson_page1=[]
      self.button_boisson1={}
      self.lab_boisson1={}

      self.list_cafe_page1=[]
      self.list_cafe_page2=[]
      self.list_cafe_page3=[]
      self.list_cafe_page4=[]
      self.list_cafe_page5=[]
      self.list_cafe_page6=[]
      self.list_cafe_page7=[]
      self.list_cafe_page8=[]
      self.button_cafe1={}
      self.button_cafe2={}
      self.button_cafe3={}
      self.button_cafe4={}
      self.button_cafe5={}
      self.button_cafe6={}
      self.button_cafe7={}
      self.button_cafe8={}
      self.lab_cafe1={}
      self.lab_cafe2={}
      self.lab_cafe3={}
      self.lab_cafe4={}
      self.lab_cafe5={}
      self.lab_cafe6={}
      self.lab_cafe7={}
      self.lab_cafe8={}

      self.list_dessert_page1=[]
      self.list_dessert_page2=[]
      self.list_dessert_page3=[]
      self.list_dessert_page4=[]
      self.list_dessert_page5=[]
      self.list_dessert_page6=[]
      self.list_dessert_page7=[]
      self.list_dessert_page8=[]
      self.button_dessert1={}
      self.button_dessert2={}
      self.button_dessert3={}
      self.button_dessert4={}
      self.button_dessert5={}
      self.button_dessert6={}
      self.button_dessert7={}
      self.button_dessert8={}
      self.lab_dessert1={}
      self.lab_dessert2={}
      self.lab_dessert3={}
      self.lab_dessert4={}
      self.lab_dessert5={}
      self.lab_dessert6={}
      self.lab_dessert7={}
      self.lab_dessert8={}

      self.list_plat_page1=[]
      self.list_plat_page2=[]
      self.list_plat_page3=[]
      self.list_plat_page4=[]
      self.list_plat_page5=[]
      self.list_plat_page6=[]
      self.list_plat_page7=[]
      self.list_plat_page8=[]
      self.button_plat1={}
      self.button_plat2={}
      self.button_plat3={}
      self.button_plat4={}
      self.button_plat5={}
      self.button_plat6={}
      self.button_plat7={}
      self.button_plat8={}
      self.lab_plat1={}
      self.lab_plat2={}
      self.lab_plat3={}
      self.lab_plat4={}
      self.lab_plat5={}
      self.lab_plat6={}
      self.lab_plat7={}
      self.lab_plat8={}
      
      self.widgets()
      self.boissons_page()
      self.refresh_all()
      self.refresh_cat()
      self.showMaximized()
      
   def widgets(self):
      #______________________________________________INTERFACE  VENTES BEGINNING
      

      #_______TITLE PRODUITS ZONE
      self.zone_title=QLabel('BOISSONS',self)
      self.zone_title.setStyleSheet("""
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:20pt;
                                  font-weight:bold
                                  """)
      self.zone_title.move(150,10)
      self.zone_title.resize(200,30)

      #_________________________________________ Button to boissons

      self.btn_boisson=QPushButton('BOISSONS',self)
      self.btn_boisson.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::hover{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#5707b3;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_boisson.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_boisson.clicked.connect(self.boissons_page)
      self.btn_boisson.move(500,20)
      self.btn_boisson.resize(105,30)
      #_________________________________________ Button to desserts

      self.btn_dessert=QPushButton('DESSERTS',self)
      self.btn_dessert.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::hover{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#5707b3;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_dessert.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_dessert.clicked.connect(self.desserts_page)
      self.btn_dessert.move(615,20)
      self.btn_dessert.resize(105,30)
      #_________________________________________ Button to cafes

      self.btn_cafe=QPushButton('CAFES',self)
      self.btn_cafe.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::hover{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#5707b3;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_cafe.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_cafe.clicked.connect(self.cafes_page)
      self.btn_cafe.move(730,20)
      self.btn_cafe.resize(105,30)
      #_________________________________________ Button to plats

      self.btn_plat=QPushButton('PLATS',self)
      self.btn_plat.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::hover{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#5707b3;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_plat.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_plat.clicked.connect(self.plats_page)
      self.btn_plat.move(845,20)
      self.btn_plat.resize(105,30)


      #================================================================================================#
      #================================================================================================#
      #========================================== BOISSONS ============================================#
      #================================================================================================#

      #_________BOISSON PAGE 1
      self.boisson1=QWidget()
      self.boisson1.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)

      self.boisson1.move(5,5)
      #self.boisson1.resize(400,800)

      
      for i in range(32):
          for j in range(4):
              self.button_boisson1[(i,j)]=QToolButton(self.boisson1)
              self.button_boisson1[(i,j)].setStyleSheet("""
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
                                  
                                """)
              self.button_boisson1[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_boisson1[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_boisson1[(i,j)].resize(100,100)

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
              self.list_boisson_page1.append(0)
              if len(self.list_boisson_page1)==4:
                 self.list_boisson_page1.clear()
                 self.x=0
                 self.y+=100
               
              #==== Event
              self.button_boisson1[(i,j)].clicked.connect(self.bb1)

      


      self.data_boisson=[self.boisson1]

      self.list_boisson=QListWidget(self)
      self.list_boisson.setGeometry(50,50,425,430)
      self.list_boisson.setStyleSheet("""
                                  background-color:#00f;color:#000

                                  QListWidget::item:selected{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-style:solid;border-size:20px;border-color:#fff;border-radius:0px}
                                  
                                  QListWidget::item:!selected{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:0px}
                                  """)

      for i in self.data_boisson:

          self.list_boisson_frame=QFrame(self.list_boisson)
          self.list_boisson_frame.setStyleSheet("""
                                  background-color:#ff0;color:#000
                                  """)
         
          self.layout_boisson = QVBoxLayout(self.list_boisson_frame)
          self.layout_boisson.setContentsMargins(0,0,0,0)
          self.layout_boisson.setSpacing(20)
          self.layout_boisson.addWidget(i)
          self.setLayout(self.layout_boisson)
      
          self.item1 = QListWidgetItem(self.list_boisson)         
          self.item_widget1 = self.list_boisson_frame        

          self.item1.setSizeHint(QSize(0,800))
         
          self.list_boisson.addItem(self.item1)
          self.list_boisson.setItemWidget(self.item1,self.item_widget1)
     

      #================================================================================================#
      #================================================================================================#
      #========================================== BOISSONS ============================================#
      #================================================================================================#

      #================================================================================================#
      #================================================================================================#
      #============================================= CAFES ============================================#
      #================================================================================================#

      #_________cafe PAGE 1
      self.cafe1=QWidget()
      self.cafe1.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.cafe1.move(5,5)
      self.cafe1.resize(400,400)
      for i in range(4):
          for j in range(4):            
              self.button_cafe1[(i,j)]=QToolButton(self.cafe1)
              self.button_cafe1[(i,j)].setStyleSheet("""
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
                                  
                                """)
              self.button_cafe1[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_cafe1[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_cafe1[(i,j)].resize(100,100)

              self.lab_cafe1[(i,j)]=QLabel(self.cafe1)
              self.lab_cafe1[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_cafe1[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_cafe1[(i,j)].adjustSize()

      #_________cafe PAGE 2

      self.cafe2=QWidget()
      self.cafe2.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.cafe2.move(5,5)
      self.cafe2.resize(400,400)
      for i in range(4):
          for j in range(4):            
              self.button_cafe2[(i,j)]=QToolButton(self.cafe2)
              self.button_cafe2[(i,j)].setStyleSheet("""
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
                                """)
              self.button_cafe2[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_cafe2[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_cafe2[(i,j)].resize(100,100)
              self.lab_cafe2[(i,j)]=QLabel(self.cafe2)
              self.lab_cafe2[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_cafe2[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_cafe2[(i,j)].adjustSize()

      #_________cafe PAGE 3
      
      self.cafe3=QWidget()
      self.cafe3.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.cafe3.move(5,5)
      self.cafe3.resize(400,400)
      for i in range(4):
          for j in range(4):            
              self.button_cafe3[(i,j)]=QToolButton(self.cafe3)
              self.button_cafe3[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_cafe3[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_cafe3[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_cafe3[(i,j)].resize(100,100)
              self.lab_cafe3[(i,j)]=QLabel(self.cafe3)
              self.lab_cafe3[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_cafe3[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_cafe3[(i,j)].adjustSize()

      #_________cafe PAGE 4
      
      self.cafe4=QWidget()
      self.cafe4.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.cafe4.move(5,5)
      self.cafe4.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_cafe4[(i,j)]=QToolButton(self.cafe4)
              self.button_cafe4[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_cafe4[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_cafe4[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_cafe4[(i,j)].resize(100,100)
              self.lab_cafe4[(i,j)]=QLabel(self.cafe4)
              self.lab_cafe4[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_cafe4[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_cafe4[(i,j)].adjustSize()

      #_________cafe PAGE 5
      
      self.cafe5=QWidget()
      self.cafe5.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.cafe5.move(5,5)
      self.cafe5.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_cafe5[(i,j)]=QToolButton(self.cafe5)
              self.button_cafe5[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_cafe5[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_cafe5[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_cafe5[(i,j)].resize(100,100)
              self.lab_cafe5[(i,j)]=QLabel(self.cafe5)
              self.lab_cafe5[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_cafe5[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_cafe5[(i,j)].adjustSize()

      #_________cafe PAGE 6
      
      self.cafe6=QWidget()
      self.cafe6.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.cafe6.move(5,5)
      self.cafe6.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_cafe6[(i,j)]=QToolButton(self.cafe6)
              self.button_cafe6[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_cafe6[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_cafe6[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_cafe6[(i,j)].resize(100,100)
              self.lab_cafe6[(i,j)]=QLabel(self.cafe6)
              self.lab_cafe6[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_cafe6[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_cafe6[(i,j)].adjustSize()

      #_________cafe PAGE 7
      
      self.cafe7=QWidget()
      self.cafe7.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.cafe7.move(5,5)
      self.cafe7.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_cafe7[(i,j)]=QToolButton(self.cafe7)
              self.button_cafe7[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_cafe7[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_cafe7[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_cafe7[(i,j)].resize(100,100)
              self.lab_cafe7[(i,j)]=QLabel(self.cafe7)
              self.lab_cafe7[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_cafe7[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_cafe7[(i,j)].adjustSize()

      #_________cafe PAGE 8
      
      self.cafe8=QWidget()
      self.cafe8.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.cafe8.move(5,5)
      self.cafe8.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_cafe8[(i,j)]=QToolButton(self.cafe8)
              self.button_cafe8[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_cafe8[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_cafe8[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_cafe8[(i,j)].resize(100,100)
              self.lab_cafe8[(i,j)]=QLabel(self.cafe8)
              self.lab_cafe8[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_cafe8[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_cafe8[(i,j)].adjustSize()


      self.data_cafe=[self.cafe1,self.cafe2,self.cafe3,self.cafe4,self.cafe5,self.cafe6,self.cafe7,self.cafe8]

      self.list_cafe=QListWidget(self)
      self.list_cafe.setGeometry(50,50,425,430)
      self.list_cafe.setStyleSheet("""
                                  background-color:#00f;color:#000

                                  QListWidget::item:selected{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-style:solid;border-size:20px;border-color:#fff;border-radius:0px}
                                  
                                  QListWidget::item:!selected{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:0px}
                                  """)

      for i in self.data_cafe:

          self.list_cafe_frame=QFrame(self.list_cafe)
          self.list_cafe_frame.setStyleSheet("""
                                  background-color:#ff0;color:#000
                                  """)
         
          self.layout_cafe = QVBoxLayout(self.list_cafe_frame)
          self.layout_cafe.setContentsMargins(0,0,0,0)
          self.layout_cafe.setSpacing(20)
          self.layout_cafe.addWidget(i)
          self.setLayout(self.layout_cafe)
      
          self.item2 = QListWidgetItem(self.list_cafe)         
          self.item_widget2 = self.list_cafe_frame        

          self.item2.setSizeHint(QSize(0,400))
         
          self.list_cafe.addItem(self.item2)
          self.list_cafe.setItemWidget(self.item2,self.item_widget2)
          

      self.lab_cafe1[(0,0)].move(self.x,self.y)
      self.lab_cafe1[(0,1)].move(self.x+100,self.y)
      self.lab_cafe1[(0,2)].move(self.x+200,self.y)
      self.lab_cafe1[(0,3)].move(self.x+300,self.y)
      self.lab_cafe1[(1,0)].move(self.x,self.y+100)
      self.lab_cafe1[(1,1)].move(self.x+100,self.y+100)
      self.lab_cafe1[(1,2)].move(self.x+200,self.y+100)
      self.lab_cafe1[(1,3)].move(self.x+300,self.y+100)
      self.lab_cafe1[(2,0)].move(self.x,self.y+200)
      self.lab_cafe1[(2,1)].move(self.x+100,self.y+200)
      self.lab_cafe1[(2,2)].move(self.x+200,self.y+200)
      self.lab_cafe1[(2,3)].move(self.x+300,self.y+200)
      self.lab_cafe1[(3,0)].move(self.x,self.y+300)
      self.lab_cafe1[(3,1)].move(self.x+100,self.y+300)
      self.lab_cafe1[(3,2)].move(self.x+200,self.y+300)
      self.lab_cafe1[(3,3)].move(self.x+300,self.y+300)
      
      self.button_cafe1[(0,0)].move(self.x,self.y)
      self.button_cafe1[(0,1)].move(self.x+100,self.y)
      self.button_cafe1[(0,2)].move(self.x+200,self.y)
      self.button_cafe1[(0,3)].move(self.x+300,self.y)
      self.button_cafe1[(1,0)].move(self.x,self.y+100)
      self.button_cafe1[(1,1)].move(self.x+100,self.y+100)
      self.button_cafe1[(1,2)].move(self.x+200,self.y+100)
      self.button_cafe1[(1,3)].move(self.x+300,self.y+100)
      self.button_cafe1[(2,0)].move(self.x,self.y+200)
      self.button_cafe1[(2,1)].move(self.x+100,self.y+200)
      self.button_cafe1[(2,2)].move(self.x+200,self.y+200)
      self.button_cafe1[(2,3)].move(self.x+300,self.y+200)
      self.button_cafe1[(3,0)].move(self.x,self.y+300)
      self.button_cafe1[(3,1)].move(self.x+100,self.y+300)
      self.button_cafe1[(3,2)].move(self.x+200,self.y+300)
      self.button_cafe1[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 2
      
      self.lab_cafe2[(0,0)].move(self.x,self.y)
      self.lab_cafe2[(0,1)].move(self.x+100,self.y)
      self.lab_cafe2[(0,2)].move(self.x+200,self.y)
      self.lab_cafe2[(0,3)].move(self.x+300,self.y)
      self.lab_cafe2[(1,0)].move(self.x,self.y+100)
      self.lab_cafe2[(1,1)].move(self.x+100,self.y+100)
      self.lab_cafe2[(1,2)].move(self.x+200,self.y+100)
      self.lab_cafe2[(1,3)].move(self.x+300,self.y+100)
      self.lab_cafe2[(2,0)].move(self.x,self.y+200)
      self.lab_cafe2[(2,1)].move(self.x+100,self.y+200)
      self.lab_cafe2[(2,2)].move(self.x+200,self.y+200)
      self.lab_cafe2[(2,3)].move(self.x+300,self.y+200)
      self.lab_cafe2[(3,0)].move(self.x,self.y+300)
      self.lab_cafe2[(3,1)].move(self.x+100,self.y+300)
      self.lab_cafe2[(3,2)].move(self.x+200,self.y+300)
      self.lab_cafe2[(3,3)].move(self.x+300,self.y+300)
      
      self.button_cafe2[(0,0)].move(self.x,self.y)
      self.button_cafe2[(0,1)].move(self.x+100,self.y)
      self.button_cafe2[(0,2)].move(self.x+200,self.y)
      self.button_cafe2[(0,3)].move(self.x+300,self.y)
      self.button_cafe2[(1,0)].move(self.x,self.y+100)
      self.button_cafe2[(1,1)].move(self.x+100,self.y+100)
      self.button_cafe2[(1,2)].move(self.x+200,self.y+100)
      self.button_cafe2[(1,3)].move(self.x+300,self.y+100)
      self.button_cafe2[(2,0)].move(self.x,self.y+200)
      self.button_cafe2[(2,1)].move(self.x+100,self.y+200)
      self.button_cafe2[(2,2)].move(self.x+200,self.y+200)
      self.button_cafe2[(2,3)].move(self.x+300,self.y+200)
      self.button_cafe2[(3,0)].move(self.x,self.y+300)
      self.button_cafe2[(3,1)].move(self.x+100,self.y+300)
      self.button_cafe2[(3,2)].move(self.x+200,self.y+300)
      self.button_cafe2[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 3

      self.lab_cafe3[(0,0)].move(self.x,self.y)
      self.lab_cafe3[(0,1)].move(self.x+100,self.y)
      self.lab_cafe3[(0,2)].move(self.x+200,self.y)
      self.lab_cafe3[(0,3)].move(self.x+300,self.y)
      self.lab_cafe3[(1,0)].move(self.x,self.y+100)
      self.lab_cafe3[(1,1)].move(self.x+100,self.y+100)
      self.lab_cafe3[(1,2)].move(self.x+200,self.y+100)
      self.lab_cafe3[(1,3)].move(self.x+300,self.y+100)
      self.lab_cafe3[(2,0)].move(self.x,self.y+200)
      self.lab_cafe3[(2,1)].move(self.x+100,self.y+200)
      self.lab_cafe3[(2,2)].move(self.x+200,self.y+200)
      self.lab_cafe3[(2,3)].move(self.x+300,self.y+200)
      self.lab_cafe3[(3,0)].move(self.x,self.y+300)
      self.lab_cafe3[(3,1)].move(self.x+100,self.y+300)
      self.lab_cafe3[(3,2)].move(self.x+200,self.y+300)
      self.lab_cafe3[(3,3)].move(self.x+300,self.y+300)

      self.button_cafe3[(0,0)].move(self.x,self.y)
      self.button_cafe3[(0,1)].move(self.x+100,self.y)
      self.button_cafe3[(0,2)].move(self.x+200,self.y)
      self.button_cafe3[(0,3)].move(self.x+300,self.y)
      self.button_cafe3[(1,0)].move(self.x,self.y+100)
      self.button_cafe3[(1,1)].move(self.x+100,self.y+100)
      self.button_cafe3[(1,2)].move(self.x+200,self.y+100)
      self.button_cafe3[(1,3)].move(self.x+300,self.y+100)
      self.button_cafe3[(2,0)].move(self.x,self.y+200)
      self.button_cafe3[(2,1)].move(self.x+100,self.y+200)
      self.button_cafe3[(2,2)].move(self.x+200,self.y+200)
      self.button_cafe3[(2,3)].move(self.x+300,self.y+200)
      self.button_cafe3[(3,0)].move(self.x,self.y+300)
      self.button_cafe3[(3,1)].move(self.x+100,self.y+300)
      self.button_cafe3[(3,2)].move(self.x+200,self.y+300)
      self.button_cafe3[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 4

      self.lab_cafe4[(0,0)].move(self.x,self.y)
      self.lab_cafe4[(0,1)].move(self.x+100,self.y)
      self.lab_cafe4[(0,2)].move(self.x+200,self.y)
      self.lab_cafe4[(0,3)].move(self.x+300,self.y)
      self.lab_cafe4[(1,0)].move(self.x,self.y+100)
      self.lab_cafe4[(1,1)].move(self.x+100,self.y+100)
      self.lab_cafe4[(1,2)].move(self.x+200,self.y+100)
      self.lab_cafe4[(1,3)].move(self.x+300,self.y+100)
      self.lab_cafe4[(2,0)].move(self.x,self.y+200)
      self.lab_cafe4[(2,1)].move(self.x+100,self.y+200)
      self.lab_cafe4[(2,2)].move(self.x+200,self.y+200)
      self.lab_cafe4[(2,3)].move(self.x+300,self.y+200)
      self.lab_cafe4[(3,0)].move(self.x,self.y+300)
      self.lab_cafe4[(3,1)].move(self.x+100,self.y+300)
      self.lab_cafe4[(3,2)].move(self.x+200,self.y+300)
      self.lab_cafe4[(3,3)].move(self.x+300,self.y+300)

      self.button_cafe4[(0,0)].move(self.x,self.y)
      self.button_cafe4[(0,1)].move(self.x+100,self.y)
      self.button_cafe4[(0,2)].move(self.x+200,self.y)
      self.button_cafe4[(0,3)].move(self.x+300,self.y)
      self.button_cafe4[(1,0)].move(self.x,self.y+100)
      self.button_cafe4[(1,1)].move(self.x+100,self.y+100)
      self.button_cafe4[(1,2)].move(self.x+200,self.y+100)
      self.button_cafe4[(1,3)].move(self.x+300,self.y+100)
      self.button_cafe4[(2,0)].move(self.x,self.y+200)
      self.button_cafe4[(2,1)].move(self.x+100,self.y+200)
      self.button_cafe4[(2,2)].move(self.x+200,self.y+200)
      self.button_cafe4[(2,3)].move(self.x+300,self.y+200)
      self.button_cafe4[(3,0)].move(self.x,self.y+300)
      self.button_cafe4[(3,1)].move(self.x+100,self.y+300)
      self.button_cafe4[(3,2)].move(self.x+200,self.y+300)
      self.button_cafe4[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 5

      self.lab_cafe5[(0,0)].move(self.x,self.y)
      self.lab_cafe5[(0,1)].move(self.x+100,self.y)
      self.lab_cafe5[(0,2)].move(self.x+200,self.y)
      self.lab_cafe5[(0,3)].move(self.x+300,self.y)
      self.lab_cafe5[(1,0)].move(self.x,self.y+100)
      self.lab_cafe5[(1,1)].move(self.x+100,self.y+100)
      self.lab_cafe5[(1,2)].move(self.x+200,self.y+100)
      self.lab_cafe5[(1,3)].move(self.x+300,self.y+100)
      self.lab_cafe5[(2,0)].move(self.x,self.y+200)
      self.lab_cafe5[(2,1)].move(self.x+100,self.y+200)
      self.lab_cafe5[(2,2)].move(self.x+200,self.y+200)
      self.lab_cafe5[(2,3)].move(self.x+300,self.y+200)
      self.lab_cafe5[(3,0)].move(self.x,self.y+300)
      self.lab_cafe5[(3,1)].move(self.x+100,self.y+300)
      self.lab_cafe5[(3,2)].move(self.x+200,self.y+300)
      self.lab_cafe5[(3,3)].move(self.x+300,self.y+300)

      self.button_cafe5[(0,0)].move(self.x,self.y)
      self.button_cafe5[(0,1)].move(self.x+100,self.y)
      self.button_cafe5[(0,2)].move(self.x+200,self.y)
      self.button_cafe5[(0,3)].move(self.x+300,self.y)
      self.button_cafe5[(1,0)].move(self.x,self.y+100)
      self.button_cafe5[(1,1)].move(self.x+100,self.y+100)
      self.button_cafe5[(1,2)].move(self.x+200,self.y+100)
      self.button_cafe5[(1,3)].move(self.x+300,self.y+100)
      self.button_cafe5[(2,0)].move(self.x,self.y+200)
      self.button_cafe5[(2,1)].move(self.x+100,self.y+200)
      self.button_cafe5[(2,2)].move(self.x+200,self.y+200)
      self.button_cafe5[(2,3)].move(self.x+300,self.y+200)
      self.button_cafe5[(3,0)].move(self.x,self.y+300)
      self.button_cafe5[(3,1)].move(self.x+100,self.y+300)
      self.button_cafe5[(3,2)].move(self.x+200,self.y+300)
      self.button_cafe5[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 6

      self.lab_cafe6[(0,0)].move(self.x,self.y)
      self.lab_cafe6[(0,1)].move(self.x+100,self.y)
      self.lab_cafe6[(0,2)].move(self.x+200,self.y)
      self.lab_cafe6[(0,3)].move(self.x+300,self.y)
      self.lab_cafe6[(1,0)].move(self.x,self.y+100)
      self.lab_cafe6[(1,1)].move(self.x+100,self.y+100)
      self.lab_cafe6[(1,2)].move(self.x+200,self.y+100)
      self.lab_cafe6[(1,3)].move(self.x+300,self.y+100)
      self.lab_cafe6[(2,0)].move(self.x,self.y+200)
      self.lab_cafe6[(2,1)].move(self.x+100,self.y+200)
      self.lab_cafe6[(2,2)].move(self.x+200,self.y+200)
      self.lab_cafe6[(2,3)].move(self.x+300,self.y+200)
      self.lab_cafe6[(3,0)].move(self.x,self.y+300)
      self.lab_cafe6[(3,1)].move(self.x+100,self.y+300)
      self.lab_cafe6[(3,2)].move(self.x+200,self.y+300)
      self.lab_cafe6[(3,3)].move(self.x+300,self.y+300)

      self.button_cafe6[(0,0)].move(self.x,self.y)
      self.button_cafe6[(0,1)].move(self.x+100,self.y)
      self.button_cafe6[(0,2)].move(self.x+200,self.y)
      self.button_cafe6[(0,3)].move(self.x+300,self.y)
      self.button_cafe6[(1,0)].move(self.x,self.y+100)
      self.button_cafe6[(1,1)].move(self.x+100,self.y+100)
      self.button_cafe6[(1,2)].move(self.x+200,self.y+100)
      self.button_cafe6[(1,3)].move(self.x+300,self.y+100)
      self.button_cafe6[(2,0)].move(self.x,self.y+200)
      self.button_cafe6[(2,1)].move(self.x+100,self.y+200)
      self.button_cafe6[(2,2)].move(self.x+200,self.y+200)
      self.button_cafe6[(2,3)].move(self.x+300,self.y+200)
      self.button_cafe6[(3,0)].move(self.x,self.y+300)
      self.button_cafe6[(3,1)].move(self.x+100,self.y+300)
      self.button_cafe6[(3,2)].move(self.x+200,self.y+300)
      self.button_cafe6[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 7

      self.lab_cafe7[(0,0)].move(self.x,self.y)
      self.lab_cafe7[(0,1)].move(self.x+100,self.y)
      self.lab_cafe7[(0,2)].move(self.x+200,self.y)
      self.lab_cafe7[(0,3)].move(self.x+300,self.y)
      self.lab_cafe7[(1,0)].move(self.x,self.y+100)
      self.lab_cafe7[(1,1)].move(self.x+100,self.y+100)
      self.lab_cafe7[(1,2)].move(self.x+200,self.y+100)
      self.lab_cafe7[(1,3)].move(self.x+300,self.y+100)
      self.lab_cafe7[(2,0)].move(self.x,self.y+200)
      self.lab_cafe7[(2,1)].move(self.x+100,self.y+200)
      self.lab_cafe7[(2,2)].move(self.x+200,self.y+200)
      self.lab_cafe7[(2,3)].move(self.x+300,self.y+200)
      self.lab_cafe7[(3,0)].move(self.x,self.y+300)
      self.lab_cafe7[(3,1)].move(self.x+100,self.y+300)
      self.lab_cafe7[(3,2)].move(self.x+200,self.y+300)
      self.lab_cafe7[(3,3)].move(self.x+300,self.y+300)

      self.button_cafe7[(0,0)].move(self.x,self.y)
      self.button_cafe7[(0,1)].move(self.x+100,self.y)
      self.button_cafe7[(0,2)].move(self.x+200,self.y)
      self.button_cafe7[(0,3)].move(self.x+300,self.y)
      self.button_cafe7[(1,0)].move(self.x,self.y+100)
      self.button_cafe7[(1,1)].move(self.x+100,self.y+100)
      self.button_cafe7[(1,2)].move(self.x+200,self.y+100)
      self.button_cafe7[(1,3)].move(self.x+300,self.y+100)
      self.button_cafe7[(2,0)].move(self.x,self.y+200)
      self.button_cafe7[(2,1)].move(self.x+100,self.y+200)
      self.button_cafe7[(2,2)].move(self.x+200,self.y+200)
      self.button_cafe7[(2,3)].move(self.x+300,self.y+200)
      self.button_cafe7[(3,0)].move(self.x,self.y+300)
      self.button_cafe7[(3,1)].move(self.x+100,self.y+300)
      self.button_cafe7[(3,2)].move(self.x+200,self.y+300)
      self.button_cafe7[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 8

      self.lab_cafe8[(0,0)].move(self.x,self.y)
      self.lab_cafe8[(0,1)].move(self.x+100,self.y)
      self.lab_cafe8[(0,2)].move(self.x+200,self.y)
      self.lab_cafe8[(0,3)].move(self.x+300,self.y)
      self.lab_cafe8[(1,0)].move(self.x,self.y+100)
      self.lab_cafe8[(1,1)].move(self.x+100,self.y+100)
      self.lab_cafe8[(1,2)].move(self.x+200,self.y+100)
      self.lab_cafe8[(1,3)].move(self.x+300,self.y+100)
      self.lab_cafe8[(2,0)].move(self.x,self.y+200)
      self.lab_cafe8[(2,1)].move(self.x+100,self.y+200)
      self.lab_cafe8[(2,2)].move(self.x+200,self.y+200)
      self.lab_cafe8[(2,3)].move(self.x+300,self.y+200)
      self.lab_cafe8[(3,0)].move(self.x,self.y+300)
      self.lab_cafe8[(3,1)].move(self.x+100,self.y+300)
      self.lab_cafe8[(3,2)].move(self.x+200,self.y+300)
      self.lab_cafe8[(3,3)].move(self.x+300,self.y+300)
      self.button_cafe8[(0,0)].move(self.x,self.y)
      self.button_cafe8[(0,1)].move(self.x+100,self.y)
      self.button_cafe8[(0,2)].move(self.x+200,self.y)
      self.button_cafe8[(0,3)].move(self.x+300,self.y)
      self.button_cafe8[(1,0)].move(self.x,self.y+100)
      self.button_cafe8[(1,1)].move(self.x+100,self.y+100)
      self.button_cafe8[(1,2)].move(self.x+200,self.y+100)
      self.button_cafe8[(1,3)].move(self.x+300,self.y+100)
      self.button_cafe8[(2,0)].move(self.x,self.y+200)
      self.button_cafe8[(2,1)].move(self.x+100,self.y+200)
      self.button_cafe8[(2,2)].move(self.x+200,self.y+200)
      self.button_cafe8[(2,3)].move(self.x+300,self.y+200)
      self.button_cafe8[(3,0)].move(self.x,self.y+300)
      self.button_cafe8[(3,1)].move(self.x+100,self.y+300)
      self.button_cafe8[(3,2)].move(self.x+200,self.y+300)
      self.button_cafe8[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++ buttons events +++++++++++++++++++++++++++++++++ DE 1 A 4

      self.button_cafe1[(0,0)].clicked.connect(self.cc1)
      self.button_cafe1[(0,1)].clicked.connect(self.cc2)
      self.button_cafe1[(0,2)].clicked.connect(self.cc3)
      self.button_cafe1[(0,3)].clicked.connect(self.cc4)
      self.button_cafe1[(1,0)].clicked.connect(self.cc5)
      self.button_cafe1[(1,1)].clicked.connect(self.cc6)
      self.button_cafe1[(1,2)].clicked.connect(self.cc7)
      self.button_cafe1[(1,3)].clicked.connect(self.cc8)
      self.button_cafe1[(2,0)].clicked.connect(self.cc9)
      self.button_cafe1[(2,1)].clicked.connect(self.cc10)
      self.button_cafe1[(2,2)].clicked.connect(self.cc11)
      self.button_cafe1[(2,3)].clicked.connect(self.cc12)
      self.button_cafe1[(3,0)].clicked.connect(self.cc13)
      self.button_cafe1[(3,1)].clicked.connect(self.cc14)
      self.button_cafe1[(3,2)].clicked.connect(self.cc15)
      self.button_cafe1[(3,3)].clicked.connect(self.cc16)

      self.button_cafe2[(0,0)].clicked.connect(self._cc1)
      self.button_cafe2[(0,1)].clicked.connect(self._cc2)
      self.button_cafe2[(0,2)].clicked.connect(self._cc3)
      self.button_cafe2[(0,3)].clicked.connect(self._cc4)
      self.button_cafe2[(1,0)].clicked.connect(self._cc5)
      self.button_cafe2[(1,1)].clicked.connect(self._cc6)
      self.button_cafe2[(1,2)].clicked.connect(self._cc7)
      self.button_cafe2[(1,3)].clicked.connect(self._cc8)
      self.button_cafe2[(2,0)].clicked.connect(self._cc9)
      self.button_cafe2[(2,1)].clicked.connect(self._cc10)
      self.button_cafe2[(2,2)].clicked.connect(self._cc11)
      self.button_cafe2[(2,3)].clicked.connect(self._cc12)
      self.button_cafe2[(3,0)].clicked.connect(self._cc13)
      self.button_cafe2[(3,1)].clicked.connect(self._cc14)
      self.button_cafe2[(3,2)].clicked.connect(self._cc15)
      self.button_cafe2[(3,3)].clicked.connect(self._cc16)

      self.button_cafe3[(0,0)].clicked.connect(self.__cc1)
      self.button_cafe3[(0,1)].clicked.connect(self.__cc2)
      self.button_cafe3[(0,2)].clicked.connect(self.__cc3)
      self.button_cafe3[(0,3)].clicked.connect(self.__cc4)
      self.button_cafe3[(1,0)].clicked.connect(self.__cc5)
      self.button_cafe3[(1,1)].clicked.connect(self.__cc6)
      self.button_cafe3[(1,2)].clicked.connect(self.__cc7)
      self.button_cafe3[(1,3)].clicked.connect(self.__cc8)
      self.button_cafe3[(2,0)].clicked.connect(self.__cc9)
      self.button_cafe3[(2,1)].clicked.connect(self.__cc10)
      self.button_cafe3[(2,2)].clicked.connect(self.__cc11)
      self.button_cafe3[(2,3)].clicked.connect(self.__cc12)
      self.button_cafe3[(3,0)].clicked.connect(self.__cc13)
      self.button_cafe3[(3,1)].clicked.connect(self.__cc14)
      self.button_cafe3[(3,2)].clicked.connect(self.__cc15)
      self.button_cafe3[(3,3)].clicked.connect(self.__cc16)

      self.button_cafe4[(0,0)].clicked.connect(self.___cc1)
      self.button_cafe4[(0,1)].clicked.connect(self.___cc2)
      self.button_cafe4[(0,2)].clicked.connect(self.___cc3)
      self.button_cafe4[(0,3)].clicked.connect(self.___cc4)
      self.button_cafe4[(1,0)].clicked.connect(self.___cc5)
      self.button_cafe4[(1,1)].clicked.connect(self.___cc6)
      self.button_cafe4[(1,2)].clicked.connect(self.___cc7)
      self.button_cafe4[(1,3)].clicked.connect(self.___cc8)
      self.button_cafe4[(2,0)].clicked.connect(self.___cc9)
      self.button_cafe4[(2,1)].clicked.connect(self.___cc10)
      self.button_cafe4[(2,2)].clicked.connect(self.___cc11)
      self.button_cafe4[(2,3)].clicked.connect(self.___cc12)
      self.button_cafe4[(3,0)].clicked.connect(self.___cc13)
      self.button_cafe4[(3,1)].clicked.connect(self.___cc14)
      self.button_cafe4[(3,2)].clicked.connect(self.___cc15)
      self.button_cafe4[(3,3)].clicked.connect(self.___cc16)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ DE 5 A 8

      self.button_cafe5[(0,0)].clicked.connect(self.c1)
      self.button_cafe5[(0,1)].clicked.connect(self.c2)
      self.button_cafe5[(0,2)].clicked.connect(self.c3)
      self.button_cafe5[(0,3)].clicked.connect(self.c4)
      self.button_cafe5[(1,0)].clicked.connect(self.c5)
      self.button_cafe5[(1,1)].clicked.connect(self.c6)
      self.button_cafe5[(1,2)].clicked.connect(self.c7)
      self.button_cafe5[(1,3)].clicked.connect(self.c8)
      self.button_cafe5[(2,0)].clicked.connect(self.c9)
      self.button_cafe5[(2,1)].clicked.connect(self.c10)
      self.button_cafe5[(2,2)].clicked.connect(self.c11)
      self.button_cafe5[(2,3)].clicked.connect(self.c12)
      self.button_cafe5[(3,0)].clicked.connect(self.c13)
      self.button_cafe5[(3,1)].clicked.connect(self.c14)
      self.button_cafe5[(3,2)].clicked.connect(self.c15)
      self.button_cafe5[(3,3)].clicked.connect(self.c16)

      self.button_cafe6[(0,0)].clicked.connect(self._c1)
      self.button_cafe6[(0,1)].clicked.connect(self._c2)
      self.button_cafe6[(0,2)].clicked.connect(self._c3)
      self.button_cafe6[(0,3)].clicked.connect(self._c4)
      self.button_cafe6[(1,0)].clicked.connect(self._c5)
      self.button_cafe6[(1,1)].clicked.connect(self._c6)
      self.button_cafe6[(1,2)].clicked.connect(self._c7)
      self.button_cafe6[(1,3)].clicked.connect(self._c8)
      self.button_cafe6[(2,0)].clicked.connect(self._c9)
      self.button_cafe6[(2,1)].clicked.connect(self._c10)
      self.button_cafe6[(2,2)].clicked.connect(self._c11)
      self.button_cafe6[(2,3)].clicked.connect(self._c12)
      self.button_cafe6[(3,0)].clicked.connect(self._c13)
      self.button_cafe6[(3,1)].clicked.connect(self._c14)
      self.button_cafe6[(3,2)].clicked.connect(self._c15)
      self.button_cafe6[(3,3)].clicked.connect(self._c16)

      self.button_cafe7[(0,0)].clicked.connect(self.__c1)
      self.button_cafe7[(0,1)].clicked.connect(self.__c2)
      self.button_cafe7[(0,2)].clicked.connect(self.__c3)
      self.button_cafe7[(0,3)].clicked.connect(self.__c4)
      self.button_cafe7[(1,0)].clicked.connect(self.__c5)
      self.button_cafe7[(1,1)].clicked.connect(self.__c6)
      self.button_cafe7[(1,2)].clicked.connect(self.__c7)
      self.button_cafe7[(1,3)].clicked.connect(self.__c8)
      self.button_cafe7[(2,0)].clicked.connect(self.__c9)
      self.button_cafe7[(2,1)].clicked.connect(self.__c10)
      self.button_cafe7[(2,2)].clicked.connect(self.__c11)
      self.button_cafe7[(2,3)].clicked.connect(self.__c12)
      self.button_cafe7[(3,0)].clicked.connect(self.__c13)
      self.button_cafe7[(3,1)].clicked.connect(self.__c14)
      self.button_cafe7[(3,2)].clicked.connect(self.__c15)
      self.button_cafe7[(3,3)].clicked.connect(self.__c16)

      self.button_cafe8[(0,0)].clicked.connect(self.___c1)
      self.button_cafe8[(0,1)].clicked.connect(self.___c2)
      self.button_cafe8[(0,2)].clicked.connect(self.___c3)
      self.button_cafe8[(0,3)].clicked.connect(self.___c4)
      self.button_cafe8[(1,0)].clicked.connect(self.___c5)
      self.button_cafe8[(1,1)].clicked.connect(self.___c6)
      self.button_cafe8[(1,2)].clicked.connect(self.___c7)
      self.button_cafe8[(1,3)].clicked.connect(self.___c8)
      self.button_cafe8[(2,0)].clicked.connect(self.___c9)
      self.button_cafe8[(2,1)].clicked.connect(self.___c10)
      self.button_cafe8[(2,2)].clicked.connect(self.___c11)
      self.button_cafe8[(2,3)].clicked.connect(self.___c12)
      self.button_cafe8[(3,0)].clicked.connect(self.___c13)
      self.button_cafe8[(3,1)].clicked.connect(self.___c14)
      self.button_cafe8[(3,2)].clicked.connect(self.___c15)
      self.button_cafe8[(3,3)].clicked.connect(self.___c16)


      #================================================================================================#
      #================================================================================================#
      #============================================= CAFES ============================================#
      #================================================================================================#

      #================================================================================================#
      #================================================================================================#
      #========================================== DESSERTS ============================================#
      #================================================================================================#

      #_________dessert PAGE 1
      self.dessert1=QWidget()
      self.dessert1.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.dessert1.move(5,5)
      self.dessert1.resize(400,400)
      for i in range(4):
          for j in range(4):            
              self.button_dessert1[(i,j)]=QToolButton(self.dessert1)
              self.button_dessert1[(i,j)].setStyleSheet("""
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
                                  
                                """)
              self.button_dessert1[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_dessert1[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_dessert1[(i,j)].resize(100,100)

              self.lab_dessert1[(i,j)]=QLabel(self.dessert1)
              self.lab_dessert1[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_dessert1[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_dessert1[(i,j)].adjustSize()

      #_________dessert PAGE 2

      self.dessert2=QWidget()
      self.dessert2.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.dessert2.move(5,5)
      self.dessert2.resize(400,400)
      for i in range(4):
          for j in range(4):            
              self.button_dessert2[(i,j)]=QToolButton(self.dessert2)
              self.button_dessert2[(i,j)].setStyleSheet("""
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
                                """)
              self.button_dessert2[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_dessert2[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_dessert2[(i,j)].resize(100,100)
              self.lab_dessert2[(i,j)]=QLabel(self.dessert2)
              self.lab_dessert2[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_dessert2[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_dessert2[(i,j)].adjustSize()

      #_________dessert PAGE 3
      
      self.dessert3=QWidget()
      self.dessert3.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.dessert3.move(5,5)
      self.dessert3.resize(400,400)
      for i in range(4):
          for j in range(4):            
              self.button_dessert3[(i,j)]=QToolButton(self.dessert3)
              self.button_dessert3[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_dessert3[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_dessert3[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_dessert3[(i,j)].resize(100,100)
              self.lab_dessert3[(i,j)]=QLabel(self.dessert3)
              self.lab_dessert3[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_dessert3[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_dessert3[(i,j)].adjustSize()

      #_________dessert PAGE 4
      
      self.dessert4=QWidget()
      self.dessert4.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.dessert4.move(5,5)
      self.dessert4.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_dessert4[(i,j)]=QToolButton(self.dessert4)
              self.button_dessert4[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_dessert4[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_dessert4[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_dessert4[(i,j)].resize(100,100)
              self.lab_dessert4[(i,j)]=QLabel(self.dessert4)
              self.lab_dessert4[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_dessert4[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_dessert4[(i,j)].adjustSize()

      #_________dessert PAGE 5
      
      self.dessert5=QWidget()
      self.dessert5.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.dessert5.move(5,5)
      self.dessert5.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_dessert5[(i,j)]=QToolButton(self.dessert5)
              self.button_dessert5[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_dessert5[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_dessert5[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_dessert5[(i,j)].resize(100,100)
              self.lab_dessert5[(i,j)]=QLabel(self.dessert5)
              self.lab_dessert5[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_dessert5[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_dessert5[(i,j)].adjustSize()

      #_________dessert PAGE 6
      
      self.dessert6=QWidget()
      self.dessert6.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.dessert6.move(5,5)
      self.dessert6.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_dessert6[(i,j)]=QToolButton(self.dessert6)
              self.button_dessert6[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_dessert6[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_dessert6[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_dessert6[(i,j)].resize(100,100)
              self.lab_dessert6[(i,j)]=QLabel(self.dessert6)
              self.lab_dessert6[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_dessert6[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_dessert6[(i,j)].adjustSize()

      #_________dessert PAGE 7
      
      self.dessert7=QWidget()
      self.dessert7.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.dessert7.move(5,5)
      self.dessert7.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_dessert7[(i,j)]=QToolButton(self.dessert7)
              self.button_dessert7[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_dessert7[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_dessert7[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_dessert7[(i,j)].resize(100,100)
              self.lab_dessert7[(i,j)]=QLabel(self.dessert7)
              self.lab_dessert7[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_dessert7[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_dessert7[(i,j)].adjustSize()

      #_________dessert PAGE 8
      
      self.dessert8=QWidget()
      self.dessert8.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.dessert8.move(5,5)
      self.dessert8.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_dessert8[(i,j)]=QToolButton(self.dessert8)
              self.button_dessert8[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_dessert8[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_dessert8[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_dessert8[(i,j)].resize(100,100)
              self.lab_dessert8[(i,j)]=QLabel(self.dessert8)
              self.lab_dessert8[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_dessert8[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_dessert8[(i,j)].adjustSize()


      self.data_dessert=[self.dessert1,self.dessert2,self.dessert3,self.dessert4,self.dessert5,self.dessert6,self.dessert7,self.dessert8]

      self.list_dessert=QListWidget(self)
      self.list_dessert.setGeometry(50,50,425,430)
      self.list_dessert.setStyleSheet("""
                                  background-color:#00f;color:#000

                                  QListWidget::item:selected{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-style:solid;border-size:20px;border-color:#fff;border-radius:0px}
                                  
                                  QListWidget::item:!selected{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:0px}
                                  """)

      for i in self.data_dessert:

          self.list_dessert_frame=QFrame(self.list_dessert)
          self.list_dessert_frame.setStyleSheet("""
                                  background-color:#ff0;color:#000
                                  """)
         
          self.layout_dessert = QVBoxLayout(self.list_dessert_frame)
          self.layout_dessert.setContentsMargins(0,0,0,0)
          self.layout_dessert.setSpacing(20)
          self.layout_dessert.addWidget(i)
          self.setLayout(self.layout_dessert)
      
          self.item3 = QListWidgetItem(self.list_dessert)         
          self.item_widget3 = self.list_dessert_frame        

          self.item3.setSizeHint(QSize(0,400))
         
          self.list_dessert.addItem(self.item3)
          self.list_dessert.setItemWidget(self.item3,self.item_widget3)
          

      self.lab_dessert1[(0,0)].move(self.x,self.y)
      self.lab_dessert1[(0,1)].move(self.x+100,self.y)
      self.lab_dessert1[(0,2)].move(self.x+200,self.y)
      self.lab_dessert1[(0,3)].move(self.x+300,self.y)
      self.lab_dessert1[(1,0)].move(self.x,self.y+100)
      self.lab_dessert1[(1,1)].move(self.x+100,self.y+100)
      self.lab_dessert1[(1,2)].move(self.x+200,self.y+100)
      self.lab_dessert1[(1,3)].move(self.x+300,self.y+100)
      self.lab_dessert1[(2,0)].move(self.x,self.y+200)
      self.lab_dessert1[(2,1)].move(self.x+100,self.y+200)
      self.lab_dessert1[(2,2)].move(self.x+200,self.y+200)
      self.lab_dessert1[(2,3)].move(self.x+300,self.y+200)
      self.lab_dessert1[(3,0)].move(self.x,self.y+300)
      self.lab_dessert1[(3,1)].move(self.x+100,self.y+300)
      self.lab_dessert1[(3,2)].move(self.x+200,self.y+300)
      self.lab_dessert1[(3,3)].move(self.x+300,self.y+300)
      
      self.button_dessert1[(0,0)].move(self.x,self.y)
      self.button_dessert1[(0,1)].move(self.x+100,self.y)
      self.button_dessert1[(0,2)].move(self.x+200,self.y)
      self.button_dessert1[(0,3)].move(self.x+300,self.y)
      self.button_dessert1[(1,0)].move(self.x,self.y+100)
      self.button_dessert1[(1,1)].move(self.x+100,self.y+100)
      self.button_dessert1[(1,2)].move(self.x+200,self.y+100)
      self.button_dessert1[(1,3)].move(self.x+300,self.y+100)
      self.button_dessert1[(2,0)].move(self.x,self.y+200)
      self.button_dessert1[(2,1)].move(self.x+100,self.y+200)
      self.button_dessert1[(2,2)].move(self.x+200,self.y+200)
      self.button_dessert1[(2,3)].move(self.x+300,self.y+200)
      self.button_dessert1[(3,0)].move(self.x,self.y+300)
      self.button_dessert1[(3,1)].move(self.x+100,self.y+300)
      self.button_dessert1[(3,2)].move(self.x+200,self.y+300)
      self.button_dessert1[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 2
      
      self.lab_dessert2[(0,0)].move(self.x,self.y)
      self.lab_dessert2[(0,1)].move(self.x+100,self.y)
      self.lab_dessert2[(0,2)].move(self.x+200,self.y)
      self.lab_dessert2[(0,3)].move(self.x+300,self.y)
      self.lab_dessert2[(1,0)].move(self.x,self.y+100)
      self.lab_dessert2[(1,1)].move(self.x+100,self.y+100)
      self.lab_dessert2[(1,2)].move(self.x+200,self.y+100)
      self.lab_dessert2[(1,3)].move(self.x+300,self.y+100)
      self.lab_dessert2[(2,0)].move(self.x,self.y+200)
      self.lab_dessert2[(2,1)].move(self.x+100,self.y+200)
      self.lab_dessert2[(2,2)].move(self.x+200,self.y+200)
      self.lab_dessert2[(2,3)].move(self.x+300,self.y+200)
      self.lab_dessert2[(3,0)].move(self.x,self.y+300)
      self.lab_dessert2[(3,1)].move(self.x+100,self.y+300)
      self.lab_dessert2[(3,2)].move(self.x+200,self.y+300)
      self.lab_dessert2[(3,3)].move(self.x+300,self.y+300)
      
      self.button_dessert2[(0,0)].move(self.x,self.y)
      self.button_dessert2[(0,1)].move(self.x+100,self.y)
      self.button_dessert2[(0,2)].move(self.x+200,self.y)
      self.button_dessert2[(0,3)].move(self.x+300,self.y)
      self.button_dessert2[(1,0)].move(self.x,self.y+100)
      self.button_dessert2[(1,1)].move(self.x+100,self.y+100)
      self.button_dessert2[(1,2)].move(self.x+200,self.y+100)
      self.button_dessert2[(1,3)].move(self.x+300,self.y+100)
      self.button_dessert2[(2,0)].move(self.x,self.y+200)
      self.button_dessert2[(2,1)].move(self.x+100,self.y+200)
      self.button_dessert2[(2,2)].move(self.x+200,self.y+200)
      self.button_dessert2[(2,3)].move(self.x+300,self.y+200)
      self.button_dessert2[(3,0)].move(self.x,self.y+300)
      self.button_dessert2[(3,1)].move(self.x+100,self.y+300)
      self.button_dessert2[(3,2)].move(self.x+200,self.y+300)
      self.button_dessert2[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 3

      self.lab_dessert3[(0,0)].move(self.x,self.y)
      self.lab_dessert3[(0,1)].move(self.x+100,self.y)
      self.lab_dessert3[(0,2)].move(self.x+200,self.y)
      self.lab_dessert3[(0,3)].move(self.x+300,self.y)
      self.lab_dessert3[(1,0)].move(self.x,self.y+100)
      self.lab_dessert3[(1,1)].move(self.x+100,self.y+100)
      self.lab_dessert3[(1,2)].move(self.x+200,self.y+100)
      self.lab_dessert3[(1,3)].move(self.x+300,self.y+100)
      self.lab_dessert3[(2,0)].move(self.x,self.y+200)
      self.lab_dessert3[(2,1)].move(self.x+100,self.y+200)
      self.lab_dessert3[(2,2)].move(self.x+200,self.y+200)
      self.lab_dessert3[(2,3)].move(self.x+300,self.y+200)
      self.lab_dessert3[(3,0)].move(self.x,self.y+300)
      self.lab_dessert3[(3,1)].move(self.x+100,self.y+300)
      self.lab_dessert3[(3,2)].move(self.x+200,self.y+300)
      self.lab_dessert3[(3,3)].move(self.x+300,self.y+300)

      self.button_dessert3[(0,0)].move(self.x,self.y)
      self.button_dessert3[(0,1)].move(self.x+100,self.y)
      self.button_dessert3[(0,2)].move(self.x+200,self.y)
      self.button_dessert3[(0,3)].move(self.x+300,self.y)
      self.button_dessert3[(1,0)].move(self.x,self.y+100)
      self.button_dessert3[(1,1)].move(self.x+100,self.y+100)
      self.button_dessert3[(1,2)].move(self.x+200,self.y+100)
      self.button_dessert3[(1,3)].move(self.x+300,self.y+100)
      self.button_dessert3[(2,0)].move(self.x,self.y+200)
      self.button_dessert3[(2,1)].move(self.x+100,self.y+200)
      self.button_dessert3[(2,2)].move(self.x+200,self.y+200)
      self.button_dessert3[(2,3)].move(self.x+300,self.y+200)
      self.button_dessert3[(3,0)].move(self.x,self.y+300)
      self.button_dessert3[(3,1)].move(self.x+100,self.y+300)
      self.button_dessert3[(3,2)].move(self.x+200,self.y+300)
      self.button_dessert3[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 4

      self.lab_dessert4[(0,0)].move(self.x,self.y)
      self.lab_dessert4[(0,1)].move(self.x+100,self.y)
      self.lab_dessert4[(0,2)].move(self.x+200,self.y)
      self.lab_dessert4[(0,3)].move(self.x+300,self.y)
      self.lab_dessert4[(1,0)].move(self.x,self.y+100)
      self.lab_dessert4[(1,1)].move(self.x+100,self.y+100)
      self.lab_dessert4[(1,2)].move(self.x+200,self.y+100)
      self.lab_dessert4[(1,3)].move(self.x+300,self.y+100)
      self.lab_dessert4[(2,0)].move(self.x,self.y+200)
      self.lab_dessert4[(2,1)].move(self.x+100,self.y+200)
      self.lab_dessert4[(2,2)].move(self.x+200,self.y+200)
      self.lab_dessert4[(2,3)].move(self.x+300,self.y+200)
      self.lab_dessert4[(3,0)].move(self.x,self.y+300)
      self.lab_dessert4[(3,1)].move(self.x+100,self.y+300)
      self.lab_dessert4[(3,2)].move(self.x+200,self.y+300)
      self.lab_dessert4[(3,3)].move(self.x+300,self.y+300)

      self.button_dessert4[(0,0)].move(self.x,self.y)
      self.button_dessert4[(0,1)].move(self.x+100,self.y)
      self.button_dessert4[(0,2)].move(self.x+200,self.y)
      self.button_dessert4[(0,3)].move(self.x+300,self.y)
      self.button_dessert4[(1,0)].move(self.x,self.y+100)
      self.button_dessert4[(1,1)].move(self.x+100,self.y+100)
      self.button_dessert4[(1,2)].move(self.x+200,self.y+100)
      self.button_dessert4[(1,3)].move(self.x+300,self.y+100)
      self.button_dessert4[(2,0)].move(self.x,self.y+200)
      self.button_dessert4[(2,1)].move(self.x+100,self.y+200)
      self.button_dessert4[(2,2)].move(self.x+200,self.y+200)
      self.button_dessert4[(2,3)].move(self.x+300,self.y+200)
      self.button_dessert4[(3,0)].move(self.x,self.y+300)
      self.button_dessert4[(3,1)].move(self.x+100,self.y+300)
      self.button_dessert4[(3,2)].move(self.x+200,self.y+300)
      self.button_dessert4[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 5

      self.lab_dessert5[(0,0)].move(self.x,self.y)
      self.lab_dessert5[(0,1)].move(self.x+100,self.y)
      self.lab_dessert5[(0,2)].move(self.x+200,self.y)
      self.lab_dessert5[(0,3)].move(self.x+300,self.y)
      self.lab_dessert5[(1,0)].move(self.x,self.y+100)
      self.lab_dessert5[(1,1)].move(self.x+100,self.y+100)
      self.lab_dessert5[(1,2)].move(self.x+200,self.y+100)
      self.lab_dessert5[(1,3)].move(self.x+300,self.y+100)
      self.lab_dessert5[(2,0)].move(self.x,self.y+200)
      self.lab_dessert5[(2,1)].move(self.x+100,self.y+200)
      self.lab_dessert5[(2,2)].move(self.x+200,self.y+200)
      self.lab_dessert5[(2,3)].move(self.x+300,self.y+200)
      self.lab_dessert5[(3,0)].move(self.x,self.y+300)
      self.lab_dessert5[(3,1)].move(self.x+100,self.y+300)
      self.lab_dessert5[(3,2)].move(self.x+200,self.y+300)
      self.lab_dessert5[(3,3)].move(self.x+300,self.y+300)

      self.button_dessert5[(0,0)].move(self.x,self.y)
      self.button_dessert5[(0,1)].move(self.x+100,self.y)
      self.button_dessert5[(0,2)].move(self.x+200,self.y)
      self.button_dessert5[(0,3)].move(self.x+300,self.y)
      self.button_dessert5[(1,0)].move(self.x,self.y+100)
      self.button_dessert5[(1,1)].move(self.x+100,self.y+100)
      self.button_dessert5[(1,2)].move(self.x+200,self.y+100)
      self.button_dessert5[(1,3)].move(self.x+300,self.y+100)
      self.button_dessert5[(2,0)].move(self.x,self.y+200)
      self.button_dessert5[(2,1)].move(self.x+100,self.y+200)
      self.button_dessert5[(2,2)].move(self.x+200,self.y+200)
      self.button_dessert5[(2,3)].move(self.x+300,self.y+200)
      self.button_dessert5[(3,0)].move(self.x,self.y+300)
      self.button_dessert5[(3,1)].move(self.x+100,self.y+300)
      self.button_dessert5[(3,2)].move(self.x+200,self.y+300)
      self.button_dessert5[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 6

      self.lab_dessert6[(0,0)].move(self.x,self.y)
      self.lab_dessert6[(0,1)].move(self.x+100,self.y)
      self.lab_dessert6[(0,2)].move(self.x+200,self.y)
      self.lab_dessert6[(0,3)].move(self.x+300,self.y)
      self.lab_dessert6[(1,0)].move(self.x,self.y+100)
      self.lab_dessert6[(1,1)].move(self.x+100,self.y+100)
      self.lab_dessert6[(1,2)].move(self.x+200,self.y+100)
      self.lab_dessert6[(1,3)].move(self.x+300,self.y+100)
      self.lab_dessert6[(2,0)].move(self.x,self.y+200)
      self.lab_dessert6[(2,1)].move(self.x+100,self.y+200)
      self.lab_dessert6[(2,2)].move(self.x+200,self.y+200)
      self.lab_dessert6[(2,3)].move(self.x+300,self.y+200)
      self.lab_dessert6[(3,0)].move(self.x,self.y+300)
      self.lab_dessert6[(3,1)].move(self.x+100,self.y+300)
      self.lab_dessert6[(3,2)].move(self.x+200,self.y+300)
      self.lab_dessert6[(3,3)].move(self.x+300,self.y+300)

      self.button_dessert6[(0,0)].move(self.x,self.y)
      self.button_dessert6[(0,1)].move(self.x+100,self.y)
      self.button_dessert6[(0,2)].move(self.x+200,self.y)
      self.button_dessert6[(0,3)].move(self.x+300,self.y)
      self.button_dessert6[(1,0)].move(self.x,self.y+100)
      self.button_dessert6[(1,1)].move(self.x+100,self.y+100)
      self.button_dessert6[(1,2)].move(self.x+200,self.y+100)
      self.button_dessert6[(1,3)].move(self.x+300,self.y+100)
      self.button_dessert6[(2,0)].move(self.x,self.y+200)
      self.button_dessert6[(2,1)].move(self.x+100,self.y+200)
      self.button_dessert6[(2,2)].move(self.x+200,self.y+200)
      self.button_dessert6[(2,3)].move(self.x+300,self.y+200)
      self.button_dessert6[(3,0)].move(self.x,self.y+300)
      self.button_dessert6[(3,1)].move(self.x+100,self.y+300)
      self.button_dessert6[(3,2)].move(self.x+200,self.y+300)
      self.button_dessert6[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 7

      self.lab_dessert7[(0,0)].move(self.x,self.y)
      self.lab_dessert7[(0,1)].move(self.x+100,self.y)
      self.lab_dessert7[(0,2)].move(self.x+200,self.y)
      self.lab_dessert7[(0,3)].move(self.x+300,self.y)
      self.lab_dessert7[(1,0)].move(self.x,self.y+100)
      self.lab_dessert7[(1,1)].move(self.x+100,self.y+100)
      self.lab_dessert7[(1,2)].move(self.x+200,self.y+100)
      self.lab_dessert7[(1,3)].move(self.x+300,self.y+100)
      self.lab_dessert7[(2,0)].move(self.x,self.y+200)
      self.lab_dessert7[(2,1)].move(self.x+100,self.y+200)
      self.lab_dessert7[(2,2)].move(self.x+200,self.y+200)
      self.lab_dessert7[(2,3)].move(self.x+300,self.y+200)
      self.lab_dessert7[(3,0)].move(self.x,self.y+300)
      self.lab_dessert7[(3,1)].move(self.x+100,self.y+300)
      self.lab_dessert7[(3,2)].move(self.x+200,self.y+300)
      self.lab_dessert7[(3,3)].move(self.x+300,self.y+300)

      self.button_dessert7[(0,0)].move(self.x,self.y)
      self.button_dessert7[(0,1)].move(self.x+100,self.y)
      self.button_dessert7[(0,2)].move(self.x+200,self.y)
      self.button_dessert7[(0,3)].move(self.x+300,self.y)
      self.button_dessert7[(1,0)].move(self.x,self.y+100)
      self.button_dessert7[(1,1)].move(self.x+100,self.y+100)
      self.button_dessert7[(1,2)].move(self.x+200,self.y+100)
      self.button_dessert7[(1,3)].move(self.x+300,self.y+100)
      self.button_dessert7[(2,0)].move(self.x,self.y+200)
      self.button_dessert7[(2,1)].move(self.x+100,self.y+200)
      self.button_dessert7[(2,2)].move(self.x+200,self.y+200)
      self.button_dessert7[(2,3)].move(self.x+300,self.y+200)
      self.button_dessert7[(3,0)].move(self.x,self.y+300)
      self.button_dessert7[(3,1)].move(self.x+100,self.y+300)
      self.button_dessert7[(3,2)].move(self.x+200,self.y+300)
      self.button_dessert7[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 8

      self.lab_dessert8[(0,0)].move(self.x,self.y)
      self.lab_dessert8[(0,1)].move(self.x+100,self.y)
      self.lab_dessert8[(0,2)].move(self.x+200,self.y)
      self.lab_dessert8[(0,3)].move(self.x+300,self.y)
      self.lab_dessert8[(1,0)].move(self.x,self.y+100)
      self.lab_dessert8[(1,1)].move(self.x+100,self.y+100)
      self.lab_dessert8[(1,2)].move(self.x+200,self.y+100)
      self.lab_dessert8[(1,3)].move(self.x+300,self.y+100)
      self.lab_dessert8[(2,0)].move(self.x,self.y+200)
      self.lab_dessert8[(2,1)].move(self.x+100,self.y+200)
      self.lab_dessert8[(2,2)].move(self.x+200,self.y+200)
      self.lab_dessert8[(2,3)].move(self.x+300,self.y+200)
      self.lab_dessert8[(3,0)].move(self.x,self.y+300)
      self.lab_dessert8[(3,1)].move(self.x+100,self.y+300)
      self.lab_dessert8[(3,2)].move(self.x+200,self.y+300)
      self.lab_dessert8[(3,3)].move(self.x+300,self.y+300)
      self.button_dessert8[(0,0)].move(self.x,self.y)
      self.button_dessert8[(0,1)].move(self.x+100,self.y)
      self.button_dessert8[(0,2)].move(self.x+200,self.y)
      self.button_dessert8[(0,3)].move(self.x+300,self.y)
      self.button_dessert8[(1,0)].move(self.x,self.y+100)
      self.button_dessert8[(1,1)].move(self.x+100,self.y+100)
      self.button_dessert8[(1,2)].move(self.x+200,self.y+100)
      self.button_dessert8[(1,3)].move(self.x+300,self.y+100)
      self.button_dessert8[(2,0)].move(self.x,self.y+200)
      self.button_dessert8[(2,1)].move(self.x+100,self.y+200)
      self.button_dessert8[(2,2)].move(self.x+200,self.y+200)
      self.button_dessert8[(2,3)].move(self.x+300,self.y+200)
      self.button_dessert8[(3,0)].move(self.x,self.y+300)
      self.button_dessert8[(3,1)].move(self.x+100,self.y+300)
      self.button_dessert8[(3,2)].move(self.x+200,self.y+300)
      self.button_dessert8[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++ buttons events +++++++++++++++++++++++++++++++++ DE 1 A 4

      self.button_dessert1[(0,0)].clicked.connect(self.dd1)
      self.button_dessert1[(0,1)].clicked.connect(self.dd2)
      self.button_dessert1[(0,2)].clicked.connect(self.dd3)
      self.button_dessert1[(0,3)].clicked.connect(self.dd4)
      self.button_dessert1[(1,0)].clicked.connect(self.dd5)
      self.button_dessert1[(1,1)].clicked.connect(self.dd6)
      self.button_dessert1[(1,2)].clicked.connect(self.dd7)
      self.button_dessert1[(1,3)].clicked.connect(self.dd8)
      self.button_dessert1[(2,0)].clicked.connect(self.dd9)
      self.button_dessert1[(2,1)].clicked.connect(self.dd10)
      self.button_dessert1[(2,2)].clicked.connect(self.dd11)
      self.button_dessert1[(2,3)].clicked.connect(self.dd12)
      self.button_dessert1[(3,0)].clicked.connect(self.dd13)
      self.button_dessert1[(3,1)].clicked.connect(self.dd14)
      self.button_dessert1[(3,2)].clicked.connect(self.dd15)
      self.button_dessert1[(3,3)].clicked.connect(self.dd16)

      self.button_dessert2[(0,0)].clicked.connect(self._dd1)
      self.button_dessert2[(0,1)].clicked.connect(self._dd2)
      self.button_dessert2[(0,2)].clicked.connect(self._dd3)
      self.button_dessert2[(0,3)].clicked.connect(self._dd4)
      self.button_dessert2[(1,0)].clicked.connect(self._dd5)
      self.button_dessert2[(1,1)].clicked.connect(self._dd6)
      self.button_dessert2[(1,2)].clicked.connect(self._dd7)
      self.button_dessert2[(1,3)].clicked.connect(self._dd8)
      self.button_dessert2[(2,0)].clicked.connect(self._dd9)
      self.button_dessert2[(2,1)].clicked.connect(self._dd10)
      self.button_dessert2[(2,2)].clicked.connect(self._dd11)
      self.button_dessert2[(2,3)].clicked.connect(self._dd12)
      self.button_dessert2[(3,0)].clicked.connect(self._dd13)
      self.button_dessert2[(3,1)].clicked.connect(self._dd14)
      self.button_dessert2[(3,2)].clicked.connect(self._dd15)
      self.button_dessert2[(3,3)].clicked.connect(self._dd16)

      self.button_dessert3[(0,0)].clicked.connect(self.__dd1)
      self.button_dessert3[(0,1)].clicked.connect(self.__dd2)
      self.button_dessert3[(0,2)].clicked.connect(self.__dd3)
      self.button_dessert3[(0,3)].clicked.connect(self.__dd4)
      self.button_dessert3[(1,0)].clicked.connect(self.__dd5)
      self.button_dessert3[(1,1)].clicked.connect(self.__dd6)
      self.button_dessert3[(1,2)].clicked.connect(self.__dd7)
      self.button_dessert3[(1,3)].clicked.connect(self.__dd8)
      self.button_dessert3[(2,0)].clicked.connect(self.__dd9)
      self.button_dessert3[(2,1)].clicked.connect(self.__dd10)
      self.button_dessert3[(2,2)].clicked.connect(self.__dd11)
      self.button_dessert3[(2,3)].clicked.connect(self.__dd12)
      self.button_dessert3[(3,0)].clicked.connect(self.__dd13)
      self.button_dessert3[(3,1)].clicked.connect(self.__dd14)
      self.button_dessert3[(3,2)].clicked.connect(self.__dd15)
      self.button_dessert3[(3,3)].clicked.connect(self.__dd16)

      self.button_dessert4[(0,0)].clicked.connect(self.___dd1)
      self.button_dessert4[(0,1)].clicked.connect(self.___dd2)
      self.button_dessert4[(0,2)].clicked.connect(self.___dd3)
      self.button_dessert4[(0,3)].clicked.connect(self.___dd4)
      self.button_dessert4[(1,0)].clicked.connect(self.___dd5)
      self.button_dessert4[(1,1)].clicked.connect(self.___dd6)
      self.button_dessert4[(1,2)].clicked.connect(self.___dd7)
      self.button_dessert4[(1,3)].clicked.connect(self.___dd8)
      self.button_dessert4[(2,0)].clicked.connect(self.___dd9)
      self.button_dessert4[(2,1)].clicked.connect(self.___dd10)
      self.button_dessert4[(2,2)].clicked.connect(self.___dd11)
      self.button_dessert4[(2,3)].clicked.connect(self.___dd12)
      self.button_dessert4[(3,0)].clicked.connect(self.___dd13)
      self.button_dessert4[(3,1)].clicked.connect(self.___dd14)
      self.button_dessert4[(3,2)].clicked.connect(self.___dd15)
      self.button_dessert4[(3,3)].clicked.connect(self.___dd16)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ DE 5 A 8

      self.button_dessert5[(0,0)].clicked.connect(self.d1)
      self.button_dessert5[(0,1)].clicked.connect(self.d2)
      self.button_dessert5[(0,2)].clicked.connect(self.d3)
      self.button_dessert5[(0,3)].clicked.connect(self.d4)
      self.button_dessert5[(1,0)].clicked.connect(self.d5)
      self.button_dessert5[(1,1)].clicked.connect(self.d6)
      self.button_dessert5[(1,2)].clicked.connect(self.d7)
      self.button_dessert5[(1,3)].clicked.connect(self.d8)
      self.button_dessert5[(2,0)].clicked.connect(self.d9)
      self.button_dessert5[(2,1)].clicked.connect(self.d10)
      self.button_dessert5[(2,2)].clicked.connect(self.d11)
      self.button_dessert5[(2,3)].clicked.connect(self.d12)
      self.button_dessert5[(3,0)].clicked.connect(self.d13)
      self.button_dessert5[(3,1)].clicked.connect(self.d14)
      self.button_dessert5[(3,2)].clicked.connect(self.d15)
      self.button_dessert5[(3,3)].clicked.connect(self.d16)

      self.button_dessert6[(0,0)].clicked.connect(self._d1)
      self.button_dessert6[(0,1)].clicked.connect(self._d2)
      self.button_dessert6[(0,2)].clicked.connect(self._d3)
      self.button_dessert6[(0,3)].clicked.connect(self._d4)
      self.button_dessert6[(1,0)].clicked.connect(self._d5)
      self.button_dessert6[(1,1)].clicked.connect(self._d6)
      self.button_dessert6[(1,2)].clicked.connect(self._d7)
      self.button_dessert6[(1,3)].clicked.connect(self._d8)
      self.button_dessert6[(2,0)].clicked.connect(self._d9)
      self.button_dessert6[(2,1)].clicked.connect(self._d10)
      self.button_dessert6[(2,2)].clicked.connect(self._d11)
      self.button_dessert6[(2,3)].clicked.connect(self._d12)
      self.button_dessert6[(3,0)].clicked.connect(self._d13)
      self.button_dessert6[(3,1)].clicked.connect(self._d14)
      self.button_dessert6[(3,2)].clicked.connect(self._d15)
      self.button_dessert6[(3,3)].clicked.connect(self._d16)

      self.button_dessert7[(0,0)].clicked.connect(self.__d1)
      self.button_dessert7[(0,1)].clicked.connect(self.__d2)
      self.button_dessert7[(0,2)].clicked.connect(self.__d3)
      self.button_dessert7[(0,3)].clicked.connect(self.__d4)
      self.button_dessert7[(1,0)].clicked.connect(self.__d5)
      self.button_dessert7[(1,1)].clicked.connect(self.__d6)
      self.button_dessert7[(1,2)].clicked.connect(self.__d7)
      self.button_dessert7[(1,3)].clicked.connect(self.__d8)
      self.button_dessert7[(2,0)].clicked.connect(self.__d9)
      self.button_dessert7[(2,1)].clicked.connect(self.__d10)
      self.button_dessert7[(2,2)].clicked.connect(self.__d11)
      self.button_dessert7[(2,3)].clicked.connect(self.__d12)
      self.button_dessert7[(3,0)].clicked.connect(self.__d13)
      self.button_dessert7[(3,1)].clicked.connect(self.__d14)
      self.button_dessert7[(3,2)].clicked.connect(self.__d15)
      self.button_dessert7[(3,3)].clicked.connect(self.__d16)

      self.button_dessert8[(0,0)].clicked.connect(self.___d1)
      self.button_dessert8[(0,1)].clicked.connect(self.___d2)
      self.button_dessert8[(0,2)].clicked.connect(self.___d3)
      self.button_dessert8[(0,3)].clicked.connect(self.___d4)
      self.button_dessert8[(1,0)].clicked.connect(self.___d5)
      self.button_dessert8[(1,1)].clicked.connect(self.___d6)
      self.button_dessert8[(1,2)].clicked.connect(self.___d7)
      self.button_dessert8[(1,3)].clicked.connect(self.___d8)
      self.button_dessert8[(2,0)].clicked.connect(self.___d9)
      self.button_dessert8[(2,1)].clicked.connect(self.___d10)
      self.button_dessert8[(2,2)].clicked.connect(self.___d11)
      self.button_dessert8[(2,3)].clicked.connect(self.___d12)
      self.button_dessert8[(3,0)].clicked.connect(self.___d13)
      self.button_dessert8[(3,1)].clicked.connect(self.___d14)
      self.button_dessert8[(3,2)].clicked.connect(self.___d15)
      self.button_dessert8[(3,3)].clicked.connect(self.___d16)

      #================================================================================================#
      #================================================================================================#
      #========================================== DESSERTS ============================================#
      #================================================================================================#

      #================================================================================================#
      #================================================================================================#
      #============================================= PLATS ============================================#
      #================================================================================================#

      #_________plat PAGE 1
      self.plat1=QWidget()
      self.plat1.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.plat1.move(5,5)
      self.plat1.resize(400,400)
      for i in range(4):
          for j in range(4):            
              self.button_plat1[(i,j)]=QToolButton(self.plat1)
              self.button_plat1[(i,j)].setStyleSheet("""
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
                                  
                                """)
              self.button_plat1[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_plat1[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_plat1[(i,j)].resize(100,100)

              self.lab_plat1[(i,j)]=QLabel(self.plat1)
              self.lab_plat1[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_plat1[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_plat1[(i,j)].adjustSize()

      #_________plat PAGE 2

      self.plat2=QWidget()
      self.plat2.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.plat2.move(5,5)
      self.plat2.resize(400,400)
      for i in range(4):
          for j in range(4):            
              self.button_plat2[(i,j)]=QToolButton(self.plat2)
              self.button_plat2[(i,j)].setStyleSheet("""
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
                                """)
              self.button_plat2[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_plat2[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_plat2[(i,j)].resize(100,100)
              self.lab_plat2[(i,j)]=QLabel(self.plat2)
              self.lab_plat2[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_plat2[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_plat2[(i,j)].adjustSize()

      #_________plat PAGE 3
      
      self.plat3=QWidget()
      self.plat3.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.plat3.move(5,5)
      self.plat3.resize(400,400)
      for i in range(4):
          for j in range(4):            
              self.button_plat3[(i,j)]=QToolButton(self.plat3)
              self.button_plat3[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_plat3[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_plat3[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_plat3[(i,j)].resize(100,100)
              self.lab_plat3[(i,j)]=QLabel(self.plat3)
              self.lab_plat3[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_plat3[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_plat3[(i,j)].adjustSize()

      #_________plat PAGE 4
      
      self.plat4=QWidget()
      self.plat4.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.plat4.move(5,5)
      self.plat4.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_plat4[(i,j)]=QToolButton(self.plat4)
              self.button_plat4[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_plat4[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_plat4[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_plat4[(i,j)].resize(100,100)
              self.lab_plat4[(i,j)]=QLabel(self.plat4)
              self.lab_plat4[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_plat4[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_plat4[(i,j)].adjustSize()

      #_________plat PAGE 5
      
      self.plat5=QWidget()
      self.plat5.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.plat5.move(5,5)
      self.plat5.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_plat5[(i,j)]=QToolButton(self.plat5)
              self.button_plat5[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_plat5[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_plat5[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_plat5[(i,j)].resize(100,100)
              self.lab_plat5[(i,j)]=QLabel(self.plat5)
              self.lab_plat5[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_plat5[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_plat5[(i,j)].adjustSize()

      #_________plat PAGE 6
      
      self.plat6=QWidget()
      self.plat6.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.plat6.move(5,5)
      self.plat6.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_plat6[(i,j)]=QToolButton(self.plat6)
              self.button_plat6[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_plat6[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_plat6[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_plat6[(i,j)].resize(100,100)
              self.lab_plat6[(i,j)]=QLabel(self.plat6)
              self.lab_plat6[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_plat6[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_plat6[(i,j)].adjustSize()

      #_________plat PAGE 7
      
      self.plat7=QWidget()
      self.plat7.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.plat7.move(5,5)
      self.plat7.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_plat7[(i,j)]=QToolButton(self.plat7)
              self.button_plat7[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_plat7[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_plat7[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_plat7[(i,j)].resize(100,100)
              self.lab_plat7[(i,j)]=QLabel(self.plat7)
              self.lab_plat7[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_plat7[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_plat7[(i,j)].adjustSize()

      #_________plat PAGE 8
      
      self.plat8=QWidget()
      self.plat8.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.plat8.move(5,5)
      self.plat8.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_plat8[(i,j)]=QToolButton(self.plat8)
              self.button_plat8[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_plat8[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_plat8[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_plat8[(i,j)].resize(100,100)
              self.lab_plat8[(i,j)]=QLabel(self.plat8)
              self.lab_plat8[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_plat8[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_plat8[(i,j)].adjustSize()


      self.data_plat=[self.plat1,self.plat2,self.plat3,self.plat4,self.plat5,self.plat6,self.plat7,self.plat8]

      self.list_plat=QListWidget(self)
      self.list_plat.setGeometry(50,50,425,430)
      self.list_plat.setStyleSheet("""
                                  background-color:#00f;color:#000

                                  QListWidget::item:selected{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-style:solid;border-size:20px;border-color:#fff;border-radius:0px}
                                  
                                  QListWidget::item:!selected{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:0px}
                                  """)

      for i in self.data_plat:

          self.list_plat_frame=QFrame(self.list_plat)
          self.list_plat_frame.setStyleSheet("""
                                  background-color:#ff0;color:#000
                                  """)
         
          self.layout_plat = QVBoxLayout(self.list_plat_frame)
          self.layout_plat.setContentsMargins(0,0,0,0)
          self.layout_plat.setSpacing(20)
          self.layout_plat.addWidget(i)
          self.setLayout(self.layout_plat)
      
          self.item4 = QListWidgetItem(self.list_plat)         
          self.item_widget4 = self.list_plat_frame        

          self.item4.setSizeHint(QSize(0,400))
         
          self.list_plat.addItem(self.item4)
          self.list_plat.setItemWidget(self.item4,self.item_widget4)
          

      self.lab_plat1[(0,0)].move(self.x,self.y)
      self.lab_plat1[(0,1)].move(self.x+100,self.y)
      self.lab_plat1[(0,2)].move(self.x+200,self.y)
      self.lab_plat1[(0,3)].move(self.x+300,self.y)
      self.lab_plat1[(1,0)].move(self.x,self.y+100)
      self.lab_plat1[(1,1)].move(self.x+100,self.y+100)
      self.lab_plat1[(1,2)].move(self.x+200,self.y+100)
      self.lab_plat1[(1,3)].move(self.x+300,self.y+100)
      self.lab_plat1[(2,0)].move(self.x,self.y+200)
      self.lab_plat1[(2,1)].move(self.x+100,self.y+200)
      self.lab_plat1[(2,2)].move(self.x+200,self.y+200)
      self.lab_plat1[(2,3)].move(self.x+300,self.y+200)
      self.lab_plat1[(3,0)].move(self.x,self.y+300)
      self.lab_plat1[(3,1)].move(self.x+100,self.y+300)
      self.lab_plat1[(3,2)].move(self.x+200,self.y+300)
      self.lab_plat1[(3,3)].move(self.x+300,self.y+300)
      
      self.button_plat1[(0,0)].move(self.x,self.y)
      self.button_plat1[(0,1)].move(self.x+100,self.y)
      self.button_plat1[(0,2)].move(self.x+200,self.y)
      self.button_plat1[(0,3)].move(self.x+300,self.y)
      self.button_plat1[(1,0)].move(self.x,self.y+100)
      self.button_plat1[(1,1)].move(self.x+100,self.y+100)
      self.button_plat1[(1,2)].move(self.x+200,self.y+100)
      self.button_plat1[(1,3)].move(self.x+300,self.y+100)
      self.button_plat1[(2,0)].move(self.x,self.y+200)
      self.button_plat1[(2,1)].move(self.x+100,self.y+200)
      self.button_plat1[(2,2)].move(self.x+200,self.y+200)
      self.button_plat1[(2,3)].move(self.x+300,self.y+200)
      self.button_plat1[(3,0)].move(self.x,self.y+300)
      self.button_plat1[(3,1)].move(self.x+100,self.y+300)
      self.button_plat1[(3,2)].move(self.x+200,self.y+300)
      self.button_plat1[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 2
      
      self.lab_plat2[(0,0)].move(self.x,self.y)
      self.lab_plat2[(0,1)].move(self.x+100,self.y)
      self.lab_plat2[(0,2)].move(self.x+200,self.y)
      self.lab_plat2[(0,3)].move(self.x+300,self.y)
      self.lab_plat2[(1,0)].move(self.x,self.y+100)
      self.lab_plat2[(1,1)].move(self.x+100,self.y+100)
      self.lab_plat2[(1,2)].move(self.x+200,self.y+100)
      self.lab_plat2[(1,3)].move(self.x+300,self.y+100)
      self.lab_plat2[(2,0)].move(self.x,self.y+200)
      self.lab_plat2[(2,1)].move(self.x+100,self.y+200)
      self.lab_plat2[(2,2)].move(self.x+200,self.y+200)
      self.lab_plat2[(2,3)].move(self.x+300,self.y+200)
      self.lab_plat2[(3,0)].move(self.x,self.y+300)
      self.lab_plat2[(3,1)].move(self.x+100,self.y+300)
      self.lab_plat2[(3,2)].move(self.x+200,self.y+300)
      self.lab_plat2[(3,3)].move(self.x+300,self.y+300)
      
      self.button_plat2[(0,0)].move(self.x,self.y)
      self.button_plat2[(0,1)].move(self.x+100,self.y)
      self.button_plat2[(0,2)].move(self.x+200,self.y)
      self.button_plat2[(0,3)].move(self.x+300,self.y)
      self.button_plat2[(1,0)].move(self.x,self.y+100)
      self.button_plat2[(1,1)].move(self.x+100,self.y+100)
      self.button_plat2[(1,2)].move(self.x+200,self.y+100)
      self.button_plat2[(1,3)].move(self.x+300,self.y+100)
      self.button_plat2[(2,0)].move(self.x,self.y+200)
      self.button_plat2[(2,1)].move(self.x+100,self.y+200)
      self.button_plat2[(2,2)].move(self.x+200,self.y+200)
      self.button_plat2[(2,3)].move(self.x+300,self.y+200)
      self.button_plat2[(3,0)].move(self.x,self.y+300)
      self.button_plat2[(3,1)].move(self.x+100,self.y+300)
      self.button_plat2[(3,2)].move(self.x+200,self.y+300)
      self.button_plat2[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 3

      self.lab_plat3[(0,0)].move(self.x,self.y)
      self.lab_plat3[(0,1)].move(self.x+100,self.y)
      self.lab_plat3[(0,2)].move(self.x+200,self.y)
      self.lab_plat3[(0,3)].move(self.x+300,self.y)
      self.lab_plat3[(1,0)].move(self.x,self.y+100)
      self.lab_plat3[(1,1)].move(self.x+100,self.y+100)
      self.lab_plat3[(1,2)].move(self.x+200,self.y+100)
      self.lab_plat3[(1,3)].move(self.x+300,self.y+100)
      self.lab_plat3[(2,0)].move(self.x,self.y+200)
      self.lab_plat3[(2,1)].move(self.x+100,self.y+200)
      self.lab_plat3[(2,2)].move(self.x+200,self.y+200)
      self.lab_plat3[(2,3)].move(self.x+300,self.y+200)
      self.lab_plat3[(3,0)].move(self.x,self.y+300)
      self.lab_plat3[(3,1)].move(self.x+100,self.y+300)
      self.lab_plat3[(3,2)].move(self.x+200,self.y+300)
      self.lab_plat3[(3,3)].move(self.x+300,self.y+300)

      self.button_plat3[(0,0)].move(self.x,self.y)
      self.button_plat3[(0,1)].move(self.x+100,self.y)
      self.button_plat3[(0,2)].move(self.x+200,self.y)
      self.button_plat3[(0,3)].move(self.x+300,self.y)
      self.button_plat3[(1,0)].move(self.x,self.y+100)
      self.button_plat3[(1,1)].move(self.x+100,self.y+100)
      self.button_plat3[(1,2)].move(self.x+200,self.y+100)
      self.button_plat3[(1,3)].move(self.x+300,self.y+100)
      self.button_plat3[(2,0)].move(self.x,self.y+200)
      self.button_plat3[(2,1)].move(self.x+100,self.y+200)
      self.button_plat3[(2,2)].move(self.x+200,self.y+200)
      self.button_plat3[(2,3)].move(self.x+300,self.y+200)
      self.button_plat3[(3,0)].move(self.x,self.y+300)
      self.button_plat3[(3,1)].move(self.x+100,self.y+300)
      self.button_plat3[(3,2)].move(self.x+200,self.y+300)
      self.button_plat3[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 4

      self.lab_plat4[(0,0)].move(self.x,self.y)
      self.lab_plat4[(0,1)].move(self.x+100,self.y)
      self.lab_plat4[(0,2)].move(self.x+200,self.y)
      self.lab_plat4[(0,3)].move(self.x+300,self.y)
      self.lab_plat4[(1,0)].move(self.x,self.y+100)
      self.lab_plat4[(1,1)].move(self.x+100,self.y+100)
      self.lab_plat4[(1,2)].move(self.x+200,self.y+100)
      self.lab_plat4[(1,3)].move(self.x+300,self.y+100)
      self.lab_plat4[(2,0)].move(self.x,self.y+200)
      self.lab_plat4[(2,1)].move(self.x+100,self.y+200)
      self.lab_plat4[(2,2)].move(self.x+200,self.y+200)
      self.lab_plat4[(2,3)].move(self.x+300,self.y+200)
      self.lab_plat4[(3,0)].move(self.x,self.y+300)
      self.lab_plat4[(3,1)].move(self.x+100,self.y+300)
      self.lab_plat4[(3,2)].move(self.x+200,self.y+300)
      self.lab_plat4[(3,3)].move(self.x+300,self.y+300)

      self.button_plat4[(0,0)].move(self.x,self.y)
      self.button_plat4[(0,1)].move(self.x+100,self.y)
      self.button_plat4[(0,2)].move(self.x+200,self.y)
      self.button_plat4[(0,3)].move(self.x+300,self.y)
      self.button_plat4[(1,0)].move(self.x,self.y+100)
      self.button_plat4[(1,1)].move(self.x+100,self.y+100)
      self.button_plat4[(1,2)].move(self.x+200,self.y+100)
      self.button_plat4[(1,3)].move(self.x+300,self.y+100)
      self.button_plat4[(2,0)].move(self.x,self.y+200)
      self.button_plat4[(2,1)].move(self.x+100,self.y+200)
      self.button_plat4[(2,2)].move(self.x+200,self.y+200)
      self.button_plat4[(2,3)].move(self.x+300,self.y+200)
      self.button_plat4[(3,0)].move(self.x,self.y+300)
      self.button_plat4[(3,1)].move(self.x+100,self.y+300)
      self.button_plat4[(3,2)].move(self.x+200,self.y+300)
      self.button_plat4[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 5

      self.lab_plat5[(0,0)].move(self.x,self.y)
      self.lab_plat5[(0,1)].move(self.x+100,self.y)
      self.lab_plat5[(0,2)].move(self.x+200,self.y)
      self.lab_plat5[(0,3)].move(self.x+300,self.y)
      self.lab_plat5[(1,0)].move(self.x,self.y+100)
      self.lab_plat5[(1,1)].move(self.x+100,self.y+100)
      self.lab_plat5[(1,2)].move(self.x+200,self.y+100)
      self.lab_plat5[(1,3)].move(self.x+300,self.y+100)
      self.lab_plat5[(2,0)].move(self.x,self.y+200)
      self.lab_plat5[(2,1)].move(self.x+100,self.y+200)
      self.lab_plat5[(2,2)].move(self.x+200,self.y+200)
      self.lab_plat5[(2,3)].move(self.x+300,self.y+200)
      self.lab_plat5[(3,0)].move(self.x,self.y+300)
      self.lab_plat5[(3,1)].move(self.x+100,self.y+300)
      self.lab_plat5[(3,2)].move(self.x+200,self.y+300)
      self.lab_plat5[(3,3)].move(self.x+300,self.y+300)

      self.button_plat5[(0,0)].move(self.x,self.y)
      self.button_plat5[(0,1)].move(self.x+100,self.y)
      self.button_plat5[(0,2)].move(self.x+200,self.y)
      self.button_plat5[(0,3)].move(self.x+300,self.y)
      self.button_plat5[(1,0)].move(self.x,self.y+100)
      self.button_plat5[(1,1)].move(self.x+100,self.y+100)
      self.button_plat5[(1,2)].move(self.x+200,self.y+100)
      self.button_plat5[(1,3)].move(self.x+300,self.y+100)
      self.button_plat5[(2,0)].move(self.x,self.y+200)
      self.button_plat5[(2,1)].move(self.x+100,self.y+200)
      self.button_plat5[(2,2)].move(self.x+200,self.y+200)
      self.button_plat5[(2,3)].move(self.x+300,self.y+200)
      self.button_plat5[(3,0)].move(self.x,self.y+300)
      self.button_plat5[(3,1)].move(self.x+100,self.y+300)
      self.button_plat5[(3,2)].move(self.x+200,self.y+300)
      self.button_plat5[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 6

      self.lab_plat6[(0,0)].move(self.x,self.y)
      self.lab_plat6[(0,1)].move(self.x+100,self.y)
      self.lab_plat6[(0,2)].move(self.x+200,self.y)
      self.lab_plat6[(0,3)].move(self.x+300,self.y)
      self.lab_plat6[(1,0)].move(self.x,self.y+100)
      self.lab_plat6[(1,1)].move(self.x+100,self.y+100)
      self.lab_plat6[(1,2)].move(self.x+200,self.y+100)
      self.lab_plat6[(1,3)].move(self.x+300,self.y+100)
      self.lab_plat6[(2,0)].move(self.x,self.y+200)
      self.lab_plat6[(2,1)].move(self.x+100,self.y+200)
      self.lab_plat6[(2,2)].move(self.x+200,self.y+200)
      self.lab_plat6[(2,3)].move(self.x+300,self.y+200)
      self.lab_plat6[(3,0)].move(self.x,self.y+300)
      self.lab_plat6[(3,1)].move(self.x+100,self.y+300)
      self.lab_plat6[(3,2)].move(self.x+200,self.y+300)
      self.lab_plat6[(3,3)].move(self.x+300,self.y+300)

      self.button_plat6[(0,0)].move(self.x,self.y)
      self.button_plat6[(0,1)].move(self.x+100,self.y)
      self.button_plat6[(0,2)].move(self.x+200,self.y)
      self.button_plat6[(0,3)].move(self.x+300,self.y)
      self.button_plat6[(1,0)].move(self.x,self.y+100)
      self.button_plat6[(1,1)].move(self.x+100,self.y+100)
      self.button_plat6[(1,2)].move(self.x+200,self.y+100)
      self.button_plat6[(1,3)].move(self.x+300,self.y+100)
      self.button_plat6[(2,0)].move(self.x,self.y+200)
      self.button_plat6[(2,1)].move(self.x+100,self.y+200)
      self.button_plat6[(2,2)].move(self.x+200,self.y+200)
      self.button_plat6[(2,3)].move(self.x+300,self.y+200)
      self.button_plat6[(3,0)].move(self.x,self.y+300)
      self.button_plat6[(3,1)].move(self.x+100,self.y+300)
      self.button_plat6[(3,2)].move(self.x+200,self.y+300)
      self.button_plat6[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 7

      self.lab_plat7[(0,0)].move(self.x,self.y)
      self.lab_plat7[(0,1)].move(self.x+100,self.y)
      self.lab_plat7[(0,2)].move(self.x+200,self.y)
      self.lab_plat7[(0,3)].move(self.x+300,self.y)
      self.lab_plat7[(1,0)].move(self.x,self.y+100)
      self.lab_plat7[(1,1)].move(self.x+100,self.y+100)
      self.lab_plat7[(1,2)].move(self.x+200,self.y+100)
      self.lab_plat7[(1,3)].move(self.x+300,self.y+100)
      self.lab_plat7[(2,0)].move(self.x,self.y+200)
      self.lab_plat7[(2,1)].move(self.x+100,self.y+200)
      self.lab_plat7[(2,2)].move(self.x+200,self.y+200)
      self.lab_plat7[(2,3)].move(self.x+300,self.y+200)
      self.lab_plat7[(3,0)].move(self.x,self.y+300)
      self.lab_plat7[(3,1)].move(self.x+100,self.y+300)
      self.lab_plat7[(3,2)].move(self.x+200,self.y+300)
      self.lab_plat7[(3,3)].move(self.x+300,self.y+300)

      self.button_plat7[(0,0)].move(self.x,self.y)
      self.button_plat7[(0,1)].move(self.x+100,self.y)
      self.button_plat7[(0,2)].move(self.x+200,self.y)
      self.button_plat7[(0,3)].move(self.x+300,self.y)
      self.button_plat7[(1,0)].move(self.x,self.y+100)
      self.button_plat7[(1,1)].move(self.x+100,self.y+100)
      self.button_plat7[(1,2)].move(self.x+200,self.y+100)
      self.button_plat7[(1,3)].move(self.x+300,self.y+100)
      self.button_plat7[(2,0)].move(self.x,self.y+200)
      self.button_plat7[(2,1)].move(self.x+100,self.y+200)
      self.button_plat7[(2,2)].move(self.x+200,self.y+200)
      self.button_plat7[(2,3)].move(self.x+300,self.y+200)
      self.button_plat7[(3,0)].move(self.x,self.y+300)
      self.button_plat7[(3,1)].move(self.x+100,self.y+300)
      self.button_plat7[(3,2)].move(self.x+200,self.y+300)
      self.button_plat7[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 8

      self.lab_plat8[(0,0)].move(self.x,self.y)
      self.lab_plat8[(0,1)].move(self.x+100,self.y)
      self.lab_plat8[(0,2)].move(self.x+200,self.y)
      self.lab_plat8[(0,3)].move(self.x+300,self.y)
      self.lab_plat8[(1,0)].move(self.x,self.y+100)
      self.lab_plat8[(1,1)].move(self.x+100,self.y+100)
      self.lab_plat8[(1,2)].move(self.x+200,self.y+100)
      self.lab_plat8[(1,3)].move(self.x+300,self.y+100)
      self.lab_plat8[(2,0)].move(self.x,self.y+200)
      self.lab_plat8[(2,1)].move(self.x+100,self.y+200)
      self.lab_plat8[(2,2)].move(self.x+200,self.y+200)
      self.lab_plat8[(2,3)].move(self.x+300,self.y+200)
      self.lab_plat8[(3,0)].move(self.x,self.y+300)
      self.lab_plat8[(3,1)].move(self.x+100,self.y+300)
      self.lab_plat8[(3,2)].move(self.x+200,self.y+300)
      self.lab_plat8[(3,3)].move(self.x+300,self.y+300)
      self.button_plat8[(0,0)].move(self.x,self.y)
      self.button_plat8[(0,1)].move(self.x+100,self.y)
      self.button_plat8[(0,2)].move(self.x+200,self.y)
      self.button_plat8[(0,3)].move(self.x+300,self.y)
      self.button_plat8[(1,0)].move(self.x,self.y+100)
      self.button_plat8[(1,1)].move(self.x+100,self.y+100)
      self.button_plat8[(1,2)].move(self.x+200,self.y+100)
      self.button_plat8[(1,3)].move(self.x+300,self.y+100)
      self.button_plat8[(2,0)].move(self.x,self.y+200)
      self.button_plat8[(2,1)].move(self.x+100,self.y+200)
      self.button_plat8[(2,2)].move(self.x+200,self.y+200)
      self.button_plat8[(2,3)].move(self.x+300,self.y+200)
      self.button_plat8[(3,0)].move(self.x,self.y+300)
      self.button_plat8[(3,1)].move(self.x+100,self.y+300)
      self.button_plat8[(3,2)].move(self.x+200,self.y+300)
      self.button_plat8[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++ buttons events +++++++++++++++++++++++++++++++++ DE 1 A 4

      self.button_plat1[(0,0)].clicked.connect(self.pp1)
      self.button_plat1[(0,1)].clicked.connect(self.pp2)
      self.button_plat1[(0,2)].clicked.connect(self.pp3)
      self.button_plat1[(0,3)].clicked.connect(self.pp4)
      self.button_plat1[(1,0)].clicked.connect(self.pp5)
      self.button_plat1[(1,1)].clicked.connect(self.pp6)
      self.button_plat1[(1,2)].clicked.connect(self.pp7)
      self.button_plat1[(1,3)].clicked.connect(self.pp8)
      self.button_plat1[(2,0)].clicked.connect(self.pp9)
      self.button_plat1[(2,1)].clicked.connect(self.pp10)
      self.button_plat1[(2,2)].clicked.connect(self.pp11)
      self.button_plat1[(2,3)].clicked.connect(self.pp12)
      self.button_plat1[(3,0)].clicked.connect(self.pp13)
      self.button_plat1[(3,1)].clicked.connect(self.pp14)
      self.button_plat1[(3,2)].clicked.connect(self.pp15)
      self.button_plat1[(3,3)].clicked.connect(self.pp16)

      self.button_plat2[(0,0)].clicked.connect(self._pp1)
      self.button_plat2[(0,1)].clicked.connect(self._pp2)
      self.button_plat2[(0,2)].clicked.connect(self._pp3)
      self.button_plat2[(0,3)].clicked.connect(self._pp4)
      self.button_plat2[(1,0)].clicked.connect(self._pp5)
      self.button_plat2[(1,1)].clicked.connect(self._pp6)
      self.button_plat2[(1,2)].clicked.connect(self._pp7)
      self.button_plat2[(1,3)].clicked.connect(self._pp8)
      self.button_plat2[(2,0)].clicked.connect(self._pp9)
      self.button_plat2[(2,1)].clicked.connect(self._pp10)
      self.button_plat2[(2,2)].clicked.connect(self._pp11)
      self.button_plat2[(2,3)].clicked.connect(self._pp12)
      self.button_plat2[(3,0)].clicked.connect(self._pp13)
      self.button_plat2[(3,1)].clicked.connect(self._pp14)
      self.button_plat2[(3,2)].clicked.connect(self._pp15)
      self.button_plat2[(3,3)].clicked.connect(self._pp16)

      self.button_plat3[(0,0)].clicked.connect(self.__pp1)
      self.button_plat3[(0,1)].clicked.connect(self.__pp2)
      self.button_plat3[(0,2)].clicked.connect(self.__pp3)
      self.button_plat3[(0,3)].clicked.connect(self.__pp4)
      self.button_plat3[(1,0)].clicked.connect(self.__pp5)
      self.button_plat3[(1,1)].clicked.connect(self.__pp6)
      self.button_plat3[(1,2)].clicked.connect(self.__pp7)
      self.button_plat3[(1,3)].clicked.connect(self.__pp8)
      self.button_plat3[(2,0)].clicked.connect(self.__pp9)
      self.button_plat3[(2,1)].clicked.connect(self.__pp10)
      self.button_plat3[(2,2)].clicked.connect(self.__pp11)
      self.button_plat3[(2,3)].clicked.connect(self.__pp12)
      self.button_plat3[(3,0)].clicked.connect(self.__pp13)
      self.button_plat3[(3,1)].clicked.connect(self.__pp14)
      self.button_plat3[(3,2)].clicked.connect(self.__pp15)
      self.button_plat3[(3,3)].clicked.connect(self.__pp16)

      self.button_plat4[(0,0)].clicked.connect(self.___pp1)
      self.button_plat4[(0,1)].clicked.connect(self.___pp2)
      self.button_plat4[(0,2)].clicked.connect(self.___pp3)
      self.button_plat4[(0,3)].clicked.connect(self.___pp4)
      self.button_plat4[(1,0)].clicked.connect(self.___pp5)
      self.button_plat4[(1,1)].clicked.connect(self.___pp6)
      self.button_plat4[(1,2)].clicked.connect(self.___pp7)
      self.button_plat4[(1,3)].clicked.connect(self.___pp8)
      self.button_plat4[(2,0)].clicked.connect(self.___pp9)
      self.button_plat4[(2,1)].clicked.connect(self.___pp10)
      self.button_plat4[(2,2)].clicked.connect(self.___pp11)
      self.button_plat4[(2,3)].clicked.connect(self.___pp12)
      self.button_plat4[(3,0)].clicked.connect(self.___pp13)
      self.button_plat4[(3,1)].clicked.connect(self.___pp14)
      self.button_plat4[(3,2)].clicked.connect(self.___pp15)
      self.button_plat4[(3,3)].clicked.connect(self.___pp16)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ DE 5 A 8

      self.button_plat5[(0,0)].clicked.connect(self.p1)
      self.button_plat5[(0,1)].clicked.connect(self.p2)
      self.button_plat5[(0,2)].clicked.connect(self.p3)
      self.button_plat5[(0,3)].clicked.connect(self.p4)
      self.button_plat5[(1,0)].clicked.connect(self.p5)
      self.button_plat5[(1,1)].clicked.connect(self.p6)
      self.button_plat5[(1,2)].clicked.connect(self.p7)
      self.button_plat5[(1,3)].clicked.connect(self.p8)
      self.button_plat5[(2,0)].clicked.connect(self.p9)
      self.button_plat5[(2,1)].clicked.connect(self.p10)
      self.button_plat5[(2,2)].clicked.connect(self.p11)
      self.button_plat5[(2,3)].clicked.connect(self.p12)
      self.button_plat5[(3,0)].clicked.connect(self.p13)
      self.button_plat5[(3,1)].clicked.connect(self.p14)
      self.button_plat5[(3,2)].clicked.connect(self.p15)
      self.button_plat5[(3,3)].clicked.connect(self.p16)

      self.button_plat6[(0,0)].clicked.connect(self._p1)
      self.button_plat6[(0,1)].clicked.connect(self._p2)
      self.button_plat6[(0,2)].clicked.connect(self._p3)
      self.button_plat6[(0,3)].clicked.connect(self._p4)
      self.button_plat6[(1,0)].clicked.connect(self._p5)
      self.button_plat6[(1,1)].clicked.connect(self._p6)
      self.button_plat6[(1,2)].clicked.connect(self._p7)
      self.button_plat6[(1,3)].clicked.connect(self._p8)
      self.button_plat6[(2,0)].clicked.connect(self._p9)
      self.button_plat6[(2,1)].clicked.connect(self._p10)
      self.button_plat6[(2,2)].clicked.connect(self._p11)
      self.button_plat6[(2,3)].clicked.connect(self._p12)
      self.button_plat6[(3,0)].clicked.connect(self._p13)
      self.button_plat6[(3,1)].clicked.connect(self._p14)
      self.button_plat6[(3,2)].clicked.connect(self._p15)
      self.button_plat6[(3,3)].clicked.connect(self._p16)

      self.button_plat7[(0,0)].clicked.connect(self.__p1)
      self.button_plat7[(0,1)].clicked.connect(self.__p2)
      self.button_plat7[(0,2)].clicked.connect(self.__p3)
      self.button_plat7[(0,3)].clicked.connect(self.__p4)
      self.button_plat7[(1,0)].clicked.connect(self.__p5)
      self.button_plat7[(1,1)].clicked.connect(self.__p6)
      self.button_plat7[(1,2)].clicked.connect(self.__p7)
      self.button_plat7[(1,3)].clicked.connect(self.__p8)
      self.button_plat7[(2,0)].clicked.connect(self.__p9)
      self.button_plat7[(2,1)].clicked.connect(self.__p10)
      self.button_plat7[(2,2)].clicked.connect(self.__p11)
      self.button_plat7[(2,3)].clicked.connect(self.__p12)
      self.button_plat7[(3,0)].clicked.connect(self.__p13)
      self.button_plat7[(3,1)].clicked.connect(self.__p14)
      self.button_plat7[(3,2)].clicked.connect(self.__p15)
      self.button_plat7[(3,3)].clicked.connect(self.__p16)

      self.button_plat8[(0,0)].clicked.connect(self.___p1)
      self.button_plat8[(0,1)].clicked.connect(self.___p2)
      self.button_plat8[(0,2)].clicked.connect(self.___p3)
      self.button_plat8[(0,3)].clicked.connect(self.___p4)
      self.button_plat8[(1,0)].clicked.connect(self.___p5)
      self.button_plat8[(1,1)].clicked.connect(self.___p6)
      self.button_plat8[(1,2)].clicked.connect(self.___p7)
      self.button_plat8[(1,3)].clicked.connect(self.___p8)
      self.button_plat8[(2,0)].clicked.connect(self.___p9)
      self.button_plat8[(2,1)].clicked.connect(self.___p10)
      self.button_plat8[(2,2)].clicked.connect(self.___p11)
      self.button_plat8[(2,3)].clicked.connect(self.___p12)
      self.button_plat8[(3,0)].clicked.connect(self.___p13)
      self.button_plat8[(3,1)].clicked.connect(self.___p14)
      self.button_plat8[(3,2)].clicked.connect(self.___p15)
      self.button_plat8[(3,3)].clicked.connect(self.___p16)
      
      #================================================================================================#
      #================================================================================================#
      #============================================= PLATS ============================================#
      #================================================================================================#

      #==================================================
      #==================================================
      #======================================== DASHBOARD
      
      
      self.dash=QFrame(self)
      self.dash.setStyleSheet("""
                                background-color:#1b1b1c;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:10px;border-bottom-left-radius:10px;
                                border-bottom-right-radius:10px;border-top-right-radius:10px
                                """)
      self.dash.move(500,450)
      self.dash.resize(450,130)

      #____________________________________FRAME BTN VIEW

      self.dash_main_frame=QFrame(self)            
      self.dash_main_frame.setStyleSheet("""border-style:solid;border-width:1px;border-color:#000;
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:10px
                            """)
      self.dash_main_frame.move(500,50)
      self.dash_main_frame.resize(450,400)
      
      self.btn_view=QToolButton(self.dash_main_frame)
      self.btn_view.setStyleSheet("""
                                  QToolButton::pressed{background-color :transparent;color:#000;border-style:solid;
                                  border-width:5px;border-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::!pressed{border-style:solid;border-width:3px;border-color:#000;
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:20pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::hover{background-color :transparent;color:#000;border-style:solid;
                                  border-width:3px;border-color:#000;font-family: Time;font-style:italic;font-size:20pt;
                                  font-weight:bold;border-radius:10px}
                                """)
      
      self.btn_view.setIconSize(QSize(350,350))
      self.btn_view.move(0,0)
      self.btn_view.resize(450,400)
      self.btn_view.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
      self.btn_view.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_view.clicked.connect(self.select_photo)


      self.dash2=QFrame(self)
      self.dash2.setStyleSheet("""
                                background-color:#1b1b1c;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:10px;border-bottom-left-radius:10px;
                                border-bottom-right-radius:10px;border-top-right-radius:10px
                                """)
      #_________________________________________
      #_________________________________________
      #_________________________________________
      self.dash2.move(980,50)
      self.dash2.resize(190,400)

      #_________________________________________DATAS PRODUCT

      #_______NOM
      self.nom_lab=QLabel('NOM',self.dash2)
      self.nom_lab.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.nom_lab.move(10,0)
      self.nom_lab.resize(100,20)

      self.nom_produit=QLineEdit(self.dash2)
      self.nom_produit.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.nom_produit.setAlignment(Qt.AlignCenter)
      self.nom_produit.move(10,20)
      self.nom_produit.resize(150,20)
      self.qte_lab=QLabel('QUANTITES',self.dash2)
      self.qte_lab.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.qte_lab.move(10,40)
      self.qte_lab.resize(200,20)

      self.qte_produit=QSpinBox(self.dash2)
      self.qte_produit.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.qte_produit.setAlignment(Qt.AlignCenter)
      self.qte_produit.setMinimum(0)
      self.qte_produit.setMaximum(1000000)
      self.qte_produit.move(10,60)
      self.qte_produit.resize(150,20)

      #_______PRIX
      self.prix_lab=QLabel('PRIX UNITAIRE',self.dash2)
      self.prix_lab.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.prix_lab.move(10,80)
      self.prix_lab.resize(100,20)

      self.prix_produit=QDoubleSpinBox(self.dash2)
      self.prix_produit.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.prix_produit.setAlignment(Qt.AlignCenter)
      self.prix_produit.setMinimum(0)
      self.prix_produit.setMaximum(1000000)
      self.prix_produit.move(10,100)
      self.prix_produit.resize(150,20)

      #_______REDUCTION
      self.reduction_lab=QLabel('REDUCTION',self.dash2)
      self.reduction_lab.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.reduction_lab.move(10,120)
      self.reduction_lab.resize(100,20)

      self.reduction_produit=QSpinBox(self.dash2)
      self.reduction_produit.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.reduction_produit.setAlignment(Qt.AlignCenter)
      self.reduction_produit.setMinimum(0)
      self.reduction_produit.setMaximum(1000000)
      self.reduction_produit.move(10,140)
      self.reduction_produit.resize(150,20)

      #_______ID CATEGORIE
      self.id_cat_lab=QLabel('ID CATEGORIE',self.dash2)
      self.id_cat_lab.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.id_cat_lab.move(10,160)
      self.id_cat_lab.resize(100,20)

      self.id_categ=QSpinBox(self.dash2)
      self.id_categ.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.id_categ.setAlignment(Qt.AlignCenter)
      self.id_categ.setValue(1)
      self.id_categ.setEnabled(False)
      self.id_categ.move(10,180)
      self.id_categ.resize(150,20)

      #_______CATEGORIES
      self.cat_lab=QLabel('CATEGORIES',self.dash2)
      self.cat_lab.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.cat_lab.move(10,200)
      self.cat_lab.resize(100,20)

      self.cat_produit=QComboBox(self.dash2)
      self.cat_produit.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.cat_produit.setAlignment(Qt.AlignCenter)
      self.cat_produit.move(10,220)
      self.cat_produit.resize(150,20)
      #self.cat_produit.currentIndexChanged.connect(self.selection_cat)
      
      #_______ID PRODUIT
      self.id_lab=QLabel('ID PRODUIT',self.dash2)
      self.id_lab.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                """)
      self.id_lab.move(10,240)
      self.id_lab.resize(100,20)

      self.id_produit=QSpinBox(self.dash2)
      self.id_produit.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.id_produit.setMaximum(1000000)
      self.id_produit.setAlignment(Qt.AlignCenter)
      self.id_produit.setValue(1)
      self.id_produit.setEnabled(False)
      self.id_produit.move(10,260)
      self.id_produit.resize(150,20)

      #_______CODE PRODUIT
      self.code_lab=QLabel('CODE PRODUIT',self.dash2)
      self.code_lab.setStyleSheet("""
                                   background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.code_lab.move(10,280)
      self.code_lab.resize(100,20)

      self.code_produit=QLineEdit(self.dash2)
      self.code_produit.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.code_produit.setAlignment(Qt.AlignCenter)
      self.code_produit.setEnabled(False)
      self.code_produit.move(10,300)
      self.code_produit.resize(150,20)

      #_________________________________________ADD PRODUCT

      self.btn_add=QPushButton('AJOUTER',self.dash2)
      self.btn_add.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_add.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_add.clicked.connect(self.add_data)
      self.btn_add.move(10,340)
      self.btn_add.resize(70,25)
      #_________________________________________REMOVE PRODUCT

      self.btn_remove=QPushButton('RETIRER',self.dash2)
      self.btn_remove.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_remove.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_remove.clicked.connect(self.remove_data)
      self.btn_remove.move(10,370)
      self.btn_remove.resize(70,25)
      #_________________________________________EDIT PRODUCT
      self.btn_edit=QPushButton('MODIFIER',self.dash2)
      self.btn_edit.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_edit.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_edit.clicked.connect(self.modify_data)
      self.btn_edit.move(90,340)
      self.btn_edit.resize(70,25)

      #_________________________________________refresh_data
      self.btn_refresh_data=QPushButton('REFRESH',self.dash2)
      self.btn_refresh_data.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_refresh_data.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_refresh_data.clicked.connect(self.refresh_data)
      self.btn_refresh_data.move(90,370)
      self.btn_refresh_data.resize(70,25)

      #=================================MULTIPLE DELETING

      #=========================LABEL 
      self.lab_id_x_produit=QLabel('RETIRER PLUSIEURS PRODUITS',self)
      self.lab_id_x_produit.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.lab_id_x_produit.move(510,460)
      self.lab_id_x_produit.resize(250,20)

      #=================================LINE EDIT
      self.id_x_produit=QLineEdit(self)
      self.id_x_produit.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.nom_cat.setAlignment(Qt.AlignCenter)
      self.id_x_produit.move(510,480)
      self.id_x_produit.resize(150,20)

      #=================================RETIRER PRODUITS
      self.btn_id_x=QPushButton('RETIRER',self)
      self.btn_id_x.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_id_x.setCursor(QCursor(Qt.PointingHandCursor))
      #self.btn_id_x.clicked.connect(self.remove_x_produit)
      self.btn_id_x.move(670,480)
      self.btn_id_x.resize(80,20)

      #=================================CATEGORIES

      #=========================LABEL CATEGORIE
      self.lab_cat=QLabel('CATEGORIES',self)
      self.lab_cat.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.lab_cat.move(510,500)
      self.lab_cat.resize(100,20)
      
      #=================================LINE EDIT
      self.nom_cat=QLineEdit(self)
      self.nom_cat.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.nom_cat.setAlignment(Qt.AlignCenter)
      self.nom_cat.move(510,520)
      self.nom_cat.resize(150,20)
      #=================================DISPONIBLE
      self.btn_cat1=QPushButton('DISPONIBLE',self)
      self.btn_cat1.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_cat1.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_cat1.clicked.connect(self.refresh_cat)
      self.btn_cat1.move(670,520)
      self.btn_cat1.resize(80,20)
      #=================================AJOUTER CATEGORIE
      self.btn_cat2=QPushButton('AJOUTER',self)
      self.btn_cat2.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_cat2.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_cat2.clicked.connect(self.add_cat)
      self.btn_cat2.move(510,550)
      self.btn_cat2.resize(80,20)
      #=================================RETIRER CATEGORIE
      self.btn_cat3=QPushButton('RETIRER',self)
      self.btn_cat3.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_cat3.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_cat3.clicked.connect(self.remove_cat)
      self.btn_cat3.move(670,550)
      self.btn_cat3.resize(80,20)

      """
      #================================= FERMER FENETRE
      self.btn_fermer=QPushButton('FERMER',self)
      self.btn_fermer.setStyleSheet(\"""
                                  QPushButton::pressed{background-color :#fff;color:#000;border-style:solid;
                                  border-width:2px;border-color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#f00;
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  \""")
      self.btn_fermer.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_fermer.clicked.connect(self.close)
      self.btn_fermer.move(1000,10)
      self.btn_fermer.resize(80,20)

      #================================= REDUIRE FENETRE
      self.btn_reduire=QPushButton('REDUIRE',self)
      self.btn_reduire.setStyleSheet(\"""
                                  QPushButton::pressed{background-color :#fff;color:#000;border-style:solid;
                                  border-width:2px;border-color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#05b7f7;
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  \""")
      self.btn_reduire.setCursor(QCursor(Qt.PointingHandCursor))
      #self.btn_reduire.clicked.connect()
      self.btn_reduire.move(1090,10)
      self.btn_reduire.resize(80,20)"""

      self.list_boisson.show()

 
   #================================================================================================#
   #================================================================================================#
   #============================================ FUNCTIONS =========================================#
   #================================================================================================#

   def close(self):
      self.question=QMessageBox.question(self,str(self.app_name),'VOUS VOULEZ QUITTER ?',QMessageBox.Yes,QMessageBox.No)
      if self.question==QMessageBox.Yes:
         os._exit(0)
      else:
         pass

   def boissons_page(self):
      self.zone_title.setText('BOISSONS')
      self.refresh_all()             
      #BOISSONS
      self.list_boisson.show()
      #DESSERTS
      self.list_dessert.hide()
      #CAFES
      self.list_cafe.hide()
      #PLATS
      self.list_plat.hide()
   def desserts_page(self):
      self.zone_title.setText('DESSERTS')
      self.refresh_all()             
      #BOISSONS
      self.list_boisson.hide()
      #DESSERTS
      self.list_dessert.show()
      #CAFES
      self.list_cafe.hide()
      #PLATS
      self.list_plat.hide()
   def cafes_page(self):
      self.zone_title.setText('CAFES')
      self.refresh_all()             
      #BOISSONS
      self.list_boisson.hide()
      #DESSERTS
      self.list_dessert.hide()
      #CAFES
      self.list_cafe.show()
      #PLATS
      self.list_plat.hide()
   def plats_page(self):
      self.zone_title.setText('PLATS')
      self.refresh_all()             
      #BOISSONS
      self.list_boisson.hide()
      #DESSERTS
      self.list_dessert.hide()
      #CAFES
      self.list_cafe.hide()
      #PLATS
      self.list_plat.show()

                          
   def bb1(self):
      signal=self.sender()
      for i in range(32):
         for j in range(4):
            if signal==self.button_boisson1[(i,j)]:
               self.btn_view.setIcon(QIcon(self.button_boisson1[(i,j)].icon()))
               self.btn_view.setText(str(self.button_boisson1[(i,j)].text()))
               self.button_boisson1[(i,j)].setFocus()
               self.id_produit.setValue(1)
               self.get_data()


   def dd1(self):
      if self.button_dessert1[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(0,0)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(0,0)].text()))
         self.button_dessert1[(0,0)].setFocus()
         self.id_produit.setValue(1)
         self.get_data()
   def dd2(self):
      if self.button_dessert1[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(0,1)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(0,1)].text()))
         self.button_dessert1[(0,1)].setFocus()
         self.id_produit.setValue(2)
         self.get_data()
   def dd3(self):
      if self.button_dessert1[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(0,2)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(0,2)].text()))
         self.button_dessert1[(0,2)].setFocus()
         self.id_produit.setValue(3)
         self.get_data()
   def dd4(self):
      if self.button_dessert1[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(0,3)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(0,3)].text()))
         self.button_dessert1[(0,3)].setFocus()
         self.id_produit.setValue(4)
         self.get_data()
   def dd5(self):
      if self.button_dessert1[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(1,0)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(1,0)].text()))
         self.button_dessert1[(1,0)].setFocus()
         self.id_produit.setValue(5)
         self.get_data()
   def dd6(self):
      if self.button_dessert1[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(1,1)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(1,1)].text()))
         self.button_dessert1[(1,1)].setFocus()
         self.id_produit.setValue(6)
         self.get_data()
   def dd7(self):
      if self.button_dessert1[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(1,2)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(1,2)].text()))
         self.button_dessert1[(1,2)].setFocus()
         self.id_produit.setValue(7)
         self.get_data()
   def dd8(self):
      if self.button_dessert1[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(1,3)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(1,3)].text()))
         self.button_dessert1[(1,3)].setFocus()
         self.id_produit.setValue(8)
         self.get_data()
   def dd9(self):
      if self.button_dessert1[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(2,0)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(2,0)].text()))
         self.button_dessert1[(2,0)].setFocus()
         self.id_produit.setValue(9)
         self.get_data()
   def dd10(self):
      if self.button_dessert1[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(2,1)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(2,1)].text()))
         self.button_dessert1[(2,1)].setFocus()
         self.id_produit.setValue(10)
         self.get_data()
   def dd11(self):
      if self.button_dessert1[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(2,2)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(2,2)].text()))
         self.button_dessert1[(2,2)].setFocus()
         self.id_produit.setValue(11)
         self.get_data()
   def dd12(self):
      if self.button_dessert1[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(2,3)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(2,3)].text()))
         self.button_dessert1[(2,3)].setFocus()
         self.id_produit.setValue(12)
         self.get_data()
   def dd13(self):
      if self.button_dessert1[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(3,0)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(3,0)].text()))
         self.button_dessert1[(3,0)].setFocus()
         self.id_produit.setValue(13)
         self.get_data()
   def dd14(self):
      if self.button_dessert1[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(3,1)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(3,1)].text()))
         self.button_dessert1[(3,1)].setFocus()
         self.id_produit.setValue(14)
         self.get_data()
   def dd15(self):
      if self.button_dessert1[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(3,2)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(3,2)].text()))
         self.button_dessert1[(3,2)].setFocus()
         self.id_produit.setValue(15)
         self.get_data()
   def dd16(self):
      if self.button_dessert1[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert1[(3,3)].icon()))
         self.btn_view.setText(str(self.button_dessert1[(3,3)].text()))
         self.button_dessert1[(3,3)].setFocus()
         self.id_produit.setValue(16)
         self.get_data()
   def _dd1(self):
      if self.button_dessert2[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(0,0)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(0,0)].text()))
         self.button_dessert2[(0,0)].setFocus()
         self.id_produit.setValue(17)
         self.get_data()
   def _dd2(self):
      if self.button_dessert2[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(0,1)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(0,1)].text()))
         self.button_dessert2[(0,1)].setFocus()
         self.id_produit.setValue(18)
         self.get_data()
   def _dd3(self):
      if self.button_dessert2[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(0,2)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(0,2)].text()))
         self.button_dessert2[(0,2)].setFocus()
         self.id_produit.setValue(19)
         self.get_data()
   def _dd4(self):
      if self.button_dessert2[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(0,3)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(0,3)].text()))
         self.button_dessert2[(0,3)].setFocus()
         self.id_produit.setValue(20)
         self.get_data()
   def _dd5(self):
      if self.button_dessert2[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(1,0)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(1,0)].text()))
         self.button_dessert2[(1,0)].setFocus()
         self.id_produit.setValue(21)
         self.get_data()
   def _dd6(self):
      if self.button_dessert2[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(1,1)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(1,1)].text()))
         self.button_dessert2[(1,1)].setFocus()
         self.id_produit.setValue(22)
         self.get_data()
   def _dd7(self):
      if self.button_dessert2[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(1,2)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(1,2)].text()))
         self.button_dessert2[(1,2)].setFocus()
         self.id_produit.setValue(23)
         self.get_data()
   def _dd8(self):
      if self.button_dessert2[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(1,3)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(1,3)].text()))
         self.button_dessert2[(1,3)].setFocus()
         self.id_produit.setValue(24)
         self.get_data()
   def _dd9(self):
      if self.button_dessert2[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(2,0)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(2,0)].text()))
         self.button_dessert2[(2,0)].setFocus()
         self.id_produit.setValue(25)
         self.get_data()
   def _dd10(self):
      if self.button_dessert2[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(2,1)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(2,1)].text()))
         self.button_dessert2[(2,1)].setFocus()
         self.id_produit.setValue(26)
         self.get_data()
   def _dd11(self):
      if self.button_dessert2[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(2,2)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(2,2)].text()))
         self.button_dessert2[(2,2)].setFocus()
         self.id_produit.setValue(27)
         self.get_data()
   def _dd12(self):
      if self.button_dessert2[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(2,3)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(2,3)].text()))
         self.button_dessert2[(2,3)].setFocus()
         self.id_produit.setValue(28)
         self.get_data()
   def _dd13(self):
      if self.button_dessert2[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(3,0)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(3,0)].text()))
         self.button_dessert2[(3,0)].setFocus()
         self.id_produit.setValue(29)
         self.get_data()
   def _dd14(self):
      if self.button_dessert2[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(3,1)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(3,1)].text()))
         self.button_dessert2[(3,1)].setFocus()
         self.id_produit.setValue(30)
         self.get_data()
   def _dd15(self):
      if self.button_dessert2[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(3,2)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(3,2)].text()))
         self.button_dessert2[(3,2)].setFocus()
         self.id_produit.setValue(31)
         self.get_data()
   def _dd16(self):
      if self.button_dessert2[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert2[(3,3)].icon()))
         self.btn_view.setText(str(self.button_dessert2[(3,3)].text()))
         self.button_dessert2[(3,3)].setFocus()
         self.id_produit.setValue(32)
         self.get_data()

   def __dd1(self):
      if self.button_dessert3[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(0,0)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(0,0)].text()))
         self.button_dessert3[(0,0)].setFocus()
         self.id_produit.setValue(33)
         self.get_data()
   def __dd2(self):
      if self.button_dessert3[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(0,1)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(0,1)].text()))
         self.button_dessert3[(0,1)].setFocus()
         self.id_produit.setValue(34)
         self.get_data()
   def __dd3(self):
      if self.button_dessert3[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(0,2)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(0,2)].text()))
         self.button_dessert3[(0,2)].setFocus()
         self.id_produit.setValue(35)
         self.get_data()
   def __dd4(self):
      if self.button_dessert3[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(0,3)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(0,3)].text()))
         self.button_dessert3[(0,3)].setFocus()
         self.id_produit.setValue(36)
         self.get_data()
   def __dd5(self):
      if self.button_dessert3[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(1,0)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(1,0)].text()))
         self.button_dessert3[(1,0)].setFocus()
         self.id_produit.setValue(37)
         self.get_data()
   def __dd6(self):
      if self.button_dessert3[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(1,1)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(1,1)].text()))
         self.button_dessert3[(1,1)].setFocus()
         self.id_produit.setValue(38)
         self.get_data()
   def __dd7(self):
      if self.button_dessert3[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(1,2)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(1,2)].text()))
         self.button_dessert3[(1,2)].setFocus()
         self.id_produit.setValue(39)
         self.get_data()
   def __dd8(self):
      if self.button_dessert3[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(1,3)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(1,3)].text()))
         self.button_dessert3[(1,3)].setFocus()
         self.id_produit.setValue(40)
         self.get_data()
   def __dd9(self):
      if self.button_dessert3[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(2,0)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(2,0)].text()))
         self.button_dessert3[(2,0)].setFocus()
         self.id_produit.setValue(41)
         self.get_data()
   def __dd10(self):
      if self.button_dessert3[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(2,1)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(2,1)].text()))
         self.button_dessert3[(2,1)].setFocus()
         self.id_produit.setValue(42)
         self.get_data()
   def __dd11(self):
      if self.button_dessert3[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(2,2)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(2,2)].text()))
         self.button_dessert3[(2,2)].setFocus()
         self.id_produit.setValue(43)
         self.get_data()
   def __dd12(self):
      if self.button_dessert3[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(2,3)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(2,3)].text()))
         self.button_dessert3[(2,3)].setFocus()
         self.id_produit.setValue(44)
         self.get_data()
   def __dd13(self):
      if self.button_dessert3[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(3,0)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(3,0)].text()))
         self.button_dessert3[(3,0)].setFocus()
         self.id_produit.setValue(45)
         self.get_data()
   def __dd14(self):
      if self.button_dessert3[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(3,1)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(3,1)].text()))
         self.button_dessert3[(3,1)].setFocus()
         self.id_produit.setValue(46)
         self.get_data()
   def __dd15(self):
      if self.button_dessert3[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(3,2)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(3,2)].text()))
         self.button_dessert3[(3,2)].setFocus()
         self.id_produit.setValue(47)
         self.get_data()
   def __dd16(self):
      if self.button_dessert3[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert3[(3,3)].icon()))
         self.btn_view.setText(str(self.button_dessert3[(3,3)].text()))
         self.button_dessert3[(3,3)].setFocus()
         self.id_produit.setValue(48)
         self.get_data()
   def ___dd1(self):
      if self.button_dessert4[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(0,0)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(0,0)].text()))
         self.button_dessert4[(0,0)].setFocus()
         self.id_produit.setValue(49)
         self.get_data()
   def ___dd2(self):
      if self.button_dessert4[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(0,1)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(0,1)].text()))
         self.button_dessert4[(0,1)].setFocus()
         self.id_produit.setValue(50)
         self.get_data()
   def ___dd3(self):
      if self.button_dessert4[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(0,2)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(0,2)].text()))
         self.button_dessert4[(0,2)].setFocus()
         self.id_produit.setValue(51)
         self.get_data()
   def ___dd4(self):
      if self.button_dessert4[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(0,3)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(0,3)].text()))
         self.button_dessert4[(0,3)].setFocus()
         self.id_produit.setValue(52)
         self.get_data()
   def ___dd5(self):
      if self.button_dessert4[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(1,0)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(1,0)].text()))
         self.button_dessert4[(1,0)].setFocus()
         self.id_produit.setValue(53)
         self.get_data()
   def ___dd6(self):
      if self.button_dessert4[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(1,1)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(1,1)].text()))
         self.button_dessert4[(1,1)].setFocus()
         self.id_produit.setValue(54)
         self.get_data()
   def ___dd7(self):
      if self.button_dessert4[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(1,2)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(1,2)].text()))
         self.button_dessert4[(1,2)].setFocus()
         self.id_produit.setValue(55)
         self.get_data()
   def ___dd8(self):
      if self.button_dessert4[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(1,3)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(1,3)].text()))
         self.button_dessert4[(1,3)].setFocus()
         self.id_produit.setValue(56)
         self.get_data()
   def ___dd9(self):
      if self.button_dessert4[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(2,0)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(2,0)].text()))
         self.button_dessert4[(2,0)].setFocus()
         self.id_produit.setValue(57)
         self.get_data()
   def ___dd10(self):
      if self.button_dessert4[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(2,1)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(2,1)].text()))
         self.button_dessert4[(2,1)].setFocus()
         self.id_produit.setValue(58)
         self.get_data()
   def ___dd11(self):
      if self.button_dessert4[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(2,2)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(2,2)].text()))
         self.button_dessert4[(2,2)].setFocus()
         self.id_produit.setValue(59)
         self.get_data()
   def ___dd12(self):
      if self.button_dessert4[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(2,3)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(2,3)].text()))
         self.button_dessert4[(2,3)].setFocus()
         self.id_produit.setValue(60)
         self.get_data()
   def ___dd13(self):
      if self.button_dessert4[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(3,0)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(3,0)].text()))
         self.button_dessert4[(3,0)].setFocus()
         self.id_produit.setValue(61)
         self.get_data()
   def ___dd14(self):
      if self.button_dessert4[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(3,1)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(3,1)].text()))
         self.button_dessert4[(3,1)].setFocus()
         self.id_produit.setValue(62)
         self.get_data()
   def ___dd15(self):
      if self.button_dessert4[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(3,2)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(3,2)].text()))
         self.button_dessert4[(3,2)].setFocus()
         self.id_produit.setValue(63)
         self.get_data()
   def ___dd16(self):
      if self.button_dessert4[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert4[(3,3)].icon()))
         self.btn_view.setText(str(self.button_dessert4[(3,3)].text()))
         self.button_dessert4[(3,3)].setFocus()
         self.id_produit.setValue(64)
         self.get_data()

   #++++++++++++++++++++++++++++++++++++++  PAGE PANIER 5 A 8

   def d1(self):
      if self.button_dessert5[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(0,0)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(0,0)].text()))
         self.button_dessert5[(0,0)].setFocus()
         self.id_produit.setValue(65)
         self.get_data()
   def d2(self):
      if self.button_dessert5[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(0,1)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(0,1)].text()))
         self.button_dessert5[(0,1)].setFocus()
         self.id_produit.setValue(66)
         self.get_data()
   def d3(self):
      if self.button_dessert5[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(0,2)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(0,2)].text()))
         self.button_dessert5[(0,2)].setFocus()
         self.id_produit.setValue(67)
         self.get_data()
   def d4(self):
      if self.button_dessert5[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(0,3)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(0,3)].text()))
         self.button_dessert5[(0,3)].setFocus()
         self.id_produit.setValue(68)
         self.get_data()
   def d5(self):
      if self.button_dessert5[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(1,0)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(1,0)].text()))
         self.button_dessert5[(1,0)].setFocus()
         self.id_produit.setValue(69)
         self.get_data()
   def d6(self):
      if self.button_dessert5[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(1,1)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(1,1)].text()))
         self.button_dessert5[(1,1)].setFocus()
         self.id_produit.setValue(70)
         self.get_data()
   def d7(self):
      if self.button_dessert5[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(1,2)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(1,2)].text()))
         self.button_dessert5[(1,2)].setFocus()
         self.id_produit.setValue(71)
         self.get_data()
   def d8(self):
      if self.button_dessert5[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(1,3)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(1,3)].text()))
         self.button_dessert5[(1,3)].setFocus()
         self.id_produit.setValue(72)
         self.get_data()
   def d9(self):
      if self.button_dessert5[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(2,0)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(2,0)].text()))
         self.button_dessert5[(2,0)].setFocus()
         self.id_produit.setValue(73)
         self.get_data()
   def d10(self):
      if self.button_dessert5[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(2,1)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(2,1)].text()))
         self.button_dessert5[(2,1)].setFocus()
         self.id_produit.setValue(74)
         self.get_data()
   def d11(self):
      if self.button_dessert5[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(2,2)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(2,2)].text()))
         self.button_dessert5[(2,2)].setFocus()
         self.id_produit.setValue(75)
         self.get_data()
   def d12(self):
      if self.button_dessert5[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(2,3)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(2,3)].text()))
         self.button_dessert5[(2,3)].setFocus()
         self.id_produit.setValue(76)
         self.get_data()
   def d13(self):
      if self.button_dessert5[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(3,0)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(3,0)].text()))
         self.button_dessert5[(3,0)].setFocus()
         self.id_produit.setValue(77)
         self.get_data()
   def d14(self):
      if self.button_dessert5[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(3,1)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(3,1)].text()))
         self.button_dessert5[(3,1)].setFocus()
         self.id_produit.setValue(78)
         self.get_data()
   def d15(self):
      if self.button_dessert5[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(3,2)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(3,2)].text()))
         self.button_dessert5[(3,2)].setFocus()
         self.id_produit.setValue(79)
         self.get_data()
   def d16(self):
      if self.button_dessert5[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert5[(3,3)].icon()))
         self.btn_view.setText(str(self.button_dessert5[(3,3)].text()))
         self.button_dessert5[(3,3)].setFocus()
         self.id_produit.setValue(80)
         self.get_data()
   def _d1(self):
      if self.button_dessert6[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(0,0)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(0,0)].text()))
         self.button_dessert6[(0,0)].setFocus()
         self.id_produit.setValue(81)
         self.get_data()
   def _d2(self):
      if self.button_dessert6[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(0,1)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(0,1)].text()))
         self.button_dessert6[(0,1)].setFocus()
         self.id_produit.setValue(82)
         self.get_data()
   def _d3(self):
      if self.button_dessert6[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(0,2)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(0,2)].text()))
         self.button_dessert6[(0,2)].setFocus()
         self.id_produit.setValue(83)
         self.get_data()
   def _d4(self):
      if self.button_dessert6[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(0,3)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(0,3)].text()))
         self.button_dessert6[(0,3)].setFocus()
         self.id_produit.setValue(84)
         self.get_data()
   def _d5(self):
      if self.button_dessert6[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(1,0)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(1,0)].text()))
         self.button_dessert6[(1,0)].setFocus()
         self.id_produit.setValue(85)
         self.get_data()
   def _d6(self):
      if self.button_dessert6[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(1,1)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(1,1)].text()))
         self.button_dessert6[(1,1)].setFocus()
         self.id_produit.setValue(86)
         self.get_data()
   def _d7(self):
      if self.button_dessert6[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(1,2)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(1,2)].text()))
         self.button_dessert6[(1,2)].setFocus()
         self.id_produit.setValue(87)
         self.get_data()
   def _d8(self):
      if self.button_dessert6[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(1,3)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(1,3)].text()))
         self.button_dessert6[(1,3)].setFocus()
         self.id_produit.setValue(88)
         self.get_data()
   def _d9(self):
      if self.button_dessert6[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(2,0)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(2,0)].text()))
         self.button_dessert6[(2,0)].setFocus()
         self.id_produit.setValue(89)
         self.get_data()
   def _d10(self):
      if self.button_dessert6[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(2,1)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(2,1)].text()))
         self.button_dessert6[(2,1)].setFocus()
         self.id_produit.setValue(90)
         self.get_data()
   def _d11(self):
      if self.button_dessert6[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(2,2)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(2,2)].text()))
         self.button_dessert6[(2,2)].setFocus()
         self.id_produit.setValue(91)
         self.get_data()
   def _d12(self):
      if self.button_dessert6[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(2,3)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(2,3)].text()))
         self.button_dessert6[(2,3)].setFocus()
         self.id_produit.setValue(92)
         self.get_data()
   def _d13(self):
      if self.button_dessert6[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(3,0)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(3,0)].text()))
         self.button_dessert6[(3,0)].setFocus()
         self.id_produit.setValue(93)
         self.get_data()
   def _d14(self):
      if self.button_dessert6[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(3,1)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(3,1)].text()))
         self.button_dessert6[(3,1)].setFocus()
         self.id_produit.setValue(94)
         self.get_data()
   def _d15(self):
      if self.button_dessert6[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(3,2)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(3,2)].text()))
         self.button_dessert6[(3,2)].setFocus()
         self.id_produit.setValue(95)
         self.get_data()
   def _d16(self):
      if self.button_dessert6[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert6[(3,3)].icon()))
         self.btn_view.setText(str(self.button_dessert6[(3,3)].text()))
         self.button_dessert6[(3,3)].setFocus()
         self.id_produit.setValue(96)
         self.get_data()

   def __d1(self):
      if self.button_dessert7[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(0,0)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(0,0)].text()))
         self.button_dessert7[(0,0)].setFocus()
         self.id_produit.setValue(97)
         self.get_data()
   def __d2(self):
      if self.button_dessert7[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(0,1)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(0,1)].text()))
         self.button_dessert7[(0,1)].setFocus()
         self.id_produit.setValue(98)
         self.get_data()
   def __d3(self):
      if self.button_dessert7[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(0,2)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(0,2)].text()))
         self.button_dessert7[(0,2)].setFocus()
         self.id_produit.setValue(99)
         self.get_data()
   def __d4(self):
      if self.button_dessert7[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(0,3)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(0,3)].text()))
         self.button_dessert7[(0,3)].setFocus()
         self.id_produit.setValue(100)
         self.get_data()
   def __d5(self):
      if self.button_dessert7[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(1,0)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(1,0)].text()))
         self.button_dessert7[(1,0)].setFocus()
         self.id_produit.setValue(101)
         self.get_data()
   def __d6(self):
      if self.button_dessert7[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(1,1)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(1,1)].text()))
         self.button_dessert7[(1,1)].setFocus()
         self.id_produit.setValue(102)
         self.get_data()
   def __d7(self):
      if self.button_dessert7[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(1,2)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(1,2)].text()))
         self.button_dessert7[(1,2)].setFocus()
         self.id_produit.setValue(103)
         self.get_data()
   def __d8(self):
      if self.button_dessert7[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(1,3)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(1,3)].text()))
         self.button_dessert7[(1,3)].setFocus()
         self.id_produit.setValue(104)
         self.get_data()
   def __d9(self):
      if self.button_dessert7[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(2,0)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(2,0)].text()))
         self.button_dessert7[(2,0)].setFocus()
         self.id_produit.setValue(105)
         self.get_data()
   def __d10(self):
      if self.button_dessert7[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(2,1)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(2,1)].text()))
         self.button_dessert7[(2,1)].setFocus()
         self.id_produit.setValue(106)
         self.get_data()
   def __d11(self):
      if self.button_dessert7[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(2,2)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(2,2)].text()))
         self.button_dessert7[(2,2)].setFocus()
         self.id_produit.setValue(107)
         self.get_data()
   def __d12(self):
      if self.button_dessert7[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(2,3)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(2,3)].text()))
         self.button_dessert7[(2,3)].setFocus()
         self.id_produit.setValue(108)
         self.get_data()
   def __d13(self):
      if self.button_dessert7[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(3,0)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(3,0)].text()))
         self.button_dessert7[(3,0)].setFocus()
         self.id_produit.setValue(109)
         self.get_data()
   def __d14(self):
      if self.button_dessert7[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(3,1)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(3,1)].text()))
         self.button_dessert7[(3,1)].setFocus()
         self.id_produit.setValue(110)
         self.get_data()
   def __d15(self):
      if self.button_dessert7[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(3,2)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(3,2)].text()))
         self.button_dessert7[(3,2)].setFocus()
         self.id_produit.setValue(111)
         self.get_data()
   def __d16(self):
      if self.button_dessert7[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert7[(3,3)].icon()))
         self.btn_view.setText(str(self.button_dessert7[(3,3)].text()))
         self.button_dessert7[(3,3)].setFocus()
         self.id_produit.setValue(112)
         self.get_data()
   def ___d1(self):
      if self.button_dessert8[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(0,0)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(0,0)].text()))
         self.button_dessert8[(0,0)].setFocus()
         self.id_produit.setValue(113)
         self.get_data()
   def ___d2(self):
      if self.button_dessert8[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(0,1)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(0,1)].text()))
         self.button_dessert8[(0,1)].setFocus()
         self.id_produit.setValue(114)
         self.get_data()
   def ___d3(self):
      if self.button_dessert8[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(0,2)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(0,2)].text()))
         self.button_dessert8[(0,2)].setFocus()
         self.id_produit.setValue(115)
         self.get_data()
   def ___d4(self):
      if self.button_dessert8[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(0,3)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(0,3)].text()))
         self.button_dessert8[(0,3)].setFocus()
         self.id_produit.setValue(116)
         self.get_data()
   def ___d5(self):
      if self.button_dessert8[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(1,0)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(1,0)].text()))
         self.button_dessert8[(1,0)].setFocus()
         self.id_produit.setValue(117)
         self.get_data()
   def ___d6(self):
      if self.button_dessert8[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(1,1)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(1,1)].text()))
         self.button_dessert8[(1,1)].setFocus()
         self.id_produit.setValue(118)
         self.get_data()
   def ___d7(self):
      if self.button_dessert8[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(1,2)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(1,2)].text()))
         self.button_dessert8[(1,2)].setFocus()
         self.id_produit.setValue(119)
         self.get_data()
   def ___d8(self):
      if self.button_dessert8[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(1,3)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(1,3)].text()))
         self.button_dessert8[(1,3)].setFocus()
         self.id_produit.setValue(120)
         self.get_data()
   def ___d9(self):
      if self.button_dessert8[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(2,0)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(2,0)].text()))
         self.button_dessert8[(2,0)].setFocus()
         self.id_produit.setValue(121)
         self.get_data()
   def ___d10(self):
      if self.button_dessert8[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(2,1)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(2,1)].text()))
         self.button_dessert8[(2,1)].setFocus()
         self.id_produit.setValue(122)
         self.get_data()
   def ___d11(self):
      if self.button_dessert8[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(2,2)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(2,2)].text()))
         self.button_dessert8[(2,2)].setFocus()
         self.id_produit.setValue(123)
         self.get_data()
   def ___d12(self):
      if self.button_dessert8[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(2,3)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(2,3)].text()))
         self.button_dessert8[(2,3)].setFocus()
         self.id_produit.setValue(124)
         self.get_data()
   def ___d13(self):
      if self.button_dessert8[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(3,0)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(3,0)].text()))
         self.button_dessert8[(3,0)].setFocus()
         self.id_produit.setValue(125)
         self.get_data()
   def ___d14(self):
      if self.button_dessert8[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(3,1)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(3,1)].text()))
         self.button_dessert8[(3,1)].setFocus()
         self.id_produit.setValue(126)
         self.get_data()
   def ___d15(self):
      if self.button_dessert8[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(3,2)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(3,2)].text()))
         self.button_dessert8[(3,2)].setFocus()
         self.id_produit.setValue(127)
         self.get_data()
   def ___d16(self):
      if self.button_dessert8[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_dessert8[(3,3)].icon()))
         self.btn_view.setText(str(self.button_dessert8[(3,3)].text()))
         self.button_dessert8[(3,3)].setFocus()
         self.id_produit.setValue(128)
         self.get_data()

   def cc1(self):
      if self.button_cafe1[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(0,0)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(0,0)].text()))
         self.button_cafe1[(0,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(1)
         self.get_data()
   def cc2(self):
      if self.button_cafe1[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(0,1)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(0,1)].text()))
         self.button_cafe1[(0,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(2)
         self.get_data()
   def cc3(self):
      if self.button_cafe1[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(0,2)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(0,2)].text()))
         self.button_cafe1[(0,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(3)
         self.get_data()
   def cc4(self):
      if self.button_cafe1[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(0,3)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(0,3)].text()))
         self.button_cafe1[(0,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(4)
         self.get_data()
   def cc5(self):
      if self.button_cafe1[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(1,0)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(1,0)].text()))
         self.button_cafe1[(1,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(5)
         self.get_data()
   def cc6(self):
      if self.button_cafe1[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(1,1)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(1,1)].text()))
         self.button_cafe1[(1,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(6)
         self.get_data()
   def cc7(self):
      if self.button_cafe1[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(1,2)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(1,2)].text()))
         self.button_cafe1[(1,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(7)
         self.get_data()
   def cc8(self):
      if self.button_cafe1[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(1,3)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(1,3)].text()))
         self.button_cafe1[(1,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(8)
         self.get_data()
   def cc9(self):
      if self.button_cafe1[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(2,0)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(2,0)].text()))
         self.button_cafe1[(2,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(9)
         self.get_data()
   def cc10(self):
      if self.button_cafe1[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(2,1)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(2,1)].text()))
         self.button_cafe1[(2,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(10)
         self.get_data()
   def cc11(self):
      if self.button_cafe1[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(2,2)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(2,2)].text()))
         self.button_cafe1[(2,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(11)
         self.get_data()
   def cc12(self):
      if self.button_cafe1[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(2,3)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(2,3)].text()))
         self.button_cafe1[(2,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(12)
         self.get_data()
   def cc13(self):
      if self.button_cafe1[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(3,0)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(3,0)].text()))
         self.button_cafe1[(3,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(13)
         self.get_data()
   def cc14(self):
      if self.button_cafe1[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(3,1)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(3,1)].text()))
         self.button_cafe1[(3,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(14)
         self.get_data()
   def cc15(self):
      if self.button_cafe1[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(3,2)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(3,2)].text()))
         self.button_cafe1[(3,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(15)
         self.get_data()
   def cc16(self):
      if self.button_cafe1[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe1[(3,3)].icon()))
         self.btn_view.setText(str(self.button_cafe1[(3,3)].text()))
         self.button_cafe1[(3,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(16)
         self.get_data()
   def _cc1(self):
      if self.button_cafe2[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(0,0)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(0,0)].text()))
         self.button_cafe2[(0,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(17)
         self.get_data()
   def _cc2(self):
      if self.button_cafe2[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(0,1)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(0,1)].text()))
         self.button_cafe2[(0,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(18)
         self.get_data()
   def _cc3(self):
      if self.button_cafe2[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(0,2)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(0,2)].text()))
         self.button_cafe2[(0,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(19)
         self.get_data()
   def _cc4(self):
      if self.button_cafe2[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(0,3)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(0,3)].text()))
         self.button_cafe2[(0,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(20)
         self.get_data()
   def _cc5(self):
      if self.button_cafe2[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(1,0)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(1,0)].text()))
         self.button_cafe2[(1,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(21)
         self.get_data()
   def _cc6(self):
      if self.button_cafe2[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(1,1)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(1,1)].text()))
         self.button_cafe2[(1,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(22)
         self.get_data()
   def _cc7(self):
      if self.button_cafe2[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(1,2)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(1,2)].text()))
         self.button_cafe2[(1,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(23)
         self.get_data()
   def _cc8(self):
      if self.button_cafe2[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(1,3)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(1,3)].text()))
         self.button_cafe2[(1,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(24)
         self.get_data()
   def _cc9(self):
      if self.button_cafe2[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(2,0)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(2,0)].text()))
         self.button_cafe2[(2,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(25)
         self.get_data()
   def _cc10(self):
      if self.button_cafe2[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(2,1)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(2,1)].text()))
         self.button_cafe2[(2,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(26)
         self.get_data()
   def _cc11(self):
      if self.button_cafe2[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(2,2)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(2,2)].text()))
         self.button_cafe2[(2,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(27)
         self.get_data()
   def _cc12(self):
      if self.button_cafe2[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(2,3)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(2,3)].text()))
         self.button_cafe2[(2,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(28)
         self.get_data()
   def _cc13(self):
      if self.button_cafe2[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(3,0)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(3,0)].text()))
         self.button_cafe2[(3,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(29)
         self.get_data()
   def _cc14(self):
      if self.button_cafe2[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(3,1)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(3,1)].text()))
         self.button_cafe2[(3,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(30)
         self.get_data()
   def _cc15(self):
      if self.button_cafe2[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(3,2)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(3,2)].text()))
         self.button_cafe2[(3,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(31)
         self.get_data()
   def _cc16(self):
      if self.button_cafe2[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe2[(3,3)].icon()))
         self.btn_view.setText(str(self.button_cafe2[(3,3)].text()))
         self.button_cafe2[(3,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(32)
         self.get_data()

   def __cc1(self):
      if self.button_cafe3[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(0,0)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(0,0)].text()))
         self.button_cafe3[(0,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(33)
         self.get_data()
   def __cc2(self):
      if self.button_cafe3[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(0,1)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(0,1)].text()))
         self.button_cafe3[(0,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(34)
         self.get_data()
   def __cc3(self):
      if self.button_cafe3[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(0,2)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(0,2)].text()))
         self.button_cafe3[(0,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(35)
         self.get_data()
   def __cc4(self):
      if self.button_cafe3[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(0,3)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(0,3)].text()))
         self.button_cafe3[(0,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(36)
         self.get_data()
   def __cc5(self):
      if self.button_cafe3[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(1,0)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(1,0)].text()))
         self.button_cafe3[(1,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(37)
         self.get_data()
   def __cc6(self):
      if self.button_cafe3[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(1,1)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(1,1)].text()))
         self.button_cafe3[(1,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(38)
         self.get_data()
   def __cc7(self):
      if self.button_cafe3[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(1,2)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(1,2)].text()))
         self.button_cafe3[(1,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(39)
         self.get_data()
   def __cc8(self):
      if self.button_cafe3[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(1,3)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(1,3)].text()))
         self.button_cafe3[(1,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(40)
         self.get_data()
   def __cc9(self):
      if self.button_cafe3[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(2,0)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(2,0)].text()))
         self.button_cafe3[(2,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(41)
         self.get_data()
   def __cc10(self):
      if self.button_cafe3[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(2,1)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(2,1)].text()))
         self.button_cafe3[(2,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(42)
         self.get_data()
   def __cc11(self):
      if self.button_cafe3[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(2,2)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(2,2)].text()))
         self.button_cafe3[(2,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(43)
         self.get_data()
   def __cc12(self):
      if self.button_cafe3[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(2,3)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(2,3)].text()))
         self.button_cafe3[(2,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(44)
         self.get_data()
   def __cc13(self):
      if self.button_cafe3[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(3,0)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(3,0)].text()))
         self.button_cafe3[(3,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(45)
         self.get_data()
   def __cc14(self):
      if self.button_cafe3[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(3,1)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(3,1)].text()))
         self.button_cafe3[(3,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(46)
         self.get_data()
   def __cc15(self):
      if self.button_cafe3[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(3,2)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(3,2)].text()))
         self.button_cafe3[(3,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(47)
         self.get_data()
   def __cc16(self):
      if self.button_cafe3[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe3[(3,3)].icon()))
         self.btn_view.setText(str(self.button_cafe3[(3,3)].text()))
         self.button_cafe3[(3,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(48)
         self.get_data()
   def ___cc1(self):
      if self.button_cafe4[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(0,0)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(0,0)].text()))
         self.button_cafe4[(0,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(49)
         self.get_data()
   def ___cc2(self):
      if self.button_cafe4[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(0,1)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(0,1)].text()))
         self.button_cafe4[(0,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(50)
         self.get_data()
   def ___cc3(self):
      if self.button_cafe4[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(0,2)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(0,2)].text()))
         self.button_cafe4[(0,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(51)
         self.get_data()
   def ___cc4(self):
      if self.button_cafe4[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(0,3)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(0,3)].text()))
         self.button_cafe4[(0,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(52)
         self.get_data()
   def ___cc5(self):
      if self.button_cafe4[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(1,0)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(1,0)].text()))
         self.button_cafe4[(1,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(53)
         self.get_data()
   def ___cc6(self):
      if self.button_cafe4[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(1,1)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(1,1)].text()))
         self.button_cafe4[(1,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(54)
         self.get_data()
   def ___cc7(self):
      if self.button_cafe4[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(1,2)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(1,2)].text()))
         self.button_cafe4[(1,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(55)
         self.get_data()
   def ___cc8(self):
      if self.button_cafe4[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(1,3)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(1,3)].text()))
         self.button_cafe4[(1,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(56)
         self.get_data()
   def ___cc9(self):
      if self.button_cafe4[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(2,0)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(2,0)].text()))
         self.button_cafe4[(2,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(57)
         self.get_data()
   def ___cc10(self):
      if self.button_cafe4[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(2,1)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(2,1)].text()))
         self.button_cafe4[(2,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(58)
         self.get_data()
   def ___cc11(self):
      if self.button_cafe4[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(2,2)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(2,2)].text()))
         self.button_cafe4[(2,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(59)
         self.get_data()
   def ___cc12(self):
      if self.button_cafe4[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(2,3)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(2,3)].text()))
         self.button_cafe4[(2,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(60)
         self.get_data()
   def ___cc13(self):
      if self.button_cafe4[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(3,0)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(3,0)].text()))
         self.button_cafe4[(3,0)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(61)
         self.get_data()
   def ___cc14(self):
      if self.button_cafe4[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(3,1)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(3,1)].text()))
         self.button_cafe4[(3,1)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(62)
         self.get_data()
   def ___cc15(self):
      if self.button_cafe4[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(3,2)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(3,2)].text()))
         self.button_cafe4[(3,2)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(63)
         self.get_data()
   def ___cc16(self):
      if self.button_cafe4[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe4[(3,3)].icon()))
         self.btn_view.setText(str(self.button_cafe4[(3,3)].text()))
         self.button_cafe4[(3,3)].setFocus()
         self.dash_main_frame.show();self.id_produit.setValue(64)
         self.get_data()

   #++++++++++++++++++++++++++++++++++++++  PAGE PANIER 5 A 8

   def c1(self):
      if self.button_cafe5[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(0,0)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(0,0)].text()))
         self.button_cafe5[(0,0)].setFocus()
         self.id_produit.setValue(65)
         self.get_data()
   def c2(self):
      if self.button_cafe5[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(0,1)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(0,1)].text()))
         self.button_cafe5[(0,1)].setFocus()
         self.id_produit.setValue(66)
         self.get_data()
   def c3(self):
      if self.button_cafe5[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(0,2)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(0,2)].text()))
         self.button_cafe5[(0,2)].setFocus()
         self.id_produit.setValue(67)
         self.get_data()
   def c4(self):
      if self.button_cafe5[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(0,3)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(0,3)].text()))
         self.button_cafe5[(0,3)].setFocus()
         self.id_produit.setValue(68)
         self.get_data()
   def c5(self):
      if self.button_cafe5[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(1,0)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(1,0)].text()))
         self.button_cafe5[(1,0)].setFocus()
         self.id_produit.setValue(69)
         self.get_data()
   def c6(self):
      if self.button_cafe5[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(1,1)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(1,1)].text()))
         self.button_cafe5[(1,1)].setFocus()
         self.id_produit.setValue(70)
         self.get_data()
   def c7(self):
      if self.button_cafe5[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(1,2)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(1,2)].text()))
         self.button_cafe5[(1,2)].setFocus()
         self.id_produit.setValue(71)
         self.get_data()
   def c8(self):
      if self.button_cafe5[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(1,3)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(1,3)].text()))
         self.button_cafe5[(1,3)].setFocus()
         self.id_produit.setValue(72)
         self.get_data()
   def c9(self):
      if self.button_cafe5[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(2,0)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(2,0)].text()))
         self.button_cafe5[(2,0)].setFocus()
         self.id_produit.setValue(73)
         self.get_data()
   def c10(self):
      if self.button_cafe5[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(2,1)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(2,1)].text()))
         self.button_cafe5[(2,1)].setFocus()
         self.id_produit.setValue(74)
         self.get_data()
   def c11(self):
      if self.button_cafe5[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(2,2)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(2,2)].text()))
         self.button_cafe5[(2,2)].setFocus()
         self.id_produit.setValue(75)
         self.get_data()
   def c12(self):
      if self.button_cafe5[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(2,3)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(2,3)].text()))
         self.button_cafe5[(2,3)].setFocus()
         self.id_produit.setValue(76)
         self.get_data()
   def c13(self):
      if self.button_cafe5[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(3,0)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(3,0)].text()))
         self.button_cafe5[(3,0)].setFocus()
         self.id_produit.setValue(77)
         self.get_data()
   def c14(self):
      if self.button_cafe5[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(3,1)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(3,1)].text()))
         self.button_cafe5[(3,1)].setFocus()
         self.id_produit.setValue(78)
         self.get_data()
   def c15(self):
      if self.button_cafe5[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(3,2)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(3,2)].text()))
         self.button_cafe5[(3,2)].setFocus()
         self.id_produit.setValue(79)
         self.get_data()
   def c16(self):
      if self.button_cafe5[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe5[(3,3)].icon()))
         self.btn_view.setText(str(self.button_cafe5[(3,3)].text()))
         self.button_cafe5[(3,3)].setFocus()
         self.id_produit.setValue(80)
         self.get_data()
   def _c1(self):
      if self.button_cafe6[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(0,0)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(0,0)].text()))
         self.button_cafe6[(0,0)].setFocus()
         self.id_produit.setValue(81)
         self.get_data()
   def _c2(self):
      if self.button_cafe6[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(0,1)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(0,1)].text()))
         self.button_cafe6[(0,1)].setFocus()
         self.id_produit.setValue(82)
         self.get_data()
   def _c3(self):
      if self.button_cafe6[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(0,2)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(0,2)].text()))
         self.button_cafe6[(0,2)].setFocus()
         self.id_produit.setValue(83)
         self.get_data()
   def _c4(self):
      if self.button_cafe6[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(0,3)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(0,3)].text()))
         self.button_cafe6[(0,3)].setFocus()
         self.id_produit.setValue(84)
         self.get_data()
   def _c5(self):
      if self.button_cafe6[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(1,0)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(1,0)].text()))
         self.button_cafe6[(1,0)].setFocus()
         self.id_produit.setValue(85)
         self.get_data()
   def _c6(self):
      if self.button_cafe6[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(1,1)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(1,1)].text()))
         self.button_cafe6[(1,1)].setFocus()
         self.id_produit.setValue(86)
         self.get_data()
   def _c7(self):
      if self.button_cafe6[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(1,2)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(1,2)].text()))
         self.button_cafe6[(1,2)].setFocus()
         self.id_produit.setValue(87)
         self.get_data()
   def _c8(self):
      if self.button_cafe6[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(1,3)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(1,3)].text()))
         self.button_cafe6[(1,3)].setFocus()
         self.id_produit.setValue(88)
         self.get_data()
   def _c9(self):
      if self.button_cafe6[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(2,0)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(2,0)].text()))
         self.button_cafe6[(2,0)].setFocus()
         self.id_produit.setValue(89)
         self.get_data()
   def _c10(self):
      if self.button_cafe6[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(2,1)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(2,1)].text()))
         self.button_cafe6[(2,1)].setFocus()
         self.id_produit.setValue(90)
         self.get_data()
   def _c11(self):
      if self.button_cafe6[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(2,2)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(2,2)].text()))
         self.button_cafe6[(2,2)].setFocus()
         self.id_produit.setValue(91)
         self.get_data()
   def _c12(self):
      if self.button_cafe6[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(2,3)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(2,3)].text()))
         self.button_cafe6[(2,3)].setFocus()
         self.id_produit.setValue(92)
         self.get_data()
   def _c13(self):
      if self.button_cafe6[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(3,0)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(3,0)].text()))
         self.button_cafe6[(3,0)].setFocus()
         self.id_produit.setValue(93)
         self.get_data()
   def _c14(self):
      if self.button_cafe6[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(3,1)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(3,1)].text()))
         self.button_cafe6[(3,1)].setFocus()
         self.id_produit.setValue(94)
         self.get_data()
   def _c15(self):
      if self.button_cafe6[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(3,2)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(3,2)].text()))
         self.button_cafe6[(3,2)].setFocus()
         self.id_produit.setValue(95)
         self.get_data()
   def _c16(self):
      if self.button_cafe6[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe6[(3,3)].icon()))
         self.btn_view.setText(str(self.button_cafe6[(3,3)].text()))
         self.button_cafe6[(3,3)].setFocus()
         self.id_produit.setValue(96)
         self.get_data()

   def __c1(self):
      if self.button_cafe7[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(0,0)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(0,0)].text()))
         self.button_cafe7[(0,0)].setFocus()
         self.id_produit.setValue(97)
         self.get_data()
   def __c2(self):
      if self.button_cafe7[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(0,1)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(0,1)].text()))
         self.button_cafe7[(0,1)].setFocus()
         self.id_produit.setValue(98)
         self.get_data()
   def __c3(self):
      if self.button_cafe7[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(0,2)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(0,2)].text()))
         self.button_cafe7[(0,2)].setFocus()
         self.id_produit.setValue(99)
         self.get_data()
   def __c4(self):
      if self.button_cafe7[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(0,3)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(0,3)].text()))
         self.button_cafe7[(0,3)].setFocus()
         self.id_produit.setValue(100)
         self.get_data()
   def __c5(self):
      if self.button_cafe7[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(1,0)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(1,0)].text()))
         self.button_cafe7[(1,0)].setFocus()
         self.id_produit.setValue(101)
         self.get_data()
   def __c6(self):
      if self.button_cafe7[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(1,1)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(1,1)].text()))
         self.button_cafe7[(1,1)].setFocus()
         self.id_produit.setValue(102)
         self.get_data()
   def __c7(self):
      if self.button_cafe7[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(1,2)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(1,2)].text()))
         self.button_cafe7[(1,2)].setFocus()
         self.id_produit.setValue(103)
         self.get_data()
   def __c8(self):
      if self.button_cafe7[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(1,3)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(1,3)].text()))
         self.button_cafe7[(1,3)].setFocus()
         self.id_produit.setValue(104)
         self.get_data()
   def __c9(self):
      if self.button_cafe7[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(2,0)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(2,0)].text()))
         self.button_cafe7[(2,0)].setFocus()
         self.id_produit.setValue(105)
         self.get_data()
   def __c10(self):
      if self.button_cafe7[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(2,1)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(2,1)].text()))
         self.button_cafe7[(2,1)].setFocus()
         self.id_produit.setValue(106)
         self.get_data()
   def __c11(self):
      if self.button_cafe7[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(2,2)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(2,2)].text()))
         self.button_cafe7[(2,2)].setFocus()
         self.id_produit.setValue(107)
         self.get_data()
   def __c12(self):
      if self.button_cafe7[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(2,3)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(2,3)].text()))
         self.button_cafe7[(2,3)].setFocus()
         self.id_produit.setValue(108)
         self.get_data()
   def __c13(self):
      if self.button_cafe7[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(3,0)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(3,0)].text()))
         self.button_cafe7[(3,0)].setFocus()
         self.id_produit.setValue(109)
         self.get_data()
   def __c14(self):
      if self.button_cafe7[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(3,1)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(3,1)].text()))
         self.button_cafe7[(3,1)].setFocus()
         self.id_produit.setValue(110)
         self.get_data()
   def __c15(self):
      if self.button_cafe7[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(3,2)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(3,2)].text()))
         self.button_cafe7[(3,2)].setFocus()
         self.id_produit.setValue(111)
         self.get_data()
   def __c16(self):
      if self.button_cafe7[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe7[(3,3)].icon()))
         self.btn_view.setText(str(self.button_cafe7[(3,3)].text()))
         self.button_cafe7[(3,3)].setFocus()
         self.id_produit.setValue(112)
         self.get_data()
   def ___c1(self):
      if self.button_cafe8[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(0,0)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(0,0)].text()))
         self.button_cafe8[(0,0)].setFocus()
         self.id_produit.setValue(113)
         self.get_data()
   def ___c2(self):
      if self.button_cafe8[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(0,1)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(0,1)].text()))
         self.button_cafe8[(0,1)].setFocus()
         self.id_produit.setValue(114)
         self.get_data()
   def ___c3(self):
      if self.button_cafe8[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(0,2)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(0,2)].text()))
         self.button_cafe8[(0,2)].setFocus()
         self.id_produit.setValue(115)
         self.get_data()
   def ___c4(self):
      if self.button_cafe8[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(0,3)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(0,3)].text()))
         self.button_cafe8[(0,3)].setFocus()
         self.id_produit.setValue(116)
         self.get_data()
   def ___c5(self):
      if self.button_cafe8[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(1,0)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(1,0)].text()))
         self.button_cafe8[(1,0)].setFocus()
         self.id_produit.setValue(117)
         self.get_data()
   def ___c6(self):
      if self.button_cafe8[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(1,1)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(1,1)].text()))
         self.button_cafe8[(1,1)].setFocus()
         self.id_produit.setValue(118)
         self.get_data()
   def ___c7(self):
      if self.button_cafe8[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(1,2)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(1,2)].text()))
         self.button_cafe8[(1,2)].setFocus()
         self.id_produit.setValue(119)
         self.get_data()
   def ___c8(self):
      if self.button_cafe8[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(1,3)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(1,3)].text()))
         self.button_cafe8[(1,3)].setFocus()
         self.id_produit.setValue(120)
         self.get_data()
   def ___c9(self):
      if self.button_cafe8[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(2,0)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(2,0)].text()))
         self.button_cafe8[(2,0)].setFocus()
         self.id_produit.setValue(121)
         self.get_data()
   def ___c10(self):
      if self.button_cafe8[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(2,1)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(2,1)].text()))
         self.button_cafe8[(2,1)].setFocus()
         self.id_produit.setValue(122)
         self.get_data()
   def ___c11(self):
      if self.button_cafe8[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(2,2)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(2,2)].text()))
         self.button_cafe8[(2,2)].setFocus()
         self.id_produit.setValue(123)
         self.get_data()
   def ___c12(self):
      if self.button_cafe8[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(2,3)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(2,3)].text()))
         self.button_cafe8[(2,3)].setFocus()
         self.id_produit.setValue(124)
         self.get_data()
   def ___c13(self):
      if self.button_cafe8[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(3,0)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(3,0)].text()))
         self.button_cafe8[(3,0)].setFocus()
         self.id_produit.setValue(125)
         self.get_data()
   def ___c14(self):
      if self.button_cafe8[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(3,1)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(3,1)].text()))
         self.button_cafe8[(3,1)].setFocus()
         self.id_produit.setValue(126)
         self.get_data()
   def ___c15(self):
      if self.button_cafe8[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(3,2)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(3,2)].text()))
         self.button_cafe8[(3,2)].setFocus()
         self.id_produit.setValue(127)
         self.get_data()
   def ___c16(self):
      if self.button_cafe8[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_cafe8[(3,3)].icon()))
         self.btn_view.setText(str(self.button_cafe8[(3,3)].text()))
         self.button_cafe8[(3,3)].setFocus()
         self.id_produit.setValue(128)
         self.get_data()

   def pp1(self):
      if self.button_plat1[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(0,0)].icon()))
         self.btn_view.setText(str(self.button_plat1[(0,0)].text()))
         self.button_plat1[(0,0)].setFocus()
         self.id_produit.setValue(1)
         self.get_data()
   def pp2(self):
      if self.button_plat1[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(0,1)].icon()))
         self.btn_view.setText(str(self.button_plat1[(0,1)].text()))
         self.button_plat1[(0,1)].setFocus()
         self.id_produit.setValue(2)
         self.get_data()
   def pp3(self):
      if self.button_plat1[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(0,2)].icon()))
         self.btn_view.setText(str(self.button_plat1[(0,2)].text()))
         self.button_plat1[(0,2)].setFocus()
         self.id_produit.setValue(3)
         self.get_data()
   def pp4(self):
      if self.button_plat1[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(0,3)].icon()))
         self.btn_view.setText(str(self.button_plat1[(0,3)].text()))
         self.button_plat1[(0,3)].setFocus()
         self.id_produit.setValue(4)
         self.get_data()
   def pp5(self):
      if self.button_plat1[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(1,0)].icon()))
         self.btn_view.setText(str(self.button_plat1[(1,0)].text()))
         self.button_plat1[(1,0)].setFocus()
         self.id_produit.setValue(5)
         self.get_data()
   def pp6(self):
      if self.button_plat1[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(1,1)].icon()))
         self.btn_view.setText(str(self.button_plat1[(1,1)].text()))
         self.button_plat1[(1,1)].setFocus()
         self.id_produit.setValue(6)
         self.get_data()
   def pp7(self):
      if self.button_plat1[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(1,2)].icon()))
         self.btn_view.setText(str(self.button_plat1[(1,2)].text()))
         self.button_plat1[(1,2)].setFocus()
         self.id_produit.setValue(7)
         self.get_data()
   def pp8(self):
      if self.button_plat1[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(1,3)].icon()))
         self.btn_view.setText(str(self.button_plat1[(1,3)].text()))
         self.button_plat1[(1,3)].setFocus()
         self.id_produit.setValue(8)
         self.get_data()
   def pp9(self):
      if self.button_plat1[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(2,0)].icon()))
         self.btn_view.setText(str(self.button_plat1[(2,0)].text()))
         self.button_plat1[(2,0)].setFocus()
         self.id_produit.setValue(9)
         self.get_data()
   def pp10(self):
      if self.button_plat1[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(2,1)].icon()))
         self.btn_view.setText(str(self.button_plat1[(2,1)].text()))
         self.button_plat1[(2,1)].setFocus()
         self.id_produit.setValue(10)
         self.get_data()
   def pp11(self):
      if self.button_plat1[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(2,2)].icon()))
         self.btn_view.setText(str(self.button_plat1[(2,2)].text()))
         self.button_plat1[(2,2)].setFocus()
         self.id_produit.setValue(11)
         self.get_data()
   def pp12(self):
      if self.button_plat1[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(2,3)].icon()))
         self.btn_view.setText(str(self.button_plat1[(2,3)].text()))
         self.button_plat1[(2,3)].setFocus()
         self.id_produit.setValue(12)
         self.get_data()
   def pp13(self):
      if self.button_plat1[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(3,0)].icon()))
         self.btn_view.setText(str(self.button_plat1[(3,0)].text()))
         self.button_plat1[(3,0)].setFocus()
         self.id_produit.setValue(13)
         self.get_data()
   def pp14(self):
      if self.button_plat1[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(3,1)].icon()))
         self.btn_view.setText(str(self.button_plat1[(3,1)].text()))
         self.button_plat1[(3,1)].setFocus()
         self.id_produit.setValue(14)
         self.get_data()
   def pp15(self):
      if self.button_plat1[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(3,2)].icon()))
         self.btn_view.setText(str(self.button_plat1[(3,2)].text()))
         self.button_plat1[(3,2)].setFocus()
         self.id_produit.setValue(15)
         self.get_data()
   def pp16(self):
      if self.button_plat1[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat1[(3,3)].icon()))
         self.btn_view.setText(str(self.button_plat1[(3,3)].text()))
         self.button_plat1[(3,3)].setFocus()
         self.id_produit.setValue(16)
         self.get_data()
   def _pp1(self):
      if self.button_plat2[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(0,0)].icon()))
         self.btn_view.setText(str(self.button_plat2[(0,0)].text()))
         self.button_plat2[(0,0)].setFocus()
         self.id_produit.setValue(17)
         self.get_data()
   def _pp2(self):
      if self.button_plat2[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(0,1)].icon()))
         self.btn_view.setText(str(self.button_plat2[(0,1)].text()))
         self.button_plat2[(0,1)].setFocus()
         self.id_produit.setValue(18)
         self.get_data()
   def _pp3(self):
      if self.button_plat2[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(0,2)].icon()))
         self.btn_view.setText(str(self.button_plat2[(0,2)].text()))
         self.button_plat2[(0,2)].setFocus()
         self.id_produit.setValue(19)
         self.get_data()
   def _pp4(self):
      if self.button_plat2[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(0,3)].icon()))
         self.btn_view.setText(str(self.button_plat2[(0,3)].text()))
         self.button_plat2[(0,3)].setFocus()
         self.id_produit.setValue(20)
         self.get_data()
   def _pp5(self):
      if self.button_plat2[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(1,0)].icon()))
         self.btn_view.setText(str(self.button_plat2[(1,0)].text()))
         self.button_plat2[(1,0)].setFocus()
         self.id_produit.setValue(21)
         self.get_data()
   def _pp6(self):
      if self.button_plat2[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(1,1)].icon()))
         self.btn_view.setText(str(self.button_plat2[(1,1)].text()))
         self.button_plat2[(1,1)].setFocus()
         self.id_produit.setValue(22)
         self.get_data()
   def _pp7(self):
      if self.button_plat2[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(1,2)].icon()))
         self.btn_view.setText(str(self.button_plat2[(1,2)].text()))
         self.button_plat2[(1,2)].setFocus()
         self.id_produit.setValue(23)
         self.get_data()
   def _pp8(self):
      if self.button_plat2[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(1,3)].icon()))
         self.btn_view.setText(str(self.button_plat2[(1,3)].text()))
         self.button_plat2[(1,3)].setFocus()
         self.id_produit.setValue(24)
         self.get_data()
   def _pp9(self):
      if self.button_plat2[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(2,0)].icon()))
         self.btn_view.setText(str(self.button_plat2[(2,0)].text()))
         self.button_plat2[(2,0)].setFocus()
         self.id_produit.setValue(25)
         self.get_data()
   def _pp10(self):
      if self.button_plat2[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(2,1)].icon()))
         self.btn_view.setText(str(self.button_plat2[(2,1)].text()))
         self.button_plat2[(2,1)].setFocus()
         self.id_produit.setValue(26)
         self.get_data()
   def _pp11(self):
      if self.button_plat2[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(2,2)].icon()))
         self.btn_view.setText(str(self.button_plat2[(2,2)].text()))
         self.button_plat2[(2,2)].setFocus()
         self.id_produit.setValue(27)
         self.get_data()
   def _pp12(self):
      if self.button_plat2[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(2,3)].icon()))
         self.btn_view.setText(str(self.button_plat2[(2,3)].text()))
         self.button_plat2[(2,3)].setFocus()
         self.id_produit.setValue(28)
         self.get_data()
   def _pp13(self):
      if self.button_plat2[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(3,0)].icon()))
         self.btn_view.setText(str(self.button_plat2[(3,0)].text()))
         self.button_plat2[(3,0)].setFocus()
         self.id_produit.setValue(29)
         self.get_data()
   def _pp14(self):
      if self.button_plat2[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(3,1)].icon()))
         self.btn_view.setText(str(self.button_plat2[(3,1)].text()))
         self.button_plat2[(3,1)].setFocus()
         self.id_produit.setValue(30)
         self.get_data()
   def _pp15(self):
      if self.button_plat2[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(3,2)].icon()))
         self.btn_view.setText(str(self.button_plat2[(3,2)].text()))
         self.button_plat2[(3,2)].setFocus()
         self.id_produit.setValue(31)
         self.get_data()
   def _pp16(self):
      if self.button_plat2[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat2[(3,3)].icon()))
         self.btn_view.setText(str(self.button_plat2[(3,3)].text()))
         self.button_plat2[(3,3)].setFocus()
         self.id_produit.setValue(32)
         self.get_data()

   def __pp1(self):
      if self.button_plat3[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(0,0)].icon()))
         self.btn_view.setText(str(self.button_plat3[(0,0)].text()))
         self.button_plat3[(0,0)].setFocus()
         self.id_produit.setValue(33)
         self.get_data()
   def __pp2(self):
      if self.button_plat3[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(0,1)].icon()))
         self.btn_view.setText(str(self.button_plat3[(0,1)].text()))
         self.button_plat3[(0,1)].setFocus()
         self.id_produit.setValue(34)
         self.get_data()
   def __pp3(self):
      if self.button_plat3[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(0,2)].icon()))
         self.btn_view.setText(str(self.button_plat3[(0,2)].text()))
         self.button_plat3[(0,2)].setFocus()
         self.id_produit.setValue(35)
         self.get_data()
   def __pp4(self):
      if self.button_plat3[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(0,3)].icon()))
         self.btn_view.setText(str(self.button_plat3[(0,3)].text()))
         self.button_plat3[(0,3)].setFocus()
         self.id_produit.setValue(36)
         self.get_data()
   def __pp5(self):
      if self.button_plat3[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(1,0)].icon()))
         self.btn_view.setText(str(self.button_plat3[(1,0)].text()))
         self.button_plat3[(1,0)].setFocus()
         self.id_produit.setValue(37)
         self.get_data()
   def __pp6(self):
      if self.button_plat3[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(1,1)].icon()))
         self.btn_view.setText(str(self.button_plat3[(1,1)].text()))
         self.button_plat3[(1,1)].setFocus()
         self.id_produit.setValue(38)
         self.get_data()
   def __pp7(self):
      if self.button_plat3[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(1,2)].icon()))
         self.btn_view.setText(str(self.button_plat3[(1,2)].text()))
         self.button_plat3[(1,2)].setFocus()
         self.id_produit.setValue(39)
         self.get_data()
   def __pp8(self):
      if self.button_plat3[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(1,3)].icon()))
         self.btn_view.setText(str(self.button_plat3[(1,3)].text()))
         self.button_plat3[(1,3)].setFocus()
         self.id_produit.setValue(40)
         self.get_data()
   def __pp9(self):
      if self.button_plat3[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(2,0)].icon()))
         self.btn_view.setText(str(self.button_plat3[(2,0)].text()))
         self.button_plat3[(2,0)].setFocus()
         self.id_produit.setValue(41)
         self.get_data()
   def __pp10(self):
      if self.button_plat3[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(2,1)].icon()))
         self.btn_view.setText(str(self.button_plat3[(2,1)].text()))
         self.button_plat3[(2,1)].setFocus()
         self.id_produit.setValue(42)
         self.get_data()
   def __pp11(self):
      if self.button_plat3[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(2,2)].icon()))
         self.btn_view.setText(str(self.button_plat3[(2,2)].text()))
         self.button_plat3[(2,2)].setFocus()
         self.id_produit.setValue(43)
         self.get_data()
   def __pp12(self):
      if self.button_plat3[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(2,3)].icon()))
         self.btn_view.setText(str(self.button_plat3[(2,3)].text()))
         self.button_plat3[(2,3)].setFocus()
         self.id_produit.setValue(44)
         self.get_data()
   def __pp13(self):
      if self.button_plat3[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(3,0)].icon()))
         self.btn_view.setText(str(self.button_plat3[(3,0)].text()))
         self.button_plat3[(3,0)].setFocus()
         self.id_produit.setValue(45)
         self.get_data()
   def __pp14(self):
      if self.button_plat3[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(3,1)].icon()))
         self.btn_view.setText(str(self.button_plat3[(3,1)].text()))
         self.button_plat3[(3,1)].setFocus()
         self.id_produit.setValue(46)
         self.get_data()
   def __pp15(self):
      if self.button_plat3[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(3,2)].icon()))
         self.btn_view.setText(str(self.button_plat3[(3,2)].text()))
         self.button_plat3[(3,2)].setFocus()
         self.id_produit.setValue(47)
         self.get_data()
   def __pp16(self):
      if self.button_plat3[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat3[(3,3)].icon()))
         self.btn_view.setText(str(self.button_plat3[(3,3)].text()))
         self.button_plat3[(3,3)].setFocus()
         self.id_produit.setValue(48)
         self.get_data()
   def ___pp1(self):
      if self.button_plat4[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(0,0)].icon()))
         self.btn_view.setText(str(self.button_plat4[(0,0)].text()))
         self.button_plat4[(0,0)].setFocus()
         self.id_produit.setValue(49)
         self.get_data()
   def ___pp2(self):
      if self.button_plat4[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(0,1)].icon()))
         self.btn_view.setText(str(self.button_plat4[(0,1)].text()))
         self.button_plat4[(0,1)].setFocus()
         self.id_produit.setValue(50)
         self.get_data()
   def ___pp3(self):
      if self.button_plat4[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(0,2)].icon()))
         self.btn_view.setText(str(self.button_plat4[(0,2)].text()))
         self.button_plat4[(0,2)].setFocus()
         self.id_produit.setValue(51)
         self.get_data()
   def ___pp4(self):
      if self.button_plat4[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(0,3)].icon()))
         self.btn_view.setText(str(self.button_plat4[(0,3)].text()))
         self.button_plat4[(0,3)].setFocus()
         self.id_produit.setValue(52)
         self.get_data()
   def ___pp5(self):
      if self.button_plat4[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(1,0)].icon()))
         self.btn_view.setText(str(self.button_plat4[(1,0)].text()))
         self.button_plat4[(1,0)].setFocus()
         self.id_produit.setValue(53)
         self.get_data()
   def ___pp6(self):
      if self.button_plat4[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(1,1)].icon()))
         self.btn_view.setText(str(self.button_plat4[(1,1)].text()))
         self.button_plat4[(1,1)].setFocus()
         self.id_produit.setValue(54)
         self.get_data()
   def ___pp7(self):
      if self.button_plat4[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(1,2)].icon()))
         self.btn_view.setText(str(self.button_plat4[(1,2)].text()))
         self.button_plat4[(1,2)].setFocus()
         self.id_produit.setValue(55)
         self.get_data()
   def ___pp8(self):
      if self.button_plat4[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(1,3)].icon()))
         self.btn_view.setText(str(self.button_plat4[(1,3)].text()))
         self.button_plat4[(1,3)].setFocus()
         self.id_produit.setValue(56)
         self.get_data()
   def ___pp9(self):
      if self.button_plat4[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(2,0)].icon()))
         self.btn_view.setText(str(self.button_plat4[(2,0)].text()))
         self.button_plat4[(2,0)].setFocus()
         self.id_produit.setValue(57)
         self.get_data()
   def ___pp10(self):
      if self.button_plat4[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(2,1)].icon()))
         self.btn_view.setText(str(self.button_plat4[(2,1)].text()))
         self.button_plat4[(2,1)].setFocus()
         self.id_produit.setValue(58)
         self.get_data()
   def ___pp11(self):
      if self.button_plat4[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(2,2)].icon()))
         self.btn_view.setText(str(self.button_plat4[(2,2)].text()))
         self.button_plat4[(2,2)].setFocus()
         self.id_produit.setValue(59)
         self.get_data()
   def ___pp12(self):
      if self.button_plat4[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(2,3)].icon()))
         self.btn_view.setText(str(self.button_plat4[(2,3)].text()))
         self.button_plat4[(2,3)].setFocus()
         self.id_produit.setValue(60)
         self.get_data()
   def ___pp13(self):
      if self.button_plat4[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(3,0)].icon()))
         self.btn_view.setText(str(self.button_plat4[(3,0)].text()))
         self.button_plat4[(3,0)].setFocus()
         self.id_produit.setValue(61)
         self.get_data()
   def ___pp14(self):
      if self.button_plat4[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(3,1)].icon()))
         self.btn_view.setText(str(self.button_plat4[(3,1)].text()))
         self.button_plat4[(3,1)].setFocus()
         self.id_produit.setValue(62)
         self.get_data()
   def ___pp15(self):
      if self.button_plat4[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(3,2)].icon()))
         self.btn_view.setText(str(self.button_plat4[(3,2)].text()))
         self.button_plat4[(3,2)].setFocus()
         self.id_produit.setValue(63)
         self.get_data()
   def ___pp16(self):
      if self.button_plat4[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat4[(3,3)].icon()))
         self.btn_view.setText(str(self.button_plat4[(3,3)].text()))
         self.button_plat4[(3,3)].setFocus()
         self.id_produit.setValue(64)
         self.get_data()

   #++++++++++++++++++++++++++++++++++++++  PAGE PANIER 5 A 8

   def p1(self):
      if self.button_plat5[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(0,0)].icon()))
         self.btn_view.setText(str(self.button_plat5[(0,0)].text()))
         self.button_plat5[(0,0)].setFocus()
         self.id_produit.setValue(65)
         self.get_data()
   def p2(self):
      if self.button_plat5[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(0,1)].icon()))
         self.btn_view.setText(str(self.button_plat5[(0,1)].text()))
         self.button_plat5[(0,1)].setFocus()
         self.id_produit.setValue(66)
         self.get_data()
   def p3(self):
      if self.button_plat5[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(0,2)].icon()))
         self.btn_view.setText(str(self.button_plat5[(0,2)].text()))
         self.button_plat5[(0,2)].setFocus()
         self.id_produit.setValue(67)
         self.get_data()
   def p4(self):
      if self.button_plat5[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(0,3)].icon()))
         self.btn_view.setText(str(self.button_plat5[(0,3)].text()))
         self.button_plat5[(0,3)].setFocus()
         self.id_produit.setValue(68)
         self.get_data()
   def p5(self):
      if self.button_plat5[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(1,0)].icon()))
         self.btn_view.setText(str(self.button_plat5[(1,0)].text()))
         self.button_plat5[(1,0)].setFocus()
         self.id_produit.setValue(69)
         self.get_data()
   def p6(self):
      if self.button_plat5[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(1,1)].icon()))
         self.btn_view.setText(str(self.button_plat5[(1,1)].text()))
         self.button_plat5[(1,1)].setFocus()
         self.id_produit.setValue(70)
         self.get_data()
   def p7(self):
      if self.button_plat5[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(1,2)].icon()))
         self.btn_view.setText(str(self.button_plat5[(1,2)].text()))
         self.button_plat5[(1,2)].setFocus()
         self.id_produit.setValue(71)
         self.get_data()
   def p8(self):
      if self.button_plat5[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(1,3)].icon()))
         self.btn_view.setText(str(self.button_plat5[(1,3)].text()))
         self.button_plat5[(1,3)].setFocus()
         self.id_produit.setValue(72)
         self.get_data()
   def p9(self):
      if self.button_plat5[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(2,0)].icon()))
         self.btn_view.setText(str(self.button_plat5[(2,0)].text()))
         self.button_plat5[(2,0)].setFocus()
         self.id_produit.setValue(73)
         self.get_data()
   def p10(self):
      if self.button_plat5[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(2,1)].icon()))
         self.btn_view.setText(str(self.button_plat5[(2,1)].text()))
         self.button_plat5[(2,1)].setFocus()
         self.id_produit.setValue(74)
         self.get_data()
   def p11(self):
      if self.button_plat5[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(2,2)].icon()))
         self.btn_view.setText(str(self.button_plat5[(2,2)].text()))
         self.button_plat5[(2,2)].setFocus()
         self.id_produit.setValue(75)
         self.get_data()
   def p12(self):
      if self.button_plat5[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(2,3)].icon()))
         self.btn_view.setText(str(self.button_plat5[(2,3)].text()))
         self.button_plat5[(2,3)].setFocus()
         self.id_produit.setValue(76)
         self.get_data()
   def p13(self):
      if self.button_plat5[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(3,0)].icon()))
         self.btn_view.setText(str(self.button_plat5[(3,0)].text()))
         self.button_plat5[(3,0)].setFocus()
         self.id_produit.setValue(77)
         self.get_data()
   def p14(self):
      if self.button_plat5[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(3,1)].icon()))
         self.btn_view.setText(str(self.button_plat5[(3,1)].text()))
         self.button_plat5[(3,1)].setFocus()
         self.id_produit.setValue(78)
         self.get_data()
   def p15(self):
      if self.button_plat5[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(3,2)].icon()))
         self.btn_view.setText(str(self.button_plat5[(3,2)].text()))
         self.button_plat5[(3,2)].setFocus()
         self.id_produit.setValue(79)
         self.get_data()
   def p16(self):
      if self.button_plat5[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat5[(3,3)].icon()))
         self.btn_view.setText(str(self.button_plat5[(3,3)].text()))
         self.button_plat5[(3,3)].setFocus()
         self.id_produit.setValue(80)
         self.get_data()
   def _p1(self):
      if self.button_plat6[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(0,0)].icon()))
         self.btn_view.setText(str(self.button_plat6[(0,0)].text()))
         self.button_plat6[(0,0)].setFocus()
         self.id_produit.setValue(81)
         self.get_data()
   def _p2(self):
      if self.button_plat6[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(0,1)].icon()))
         self.btn_view.setText(str(self.button_plat6[(0,1)].text()))
         self.button_plat6[(0,1)].setFocus()
         self.id_produit.setValue(82)
         self.get_data()
   def _p3(self):
      if self.button_plat6[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(0,2)].icon()))
         self.btn_view.setText(str(self.button_plat6[(0,2)].text()))
         self.button_plat6[(0,2)].setFocus()
         self.id_produit.setValue(83)
         self.get_data()
   def _p4(self):
      if self.button_plat6[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(0,3)].icon()))
         self.btn_view.setText(str(self.button_plat6[(0,3)].text()))
         self.button_plat6[(0,3)].setFocus()
         self.id_produit.setValue(84)
         self.get_data()
   def _p5(self):
      if self.button_plat6[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(1,0)].icon()))
         self.btn_view.setText(str(self.button_plat6[(1,0)].text()))
         self.button_plat6[(1,0)].setFocus()
         self.id_produit.setValue(85)
         self.get_data()
   def _p6(self):
      if self.button_plat6[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(1,1)].icon()))
         self.btn_view.setText(str(self.button_plat6[(1,1)].text()))
         self.button_plat6[(1,1)].setFocus()
         self.id_produit.setValue(86)
         self.get_data()
   def _p7(self):
      if self.button_plat6[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(1,2)].icon()))
         self.btn_view.setText(str(self.button_plat6[(1,2)].text()))
         self.button_plat6[(1,2)].setFocus()
         self.id_produit.setValue(87)
         self.get_data()
   def _p8(self):
      if self.button_plat6[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(1,3)].icon()))
         self.btn_view.setText(str(self.button_plat6[(1,3)].text()))
         self.button_plat6[(1,3)].setFocus()
         self.id_produit.setValue(88)
         self.get_data()
   def _p9(self):
      if self.button_plat6[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(2,0)].icon()))
         self.btn_view.setText(str(self.button_plat6[(2,0)].text()))
         self.button_plat6[(2,0)].setFocus()
         self.id_produit.setValue(89)
         self.get_data()
   def _p10(self):
      if self.button_plat6[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(2,1)].icon()))
         self.btn_view.setText(str(self.button_plat6[(2,1)].text()))
         self.button_plat6[(2,1)].setFocus()
         self.id_produit.setValue(90)
         self.get_data()
   def _p11(self):
      if self.button_plat6[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(2,2)].icon()))
         self.btn_view.setText(str(self.button_plat6[(2,2)].text()))
         self.button_plat6[(2,2)].setFocus()
         self.id_produit.setValue(91)
         self.get_data()
   def _p12(self):
      if self.button_plat6[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(2,3)].icon()))
         self.btn_view.setText(str(self.button_plat6[(2,3)].text()))
         self.button_plat6[(2,3)].setFocus()
         self.id_produit.setValue(92)
         self.get_data()
   def _p13(self):
      if self.button_plat6[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(3,0)].icon()))
         self.btn_view.setText(str(self.button_plat6[(3,0)].text()))
         self.button_plat6[(3,0)].setFocus()
         self.id_produit.setValue(93)
         self.get_data()
   def _p14(self):
      if self.button_plat6[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(3,1)].icon()))
         self.btn_view.setText(str(self.button_plat6[(3,1)].text()))
         self.button_plat6[(3,1)].setFocus()
         self.id_produit.setValue(94)
         self.get_data()
   def _p15(self):
      if self.button_plat6[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(3,2)].icon()))
         self.btn_view.setText(str(self.button_plat6[(3,2)].text()))
         self.button_plat6[(3,2)].setFocus()
         self.id_produit.setValue(95)
         self.get_data()
   def _p16(self):
      if self.button_plat6[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat6[(3,3)].icon()))
         self.btn_view.setText(str(self.button_plat6[(3,3)].text()))
         self.button_plat6[(3,3)].setFocus()
         self.id_produit.setValue(96)
         self.get_data()

   def __p1(self):
      if self.button_plat7[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(0,0)].icon()))
         self.btn_view.setText(str(self.button_plat7[(0,0)].text()))
         self.button_plat7[(0,0)].setFocus()
         self.id_produit.setValue(97)
         self.get_data()
   def __p2(self):
      if self.button_plat7[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(0,1)].icon()))
         self.btn_view.setText(str(self.button_plat7[(0,1)].text()))
         self.button_plat7[(0,1)].setFocus()
         self.id_produit.setValue(98)
         self.get_data()
   def __p3(self):
      if self.button_plat7[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(0,2)].icon()))
         self.btn_view.setText(str(self.button_plat7[(0,2)].text()))
         self.button_plat7[(0,2)].setFocus()
         self.id_produit.setValue(99)
         self.get_data()
   def __p4(self):
      if self.button_plat7[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(0,3)].icon()))
         self.btn_view.setText(str(self.button_plat7[(0,3)].text()))
         self.button_plat7[(0,3)].setFocus()
         self.id_produit.setValue(100)
         self.get_data()
   def __p5(self):
      if self.button_plat7[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(1,0)].icon()))
         self.btn_view.setText(str(self.button_plat7[(1,0)].text()))
         self.button_plat7[(1,0)].setFocus()
         self.id_produit.setValue(101)
         self.get_data()
   def __p6(self):
      if self.button_plat7[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(1,1)].icon()))
         self.btn_view.setText(str(self.button_plat7[(1,1)].text()))
         self.button_plat7[(1,1)].setFocus()
         self.id_produit.setValue(102)
         self.get_data()
   def __p7(self):
      if self.button_plat7[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(1,2)].icon()))
         self.btn_view.setText(str(self.button_plat7[(1,2)].text()))
         self.button_plat7[(1,2)].setFocus()
         self.id_produit.setValue(103)
         self.get_data()
   def __p8(self):
      if self.button_plat7[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(1,3)].icon()))
         self.btn_view.setText(str(self.button_plat7[(1,3)].text()))
         self.button_plat7[(1,3)].setFocus()
         self.id_produit.setValue(104)
         self.get_data()
   def __p9(self):
      if self.button_plat7[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(2,0)].icon()))
         self.btn_view.setText(str(self.button_plat7[(2,0)].text()))
         self.button_plat7[(2,0)].setFocus()
         self.id_produit.setValue(105)
         self.get_data()
   def __p10(self):
      if self.button_plat7[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(2,1)].icon()))
         self.btn_view.setText(str(self.button_plat7[(2,1)].text()))
         self.button_plat7[(2,1)].setFocus()
         self.id_produit.setValue(106)
         self.get_data()
   def __p11(self):
      if self.button_plat7[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(2,2)].icon()))
         self.btn_view.setText(str(self.button_plat7[(2,2)].text()))
         self.button_plat7[(2,2)].setFocus()
         self.id_produit.setValue(107)
         self.get_data()
   def __p12(self):
      if self.button_plat7[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(2,3)].icon()))
         self.btn_view.setText(str(self.button_plat7[(2,3)].text()))
         self.button_plat7[(2,3)].setFocus()
         self.id_produit.setValue(108)
         self.get_data()
   def __p13(self):
      if self.button_plat7[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(3,0)].icon()))
         self.btn_view.setText(str(self.button_plat7[(3,0)].text()))
         self.button_plat7[(3,0)].setFocus()
         self.id_produit.setValue(109)
         self.get_data()
   def __p14(self):
      if self.button_plat7[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(3,1)].icon()))
         self.btn_view.setText(str(self.button_plat7[(3,1)].text()))
         self.button_plat7[(3,1)].setFocus()
         self.id_produit.setValue(110)
         self.get_data()
   def __p15(self):
      if self.button_plat7[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(3,2)].icon()))
         self.btn_view.setText(str(self.button_plat7[(3,2)].text()))
         self.button_plat7[(3,2)].setFocus()
         self.id_produit.setValue(111)
         self.get_data()
   def __p16(self):
      if self.button_plat7[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat7[(3,3)].icon()))
         self.btn_view.setText(str(self.button_plat7[(3,3)].text()))
         self.button_plat7[(3,3)].setFocus()
         self.id_produit.setValue(112)
         self.get_data()
   def ___p1(self):
      if self.button_plat8[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(0,0)].icon()))
         self.btn_view.setText(str(self.button_plat8[(0,0)].text()))
         self.button_plat8[(0,0)].setFocus()
         self.id_produit.setValue(113)
         self.get_data()
   def ___p2(self):
      if self.button_plat8[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(0,1)].icon()))
         self.btn_view.setText(str(self.button_plat8[(0,1)].text()))
         self.button_plat8[(0,1)].setFocus()
         self.id_produit.setValue(114)
         self.get_data()
   def ___p3(self):
      if self.button_plat8[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(0,2)].icon()))
         self.btn_view.setText(str(self.button_plat8[(0,2)].text()))
         self.button_plat8[(0,2)].setFocus()
         self.id_produit.setValue(115)
         self.get_data()
   def ___p4(self):
      if self.button_plat8[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(0,3)].icon()))
         self.btn_view.setText(str(self.button_plat8[(0,3)].text()))
         self.button_plat8[(0,3)].setFocus()
         self.id_produit.setValue(116)
         self.get_data()
   def ___p5(self):
      if self.button_plat8[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(1,0)].icon()))
         self.btn_view.setText(str(self.button_plat8[(1,0)].text()))
         self.button_plat8[(1,0)].setFocus()
         self.id_produit.setValue(117)
         self.get_data()
   def ___p6(self):
      if self.button_plat8[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(1,1)].icon()))
         self.btn_view.setText(str(self.button_plat8[(1,1)].text()))
         self.button_plat8[(1,1)].setFocus()
         self.id_produit.setValue(118)
         self.get_data()
   def ___p7(self):
      if self.button_plat8[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(1,2)].icon()))
         self.btn_view.setText(str(self.button_plat8[(1,2)].text()))
         self.button_plat8[(1,2)].setFocus()
         self.id_produit.setValue(119)
         self.get_data()
   def ___p8(self):
      if self.button_plat8[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(1,3)].icon()))
         self.btn_view.setText(str(self.button_plat8[(1,3)].text()))
         self.button_plat8[(1,3)].setFocus()
         self.id_produit.setValue(120)
         self.get_data()
   def ___p9(self):
      if self.button_plat8[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(2,0)].icon()))
         self.btn_view.setText(str(self.button_plat8[(2,0)].text()))
         self.button_plat8[(2,0)].setFocus()
         self.id_produit.setValue(121)
         self.get_data()
   def ___p10(self):
      if self.button_plat8[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(2,1)].icon()))
         self.btn_view.setText(str(self.button_plat8[(2,1)].text()))
         self.button_plat8[(2,1)].setFocus()
         self.id_produit.setValue(122)
         self.get_data()
   def ___p11(self):
      if self.button_plat8[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(2,2)].icon()))
         self.btn_view.setText(str(self.button_plat8[(2,2)].text()))
         self.button_plat8[(2,2)].setFocus()
         self.id_produit.setValue(123)
         self.get_data()
   def ___p12(self):
      if self.button_plat8[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(2,3)].icon()))
         self.btn_view.setText(str(self.button_plat8[(2,3)].text()))
         self.button_plat8[(2,3)].setFocus()
         self.id_produit.setValue(124)
         self.get_data()
   def ___p13(self):
      if self.button_plat8[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(3,0)].icon()))
         self.btn_view.setText(str(self.button_plat8[(3,0)].text()))
         self.button_plat8[(3,0)].setFocus()
         self.id_produit.setValue(125)
         self.get_data()
   def ___p14(self):
      if self.button_plat8[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(3,1)].icon()))
         self.btn_view.setText(str(self.button_plat8[(3,1)].text()))
         self.button_plat8[(3,1)].setFocus()
         self.id_produit.setValue(126)
         self.get_data()
   def ___p15(self):
      if self.button_plat8[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(3,2)].icon()))
         self.btn_view.setText(str(self.button_plat8[(3,2)].text()))
         self.button_plat8[(3,2)].setFocus()
         self.id_produit.setValue(127)
         self.get_data()
   def ___p16(self):
      if self.button_plat8[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_plat8[(3,3)].icon()))
         self.btn_view.setText(str(self.button_plat8[(3,3)].text()))
         self.button_plat8[(3,3)].setFocus()
         self.id_produit.setValue(128)
         self.get_data()

   def select_photo(self):
      if (self.zone_title.text()=='BOISSONS' or
          self.zone_title.text()=='DESSERTS' or
          self.zone_title.text()=='CAFES' or
          self.zone_title.text()=='PLATS'):
         self.question=QMessageBox.question(self,str(self.app_name),'VOULEZ VOUS CHOISIR UNE IMAGE ?',QMessageBox.Yes,QMessageBox.No)
         if self.question==QMessageBox.Yes:
            filename = QFileDialog.getOpenFileName(self,"CHOISIR UNE IMAGE")
            self.photo="png"+str(str(filename).split(",")[0].split("(")[1].split("'")[1].split("/png")[-1])
            self.btn_view.setIcon(QIcon(self.photo))
            
            #QMessageBox.information(self,str(self.app_name),'--PHOTO SELECTIONNEE AVEC SUCCES--'+'\n\n\n ADRESSE DU FICHIER: '+self.photo+'\n')
         else:
            pass

   def refresh_data(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd and self.zone_title.text()=='BOISSONS':
               self.cursor=self.bdd.cursor()
               #________PAGE 1
               self.b1=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=1")               
               for row in self.b1:
                  self.button_boisson1[(0,0)].setText(str(row[0]))
                  self.lab_boisson1[(0,0)].setText(str(row[1]))
                  self.button_boisson1[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b2=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=2")             
               for row in self.b2:
                  self.button_boisson1[(0,1)].setText(str(row[0]))
                  self.lab_boisson1[(0,1)].setText(str(row[1]))
                  self.button_boisson1[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b3=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=3")               
               for row in self.b3:
                  self.button_boisson1[(0,2)].setText(str(row[0]))
                  self.lab_boisson1[(0,2)].setText(str(row[1]))
                  self.button_boisson1[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b4=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=4")               
               for row in self.b4:
                  self.button_boisson1[(0,3)].setText(str(row[0]))
                  self.lab_boisson1[(0,3)].setText(str(row[1]))
                  self.button_boisson1[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b5=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=5")               
               for row in self.b5:
                  self.button_boisson1[(1,0)].setText(str(row[0]))
                  self.lab_boisson1[(1,0)].setText(str(row[1]))
                  self.button_boisson1[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b6=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=6")               
               for row in self.b6:
                  self.button_boisson1[(1,1)].setText(str(row[0]))
                  self.lab_boisson1[(1,1)].setText(str(row[1]))
                  self.button_boisson1[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b7=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=7")               
               for row in self.b7:
                  self.button_boisson1[(1,2)].setText(str(row[0]))
                  self.lab_boisson1[(1,2)].setText(str(row[1]))
                  self.button_boisson1[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b8=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=8")               
               for row in self.b8:
                  self.button_boisson1[(1,3)].setText(str(row[0]))
                  self.lab_boisson1[(1,3)].setText(str(row[1]))
                  self.button_boisson1[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b9=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=9")               
               for row in self.b9:
                  self.button_boisson1[(2,0)].setText(str(row[0]))
                  self.lab_boisson1[(2,0)].setText(str(row[1]))
                  self.button_boisson1[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b10=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=10")               
               for row in self.b10:
                  self.button_boisson1[(2,1)].setText(str(row[0]))
                  self.lab_boisson1[(2,1)].setText(str(row[1]))
                  self.button_boisson1[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b11=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=11")               
               for row in self.b11:
                  self.button_boisson1[(2,2)].setText(str(row[0]))
                  self.lab_boisson1[(2,2)].setText(str(row[1]))
                  self.button_boisson1[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b12=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=12")               
               for row in self.b12:
                  self.button_boisson1[(2,3)].setText(str(row[0]))
                  self.lab_boisson1[(2,3)].setText(str(row[1]))
                  self.button_boisson1[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b13=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=13")               
               for row in self.b13:
                  self.button_boisson1[(3,0)].setText(str(row[0]))
                  self.lab_boisson1[(3,0)].setText(str(row[1]))
                  self.button_boisson1[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b14=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=14")               
               for row in self.b14:
                  self.button_boisson1[(3,1)].setText(str(row[0]))
                  self.lab_boisson1[(3,1)].setText(str(row[1]))
                  self.button_boisson1[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b15=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=15")               
               for row in self.b15:
                  self.button_boisson1[(3,2)].setText(str(row[0]))
                  self.lab_boisson1[(3,2)].setText(str(row[1]))
                  self.button_boisson1[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b16=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=16")               
               for row in self.b16:
                  self.button_boisson1[(3,3)].setText(str(row[0]))
                  self.lab_boisson1[(3,3)].setText(str(row[1]))
                  self.button_boisson1[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               
               #====================== REFRESH LAB ==#
               #=====================================#
               for x in range(32):
                  for y in range(4):
                     #====================== BOISSONS
                     self.lab_boisson1[(x,y)].adjustSize()

            elif self.bdd and self.zone_title.text()=='DESSERTS':
               self.cursor=self.bdd.cursor()               
               #________PAGE 1
               self.b1=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=1")               
               for row in self.b1:
                  self.button_dessert1[(0,0)].setText(str(row[0]))
                  self.lab_dessert1[(0,0)].setText(str(row[1]))
                  self.button_dessert1[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b2=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=2")             
               for row in self.b2:
                  self.button_dessert1[(0,1)].setText(str(row[0]))
                  self.lab_dessert1[(0,1)].setText(str(row[1]))
                  self.button_dessert1[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b3=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=3")               
               for row in self.b3:
                  self.button_dessert1[(0,2)].setText(str(row[0]))
                  self.lab_dessert1[(0,2)].setText(str(row[1]))
                  self.button_dessert1[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b4=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=4")               
               for row in self.b4:
                  self.button_dessert1[(0,3)].setText(str(row[0]))
                  self.lab_dessert1[(0,3)].setText(str(row[1]))
                  self.button_dessert1[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b5=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=5")               
               for row in self.b5:
                  self.button_dessert1[(1,0)].setText(str(row[0]))
                  self.lab_dessert1[(1,0)].setText(str(row[1]))
                  self.button_dessert1[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b6=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=6")               
               for row in self.b6:
                  self.button_dessert1[(1,1)].setText(str(row[0]))
                  self.lab_dessert1[(1,1)].setText(str(row[1]))
                  self.button_dessert1[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b7=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=7")               
               for row in self.b7:
                  self.button_dessert1[(1,2)].setText(str(row[0]))
                  self.lab_dessert1[(1,2)].setText(str(row[1]))
                  self.button_dessert1[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b8=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=8")               
               for row in self.b8:
                  self.button_dessert1[(1,3)].setText(str(row[0]))
                  self.lab_dessert1[(1,3)].setText(str(row[1]))
                  self.button_dessert1[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b9=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=9")               
               for row in self.b9:
                  self.button_dessert1[(2,0)].setText(str(row[0]))
                  self.lab_dessert1[(2,0)].setText(str(row[1]))
                  self.button_dessert1[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b10=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=10")               
               for row in self.b10:
                  self.button_dessert1[(2,1)].setText(str(row[0]))
                  self.lab_dessert1[(2,1)].setText(str(row[1]))
                  self.button_dessert1[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b11=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=11")               
               for row in self.b11:
                  self.button_dessert1[(2,2)].setText(str(row[0]))
                  self.lab_dessert1[(2,2)].setText(str(row[1]))
                  self.button_dessert1[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b12=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=12")               
               for row in self.b12:
                  self.button_dessert1[(2,3)].setText(str(row[0]))
                  self.lab_dessert1[(2,3)].setText(str(row[1]))
                  self.button_dessert1[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b13=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=13")               
               for row in self.b13:
                  self.button_dessert1[(3,0)].setText(str(row[0]))
                  self.lab_dessert1[(3,0)].setText(str(row[1]))
                  self.button_dessert1[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b14=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=14")               
               for row in self.b14:
                  self.button_dessert1[(3,1)].setText(str(row[0]))
                  self.lab_dessert1[(3,1)].setText(str(row[1]))
                  self.button_dessert1[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b15=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=15")               
               for row in self.b15:
                  self.button_dessert1[(3,2)].setText(str(row[0]))
                  self.lab_dessert1[(3,2)].setText(str(row[1]))
                  self.button_dessert1[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b16=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=16")               
               for row in self.b16:
                  self.button_dessert1[(3,3)].setText(str(row[0]))
                  self.lab_dessert1[(3,3)].setText(str(row[1]))
                  self.button_dessert1[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 2
               self.b17=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=17")               
               for row in self.b17:
                  self.button_dessert2[(0,0)].setText(str(row[0]))
                  self.lab_dessert2[(0,0)].setText(str(row[1]))
                  self.button_dessert2[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b18=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=18")               
               for row in self.b18:
                  self.button_dessert2[(0,1)].setText(str(row[0]))
                  self.lab_dessert2[(0,1)].setText(str(row[1]))
                  self.button_dessert2[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b19=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=19")               
               for row in self.b19:
                  self.button_dessert2[(0,2)].setText(str(row[0]))
                  self.lab_dessert2[(0,2)].setText(str(row[1]))
                  self.button_dessert2[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b20=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=20")               
               for row in self.b20:
                  self.button_dessert2[(0,3)].setText(str(row[0]))
                  self.lab_dessert2[(0,3)].setText(str(row[1]))
                  self.button_dessert2[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b21=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=21")               
               for row in self.b21:
                  self.button_dessert2[(1,0)].setText(str(row[0]))
                  self.lab_dessert2[(1,0)].setText(str(row[1]))
                  self.button_dessert2[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b22=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=22")               
               for row in self.b22:
                  self.button_dessert2[(1,1)].setText(str(row[0]))
                  self.lab_dessert2[(1,1)].setText(str(row[1]))
                  self.button_dessert2[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b23=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=23")               
               for row in self.b23:
                  self.button_dessert2[(1,2)].setText(str(row[0]))
                  self.lab_dessert2[(1,2)].setText(str(row[1]))
                  self.button_dessert2[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b24=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=24")               
               for row in self.b24:
                  self.button_dessert2[(1,3)].setText(str(row[0]))
                  self.lab_dessert2[(1,3)].setText(str(row[1]))
                  self.button_dessert2[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b25=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=25")               
               for row in self.b25:
                  self.button_dessert2[(2,0)].setText(str(row[0]))
                  self.lab_dessert2[(2,0)].setText(str(row[1]))
                  self.button_dessert2[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b26=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=26")               
               for row in self.b26:
                  self.button_dessert2[(2,1)].setText(str(row[0]))
                  self.lab_dessert2[(2,1)].setText(str(row[1]))
                  self.button_dessert2[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b27=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=27")               
               for row in self.b27:
                  self.button_dessert2[(2,2)].setText(str(row[0]))
                  self.lab_dessert2[(2,2)].setText(str(row[1]))
                  self.button_dessert2[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b28=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=28")               
               for row in self.b28:
                  self.button_dessert2[(2,3)].setText(str(row[0]))
                  self.lab_dessert2[(2,3)].setText(str(row[1]))
                  self.button_dessert2[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b29=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=29")               
               for row in self.b29:
                  self.button_dessert2[(3,0)].setText(str(row[0]))
                  self.lab_dessert2[(3,0)].setText(str(row[1]))
                  self.button_dessert2[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b30=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=30")               
               for row in self.b30:
                  self.button_dessert2[(3,1)].setText(str(row[0]))
                  self.lab_dessert2[(3,1)].setText(str(row[1]))
                  self.button_dessert2[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b31=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=31")               
               for row in self.b31:
                  self.button_dessert2[(3,2)].setText(str(row[0]))
                  self.lab_dessert2[(3,2)].setText(str(row[1]))
                  self.button_dessert2[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b32=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=32")               
               for row in self.b32:
                  self.button_dessert2[(3,3)].setText(str(row[0]))
                  self.lab_dessert2[(3,3)].setText(str(row[1]))
                  self.button_dessert2[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 3
               self.b33=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=33")               
               for row in self.b33:
                  self.button_dessert3[(0,0)].setText(str(row[0]))
                  self.lab_dessert3[(0,0)].setText(str(row[1]))
                  self.button_dessert3[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b34=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=34")               
               for row in self.b34:
                  self.button_dessert3[(0,1)].setText(str(row[0]))
                  self.lab_dessert3[(0,1)].setText(str(row[1]))
                  self.button_dessert3[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b35=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=35")               
               for row in self.b35:
                  self.button_dessert3[(0,2)].setText(str(row[0]))
                  self.lab_dessert3[(0,2)].setText(str(row[1]))
                  self.button_dessert3[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b36=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=36")               
               for row in self.b36:
                  self.button_dessert3[(0,3)].setText(str(row[0]))
                  self.lab_dessert3[(0,3)].setText(str(row[1]))
                  self.button_dessert3[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b37=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=37")               
               for row in self.b37:
                  self.button_dessert3[(1,0)].setText(str(row[0]))
                  self.lab_dessert3[(1,0)].setText(str(row[1]))
                  self.button_dessert3[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b38=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=38")               
               for row in self.b38:
                  self.button_dessert3[(1,1)].setText(str(row[0]))
                  self.lab_dessert3[(1,1)].setText(str(row[1]))
                  self.button_dessert3[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b39=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=39")               
               for row in self.b39:
                  self.button_dessert3[(1,2)].setText(str(row[0]))
                  self.lab_dessert3[(1,2)].setText(str(row[1]))
                  self.button_dessert3[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b40=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=40")               
               for row in self.b40:
                  self.button_dessert3[(1,3)].setText(str(row[0]))
                  self.lab_dessert3[(1,3)].setText(str(row[1]))
                  self.button_dessert3[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b41=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=41")               
               for row in self.b41:
                  self.button_dessert3[(2,0)].setText(str(row[0]))
                  self.lab_dessert3[(2,0)].setText(str(row[1]))
                  self.button_dessert3[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b42=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=42")               
               for row in self.b42:
                  self.button_dessert3[(2,1)].setText(str(row[0]))
                  self.lab_dessert3[(2,1)].setText(str(row[1]))
                  self.button_dessert3[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b43=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=43")               
               for row in self.b43:
                  self.button_dessert3[(2,2)].setText(str(row[0]))
                  self.lab_dessert3[(2,2)].setText(str(row[1]))
                  self.button_dessert3[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b44=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=44")               
               for row in self.b44:
                  self.button_dessert3[(2,3)].setText(str(row[0]))
                  self.lab_dessert3[(2,3)].setText(str(row[1]))
                  self.button_dessert3[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b45=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=45")               
               for row in self.b45:
                  self.button_dessert3[(3,0)].setText(str(row[0]))
                  self.lab_dessert3[(3,0)].setText(str(row[1]))
                  self.button_dessert3[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b46=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=46")               
               for row in self.b46:
                  self.button_dessert3[(3,1)].setText(str(row[0]))
                  self.lab_dessert3[(3,1)].setText(str(row[1]))
                  self.button_dessert3[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b47=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=47")               
               for row in self.b47:
                  self.button_dessert3[(3,2)].setText(str(row[0]))
                  self.lab_dessert3[(3,2)].setText(str(row[1]))
                  self.button_dessert3[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b48=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=48")               
               for row in self.b48:
                  self.button_dessert3[(3,3)].setText(str(row[0]))
                  self.lab_dessert3[(3,3)].setText(str(row[1]))
                  self.button_dessert3[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 4
               self.b49=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=49")               
               for row in self.b49:
                  self.button_dessert4[(0,0)].setText(str(row[0]))
                  self.lab_dessert4[(0,0)].setText(str(row[1]))
                  self.button_dessert4[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b50=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=50")           
               for row in self.b50:
                  self.button_dessert4[(0,1)].setText(str(row[0]))
                  self.lab_dessert4[(0,1)].setText(str(row[1]))
                  self.button_dessert4[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b51=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=51")               
               for row in self.b51:
                  self.button_dessert4[(0,2)].setText(str(row[0]))
                  self.lab_dessert4[(0,2)].setText(str(row[1]))
                  self.button_dessert4[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b52=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=52")               
               for row in self.b52:
                  self.button_dessert4[(0,3)].setText(str(row[0]))
                  self.lab_dessert4[(0,3)].setText(str(row[1]))
                  self.button_dessert4[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b53=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=53")               
               for row in self.b53:
                  self.button_dessert4[(1,0)].setText(str(row[0]))
                  self.lab_dessert4[(1,0)].setText(str(row[1]))
                  self.button_dessert4[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b54=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=54")               
               for row in self.b54:
                  self.button_dessert4[(1,1)].setText(str(row[0]))
                  self.lab_dessert4[(1,1)].setText(str(row[1]))
                  self.button_dessert4[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b55=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=55")               
               for row in self.b55:
                  self.button_dessert4[(1,2)].setText(str(row[0]))
                  self.lab_dessert4[(1,2)].setText(str(row[1]))
                  self.button_dessert4[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b56=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=56")               
               for row in self.b56:
                  self.button_dessert4[(1,3)].setText(str(row[0]))
                  self.lab_dessert4[(1,3)].setText(str(row[1]))
                  self.button_dessert4[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b57=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=57")               
               for row in self.b57:
                  self.button_dessert4[(2,0)].setText(str(row[0]))
                  self.lab_dessert4[(2,0)].setText(str(row[1]))
                  self.button_dessert4[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b58=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=58")               
               for row in self.b58:
                  self.button_dessert4[(2,1)].setText(str(row[0]))
                  self.lab_dessert4[(2,1)].setText(str(row[1]))
                  self.button_dessert4[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b59=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=59")               
               for row in self.b59:
                  self.button_dessert4[(2,2)].setText(str(row[0]))
                  self.lab_dessert4[(2,2)].setText(str(row[1]))
                  self.button_dessert4[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b60=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=60")               
               for row in self.b60:
                  self.button_dessert4[(2,3)].setText(str(row[0]))
                  self.lab_dessert4[(2,3)].setText(str(row[1]))
                  self.button_dessert4[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b61=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=61")               
               for row in self.b61:
                  self.button_dessert4[(3,0)].setText(str(row[0]))
                  self.lab_dessert4[(3,0)].setText(str(row[1]))
                  self.button_dessert4[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b62=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=62")               
               for row in self.b62:
                  self.button_dessert4[(3,1)].setText(str(row[0]))
                  self.lab_dessert4[(3,1)].setText(str(row[1]))
                  self.button_dessert4[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b63=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=63")               
               for row in self.b63:
                  self.button_dessert4[(3,2)].setText(str(row[0]))
                  self.lab_dessert4[(3,2)].setText(str(row[1]))
                  self.button_dessert4[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b64=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=64")               
               for row in self.b64:
                  self.button_dessert4[(3,3)].setText(str(row[0]))
                  self.lab_dessert4[(3,3)].setText(str(row[1]))
                  self.button_dessert4[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 5
               self.b65=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=65")               
               for row in self.b65:
                  self.button_dessert5[(0,0)].setText(str(row[0]))
                  self.lab_dessert5[(0,0)].setText(str(row[1]))
                  self.button_dessert5[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b66=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=66")             
               for row in self.b66:
                  self.button_dessert5[(0,1)].setText(str(row[0]))
                  self.lab_dessert5[(0,1)].setText(str(row[1]))
                  self.button_dessert5[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b67=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=67")               
               for row in self.b67:
                  self.button_dessert5[(0,2)].setText(str(row[0]))
                  self.lab_dessert5[(0,2)].setText(str(row[1]))
                  self.button_dessert5[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b68=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=68")               
               for row in self.b68:
                  self.button_dessert5[(0,3)].setText(str(row[0]))
                  self.lab_dessert5[(0,3)].setText(str(row[1]))
                  self.button_dessert5[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b69=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=69")               
               for row in self.b69:
                  self.button_dessert5[(1,0)].setText(str(row[0]))
                  self.lab_dessert5[(1,0)].setText(str(row[1]))
                  self.button_dessert5[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b70=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=70")               
               for row in self.b70:
                  self.button_dessert5[(1,1)].setText(str(row[0]))
                  self.lab_dessert5[(1,1)].setText(str(row[1]))
                  self.button_dessert5[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b71=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=71")               
               for row in self.b71:
                  self.button_dessert5[(1,2)].setText(str(row[0]))
                  self.lab_dessert5[(1,2)].setText(str(row[1]))
                  self.button_dessert5[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b72=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=72")               
               for row in self.b72:
                  self.button_dessert5[(1,3)].setText(str(row[0]))
                  self.lab_dessert5[(1,3)].setText(str(row[1]))
                  self.button_dessert5[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b73=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=73")               
               for row in self.b73:
                  self.button_dessert5[(2,0)].setText(str(row[0]))
                  self.lab_dessert5[(2,0)].setText(str(row[1]))
                  self.button_dessert5[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b74=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=74")               
               for row in self.b74:
                  self.button_dessert5[(2,1)].setText(str(row[0]))
                  self.lab_dessert5[(2,1)].setText(str(row[1]))
                  self.button_dessert5[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b75=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=75")               
               for row in self.b75:
                  self.button_dessert5[(2,2)].setText(str(row[0]))
                  self.lab_dessert5[(2,2)].setText(str(row[1]))
                  self.button_dessert5[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b76=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=76")               
               for row in self.b76:
                  self.button_dessert5[(2,3)].setText(str(row[0]))
                  self.lab_dessert5[(2,3)].setText(str(row[1]))
                  self.button_dessert5[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b77=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=77")               
               for row in self.b77:
                  self.button_dessert5[(3,0)].setText(str(row[0]))
                  self.lab_dessert5[(3,0)].setText(str(row[1]))
                  self.button_dessert5[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b78=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=78")               
               for row in self.b78:
                  self.button_dessert5[(3,1)].setText(str(row[0]))
                  self.lab_dessert5[(3,1)].setText(str(row[1]))
                  self.button_dessert5[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b79=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=79")               
               for row in self.b79:
                  self.button_dessert5[(3,2)].setText(str(row[0]))
                  self.lab_dessert5[(3,2)].setText(str(row[1]))
                  self.button_dessert5[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b80=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=80")               
               for row in self.b80:
                  self.button_dessert5[(3,3)].setText(str(row[0]))
                  self.lab_dessert5[(3,3)].setText(str(row[1]))
                  self.button_dessert5[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 6
               self.b81=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=81")               
               for row in self.b81:
                  self.button_dessert6[(0,0)].setText(str(row[0]))
                  self.lab_dessert6[(0,0)].setText(str(row[1]))
                  self.button_dessert6[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b82=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=82")               
               for row in self.b82:
                  self.button_dessert6[(0,1)].setText(str(row[0]))
                  self.lab_dessert6[(0,1)].setText(str(row[1]))
                  self.button_dessert6[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b83=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=83")               
               for row in self.b83:
                  self.button_dessert6[(0,2)].setText(str(row[0]))
                  self.lab_dessert6[(0,2)].setText(str(row[1]))
                  self.button_dessert6[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b84=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=84")               
               for row in self.b84:
                  self.button_dessert6[(0,3)].setText(str(row[0]))
                  self.lab_dessert6[(0,3)].setText(str(row[1]))
                  self.button_dessert6[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b85=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=85")               
               for row in self.b85:
                  self.button_dessert6[(1,0)].setText(str(row[0]))
                  self.lab_dessert6[(1,0)].setText(str(row[1]))
                  self.button_dessert6[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b86=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=86")               
               for row in self.b86:
                  self.button_dessert6[(1,1)].setText(str(row[0]))
                  self.lab_dessert6[(1,1)].setText(str(row[1]))
                  self.button_dessert6[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b87=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=87")               
               for row in self.b87:
                  self.button_dessert6[(1,2)].setText(str(row[0]))
                  self.lab_dessert6[(1,2)].setText(str(row[1]))
                  self.button_dessert6[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b88=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=88")               
               for row in self.b88:
                  self.button_dessert6[(1,3)].setText(str(row[0]))
                  self.lab_dessert6[(1,3)].setText(str(row[1]))
                  self.button_dessert6[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b89=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=89")               
               for row in self.b89:
                  self.button_dessert6[(2,0)].setText(str(row[0]))
                  self.lab_dessert6[(2,0)].setText(str(row[1]))
                  self.button_dessert6[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b90=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=90")               
               for row in self.b90:
                  self.button_dessert6[(2,1)].setText(str(row[0]))
                  self.lab_dessert6[(2,1)].setText(str(row[1]))
                  self.button_dessert6[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b91=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=91")               
               for row in self.b91:
                  self.button_dessert6[(2,2)].setText(str(row[0]))
                  self.lab_dessert6[(2,2)].setText(str(row[1]))
                  self.button_dessert6[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b92=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=92")               
               for row in self.b92:
                  self.button_dessert6[(2,3)].setText(str(row[0]))
                  self.lab_dessert6[(2,3)].setText(str(row[1]))
                  self.button_dessert6[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b93=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=93")               
               for row in self.b93:
                  self.button_dessert6[(3,0)].setText(str(row[0]))
                  self.lab_dessert6[(3,0)].setText(str(row[1]))
                  self.button_dessert6[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b94=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=94")               
               for row in self.b94:
                  self.button_dessert6[(3,1)].setText(str(row[0]))
                  self.lab_dessert6[(3,1)].setText(str(row[1]))
                  self.button_dessert6[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b95=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=95")               
               for row in self.b95:
                  self.button_dessert6[(3,2)].setText(str(row[0]))
                  self.lab_dessert6[(3,2)].setText(str(row[1]))
                  self.button_dessert6[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b96=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=96")               
               for row in self.b96:
                  self.button_dessert6[(3,3)].setText(str(row[0]))
                  self.lab_dessert6[(3,3)].setText(str(row[1]))
                  self.button_dessert6[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 7
               self.b97=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=97")               
               for row in self.b97:
                  self.button_dessert7[(0,0)].setText(str(row[0]))
                  self.lab_dessert7[(0,0)].setText(str(row[1]))
                  self.button_dessert7[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b98=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=98")               
               for row in self.b98:
                  self.button_dessert7[(0,1)].setText(str(row[0]))
                  self.lab_dessert7[(0,1)].setText(str(row[1]))
                  self.button_dessert7[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b99=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=99")               
               for row in self.b99:
                  self.button_dessert7[(0,2)].setText(str(row[0]))
                  self.lab_dessert7[(0,2)].setText(str(row[1]))
                  self.button_dessert7[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b100=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=100")               
               for row in self.b100:
                  self.button_dessert7[(0,3)].setText(str(row[0]))
                  self.lab_dessert7[(0,3)].setText(str(row[1]))
                  self.button_dessert7[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b101=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=101")               
               for row in self.b101:
                  self.button_dessert7[(1,0)].setText(str(row[0]))
                  self.lab_dessert7[(1,0)].setText(str(row[1]))
                  self.button_dessert7[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b102=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=102")               
               for row in self.b101:
                  self.button_dessert7[(1,1)].setText(str(row[0]))
                  self.lab_dessert7[(1,1)].setText(str(row[1]))
                  self.button_dessert7[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b103=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=103")               
               for row in self.b103:
                  self.button_dessert7[(1,2)].setText(str(row[0]))
                  self.lab_dessert7[(1,2)].setText(str(row[1]))
                  self.button_dessert7[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b104=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=104")               
               for row in self.b104:
                  self.button_dessert7[(1,3)].setText(str(row[0]))
                  self.lab_dessert7[(1,3)].setText(str(row[1]))
                  self.button_dessert7[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b105=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=105")               
               for row in self.b105:
                  self.button_dessert7[(2,0)].setText(str(row[0]))
                  self.lab_dessert7[(2,0)].setText(str(row[1]))
                  self.button_dessert7[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b106=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=106")               
               for row in self.b106:
                  self.button_dessert7[(2,1)].setText(str(row[0]))
                  self.lab_dessert7[(2,1)].setText(str(row[1]))
                  self.button_dessert7[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b107=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=107")               
               for row in self.b107:
                  self.button_dessert7[(2,2)].setText(str(row[0]))
                  self.lab_dessert7[(2,2)].setText(str(row[1]))
                  self.button_dessert7[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b108=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=108")               
               for row in self.b108:
                  self.button_dessert7[(2,3)].setText(str(row[0]))
                  self.lab_dessert7[(2,3)].setText(str(row[1]))
                  self.button_dessert7[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b109=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=109")               
               for row in self.b109:
                  self.button_dessert7[(3,0)].setText(str(row[0]))
                  self.lab_dessert7[(3,0)].setText(str(row[1]))
                  self.button_dessert7[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b110=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=110")               
               for row in self.b110:
                  self.button_dessert7[(3,1)].setText(str(row[0]))
                  self.lab_dessert7[(3,1)].setText(str(row[1]))
                  self.button_dessert7[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b111=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=111")               
               for row in self.b111:
                  self.button_dessert7[(3,2)].setText(str(row[0]))
                  self.lab_dessert7[(3,2)].setText(str(row[1]))
                  self.button_dessert7[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b112=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=112")               
               for row in self.b112:
                  self.button_dessert7[(3,3)].setText(str(row[0]))
                  self.lab_dessert7[(3,3)].setText(str(row[1]))
                  self.button_dessert7[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 8
               self.b113=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=113")               
               for row in self.b113:
                  self.button_dessert8[(0,0)].setText(str(row[0]))
                  self.lab_dessert8[(0,0)].setText(str(row[1]))
                  self.button_dessert8[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b114=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=114")           
               for row in self.b114:
                  self.button_dessert8[(0,1)].setText(str(row[0]))
                  self.lab_dessert8[(0,1)].setText(str(row[1]))
                  self.button_dessert8[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b115=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=115")               
               for row in self.b115:
                  self.button_dessert8[(0,2)].setText(str(row[0]))
                  self.lab_dessert8[(0,2)].setText(str(row[1]))
                  self.button_dessert8[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b116=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=116")               
               for row in self.b116:
                  self.button_dessert8[(0,3)].setText(str(row[0]))
                  self.lab_dessert8[(0,3)].setText(str(row[1]))
                  self.button_dessert8[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b117=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=117")               
               for row in self.b117:
                  self.button_dessert8[(1,0)].setText(str(row[0]))
                  self.lab_dessert8[(1,0)].setText(str(row[1]))
                  self.button_dessert8[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b118=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=118")               
               for row in self.b118:
                  self.button_dessert8[(1,1)].setText(str(row[0]))
                  self.lab_dessert8[(1,1)].setText(str(row[1]))
                  self.button_dessert8[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b119=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=119")               
               for row in self.b119:
                  self.button_dessert8[(1,2)].setText(str(row[0]))
                  self.lab_dessert8[(1,2)].setText(str(row[1]))
                  self.button_dessert8[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b120=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=120")               
               for row in self.b120:
                  self.button_dessert4[(1,3)].setText(str(row[0]))
                  self.lab_dessert8[(1,3)].setText(str(row[1]))
                  self.button_dessert8[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b121=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=121")               
               for row in self.b121:
                  self.button_dessert8[(2,0)].setText(str(row[0]))
                  self.lab_dessert8[(2,0)].setText(str(row[1]))
                  self.button_dessert8[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b122=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=122")               
               for row in self.b122:
                  self.button_dessert8[(2,1)].setText(str(row[0]))
                  self.lab_dessert8[(2,1)].setText(str(row[1]))
                  self.button_dessert8[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b123=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=123")               
               for row in self.b123:
                  self.button_dessert8[(2,2)].setText(str(row[0]))
                  self.lab_dessert8[(2,2)].setText(str(row[1]))
                  self.button_dessert8[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b124=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=124")               
               for row in self.b124:
                  self.button_dessert8[(2,3)].setText(str(row[0]))
                  self.lab_dessert8[(2,3)].setText(str(row[1]))
                  self.button_dessert8[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b125=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=125")               
               for row in self.b125:
                  self.button_dessert8[(3,0)].setText(str(row[0]))
                  self.lab_dessert8[(3,0)].setText(str(row[1]))
                  self.button_dessert8[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b126=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=126")               
               for row in self.b126:
                  self.button_dessert8[(3,1)].setText(str(row[0]))
                  self.lab_dessert8[(3,1)].setText(str(row[1]))
                  self.button_dessert8[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b127=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=127")               
               for row in self.b127:
                  self.button_dessert8[(3,2)].setText(str(row[0]))
                  self.lab_dessert8[(3,2)].setText(str(row[1]))
                  self.button_dessert8[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b128=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=128")               
               for row in self.b128:
                  self.button_dessert8[(3,3)].setText(str(row[0]))
                  self.lab_dessert8[(3,3)].setText(str(row[1]))
                  self.button_dessert8[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.bdd.commit()
               #====================== REFRESH LAB ==#
               #=====================================#
               for x in range(4):
                  for y in range(4):
                     #====================== DESSERTS
                     self.lab_dessert1[(x,y)].adjustSize()
                     self.lab_dessert2[(x,y)].adjustSize()
                     self.lab_dessert3[(x,y)].adjustSize()
                     self.lab_dessert4[(x,y)].adjustSize()
                     self.lab_dessert5[(x,y)].adjustSize()
                     self.lab_dessert6[(x,y)].adjustSize()
                     self.lab_dessert7[(x,y)].adjustSize()
                     self.lab_dessert8[(x,y)].adjustSize()
            elif self.bdd and self.zone_title.text()=='CAFES':
               self.cursor=self.bdd.cursor()
               #________PAGE 1
               self.b1=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=1")               
               for row in self.b1:
                  self.button_cafe1[(0,0)].setText(str(row[0]))
                  self.lab_cafe1[(0,0)].setText(str(row[1]))
                  self.button_cafe1[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b2=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=2")             
               for row in self.b2:
                  self.button_cafe1[(0,1)].setText(str(row[0]))
                  self.lab_cafe1[(0,1)].setText(str(row[1]))
                  self.button_cafe1[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b3=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=3")               
               for row in self.b3:
                  self.button_cafe1[(0,2)].setText(str(row[0]))
                  self.lab_cafe1[(0,2)].setText(str(row[1]))
                  self.button_cafe1[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b4=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=4")               
               for row in self.b4:
                  self.button_cafe1[(0,3)].setText(str(row[0]))
                  self.lab_cafe1[(0,3)].setText(str(row[1]))
                  self.button_cafe1[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b5=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=5")               
               for row in self.b5:
                  self.button_cafe1[(1,0)].setText(str(row[0]))
                  self.lab_cafe1[(1,0)].setText(str(row[1]))
                  self.button_cafe1[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b6=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=6")               
               for row in self.b6:
                  self.button_cafe1[(1,1)].setText(str(row[0]))
                  self.lab_cafe1[(1,1)].setText(str(row[1]))
                  self.button_cafe1[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b7=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=7")               
               for row in self.b7:
                  self.button_cafe1[(1,2)].setText(str(row[0]))
                  self.lab_cafe1[(1,2)].setText(str(row[1]))
                  self.button_cafe1[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b8=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=8")               
               for row in self.b8:
                  self.button_cafe1[(1,3)].setText(str(row[0]))
                  self.lab_cafe1[(1,3)].setText(str(row[1]))
                  self.button_cafe1[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b9=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=9")               
               for row in self.b9:
                  self.button_cafe1[(2,0)].setText(str(row[0]))
                  self.lab_cafe1[(2,0)].setText(str(row[1]))
                  self.button_cafe1[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b10=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=10")               
               for row in self.b10:
                  self.button_cafe1[(2,1)].setText(str(row[0]))
                  self.lab_cafe1[(2,1)].setText(str(row[1]))
                  self.button_cafe1[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b11=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=11")               
               for row in self.b11:
                  self.button_cafe1[(2,2)].setText(str(row[0]))
                  self.lab_cafe1[(2,2)].setText(str(row[1]))
                  self.button_cafe1[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b12=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=12")               
               for row in self.b12:
                  self.button_cafe1[(2,3)].setText(str(row[0]))
                  self.lab_cafe1[(2,3)].setText(str(row[1]))
                  self.button_cafe1[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b13=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=13")               
               for row in self.b13:
                  self.button_cafe1[(3,0)].setText(str(row[0]))
                  self.lab_cafe1[(3,0)].setText(str(row[1]))
                  self.button_cafe1[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b14=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=14")               
               for row in self.b14:
                  self.button_cafe1[(3,1)].setText(str(row[0]))
                  self.lab_cafe1[(3,1)].setText(str(row[1]))
                  self.button_cafe1[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b15=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=15")               
               for row in self.b15:
                  self.button_cafe1[(3,2)].setText(str(row[0]))
                  self.lab_cafe1[(3,2)].setText(str(row[1]))
                  self.button_cafe1[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b16=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=16")               
               for row in self.b16:
                  self.button_cafe1[(3,3)].setText(str(row[0]))
                  self.lab_cafe1[(3,3)].setText(str(row[1]))
                  self.button_cafe1[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 2
               self.b17=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=17")               
               for row in self.b17:
                  self.button_cafe2[(0,0)].setText(str(row[0]))
                  self.lab_cafe2[(0,0)].setText(str(row[1]))
                  self.button_cafe2[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b18=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=18")               
               for row in self.b18:
                  self.button_cafe2[(0,1)].setText(str(row[0]))
                  self.lab_cafe2[(0,1)].setText(str(row[1]))
                  self.button_cafe2[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b19=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=19")               
               for row in self.b19:
                  self.button_cafe2[(0,2)].setText(str(row[0]))
                  self.lab_cafe2[(0,2)].setText(str(row[1]))
                  self.button_cafe2[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b20=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=20")               
               for row in self.b20:
                  self.button_cafe2[(0,3)].setText(str(row[0]))
                  self.lab_cafe2[(0,3)].setText(str(row[1]))
                  self.button_cafe2[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b21=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=21")               
               for row in self.b21:
                  self.button_cafe2[(1,0)].setText(str(row[0]))
                  self.lab_cafe2[(1,0)].setText(str(row[1]))
                  self.button_cafe2[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b22=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=22")               
               for row in self.b22:
                  self.button_cafe2[(1,1)].setText(str(row[0]))
                  self.lab_cafe2[(1,1)].setText(str(row[1]))
                  self.button_cafe2[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b23=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=23")               
               for row in self.b23:
                  self.button_cafe2[(1,2)].setText(str(row[0]))
                  self.lab_cafe2[(1,2)].setText(str(row[1]))
                  self.button_cafe2[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b24=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=24")               
               for row in self.b24:
                  self.button_cafe2[(1,3)].setText(str(row[0]))
                  self.lab_cafe2[(1,3)].setText(str(row[1]))
                  self.button_cafe2[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b25=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=25")               
               for row in self.b25:
                  self.button_cafe2[(2,0)].setText(str(row[0]))
                  self.lab_cafe2[(2,0)].setText(str(row[1]))
                  self.button_cafe2[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b26=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=26")               
               for row in self.b26:
                  self.button_cafe2[(2,1)].setText(str(row[0]))
                  self.lab_cafe2[(2,1)].setText(str(row[1]))
                  self.button_cafe2[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b27=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=27")               
               for row in self.b27:
                  self.button_cafe2[(2,2)].setText(str(row[0]))
                  self.lab_cafe2[(2,2)].setText(str(row[1]))
                  self.button_cafe2[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b28=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=28")               
               for row in self.b28:
                  self.button_cafe2[(2,3)].setText(str(row[0]))
                  self.lab_cafe2[(2,3)].setText(str(row[1]))
                  self.button_cafe2[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b29=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=29")               
               for row in self.b29:
                  self.button_cafe2[(3,0)].setText(str(row[0]))
                  self.lab_cafe2[(3,0)].setText(str(row[1]))
                  self.button_cafe2[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b30=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=30")               
               for row in self.b30:
                  self.button_cafe2[(3,1)].setText(str(row[0]))
                  self.lab_cafe2[(3,1)].setText(str(row[1]))
                  self.button_cafe2[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b31=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=31")               
               for row in self.b31:
                  self.button_cafe2[(3,2)].setText(str(row[0]))
                  self.lab_cafe2[(3,2)].setText(str(row[1]))
                  self.button_cafe2[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b32=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=32")               
               for row in self.b32:
                  self.button_cafe2[(3,3)].setText(str(row[0]))
                  self.lab_cafe2[(3,3)].setText(str(row[1]))
                  self.button_cafe2[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 3
               self.b33=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=33")               
               for row in self.b33:
                  self.button_cafe3[(0,0)].setText(str(row[0]))
                  self.lab_cafe3[(0,0)].setText(str(row[1]))
                  self.button_cafe3[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b34=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=34")               
               for row in self.b34:
                  self.button_cafe3[(0,1)].setText(str(row[0]))
                  self.lab_cafe3[(0,1)].setText(str(row[1]))
                  self.button_cafe3[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b35=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=35")               
               for row in self.b35:
                  self.button_cafe3[(0,2)].setText(str(row[0]))
                  self.lab_cafe3[(0,2)].setText(str(row[1]))
                  self.button_cafe3[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b36=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=36")               
               for row in self.b36:
                  self.button_cafe3[(0,3)].setText(str(row[0]))
                  self.lab_cafe3[(0,3)].setText(str(row[1]))
                  self.button_cafe3[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b37=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=37")               
               for row in self.b37:
                  self.button_cafe3[(1,0)].setText(str(row[0]))
                  self.lab_cafe3[(1,0)].setText(str(row[1]))
                  self.button_cafe3[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b38=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=38")               
               for row in self.b38:
                  self.button_cafe3[(1,1)].setText(str(row[0]))
                  self.lab_cafe3[(1,1)].setText(str(row[1]))
                  self.button_cafe3[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b39=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=39")               
               for row in self.b39:
                  self.button_cafe3[(1,2)].setText(str(row[0]))
                  self.lab_cafe3[(1,2)].setText(str(row[1]))
                  self.button_cafe3[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b40=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=40")               
               for row in self.b40:
                  self.button_cafe3[(1,3)].setText(str(row[0]))
                  self.lab_cafe3[(1,3)].setText(str(row[1]))
                  self.button_cafe3[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b41=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=41")               
               for row in self.b41:
                  self.button_cafe3[(2,0)].setText(str(row[0]))
                  self.lab_cafe3[(2,0)].setText(str(row[1]))
                  self.button_cafe3[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b42=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=42")               
               for row in self.b42:
                  self.button_cafe3[(2,1)].setText(str(row[0]))
                  self.lab_cafe3[(2,1)].setText(str(row[1]))
                  self.button_cafe3[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b43=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=43")               
               for row in self.b43:
                  self.button_cafe3[(2,2)].setText(str(row[0]))
                  self.lab_cafe3[(2,2)].setText(str(row[1]))
                  self.button_cafe3[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b44=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=44")               
               for row in self.b44:
                  self.button_cafe3[(2,3)].setText(str(row[0]))
                  self.lab_cafe3[(2,3)].setText(str(row[1]))
                  self.button_cafe3[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b45=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=45")               
               for row in self.b45:
                  self.button_cafe3[(3,0)].setText(str(row[0]))
                  self.lab_cafe3[(3,0)].setText(str(row[1]))
                  self.button_cafe3[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b46=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=46")               
               for row in self.b46:
                  self.button_cafe3[(3,1)].setText(str(row[0]))
                  self.lab_cafe3[(3,1)].setText(str(row[1]))
                  self.button_cafe3[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b47=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=47")               
               for row in self.b47:
                  self.button_cafe3[(3,2)].setText(str(row[0]))
                  self.lab_cafe3[(3,2)].setText(str(row[1]))
                  self.button_cafe3[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b48=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=48")               
               for row in self.b48:
                  self.button_cafe3[(3,3)].setText(str(row[0]))
                  self.lab_cafe3[(3,3)].setText(str(row[1]))
                  self.button_cafe3[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 4
               self.b49=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=49")               
               for row in self.b49:
                  self.button_cafe4[(0,0)].setText(str(row[0]))
                  self.lab_cafe4[(0,0)].setText(str(row[1]))
                  self.button_cafe4[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b50=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=50")           
               for row in self.b50:
                  self.button_cafe4[(0,1)].setText(str(row[0]))
                  self.lab_cafe4[(0,1)].setText(str(row[1]))
                  self.button_cafe4[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b51=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=51")               
               for row in self.b51:
                  self.button_cafe4[(0,2)].setText(str(row[0]))
                  self.lab_cafe4[(0,2)].setText(str(row[1]))
                  self.button_cafe4[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b52=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=52")               
               for row in self.b52:
                  self.button_cafe4[(0,3)].setText(str(row[0]))
                  self.lab_cafe4[(0,3)].setText(str(row[1]))
                  self.button_cafe4[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b53=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=53")               
               for row in self.b53:
                  self.button_cafe4[(1,0)].setText(str(row[0]))
                  self.lab_cafe4[(1,0)].setText(str(row[1]))
                  self.button_cafe4[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b54=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=54")               
               for row in self.b54:
                  self.button_cafe4[(1,1)].setText(str(row[0]))
                  self.lab_cafe4[(1,1)].setText(str(row[1]))
                  self.button_cafe4[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b55=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=55")               
               for row in self.b55:
                  self.button_cafe4[(1,2)].setText(str(row[0]))
                  self.lab_cafe4[(1,2)].setText(str(row[1]))
                  self.button_cafe4[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b56=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=56")               
               for row in self.b56:
                  self.button_cafe4[(1,3)].setText(str(row[0]))
                  self.lab_cafe4[(1,3)].setText(str(row[1]))
                  self.button_cafe4[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b57=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=57")               
               for row in self.b57:
                  self.button_cafe4[(2,0)].setText(str(row[0]))
                  self.lab_cafe4[(2,0)].setText(str(row[1]))
                  self.button_cafe4[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b58=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=58")               
               for row in self.b58:
                  self.button_cafe4[(2,1)].setText(str(row[0]))
                  self.lab_cafe4[(2,1)].setText(str(row[1]))
                  self.button_cafe4[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b59=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=59")               
               for row in self.b59:
                  self.button_cafe4[(2,2)].setText(str(row[0]))
                  self.lab_cafe4[(2,2)].setText(str(row[1]))
                  self.button_cafe4[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b60=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=60")               
               for row in self.b60:
                  self.button_cafe4[(2,3)].setText(str(row[0]))
                  self.lab_cafe4[(2,3)].setText(str(row[1]))
                  self.button_cafe4[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b61=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=61")               
               for row in self.b61:
                  self.button_cafe4[(3,0)].setText(str(row[0]))
                  self.lab_cafe4[(3,0)].setText(str(row[1]))
                  self.button_cafe4[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b62=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=62")               
               for row in self.b62:
                  self.button_cafe4[(3,1)].setText(str(row[0]))
                  self.lab_cafe4[(3,1)].setText(str(row[1]))
                  self.button_cafe4[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b63=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=63")               
               for row in self.b63:
                  self.button_cafe4[(3,2)].setText(str(row[0]))
                  self.lab_cafe4[(3,2)].setText(str(row[1]))
                  self.button_cafe4[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b64=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=64")               
               for row in self.b64:
                  self.button_cafe4[(3,3)].setText(str(row[0]))
                  self.lab_cafe4[(3,3)].setText(str(row[1]))
                  self.button_cafe4[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 5
               self.b65=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=65")               
               for row in self.b65:
                  self.button_cafe5[(0,0)].setText(str(row[0]))
                  self.lab_cafe5[(0,0)].setText(str(row[1]))
                  self.button_cafe5[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b66=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=66")             
               for row in self.b66:
                  self.button_cafe5[(0,1)].setText(str(row[0]))
                  self.lab_cafe5[(0,1)].setText(str(row[1]))
                  self.button_cafe5[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b67=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=67")               
               for row in self.b67:
                  self.button_cafe5[(0,2)].setText(str(row[0]))
                  self.lab_cafe5[(0,2)].setText(str(row[1]))
                  self.button_cafe5[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b68=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=68")               
               for row in self.b68:
                  self.button_cafe5[(0,3)].setText(str(row[0]))
                  self.lab_cafe5[(0,3)].setText(str(row[1]))
                  self.button_cafe5[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b69=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=69")               
               for row in self.b69:
                  self.button_cafe5[(1,0)].setText(str(row[0]))
                  self.lab_cafe5[(1,0)].setText(str(row[1]))
                  self.button_cafe5[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b70=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=70")               
               for row in self.b70:
                  self.button_cafe5[(1,1)].setText(str(row[0]))
                  self.lab_cafe5[(1,1)].setText(str(row[1]))
                  self.button_cafe5[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b71=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=71")               
               for row in self.b71:
                  self.button_cafe5[(1,2)].setText(str(row[0]))
                  self.lab_cafe5[(1,2)].setText(str(row[1]))
                  self.button_cafe5[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b72=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=72")               
               for row in self.b72:
                  self.button_cafe5[(1,3)].setText(str(row[0]))
                  self.lab_cafe5[(1,3)].setText(str(row[1]))
                  self.button_cafe5[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b73=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=73")               
               for row in self.b73:
                  self.button_cafe5[(2,0)].setText(str(row[0]))
                  self.lab_cafe5[(2,0)].setText(str(row[1]))
                  self.button_cafe5[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b74=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=74")               
               for row in self.b74:
                  self.button_cafe5[(2,1)].setText(str(row[0]))
                  self.lab_cafe5[(2,1)].setText(str(row[1]))
                  self.button_cafe5[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b75=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=75")               
               for row in self.b75:
                  self.button_cafe5[(2,2)].setText(str(row[0]))
                  self.lab_cafe5[(2,2)].setText(str(row[1]))
                  self.button_cafe5[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b76=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=76")               
               for row in self.b76:
                  self.button_cafe5[(2,3)].setText(str(row[0]))
                  self.lab_cafe5[(2,3)].setText(str(row[1]))
                  self.button_cafe5[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b77=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=77")               
               for row in self.b77:
                  self.button_cafe5[(3,0)].setText(str(row[0]))
                  self.lab_cafe5[(3,0)].setText(str(row[1]))
                  self.button_cafe5[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b78=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=78")               
               for row in self.b78:
                  self.button_cafe5[(3,1)].setText(str(row[0]))
                  self.lab_cafe5[(3,1)].setText(str(row[1]))
                  self.button_cafe5[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b79=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=79")               
               for row in self.b79:
                  self.button_cafe5[(3,2)].setText(str(row[0]))
                  self.lab_cafe5[(3,2)].setText(str(row[1]))
                  self.button_cafe5[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b80=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=80")               
               for row in self.b80:
                  self.button_cafe5[(3,3)].setText(str(row[0]))
                  self.lab_cafe5[(3,3)].setText(str(row[1]))
                  self.button_cafe5[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 6
               self.b81=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=81")               
               for row in self.b81:
                  self.button_cafe6[(0,0)].setText(str(row[0]))
                  self.lab_cafe6[(0,0)].setText(str(row[1]))
                  self.button_cafe6[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b82=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=82")               
               for row in self.b82:
                  self.button_cafe6[(0,1)].setText(str(row[0]))
                  self.lab_cafe6[(0,1)].setText(str(row[1]))
                  self.button_cafe6[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b83=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=83")               
               for row in self.b83:
                  self.button_cafe6[(0,2)].setText(str(row[0]))
                  self.lab_cafe6[(0,2)].setText(str(row[1]))
                  self.button_cafe6[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b84=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=84")               
               for row in self.b84:
                  self.button_cafe6[(0,3)].setText(str(row[0]))
                  self.lab_cafe6[(0,3)].setText(str(row[1]))
                  self.button_cafe6[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b85=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=85")               
               for row in self.b85:
                  self.button_cafe6[(1,0)].setText(str(row[0]))
                  self.lab_cafe6[(1,0)].setText(str(row[1]))
                  self.button_cafe6[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b86=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=86")               
               for row in self.b86:
                  self.button_cafe6[(1,1)].setText(str(row[0]))
                  self.lab_cafe6[(1,1)].setText(str(row[1]))
                  self.button_cafe6[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b87=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=87")               
               for row in self.b87:
                  self.button_cafe6[(1,2)].setText(str(row[0]))
                  self.lab_cafe6[(1,2)].setText(str(row[1]))
                  self.button_cafe6[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b88=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=88")               
               for row in self.b88:
                  self.button_cafe6[(1,3)].setText(str(row[0]))
                  self.lab_cafe6[(1,3)].setText(str(row[1]))
                  self.button_cafe6[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b89=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=89")               
               for row in self.b89:
                  self.button_cafe6[(2,0)].setText(str(row[0]))
                  self.lab_cafe6[(2,0)].setText(str(row[1]))
                  self.button_cafe6[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b90=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=90")               
               for row in self.b90:
                  self.button_cafe6[(2,1)].setText(str(row[0]))
                  self.lab_cafe6[(2,1)].setText(str(row[1]))
                  self.button_cafe6[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b91=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=91")               
               for row in self.b91:
                  self.button_cafe6[(2,2)].setText(str(row[0]))
                  self.lab_cafe6[(2,2)].setText(str(row[1]))
                  self.button_cafe6[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b92=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=92")               
               for row in self.b92:
                  self.button_cafe6[(2,3)].setText(str(row[0]))
                  self.lab_cafe6[(2,3)].setText(str(row[1]))
                  self.button_cafe6[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b93=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=93")               
               for row in self.b93:
                  self.button_cafe6[(3,0)].setText(str(row[0]))
                  self.lab_cafe6[(3,0)].setText(str(row[1]))
                  self.button_cafe6[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b94=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=94")               
               for row in self.b94:
                  self.button_cafe6[(3,1)].setText(str(row[0]))
                  self.lab_cafe6[(3,1)].setText(str(row[1]))
                  self.button_cafe6[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b95=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=95")               
               for row in self.b95:
                  self.button_cafe6[(3,2)].setText(str(row[0]))
                  self.lab_cafe6[(3,2)].setText(str(row[1]))
                  self.button_cafe6[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b96=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=96")               
               for row in self.b96:
                  self.button_cafe6[(3,3)].setText(str(row[0]))
                  self.lab_cafe6[(3,3)].setText(str(row[1]))
                  self.button_cafe6[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 7
               self.b97=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=97")               
               for row in self.b97:
                  self.button_cafe7[(0,0)].setText(str(row[0]))
                  self.lab_cafe7[(0,0)].setText(str(row[1]))
                  self.button_cafe7[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b98=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=98")               
               for row in self.b98:
                  self.button_cafe7[(0,1)].setText(str(row[0]))
                  self.lab_cafe7[(0,1)].setText(str(row[1]))
                  self.button_cafe7[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b99=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=99")               
               for row in self.b99:
                  self.button_cafe7[(0,2)].setText(str(row[0]))
                  self.lab_cafe7[(0,2)].setText(str(row[1]))
                  self.button_cafe7[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b100=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=100")               
               for row in self.b100:
                  self.button_cafe7[(0,3)].setText(str(row[0]))
                  self.lab_cafe7[(0,3)].setText(str(row[1]))
                  self.button_cafe7[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b101=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=101")               
               for row in self.b101:
                  self.button_cafe7[(1,0)].setText(str(row[0]))
                  self.lab_cafe7[(1,0)].setText(str(row[1]))
                  self.button_cafe7[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b102=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=102")               
               for row in self.b101:
                  self.button_cafe7[(1,1)].setText(str(row[0]))
                  self.lab_cafe7[(1,1)].setText(str(row[1]))
                  self.button_cafe7[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b103=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=103")               
               for row in self.b103:
                  self.button_cafe7[(1,2)].setText(str(row[0]))
                  self.lab_cafe7[(1,2)].setText(str(row[1]))
                  self.button_cafe7[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b104=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=104")               
               for row in self.b104:
                  self.button_cafe7[(1,3)].setText(str(row[0]))
                  self.lab_cafe7[(1,3)].setText(str(row[1]))
                  self.button_cafe7[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b105=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=105")               
               for row in self.b105:
                  self.button_cafe7[(2,0)].setText(str(row[0]))
                  self.lab_cafe7[(2,0)].setText(str(row[1]))
                  self.button_cafe7[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b106=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=106")               
               for row in self.b106:
                  self.button_cafe7[(2,1)].setText(str(row[0]))
                  self.lab_cafe7[(2,1)].setText(str(row[1]))
                  self.button_cafe7[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b107=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=107")               
               for row in self.b107:
                  self.button_cafe7[(2,2)].setText(str(row[0]))
                  self.lab_cafe7[(2,2)].setText(str(row[1]))
                  self.button_cafe7[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b108=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=108")               
               for row in self.b108:
                  self.button_cafe7[(2,3)].setText(str(row[0]))
                  self.lab_cafe7[(2,3)].setText(str(row[1]))
                  self.button_cafe7[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b109=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=109")               
               for row in self.b109:
                  self.button_cafe7[(3,0)].setText(str(row[0]))
                  self.lab_cafe7[(3,0)].setText(str(row[1]))
                  self.button_cafe7[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b110=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=110")               
               for row in self.b110:
                  self.button_cafe7[(3,1)].setText(str(row[0]))
                  self.lab_cafe7[(3,1)].setText(str(row[1]))
                  self.button_cafe7[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b111=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=111")               
               for row in self.b111:
                  self.button_cafe7[(3,2)].setText(str(row[0]))
                  self.lab_cafe7[(3,2)].setText(str(row[1]))
                  self.button_cafe7[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b112=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=112")               
               for row in self.b112:
                  self.button_cafe7[(3,3)].setText(str(row[0]))
                  self.lab_cafe7[(3,3)].setText(str(row[1]))
                  self.button_cafe7[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 8
               self.b113=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=113")               
               for row in self.b113:
                  self.button_cafe8[(0,0)].setText(str(row[0]))
                  self.lab_cafe8[(0,0)].setText(str(row[1]))
                  self.button_cafe8[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b114=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=114")           
               for row in self.b114:
                  self.button_cafe8[(0,1)].setText(str(row[0]))
                  self.lab_cafe8[(0,1)].setText(str(row[1]))
                  self.button_cafe8[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b115=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=115")               
               for row in self.b115:
                  self.button_cafe8[(0,2)].setText(str(row[0]))
                  self.lab_cafe8[(0,2)].setText(str(row[1]))
                  self.button_cafe8[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b116=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=116")               
               for row in self.b116:
                  self.button_cafe8[(0,3)].setText(str(row[0]))
                  self.lab_cafe8[(0,3)].setText(str(row[1]))
                  self.button_cafe8[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b117=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=117")               
               for row in self.b117:
                  self.button_cafe8[(1,0)].setText(str(row[0]))
                  self.lab_cafe8[(1,0)].setText(str(row[1]))
                  self.button_cafe8[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b118=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=118")               
               for row in self.b118:
                  self.button_cafe8[(1,1)].setText(str(row[0]))
                  self.lab_cafe8[(1,1)].setText(str(row[1]))
                  self.button_cafe8[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b119=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=119")               
               for row in self.b119:
                  self.button_cafe8[(1,2)].setText(str(row[0]))
                  self.lab_cafe8[(1,2)].setText(str(row[1]))
                  self.button_cafe8[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b120=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=120")               
               for row in self.b120:
                  self.button_cafe4[(1,3)].setText(str(row[0]))
                  self.lab_cafe8[(1,3)].setText(str(row[1]))
                  self.button_cafe8[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b121=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=121")               
               for row in self.b121:
                  self.button_cafe8[(2,0)].setText(str(row[0]))
                  self.lab_cafe8[(2,0)].setText(str(row[1]))
                  self.button_cafe8[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b122=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=122")               
               for row in self.b122:
                  self.button_cafe8[(2,1)].setText(str(row[0]))
                  self.lab_cafe8[(2,1)].setText(str(row[1]))
                  self.button_cafe8[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b123=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=123")               
               for row in self.b123:
                  self.button_cafe8[(2,2)].setText(str(row[0]))
                  self.lab_cafe8[(2,2)].setText(str(row[1]))
                  self.button_cafe8[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b124=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=124")               
               for row in self.b124:
                  self.button_cafe8[(2,3)].setText(str(row[0]))
                  self.lab_cafe8[(2,3)].setText(str(row[1]))
                  self.button_cafe8[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b125=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=125")               
               for row in self.b125:
                  self.button_cafe8[(3,0)].setText(str(row[0]))
                  self.lab_cafe8[(3,0)].setText(str(row[1]))
                  self.button_cafe8[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b126=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=126")               
               for row in self.b126:
                  self.button_cafe8[(3,1)].setText(str(row[0]))
                  self.lab_cafe8[(3,1)].setText(str(row[1]))
                  self.button_cafe8[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b127=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=127")               
               for row in self.b127:
                  self.button_cafe8[(3,2)].setText(str(row[0]))
                  self.lab_cafe8[(3,2)].setText(str(row[1]))
                  self.button_cafe8[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b128=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=128")               
               for row in self.b128:
                  self.button_cafe8[(3,3)].setText(str(row[0]))
                  self.lab_cafe8[(3,3)].setText(str(row[1]))
                  self.button_cafe8[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.bdd.commit()
               #====================== REFRESH LAB ==#
               #=====================================#
               for x in range(4):
                  for y in range(4):
                     #====================== CAFES
                     self.lab_cafe1[(x,y)].adjustSize()
                     self.lab_cafe2[(x,y)].adjustSize()
                     self.lab_cafe3[(x,y)].adjustSize()
                     self.lab_cafe4[(x,y)].adjustSize()
                     self.lab_cafe5[(x,y)].adjustSize()
                     self.lab_cafe6[(x,y)].adjustSize()
                     self.lab_cafe7[(x,y)].adjustSize()
                     self.lab_cafe8[(x,y)].adjustSize()
            elif self.bdd and self.zone_title.text()=='PLATS':
               self.cursor=self.bdd.cursor()
               #________PAGE 1
               self.b1=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=1")               
               for row in self.b1:
                  self.button_plat1[(0,0)].setText(str(row[0]))
                  self.lab_plat1[(0,0)].setText(str(row[1]))
                  self.button_plat1[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b2=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=2")             
               for row in self.b2:
                  self.button_plat1[(0,1)].setText(str(row[0]))
                  self.lab_plat1[(0,1)].setText(str(row[1]))
                  self.button_plat1[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b3=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=3")               
               for row in self.b3:
                  self.button_plat1[(0,2)].setText(str(row[0]))
                  self.lab_plat1[(0,2)].setText(str(row[1]))
                  self.button_plat1[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b4=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=4")               
               for row in self.b4:
                  self.button_plat1[(0,3)].setText(str(row[0]))
                  self.lab_plat1[(0,3)].setText(str(row[1]))
                  self.button_plat1[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b5=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=5")               
               for row in self.b5:
                  self.button_plat1[(1,0)].setText(str(row[0]))
                  self.lab_plat1[(1,0)].setText(str(row[1]))
                  self.button_plat1[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b6=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=6")               
               for row in self.b6:
                  self.button_plat1[(1,1)].setText(str(row[0]))
                  self.lab_plat1[(1,1)].setText(str(row[1]))
                  self.button_plat1[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b7=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=7")               
               for row in self.b7:
                  self.button_plat1[(1,2)].setText(str(row[0]))
                  self.lab_plat1[(1,2)].setText(str(row[1]))
                  self.button_plat1[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b8=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=8")               
               for row in self.b8:
                  self.button_plat1[(1,3)].setText(str(row[0]))
                  self.lab_plat1[(1,3)].setText(str(row[1]))
                  self.button_plat1[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b9=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=9")               
               for row in self.b9:
                  self.button_plat1[(2,0)].setText(str(row[0]))
                  self.lab_plat1[(2,0)].setText(str(row[1]))
                  self.button_plat1[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b10=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=10")               
               for row in self.b10:
                  self.button_plat1[(2,1)].setText(str(row[0]))
                  self.lab_plat1[(2,1)].setText(str(row[1]))
                  self.button_plat1[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b11=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=11")               
               for row in self.b11:
                  self.button_plat1[(2,2)].setText(str(row[0]))
                  self.lab_plat1[(2,2)].setText(str(row[1]))
                  self.button_plat1[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b12=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=12")               
               for row in self.b12:
                  self.button_plat1[(2,3)].setText(str(row[0]))
                  self.lab_plat1[(2,3)].setText(str(row[1]))
                  self.button_plat1[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b13=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=13")               
               for row in self.b13:
                  self.button_plat1[(3,0)].setText(str(row[0]))
                  self.lab_plat1[(3,0)].setText(str(row[1]))
                  self.button_plat1[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b14=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=14")               
               for row in self.b14:
                  self.button_plat1[(3,1)].setText(str(row[0]))
                  self.lab_plat1[(3,1)].setText(str(row[1]))
                  self.button_plat1[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b15=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=15")               
               for row in self.b15:
                  self.button_plat1[(3,2)].setText(str(row[0]))
                  self.lab_plat1[(3,2)].setText(str(row[1]))
                  self.button_plat1[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b16=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=16")               
               for row in self.b16:
                  self.button_plat1[(3,3)].setText(str(row[0]))
                  self.lab_plat1[(3,3)].setText(str(row[1]))
                  self.button_plat1[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 2
               self.b17=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=17")               
               for row in self.b17:
                  self.button_plat2[(0,0)].setText(str(row[0]))
                  self.lab_plat2[(0,0)].setText(str(row[1]))
                  self.button_plat2[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b18=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=18")               
               for row in self.b18:
                  self.button_plat2[(0,1)].setText(str(row[0]))
                  self.lab_plat2[(0,1)].setText(str(row[1]))
                  self.button_plat2[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b19=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=19")               
               for row in self.b19:
                  self.button_plat2[(0,2)].setText(str(row[0]))
                  self.lab_plat2[(0,2)].setText(str(row[1]))
                  self.button_plat2[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b20=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=20")               
               for row in self.b20:
                  self.button_plat2[(0,3)].setText(str(row[0]))
                  self.lab_plat2[(0,3)].setText(str(row[1]))
                  self.button_plat2[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b21=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=21")               
               for row in self.b21:
                  self.button_plat2[(1,0)].setText(str(row[0]))
                  self.lab_plat2[(1,0)].setText(str(row[1]))
                  self.button_plat2[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b22=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=22")               
               for row in self.b22:
                  self.button_plat2[(1,1)].setText(str(row[0]))
                  self.lab_plat2[(1,1)].setText(str(row[1]))
                  self.button_plat2[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b23=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=23")               
               for row in self.b23:
                  self.button_plat2[(1,2)].setText(str(row[0]))
                  self.lab_plat2[(1,2)].setText(str(row[1]))
                  self.button_plat2[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b24=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=24")               
               for row in self.b24:
                  self.button_plat2[(1,3)].setText(str(row[0]))
                  self.lab_plat2[(1,3)].setText(str(row[1]))
                  self.button_plat2[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b25=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=25")               
               for row in self.b25:
                  self.button_plat2[(2,0)].setText(str(row[0]))
                  self.lab_plat2[(2,0)].setText(str(row[1]))
                  self.button_plat2[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b26=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=26")               
               for row in self.b26:
                  self.button_plat2[(2,1)].setText(str(row[0]))
                  self.lab_plat2[(2,1)].setText(str(row[1]))
                  self.button_plat2[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b27=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=27")               
               for row in self.b27:
                  self.button_plat2[(2,2)].setText(str(row[0]))
                  self.lab_plat2[(2,2)].setText(str(row[1]))
                  self.button_plat2[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b28=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=28")               
               for row in self.b28:
                  self.button_plat2[(2,3)].setText(str(row[0]))
                  self.lab_plat2[(2,3)].setText(str(row[1]))
                  self.button_plat2[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b29=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=29")               
               for row in self.b29:
                  self.button_plat2[(3,0)].setText(str(row[0]))
                  self.lab_plat2[(3,0)].setText(str(row[1]))
                  self.button_plat2[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b30=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=30")               
               for row in self.b30:
                  self.button_plat2[(3,1)].setText(str(row[0]))
                  self.lab_plat2[(3,1)].setText(str(row[1]))
                  self.button_plat2[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b31=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=31")               
               for row in self.b31:
                  self.button_plat2[(3,2)].setText(str(row[0]))
                  self.lab_plat2[(3,2)].setText(str(row[1]))
                  self.button_plat2[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b32=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=32")               
               for row in self.b32:
                  self.button_plat2[(3,3)].setText(str(row[0]))
                  self.lab_plat2[(3,3)].setText(str(row[1]))
                  self.button_plat2[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 3
               self.b33=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=33")               
               for row in self.b33:
                  self.button_plat3[(0,0)].setText(str(row[0]))
                  self.lab_plat3[(0,0)].setText(str(row[1]))
                  self.button_plat3[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b34=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=34")               
               for row in self.b34:
                  self.button_plat3[(0,1)].setText(str(row[0]))
                  self.lab_plat3[(0,1)].setText(str(row[1]))
                  self.button_plat3[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b35=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=35")               
               for row in self.b35:
                  self.button_plat3[(0,2)].setText(str(row[0]))
                  self.lab_plat3[(0,2)].setText(str(row[1]))
                  self.button_plat3[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b36=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=36")               
               for row in self.b36:
                  self.button_plat3[(0,3)].setText(str(row[0]))
                  self.lab_plat3[(0,3)].setText(str(row[1]))
                  self.button_plat3[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b37=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=37")               
               for row in self.b37:
                  self.button_plat3[(1,0)].setText(str(row[0]))
                  self.lab_plat3[(1,0)].setText(str(row[1]))
                  self.button_plat3[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b38=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=38")               
               for row in self.b38:
                  self.button_plat3[(1,1)].setText(str(row[0]))
                  self.lab_plat3[(1,1)].setText(str(row[1]))
                  self.button_plat3[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b39=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=39")               
               for row in self.b39:
                  self.button_plat3[(1,2)].setText(str(row[0]))
                  self.lab_plat3[(1,2)].setText(str(row[1]))
                  self.button_plat3[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b40=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=40")               
               for row in self.b40:
                  self.button_plat3[(1,3)].setText(str(row[0]))
                  self.lab_plat3[(1,3)].setText(str(row[1]))
                  self.button_plat3[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b41=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=41")               
               for row in self.b41:
                  self.button_plat3[(2,0)].setText(str(row[0]))
                  self.lab_plat3[(2,0)].setText(str(row[1]))
                  self.button_plat3[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b42=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=42")               
               for row in self.b42:
                  self.button_plat3[(2,1)].setText(str(row[0]))
                  self.lab_plat3[(2,1)].setText(str(row[1]))
                  self.button_plat3[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b43=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=43")               
               for row in self.b43:
                  self.button_plat3[(2,2)].setText(str(row[0]))
                  self.lab_plat3[(2,2)].setText(str(row[1]))
                  self.button_plat3[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b44=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=44")               
               for row in self.b44:
                  self.button_plat3[(2,3)].setText(str(row[0]))
                  self.lab_plat3[(2,3)].setText(str(row[1]))
                  self.button_plat3[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b45=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=45")               
               for row in self.b45:
                  self.button_plat3[(3,0)].setText(str(row[0]))
                  self.lab_plat3[(3,0)].setText(str(row[1]))
                  self.button_plat3[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b46=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=46")               
               for row in self.b46:
                  self.button_plat3[(3,1)].setText(str(row[0]))
                  self.lab_plat3[(3,1)].setText(str(row[1]))
                  self.button_plat3[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b47=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=47")               
               for row in self.b47:
                  self.button_plat3[(3,2)].setText(str(row[0]))
                  self.lab_plat3[(3,2)].setText(str(row[1]))
                  self.button_plat3[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b48=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=48")               
               for row in self.b48:
                  self.button_plat3[(3,3)].setText(str(row[0]))
                  self.lab_plat3[(3,3)].setText(str(row[1]))
                  self.button_plat3[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 4
               self.b49=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=49")               
               for row in self.b49:
                  self.button_plat4[(0,0)].setText(str(row[0]))
                  self.lab_plat4[(0,0)].setText(str(row[1]))
                  self.button_plat4[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b50=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=50")           
               for row in self.b50:
                  self.button_plat4[(0,1)].setText(str(row[0]))
                  self.lab_plat4[(0,1)].setText(str(row[1]))
                  self.button_plat4[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b51=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=51")               
               for row in self.b51:
                  self.button_plat4[(0,2)].setText(str(row[0]))
                  self.lab_plat4[(0,2)].setText(str(row[1]))
                  self.button_plat4[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b52=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=52")               
               for row in self.b52:
                  self.button_plat4[(0,3)].setText(str(row[0]))
                  self.lab_plat4[(0,3)].setText(str(row[1]))
                  self.button_plat4[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b53=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=53")               
               for row in self.b53:
                  self.button_plat4[(1,0)].setText(str(row[0]))
                  self.lab_plat4[(1,0)].setText(str(row[1]))
                  self.button_plat4[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b54=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=54")               
               for row in self.b54:
                  self.button_plat4[(1,1)].setText(str(row[0]))
                  self.lab_plat4[(1,1)].setText(str(row[1]))
                  self.button_plat4[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b55=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=55")               
               for row in self.b55:
                  self.button_plat4[(1,2)].setText(str(row[0]))
                  self.lab_plat4[(1,2)].setText(str(row[1]))
                  self.button_plat4[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b56=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=56")               
               for row in self.b56:
                  self.button_plat4[(1,3)].setText(str(row[0]))
                  self.lab_plat4[(1,3)].setText(str(row[1]))
                  self.button_plat4[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b57=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=57")               
               for row in self.b57:
                  self.button_plat4[(2,0)].setText(str(row[0]))
                  self.lab_plat4[(2,0)].setText(str(row[1]))
                  self.button_plat4[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b58=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=58")               
               for row in self.b58:
                  self.button_plat4[(2,1)].setText(str(row[0]))
                  self.lab_plat4[(2,1)].setText(str(row[1]))
                  self.button_plat4[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b59=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=59")               
               for row in self.b59:
                  self.button_plat4[(2,2)].setText(str(row[0]))
                  self.lab_plat4[(2,2)].setText(str(row[1]))
                  self.button_plat4[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b60=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=60")               
               for row in self.b60:
                  self.button_plat4[(2,3)].setText(str(row[0]))
                  self.lab_plat4[(2,3)].setText(str(row[1]))
                  self.button_plat4[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b61=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=61")               
               for row in self.b61:
                  self.button_plat4[(3,0)].setText(str(row[0]))
                  self.lab_plat4[(3,0)].setText(str(row[1]))
                  self.button_plat4[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b62=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=62")               
               for row in self.b62:
                  self.button_plat4[(3,1)].setText(str(row[0]))
                  self.lab_plat4[(3,1)].setText(str(row[1]))
                  self.button_plat4[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b63=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=63")               
               for row in self.b63:
                  self.button_plat4[(3,2)].setText(str(row[0]))
                  self.lab_plat4[(3,2)].setText(str(row[1]))
                  self.button_plat4[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b64=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=64")               
               for row in self.b64:
                  self.button_plat4[(3,3)].setText(str(row[0]))
                  self.lab_plat4[(3,3)].setText(str(row[1]))
                  self.button_plat4[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 5
               self.b65=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=65")               
               for row in self.b65:
                  self.button_plat5[(0,0)].setText(str(row[0]))
                  self.lab_plat5[(0,0)].setText(str(row[1]))
                  self.button_plat5[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b66=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=66")             
               for row in self.b66:
                  self.button_plat5[(0,1)].setText(str(row[0]))
                  self.lab_plat5[(0,1)].setText(str(row[1]))
                  self.button_plat5[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b67=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=67")               
               for row in self.b67:
                  self.button_plat5[(0,2)].setText(str(row[0]))
                  self.lab_plat5[(0,2)].setText(str(row[1]))
                  self.button_plat5[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b68=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=68")               
               for row in self.b68:
                  self.button_plat5[(0,3)].setText(str(row[0]))
                  self.lab_plat5[(0,3)].setText(str(row[1]))
                  self.button_plat5[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b69=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=69")               
               for row in self.b69:
                  self.button_plat5[(1,0)].setText(str(row[0]))
                  self.lab_plat5[(1,0)].setText(str(row[1]))
                  self.button_plat5[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b70=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=70")               
               for row in self.b70:
                  self.button_plat5[(1,1)].setText(str(row[0]))
                  self.lab_plat5[(1,1)].setText(str(row[1]))
                  self.button_plat5[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b71=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=71")               
               for row in self.b71:
                  self.button_plat5[(1,2)].setText(str(row[0]))
                  self.lab_plat5[(1,2)].setText(str(row[1]))
                  self.button_plat5[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b72=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=72")               
               for row in self.b72:
                  self.button_plat5[(1,3)].setText(str(row[0]))
                  self.lab_plat5[(1,3)].setText(str(row[1]))
                  self.button_plat5[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b73=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=73")               
               for row in self.b73:
                  self.button_plat5[(2,0)].setText(str(row[0]))
                  self.lab_plat5[(2,0)].setText(str(row[1]))
                  self.button_plat5[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b74=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=74")               
               for row in self.b74:
                  self.button_plat5[(2,1)].setText(str(row[0]))
                  self.lab_plat5[(2,1)].setText(str(row[1]))
                  self.button_plat5[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b75=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=75")               
               for row in self.b75:
                  self.button_plat5[(2,2)].setText(str(row[0]))
                  self.lab_plat5[(2,2)].setText(str(row[1]))
                  self.button_plat5[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b76=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=76")               
               for row in self.b76:
                  self.button_plat5[(2,3)].setText(str(row[0]))
                  self.lab_plat5[(2,3)].setText(str(row[1]))
                  self.button_plat5[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b77=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=77")               
               for row in self.b77:
                  self.button_plat5[(3,0)].setText(str(row[0]))
                  self.lab_plat5[(3,0)].setText(str(row[1]))
                  self.button_plat5[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b78=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=78")               
               for row in self.b78:
                  self.button_plat5[(3,1)].setText(str(row[0]))
                  self.lab_plat5[(3,1)].setText(str(row[1]))
                  self.button_plat5[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b79=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=79")               
               for row in self.b79:
                  self.button_plat5[(3,2)].setText(str(row[0]))
                  self.lab_plat5[(3,2)].setText(str(row[1]))
                  self.button_plat5[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b80=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=80")               
               for row in self.b80:
                  self.button_plat5[(3,3)].setText(str(row[0]))
                  self.lab_plat5[(3,3)].setText(str(row[1]))
                  self.button_plat5[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 6
               self.b81=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=81")               
               for row in self.b81:
                  self.button_plat6[(0,0)].setText(str(row[0]))
                  self.lab_plat6[(0,0)].setText(str(row[1]))
                  self.button_plat6[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b82=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=82")               
               for row in self.b82:
                  self.button_plat6[(0,1)].setText(str(row[0]))
                  self.lab_plat6[(0,1)].setText(str(row[1]))
                  self.button_plat6[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b83=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=83")               
               for row in self.b83:
                  self.button_plat6[(0,2)].setText(str(row[0]))
                  self.lab_plat6[(0,2)].setText(str(row[1]))
                  self.button_plat6[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b84=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=84")               
               for row in self.b84:
                  self.button_plat6[(0,3)].setText(str(row[0]))
                  self.lab_plat6[(0,3)].setText(str(row[1]))
                  self.button_plat6[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b85=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=85")               
               for row in self.b85:
                  self.button_plat6[(1,0)].setText(str(row[0]))
                  self.lab_plat6[(1,0)].setText(str(row[1]))
                  self.button_plat6[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b86=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=86")               
               for row in self.b86:
                  self.button_plat6[(1,1)].setText(str(row[0]))
                  self.lab_plat6[(1,1)].setText(str(row[1]))
                  self.button_plat6[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b87=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=87")               
               for row in self.b87:
                  self.button_plat6[(1,2)].setText(str(row[0]))
                  self.lab_plat6[(1,2)].setText(str(row[1]))
                  self.button_plat6[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b88=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=88")               
               for row in self.b88:
                  self.button_plat6[(1,3)].setText(str(row[0]))
                  self.lab_plat6[(1,3)].setText(str(row[1]))
                  self.button_plat6[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b89=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=89")               
               for row in self.b89:
                  self.button_plat6[(2,0)].setText(str(row[0]))
                  self.lab_plat6[(2,0)].setText(str(row[1]))
                  self.button_plat6[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b90=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=90")               
               for row in self.b90:
                  self.button_plat6[(2,1)].setText(str(row[0]))
                  self.lab_plat6[(2,1)].setText(str(row[1]))
                  self.button_plat6[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b91=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=91")               
               for row in self.b91:
                  self.button_plat6[(2,2)].setText(str(row[0]))
                  self.lab_plat6[(2,2)].setText(str(row[1]))
                  self.button_plat6[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b92=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=92")               
               for row in self.b92:
                  self.button_plat6[(2,3)].setText(str(row[0]))
                  self.lab_plat6[(2,3)].setText(str(row[1]))
                  self.button_plat6[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b93=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=93")               
               for row in self.b93:
                  self.button_plat6[(3,0)].setText(str(row[0]))
                  self.lab_plat6[(3,0)].setText(str(row[1]))
                  self.button_plat6[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b94=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=94")               
               for row in self.b94:
                  self.button_plat6[(3,1)].setText(str(row[0]))
                  self.lab_plat6[(3,1)].setText(str(row[1]))
                  self.button_plat6[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b95=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=95")               
               for row in self.b95:
                  self.button_plat6[(3,2)].setText(str(row[0]))
                  self.lab_plat6[(3,2)].setText(str(row[1]))
                  self.button_plat6[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b96=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=96")               
               for row in self.b96:
                  self.button_plat6[(3,3)].setText(str(row[0]))
                  self.lab_plat6[(3,3)].setText(str(row[1]))
                  self.button_plat6[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 7
               self.b97=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=97")               
               for row in self.b97:
                  self.button_plat7[(0,0)].setText(str(row[0]))
                  self.lab_plat7[(0,0)].setText(str(row[1]))
                  self.button_plat7[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b98=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=98")               
               for row in self.b98:
                  self.button_plat7[(0,1)].setText(str(row[0]))
                  self.lab_plat7[(0,1)].setText(str(row[1]))
                  self.button_plat7[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b99=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=99")               
               for row in self.b99:
                  self.button_plat7[(0,2)].setText(str(row[0]))
                  self.lab_plat7[(0,2)].setText(str(row[1]))
                  self.button_plat7[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b100=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=100")               
               for row in self.b100:
                  self.button_plat7[(0,3)].setText(str(row[0]))
                  self.lab_plat7[(0,3)].setText(str(row[1]))
                  self.button_plat7[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b101=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=101")               
               for row in self.b101:
                  self.button_plat7[(1,0)].setText(str(row[0]))
                  self.lab_plat7[(1,0)].setText(str(row[1]))
                  self.button_plat7[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b102=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=102")               
               for row in self.b101:
                  self.button_plat7[(1,1)].setText(str(row[0]))
                  self.lab_plat7[(1,1)].setText(str(row[1]))
                  self.button_plat7[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b103=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=103")               
               for row in self.b103:
                  self.button_plat7[(1,2)].setText(str(row[0]))
                  self.lab_plat7[(1,2)].setText(str(row[1]))
                  self.button_plat7[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b104=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=104")               
               for row in self.b104:
                  self.button_plat7[(1,3)].setText(str(row[0]))
                  self.lab_plat7[(1,3)].setText(str(row[1]))
                  self.button_plat7[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b105=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=105")               
               for row in self.b105:
                  self.button_plat7[(2,0)].setText(str(row[0]))
                  self.lab_plat7[(2,0)].setText(str(row[1]))
                  self.button_plat7[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b106=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=106")               
               for row in self.b106:
                  self.button_plat7[(2,1)].setText(str(row[0]))
                  self.lab_plat7[(2,1)].setText(str(row[1]))
                  self.button_plat7[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b107=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=107")               
               for row in self.b107:
                  self.button_plat7[(2,2)].setText(str(row[0]))
                  self.lab_plat7[(2,2)].setText(str(row[1]))
                  self.button_plat7[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b108=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=108")               
               for row in self.b108:
                  self.button_plat7[(2,3)].setText(str(row[0]))
                  self.lab_plat7[(2,3)].setText(str(row[1]))
                  self.button_plat7[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b109=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=109")               
               for row in self.b109:
                  self.button_plat7[(3,0)].setText(str(row[0]))
                  self.lab_plat7[(3,0)].setText(str(row[1]))
                  self.button_plat7[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b110=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=110")               
               for row in self.b110:
                  self.button_plat7[(3,1)].setText(str(row[0]))
                  self.lab_plat7[(3,1)].setText(str(row[1]))
                  self.button_plat7[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b111=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=111")               
               for row in self.b111:
                  self.button_plat7[(3,2)].setText(str(row[0]))
                  self.lab_plat7[(3,2)].setText(str(row[1]))
                  self.button_plat7[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b112=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=112")               
               for row in self.b112:
                  self.button_plat7[(3,3)].setText(str(row[0]))
                  self.lab_plat7[(3,3)].setText(str(row[1]))
                  self.button_plat7[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 8
               self.b113=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=113")               
               for row in self.b113:
                  self.button_plat8[(0,0)].setText(str(row[0]))
                  self.lab_plat8[(0,0)].setText(str(row[1]))
                  self.button_plat8[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b114=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=114")           
               for row in self.b114:
                  self.button_plat8[(0,1)].setText(str(row[0]))
                  self.lab_plat8[(0,1)].setText(str(row[1]))
                  self.button_plat8[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b115=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=115")               
               for row in self.b115:
                  self.button_plat8[(0,2)].setText(str(row[0]))
                  self.lab_plat8[(0,2)].setText(str(row[1]))
                  self.button_plat8[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b116=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=116")               
               for row in self.b116:
                  self.button_plat8[(0,3)].setText(str(row[0]))
                  self.lab_plat8[(0,3)].setText(str(row[1]))
                  self.button_plat8[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b117=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=117")               
               for row in self.b117:
                  self.button_plat8[(1,0)].setText(str(row[0]))
                  self.lab_plat8[(1,0)].setText(str(row[1]))
                  self.button_plat8[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b118=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=118")               
               for row in self.b118:
                  self.button_plat8[(1,1)].setText(str(row[0]))
                  self.lab_plat8[(1,1)].setText(str(row[1]))
                  self.button_plat8[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b119=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=119")               
               for row in self.b119:
                  self.button_plat8[(1,2)].setText(str(row[0]))
                  self.lab_plat8[(1,2)].setText(str(row[1]))
                  self.button_plat8[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b120=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=120")               
               for row in self.b120:
                  self.button_plat4[(1,3)].setText(str(row[0]))
                  self.lab_plat8[(1,3)].setText(str(row[1]))
                  self.button_plat8[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b121=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=121")               
               for row in self.b121:
                  self.button_plat8[(2,0)].setText(str(row[0]))
                  self.lab_plat8[(2,0)].setText(str(row[1]))
                  self.button_plat8[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b122=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=122")               
               for row in self.b122:
                  self.button_plat8[(2,1)].setText(str(row[0]))
                  self.lab_plat8[(2,1)].setText(str(row[1]))
                  self.button_plat8[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b123=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=123")               
               for row in self.b123:
                  self.button_plat8[(2,2)].setText(str(row[0]))
                  self.lab_plat8[(2,2)].setText(str(row[1]))
                  self.button_plat8[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b124=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=124")               
               for row in self.b124:
                  self.button_plat8[(2,3)].setText(str(row[0]))
                  self.lab_plat8[(2,3)].setText(str(row[1]))
                  self.button_plat8[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b125=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=125")               
               for row in self.b125:
                  self.button_plat8[(3,0)].setText(str(row[0]))
                  self.lab_plat8[(3,0)].setText(str(row[1]))
                  self.button_plat8[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b126=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=126")               
               for row in self.b126:
                  self.button_plat8[(3,1)].setText(str(row[0]))
                  self.lab_plat8[(3,1)].setText(str(row[1]))
                  self.button_plat8[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b127=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=127")               
               for row in self.b127:
                  self.button_plat8[(3,2)].setText(str(row[0]))
                  self.lab_plat8[(3,2)].setText(str(row[1]))
                  self.button_plat8[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b128=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=128")               
               for row in self.b128:
                  self.button_plat8[(3,3)].setText(str(row[0]))
                  self.lab_plat8[(3,3)].setText(str(row[1]))
                  self.button_plat8[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.bdd.commit()
               #====================== REFRESH LAB ==#
               #=====================================#
               for x in range(4):
                  for y in range(4):
                     #====================== PLATS
                     self.lab_plat1[(x,y)].adjustSize()
                     self.lab_plat2[(x,y)].adjustSize()
                     self.lab_plat3[(x,y)].adjustSize()
                     self.lab_plat4[(x,y)].adjustSize()
                     self.lab_plat5[(x,y)].adjustSize()
                     self.lab_plat6[(x,y)].adjustSize()
                     self.lab_plat7[(x,y)].adjustSize()
                     self.lab_plat8[(x,y)].adjustSize()
                  
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass

   def refresh_all(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()              

               #====================== REFRESH BOISSONS ==#
               #==========================================#                  
               #________PAGE 1
               self.b1=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=1")               
               for row in self.b1:
                  self.button_boisson1[(0,0)].setText(str(row[0]))
                  self.lab_boisson1[(0,0)].setText(str(row[1]))
                  self.button_boisson1[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b2=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=2")             
               for row in self.b2:
                  self.button_boisson1[(0,1)].setText(str(row[0]))
                  self.lab_boisson1[(0,1)].setText(str(row[1]))
                  self.button_boisson1[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b3=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=3")               
               for row in self.b3:
                  self.button_boisson1[(0,2)].setText(str(row[0]))
                  self.lab_boisson1[(0,2)].setText(str(row[1]))
                  self.button_boisson1[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b4=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=4")               
               for row in self.b4:
                  self.button_boisson1[(0,3)].setText(str(row[0]))
                  self.lab_boisson1[(0,3)].setText(str(row[1]))
                  self.button_boisson1[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b5=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=5")               
               for row in self.b5:
                  self.button_boisson1[(1,0)].setText(str(row[0]))
                  self.lab_boisson1[(1,0)].setText(str(row[1]))
                  self.button_boisson1[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b6=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=6")               
               for row in self.b6:
                  self.button_boisson1[(1,1)].setText(str(row[0]))
                  self.lab_boisson1[(1,1)].setText(str(row[1]))
                  self.button_boisson1[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b7=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=7")               
               for row in self.b7:
                  self.button_boisson1[(1,2)].setText(str(row[0]))
                  self.lab_boisson1[(1,2)].setText(str(row[1]))
                  self.button_boisson1[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b8=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=8")               
               for row in self.b8:
                  self.button_boisson1[(1,3)].setText(str(row[0]))
                  self.lab_boisson1[(1,3)].setText(str(row[1]))
                  self.button_boisson1[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b9=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=9")               
               for row in self.b9:
                  self.button_boisson1[(2,0)].setText(str(row[0]))
                  self.lab_boisson1[(2,0)].setText(str(row[1]))
                  self.button_boisson1[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b10=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=10")               
               for row in self.b10:
                  self.button_boisson1[(2,1)].setText(str(row[0]))
                  self.lab_boisson1[(2,1)].setText(str(row[1]))
                  self.button_boisson1[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b11=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=11")               
               for row in self.b11:
                  self.button_boisson1[(2,2)].setText(str(row[0]))
                  self.lab_boisson1[(2,2)].setText(str(row[1]))
                  self.button_boisson1[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b12=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=12")               
               for row in self.b12:
                  self.button_boisson1[(2,3)].setText(str(row[0]))
                  self.lab_boisson1[(2,3)].setText(str(row[1]))
                  self.button_boisson1[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b13=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=13")               
               for row in self.b13:
                  self.button_boisson1[(3,0)].setText(str(row[0]))
                  self.lab_boisson1[(3,0)].setText(str(row[1]))
                  self.button_boisson1[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b14=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=14")               
               for row in self.b14:
                  self.button_boisson1[(3,1)].setText(str(row[0]))
                  self.lab_boisson1[(3,1)].setText(str(row[1]))
                  self.button_boisson1[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b15=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=15")               
               for row in self.b15:
                  self.button_boisson1[(3,2)].setText(str(row[0]))
                  self.lab_boisson1[(3,2)].setText(str(row[1]))
                  self.button_boisson1[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b16=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=16")               
               for row in self.b16:
                  self.button_boisson1[(3,3)].setText(str(row[0]))
                  self.lab_boisson1[(3,3)].setText(str(row[1]))
                  self.button_boisson1[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson1[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               

               #====================== REFRESH DESSERTS ==#
               #==========================================#
               #________PAGE 1
               self.b1=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=1")               
               for row in self.b1:
                  self.button_dessert1[(0,0)].setText(str(row[0]))
                  self.lab_dessert1[(0,0)].setText(str(row[1]))
                  self.button_dessert1[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b2=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=2")             
               for row in self.b2:
                  self.button_dessert1[(0,1)].setText(str(row[0]))
                  self.lab_dessert1[(0,1)].setText(str(row[1]))
                  self.button_dessert1[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b3=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=3")               
               for row in self.b3:
                  self.button_dessert1[(0,2)].setText(str(row[0]))
                  self.lab_dessert1[(0,2)].setText(str(row[1]))
                  self.button_dessert1[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b4=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=4")               
               for row in self.b4:
                  self.button_dessert1[(0,3)].setText(str(row[0]))
                  self.lab_dessert1[(0,3)].setText(str(row[1]))
                  self.button_dessert1[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b5=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=5")               
               for row in self.b5:
                  self.button_dessert1[(1,0)].setText(str(row[0]))
                  self.lab_dessert1[(1,0)].setText(str(row[1]))
                  self.button_dessert1[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b6=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=6")               
               for row in self.b6:
                  self.button_dessert1[(1,1)].setText(str(row[0]))
                  self.lab_dessert1[(1,1)].setText(str(row[1]))
                  self.button_dessert1[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b7=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=7")               
               for row in self.b7:
                  self.button_dessert1[(1,2)].setText(str(row[0]))
                  self.lab_dessert1[(1,2)].setText(str(row[1]))
                  self.button_dessert1[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b8=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=8")               
               for row in self.b8:
                  self.button_dessert1[(1,3)].setText(str(row[0]))
                  self.lab_dessert1[(1,3)].setText(str(row[1]))
                  self.button_dessert1[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b9=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=9")               
               for row in self.b9:
                  self.button_dessert1[(2,0)].setText(str(row[0]))
                  self.lab_dessert1[(2,0)].setText(str(row[1]))
                  self.button_dessert1[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b10=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=10")               
               for row in self.b10:
                  self.button_dessert1[(2,1)].setText(str(row[0]))
                  self.lab_dessert1[(2,1)].setText(str(row[1]))
                  self.button_dessert1[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b11=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=11")               
               for row in self.b11:
                  self.button_dessert1[(2,2)].setText(str(row[0]))
                  self.lab_dessert1[(2,2)].setText(str(row[1]))
                  self.button_dessert1[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b12=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=12")               
               for row in self.b12:
                  self.button_dessert1[(2,3)].setText(str(row[0]))
                  self.lab_dessert1[(2,3)].setText(str(row[1]))
                  self.button_dessert1[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b13=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=13")               
               for row in self.b13:
                  self.button_dessert1[(3,0)].setText(str(row[0]))
                  self.lab_dessert1[(3,0)].setText(str(row[1]))
                  self.button_dessert1[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b14=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=14")               
               for row in self.b14:
                  self.button_dessert1[(3,1)].setText(str(row[0]))
                  self.lab_dessert1[(3,1)].setText(str(row[1]))
                  self.button_dessert1[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b15=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=15")               
               for row in self.b15:
                  self.button_dessert1[(3,2)].setText(str(row[0]))
                  self.lab_dessert1[(3,2)].setText(str(row[1]))
                  self.button_dessert1[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b16=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=16")               
               for row in self.b16:
                  self.button_dessert1[(3,3)].setText(str(row[0]))
                  self.lab_dessert1[(3,3)].setText(str(row[1]))
                  self.button_dessert1[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert1[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 2
               self.b17=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=17")               
               for row in self.b17:
                  self.button_dessert2[(0,0)].setText(str(row[0]))
                  self.lab_dessert2[(0,0)].setText(str(row[1]))
                  self.button_dessert2[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b18=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=18")               
               for row in self.b18:
                  self.button_dessert2[(0,1)].setText(str(row[0]))
                  self.lab_dessert2[(0,1)].setText(str(row[1]))
                  self.button_dessert2[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b19=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=19")               
               for row in self.b19:
                  self.button_dessert2[(0,2)].setText(str(row[0]))
                  self.lab_dessert2[(0,2)].setText(str(row[1]))
                  self.button_dessert2[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b20=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=20")               
               for row in self.b20:
                  self.button_dessert2[(0,3)].setText(str(row[0]))
                  self.lab_dessert2[(0,3)].setText(str(row[1]))
                  self.button_dessert2[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b21=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=21")               
               for row in self.b21:
                  self.button_dessert2[(1,0)].setText(str(row[0]))
                  self.lab_dessert2[(1,0)].setText(str(row[1]))
                  self.button_dessert2[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b22=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=22")               
               for row in self.b22:
                  self.button_dessert2[(1,1)].setText(str(row[0]))
                  self.lab_dessert2[(1,1)].setText(str(row[1]))
                  self.button_dessert2[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b23=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=23")               
               for row in self.b23:
                  self.button_dessert2[(1,2)].setText(str(row[0]))
                  self.lab_dessert2[(1,2)].setText(str(row[1]))
                  self.button_dessert2[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b24=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=24")               
               for row in self.b24:
                  self.button_dessert2[(1,3)].setText(str(row[0]))
                  self.lab_dessert2[(1,3)].setText(str(row[1]))
                  self.button_dessert2[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b25=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=25")               
               for row in self.b25:
                  self.button_dessert2[(2,0)].setText(str(row[0]))
                  self.lab_dessert2[(2,0)].setText(str(row[1]))
                  self.button_dessert2[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b26=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=26")               
               for row in self.b26:
                  self.button_dessert2[(2,1)].setText(str(row[0]))
                  self.lab_dessert2[(2,1)].setText(str(row[1]))
                  self.button_dessert2[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b27=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=27")               
               for row in self.b27:
                  self.button_dessert2[(2,2)].setText(str(row[0]))
                  self.lab_dessert2[(2,2)].setText(str(row[1]))
                  self.button_dessert2[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b28=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=28")               
               for row in self.b28:
                  self.button_dessert2[(2,3)].setText(str(row[0]))
                  self.lab_dessert2[(2,3)].setText(str(row[1]))
                  self.button_dessert2[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b29=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=29")               
               for row in self.b29:
                  self.button_dessert2[(3,0)].setText(str(row[0]))
                  self.lab_dessert2[(3,0)].setText(str(row[1]))
                  self.button_dessert2[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b30=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=30")               
               for row in self.b30:
                  self.button_dessert2[(3,1)].setText(str(row[0]))
                  self.lab_dessert2[(3,1)].setText(str(row[1]))
                  self.button_dessert2[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b31=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=31")               
               for row in self.b31:
                  self.button_dessert2[(3,2)].setText(str(row[0]))
                  self.lab_dessert2[(3,2)].setText(str(row[1]))
                  self.button_dessert2[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b32=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=32")               
               for row in self.b32:
                  self.button_dessert2[(3,3)].setText(str(row[0]))
                  self.lab_dessert2[(3,3)].setText(str(row[1]))
                  self.button_dessert2[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert2[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 3
               self.b33=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=33")               
               for row in self.b33:
                  self.button_dessert3[(0,0)].setText(str(row[0]))
                  self.lab_dessert3[(0,0)].setText(str(row[1]))
                  self.button_dessert3[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b34=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=34")               
               for row in self.b34:
                  self.button_dessert3[(0,1)].setText(str(row[0]))
                  self.lab_dessert3[(0,1)].setText(str(row[1]))
                  self.button_dessert3[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b35=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=35")               
               for row in self.b35:
                  self.button_dessert3[(0,2)].setText(str(row[0]))
                  self.lab_dessert3[(0,2)].setText(str(row[1]))
                  self.button_dessert3[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b36=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=36")               
               for row in self.b36:
                  self.button_dessert3[(0,3)].setText(str(row[0]))
                  self.lab_dessert3[(0,3)].setText(str(row[1]))
                  self.button_dessert3[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b37=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=37")               
               for row in self.b37:
                  self.button_dessert3[(1,0)].setText(str(row[0]))
                  self.lab_dessert3[(1,0)].setText(str(row[1]))
                  self.button_dessert3[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b38=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=38")               
               for row in self.b38:
                  self.button_dessert3[(1,1)].setText(str(row[0]))
                  self.lab_dessert3[(1,1)].setText(str(row[1]))
                  self.button_dessert3[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b39=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=39")               
               for row in self.b39:
                  self.button_dessert3[(1,2)].setText(str(row[0]))
                  self.lab_dessert3[(1,2)].setText(str(row[1]))
                  self.button_dessert3[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b40=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=40")               
               for row in self.b40:
                  self.button_dessert3[(1,3)].setText(str(row[0]))
                  self.lab_dessert3[(1,3)].setText(str(row[1]))
                  self.button_dessert3[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b41=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=41")               
               for row in self.b41:
                  self.button_dessert3[(2,0)].setText(str(row[0]))
                  self.lab_dessert3[(2,0)].setText(str(row[1]))
                  self.button_dessert3[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b42=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=42")               
               for row in self.b42:
                  self.button_dessert3[(2,1)].setText(str(row[0]))
                  self.lab_dessert3[(2,1)].setText(str(row[1]))
                  self.button_dessert3[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b43=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=43")               
               for row in self.b43:
                  self.button_dessert3[(2,2)].setText(str(row[0]))
                  self.lab_dessert3[(2,2)].setText(str(row[1]))
                  self.button_dessert3[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b44=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=44")               
               for row in self.b44:
                  self.button_dessert3[(2,3)].setText(str(row[0]))
                  self.lab_dessert3[(2,3)].setText(str(row[1]))
                  self.button_dessert3[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b45=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=45")               
               for row in self.b45:
                  self.button_dessert3[(3,0)].setText(str(row[0]))
                  self.lab_dessert3[(3,0)].setText(str(row[1]))
                  self.button_dessert3[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b46=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=46")               
               for row in self.b46:
                  self.button_dessert3[(3,1)].setText(str(row[0]))
                  self.lab_dessert3[(3,1)].setText(str(row[1]))
                  self.button_dessert3[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b47=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=47")               
               for row in self.b47:
                  self.button_dessert3[(3,2)].setText(str(row[0]))
                  self.lab_dessert3[(3,2)].setText(str(row[1]))
                  self.button_dessert3[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b48=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=48")               
               for row in self.b48:
                  self.button_dessert3[(3,3)].setText(str(row[0]))
                  self.lab_dessert3[(3,3)].setText(str(row[1]))
                  self.button_dessert3[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert3[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 4
               self.b49=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=49")               
               for row in self.b49:
                  self.button_dessert4[(0,0)].setText(str(row[0]))
                  self.lab_dessert4[(0,0)].setText(str(row[1]))
                  self.button_dessert4[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b50=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=50")           
               for row in self.b50:
                  self.button_dessert4[(0,1)].setText(str(row[0]))
                  self.lab_dessert4[(0,1)].setText(str(row[1]))
                  self.button_dessert4[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b51=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=51")               
               for row in self.b51:
                  self.button_dessert4[(0,2)].setText(str(row[0]))
                  self.lab_dessert4[(0,2)].setText(str(row[1]))
                  self.button_dessert4[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b52=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=52")               
               for row in self.b52:
                  self.button_dessert4[(0,3)].setText(str(row[0]))
                  self.lab_dessert4[(0,3)].setText(str(row[1]))
                  self.button_dessert4[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b53=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=53")               
               for row in self.b53:
                  self.button_dessert4[(1,0)].setText(str(row[0]))
                  self.lab_dessert4[(1,0)].setText(str(row[1]))
                  self.button_dessert4[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b54=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=54")               
               for row in self.b54:
                  self.button_dessert4[(1,1)].setText(str(row[0]))
                  self.lab_dessert4[(1,1)].setText(str(row[1]))
                  self.button_dessert4[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b55=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=55")               
               for row in self.b55:
                  self.button_dessert4[(1,2)].setText(str(row[0]))
                  self.lab_dessert4[(1,2)].setText(str(row[1]))
                  self.button_dessert4[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b56=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=56")               
               for row in self.b56:
                  self.button_dessert4[(1,3)].setText(str(row[0]))
                  self.lab_dessert4[(1,3)].setText(str(row[1]))
                  self.button_dessert4[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b57=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=57")               
               for row in self.b57:
                  self.button_dessert4[(2,0)].setText(str(row[0]))
                  self.lab_dessert4[(2,0)].setText(str(row[1]))
                  self.button_dessert4[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b58=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=58")               
               for row in self.b58:
                  self.button_dessert4[(2,1)].setText(str(row[0]))
                  self.lab_dessert4[(2,1)].setText(str(row[1]))
                  self.button_dessert4[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b59=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=59")               
               for row in self.b59:
                  self.button_dessert4[(2,2)].setText(str(row[0]))
                  self.lab_dessert4[(2,2)].setText(str(row[1]))
                  self.button_dessert4[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b60=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=60")               
               for row in self.b60:
                  self.button_dessert4[(2,3)].setText(str(row[0]))
                  self.lab_dessert4[(2,3)].setText(str(row[1]))
                  self.button_dessert4[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b61=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=61")               
               for row in self.b61:
                  self.button_dessert4[(3,0)].setText(str(row[0]))
                  self.lab_dessert4[(3,0)].setText(str(row[1]))
                  self.button_dessert4[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b62=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=62")               
               for row in self.b62:
                  self.button_dessert4[(3,1)].setText(str(row[0]))
                  self.lab_dessert4[(3,1)].setText(str(row[1]))
                  self.button_dessert4[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b63=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=63")               
               for row in self.b63:
                  self.button_dessert4[(3,2)].setText(str(row[0]))
                  self.lab_dessert4[(3,2)].setText(str(row[1]))
                  self.button_dessert4[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b64=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=64")               
               for row in self.b64:
                  self.button_dessert4[(3,3)].setText(str(row[0]))
                  self.lab_dessert4[(3,3)].setText(str(row[1]))
                  self.button_dessert4[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert4[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 5
               self.b65=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=65")               
               for row in self.b65:
                  self.button_dessert5[(0,0)].setText(str(row[0]))
                  self.lab_dessert5[(0,0)].setText(str(row[1]))
                  self.button_dessert5[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b66=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=66")             
               for row in self.b66:
                  self.button_dessert5[(0,1)].setText(str(row[0]))
                  self.lab_dessert5[(0,1)].setText(str(row[1]))
                  self.button_dessert5[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b67=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=67")               
               for row in self.b67:
                  self.button_dessert5[(0,2)].setText(str(row[0]))
                  self.lab_dessert5[(0,2)].setText(str(row[1]))
                  self.button_dessert5[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b68=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=68")               
               for row in self.b68:
                  self.button_dessert5[(0,3)].setText(str(row[0]))
                  self.lab_dessert5[(0,3)].setText(str(row[1]))
                  self.button_dessert5[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b69=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=69")               
               for row in self.b69:
                  self.button_dessert5[(1,0)].setText(str(row[0]))
                  self.lab_dessert5[(1,0)].setText(str(row[1]))
                  self.button_dessert5[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b70=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=70")               
               for row in self.b70:
                  self.button_dessert5[(1,1)].setText(str(row[0]))
                  self.lab_dessert5[(1,1)].setText(str(row[1]))
                  self.button_dessert5[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b71=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=71")               
               for row in self.b71:
                  self.button_dessert5[(1,2)].setText(str(row[0]))
                  self.lab_dessert5[(1,2)].setText(str(row[1]))
                  self.button_dessert5[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b72=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=72")               
               for row in self.b72:
                  self.button_dessert5[(1,3)].setText(str(row[0]))
                  self.lab_dessert5[(1,3)].setText(str(row[1]))
                  self.button_dessert5[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b73=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=73")               
               for row in self.b73:
                  self.button_dessert5[(2,0)].setText(str(row[0]))
                  self.lab_dessert5[(2,0)].setText(str(row[1]))
                  self.button_dessert5[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b74=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=74")               
               for row in self.b74:
                  self.button_dessert5[(2,1)].setText(str(row[0]))
                  self.lab_dessert5[(2,1)].setText(str(row[1]))
                  self.button_dessert5[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b75=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=75")               
               for row in self.b75:
                  self.button_dessert5[(2,2)].setText(str(row[0]))
                  self.lab_dessert5[(2,2)].setText(str(row[1]))
                  self.button_dessert5[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b76=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=76")               
               for row in self.b76:
                  self.button_dessert5[(2,3)].setText(str(row[0]))
                  self.lab_dessert5[(2,3)].setText(str(row[1]))
                  self.button_dessert5[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b77=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=77")               
               for row in self.b77:
                  self.button_dessert5[(3,0)].setText(str(row[0]))
                  self.lab_dessert5[(3,0)].setText(str(row[1]))
                  self.button_dessert5[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b78=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=78")               
               for row in self.b78:
                  self.button_dessert5[(3,1)].setText(str(row[0]))
                  self.lab_dessert5[(3,1)].setText(str(row[1]))
                  self.button_dessert5[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b79=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=79")               
               for row in self.b79:
                  self.button_dessert5[(3,2)].setText(str(row[0]))
                  self.lab_dessert5[(3,2)].setText(str(row[1]))
                  self.button_dessert5[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b80=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=80")               
               for row in self.b80:
                  self.button_dessert5[(3,3)].setText(str(row[0]))
                  self.lab_dessert5[(3,3)].setText(str(row[1]))
                  self.button_dessert5[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert5[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 6
               self.b81=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=81")               
               for row in self.b81:
                  self.button_dessert6[(0,0)].setText(str(row[0]))
                  self.lab_dessert6[(0,0)].setText(str(row[1]))
                  self.button_dessert6[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b82=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=82")               
               for row in self.b82:
                  self.button_dessert6[(0,1)].setText(str(row[0]))
                  self.lab_dessert6[(0,1)].setText(str(row[1]))
                  self.button_dessert6[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b83=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=83")               
               for row in self.b83:
                  self.button_dessert6[(0,2)].setText(str(row[0]))
                  self.lab_dessert6[(0,2)].setText(str(row[1]))
                  self.button_dessert6[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b84=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=84")               
               for row in self.b84:
                  self.button_dessert6[(0,3)].setText(str(row[0]))
                  self.lab_dessert6[(0,3)].setText(str(row[1]))
                  self.button_dessert6[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b85=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=85")               
               for row in self.b85:
                  self.button_dessert6[(1,0)].setText(str(row[0]))
                  self.lab_dessert6[(1,0)].setText(str(row[1]))
                  self.button_dessert6[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b86=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=86")               
               for row in self.b86:
                  self.button_dessert6[(1,1)].setText(str(row[0]))
                  self.lab_dessert6[(1,1)].setText(str(row[1]))
                  self.button_dessert6[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b87=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=87")               
               for row in self.b87:
                  self.button_dessert6[(1,2)].setText(str(row[0]))
                  self.lab_dessert6[(1,2)].setText(str(row[1]))
                  self.button_dessert6[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b88=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=88")               
               for row in self.b88:
                  self.button_dessert6[(1,3)].setText(str(row[0]))
                  self.lab_dessert6[(1,3)].setText(str(row[1]))
                  self.button_dessert6[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b89=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=89")               
               for row in self.b89:
                  self.button_dessert6[(2,0)].setText(str(row[0]))
                  self.lab_dessert6[(2,0)].setText(str(row[1]))
                  self.button_dessert6[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b90=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=90")               
               for row in self.b90:
                  self.button_dessert6[(2,1)].setText(str(row[0]))
                  self.lab_dessert6[(2,1)].setText(str(row[1]))
                  self.button_dessert6[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b91=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=91")               
               for row in self.b91:
                  self.button_dessert6[(2,2)].setText(str(row[0]))
                  self.lab_dessert6[(2,2)].setText(str(row[1]))
                  self.button_dessert6[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b92=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=92")               
               for row in self.b92:
                  self.button_dessert6[(2,3)].setText(str(row[0]))
                  self.lab_dessert6[(2,3)].setText(str(row[1]))
                  self.button_dessert6[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b93=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=93")               
               for row in self.b93:
                  self.button_dessert6[(3,0)].setText(str(row[0]))
                  self.lab_dessert6[(3,0)].setText(str(row[1]))
                  self.button_dessert6[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b94=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=94")               
               for row in self.b94:
                  self.button_dessert6[(3,1)].setText(str(row[0]))
                  self.lab_dessert6[(3,1)].setText(str(row[1]))
                  self.button_dessert6[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b95=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=95")               
               for row in self.b95:
                  self.button_dessert6[(3,2)].setText(str(row[0]))
                  self.lab_dessert6[(3,2)].setText(str(row[1]))
                  self.button_dessert6[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b96=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=96")               
               for row in self.b96:
                  self.button_dessert6[(3,3)].setText(str(row[0]))
                  self.lab_dessert6[(3,3)].setText(str(row[1]))
                  self.button_dessert6[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert6[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 7
               self.b97=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=97")               
               for row in self.b97:
                  self.button_dessert7[(0,0)].setText(str(row[0]))
                  self.lab_dessert7[(0,0)].setText(str(row[1]))
                  self.button_dessert7[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b98=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=98")               
               for row in self.b98:
                  self.button_dessert7[(0,1)].setText(str(row[0]))
                  self.lab_dessert7[(0,1)].setText(str(row[1]))
                  self.button_dessert7[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b99=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=99")               
               for row in self.b99:
                  self.button_dessert7[(0,2)].setText(str(row[0]))
                  self.lab_dessert7[(0,2)].setText(str(row[1]))
                  self.button_dessert7[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b100=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=100")               
               for row in self.b100:
                  self.button_dessert7[(0,3)].setText(str(row[0]))
                  self.lab_dessert7[(0,3)].setText(str(row[1]))
                  self.button_dessert7[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b101=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=101")               
               for row in self.b101:
                  self.button_dessert7[(1,0)].setText(str(row[0]))
                  self.lab_dessert7[(1,0)].setText(str(row[1]))
                  self.button_dessert7[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b102=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=102")               
               for row in self.b101:
                  self.button_dessert7[(1,1)].setText(str(row[0]))
                  self.lab_dessert7[(1,1)].setText(str(row[1]))
                  self.button_dessert7[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b103=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=103")               
               for row in self.b103:
                  self.button_dessert7[(1,2)].setText(str(row[0]))
                  self.lab_dessert7[(1,2)].setText(str(row[1]))
                  self.button_dessert7[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b104=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=104")               
               for row in self.b104:
                  self.button_dessert7[(1,3)].setText(str(row[0]))
                  self.lab_dessert7[(1,3)].setText(str(row[1]))
                  self.button_dessert7[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b105=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=105")               
               for row in self.b105:
                  self.button_dessert7[(2,0)].setText(str(row[0]))
                  self.lab_dessert7[(2,0)].setText(str(row[1]))
                  self.button_dessert7[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b106=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=106")               
               for row in self.b106:
                  self.button_dessert7[(2,1)].setText(str(row[0]))
                  self.lab_dessert7[(2,1)].setText(str(row[1]))
                  self.button_dessert7[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b107=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=107")               
               for row in self.b107:
                  self.button_dessert7[(2,2)].setText(str(row[0]))
                  self.lab_dessert7[(2,2)].setText(str(row[1]))
                  self.button_dessert7[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b108=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=108")               
               for row in self.b108:
                  self.button_dessert7[(2,3)].setText(str(row[0]))
                  self.lab_dessert7[(2,3)].setText(str(row[1]))
                  self.button_dessert7[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b109=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=109")               
               for row in self.b109:
                  self.button_dessert7[(3,0)].setText(str(row[0]))
                  self.lab_dessert7[(3,0)].setText(str(row[1]))
                  self.button_dessert7[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b110=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=110")               
               for row in self.b110:
                  self.button_dessert7[(3,1)].setText(str(row[0]))
                  self.lab_dessert7[(3,1)].setText(str(row[1]))
                  self.button_dessert7[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b111=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=111")               
               for row in self.b111:
                  self.button_dessert7[(3,2)].setText(str(row[0]))
                  self.lab_dessert7[(3,2)].setText(str(row[1]))
                  self.button_dessert7[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b112=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=112")               
               for row in self.b112:
                  self.button_dessert7[(3,3)].setText(str(row[0]))
                  self.lab_dessert7[(3,3)].setText(str(row[1]))
                  self.button_dessert7[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert7[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 8
               self.b113=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=113")               
               for row in self.b113:
                  self.button_dessert8[(0,0)].setText(str(row[0]))
                  self.lab_dessert8[(0,0)].setText(str(row[1]))
                  self.button_dessert8[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b114=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=114")           
               for row in self.b114:
                  self.button_dessert8[(0,1)].setText(str(row[0]))
                  self.lab_dessert8[(0,1)].setText(str(row[1]))
                  self.button_dessert8[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b115=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=115")               
               for row in self.b115:
                  self.button_dessert8[(0,2)].setText(str(row[0]))
                  self.lab_dessert8[(0,2)].setText(str(row[1]))
                  self.button_dessert8[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b116=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=116")               
               for row in self.b116:
                  self.button_dessert8[(0,3)].setText(str(row[0]))
                  self.lab_dessert8[(0,3)].setText(str(row[1]))
                  self.button_dessert8[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b117=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=117")               
               for row in self.b117:
                  self.button_dessert8[(1,0)].setText(str(row[0]))
                  self.lab_dessert8[(1,0)].setText(str(row[1]))
                  self.button_dessert8[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b118=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=118")               
               for row in self.b118:
                  self.button_dessert8[(1,1)].setText(str(row[0]))
                  self.lab_dessert8[(1,1)].setText(str(row[1]))
                  self.button_dessert8[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b119=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=119")               
               for row in self.b119:
                  self.button_dessert8[(1,2)].setText(str(row[0]))
                  self.lab_dessert8[(1,2)].setText(str(row[1]))
                  self.button_dessert8[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b120=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=120")               
               for row in self.b120:
                  self.button_dessert4[(1,3)].setText(str(row[0]))
                  self.lab_dessert8[(1,3)].setText(str(row[1]))
                  self.button_dessert8[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b121=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=121")               
               for row in self.b121:
                  self.button_dessert8[(2,0)].setText(str(row[0]))
                  self.lab_dessert8[(2,0)].setText(str(row[1]))
                  self.button_dessert8[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b122=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=122")               
               for row in self.b122:
                  self.button_dessert8[(2,1)].setText(str(row[0]))
                  self.lab_dessert8[(2,1)].setText(str(row[1]))
                  self.button_dessert8[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b123=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=123")               
               for row in self.b123:
                  self.button_dessert8[(2,2)].setText(str(row[0]))
                  self.lab_dessert8[(2,2)].setText(str(row[1]))
                  self.button_dessert8[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b124=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=124")               
               for row in self.b124:
                  self.button_dessert8[(2,3)].setText(str(row[0]))
                  self.lab_dessert8[(2,3)].setText(str(row[1]))
                  self.button_dessert8[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b125=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=125")               
               for row in self.b125:
                  self.button_dessert8[(3,0)].setText(str(row[0]))
                  self.lab_dessert8[(3,0)].setText(str(row[1]))
                  self.button_dessert8[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b126=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=126")               
               for row in self.b126:
                  self.button_dessert8[(3,1)].setText(str(row[0]))
                  self.lab_dessert8[(3,1)].setText(str(row[1]))
                  self.button_dessert8[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b127=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=127")               
               for row in self.b127:
                  self.button_dessert8[(3,2)].setText(str(row[0]))
                  self.lab_dessert8[(3,2)].setText(str(row[1]))
                  self.button_dessert8[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b128=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM desserts WHERE rowid=128")               
               for row in self.b128:
                  self.button_dessert8[(3,3)].setText(str(row[0]))
                  self.lab_dessert8[(3,3)].setText(str(row[1]))
                  self.button_dessert8[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_dessert8[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))

               #====================== REFRESH CAFES ==#
               #=======================================#
               #________PAGE 1
               self.b1=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=1")               
               for row in self.b1:
                  self.button_cafe1[(0,0)].setText(str(row[0]))
                  self.lab_cafe1[(0,0)].setText(str(row[1]))
                  self.button_cafe1[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b2=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=2")             
               for row in self.b2:
                  self.button_cafe1[(0,1)].setText(str(row[0]))
                  self.lab_cafe1[(0,1)].setText(str(row[1]))
                  self.button_cafe1[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b3=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=3")               
               for row in self.b3:
                  self.button_cafe1[(0,2)].setText(str(row[0]))
                  self.lab_cafe1[(0,2)].setText(str(row[1]))
                  self.button_cafe1[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b4=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=4")               
               for row in self.b4:
                  self.button_cafe1[(0,3)].setText(str(row[0]))
                  self.lab_cafe1[(0,3)].setText(str(row[1]))
                  self.button_cafe1[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b5=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=5")               
               for row in self.b5:
                  self.button_cafe1[(1,0)].setText(str(row[0]))
                  self.lab_cafe1[(1,0)].setText(str(row[1]))
                  self.button_cafe1[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b6=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=6")               
               for row in self.b6:
                  self.button_cafe1[(1,1)].setText(str(row[0]))
                  self.lab_cafe1[(1,1)].setText(str(row[1]))
                  self.button_cafe1[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b7=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=7")               
               for row in self.b7:
                  self.button_cafe1[(1,2)].setText(str(row[0]))
                  self.lab_cafe1[(1,2)].setText(str(row[1]))
                  self.button_cafe1[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b8=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=8")               
               for row in self.b8:
                  self.button_cafe1[(1,3)].setText(str(row[0]))
                  self.lab_cafe1[(1,3)].setText(str(row[1]))
                  self.button_cafe1[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b9=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=9")               
               for row in self.b9:
                  self.button_cafe1[(2,0)].setText(str(row[0]))
                  self.lab_cafe1[(2,0)].setText(str(row[1]))
                  self.button_cafe1[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b10=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=10")               
               for row in self.b10:
                  self.button_cafe1[(2,1)].setText(str(row[0]))
                  self.lab_cafe1[(2,1)].setText(str(row[1]))
                  self.button_cafe1[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b11=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=11")               
               for row in self.b11:
                  self.button_cafe1[(2,2)].setText(str(row[0]))
                  self.lab_cafe1[(2,2)].setText(str(row[1]))
                  self.button_cafe1[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b12=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=12")               
               for row in self.b12:
                  self.button_cafe1[(2,3)].setText(str(row[0]))
                  self.lab_cafe1[(2,3)].setText(str(row[1]))
                  self.button_cafe1[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b13=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=13")               
               for row in self.b13:
                  self.button_cafe1[(3,0)].setText(str(row[0]))
                  self.lab_cafe1[(3,0)].setText(str(row[1]))
                  self.button_cafe1[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b14=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=14")               
               for row in self.b14:
                  self.button_cafe1[(3,1)].setText(str(row[0]))
                  self.lab_cafe1[(3,1)].setText(str(row[1]))
                  self.button_cafe1[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b15=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=15")               
               for row in self.b15:
                  self.button_cafe1[(3,2)].setText(str(row[0]))
                  self.lab_cafe1[(3,2)].setText(str(row[1]))
                  self.button_cafe1[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b16=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=16")               
               for row in self.b16:
                  self.button_cafe1[(3,3)].setText(str(row[0]))
                  self.lab_cafe1[(3,3)].setText(str(row[1]))
                  self.button_cafe1[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe1[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 2
               self.b17=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=17")               
               for row in self.b17:
                  self.button_cafe2[(0,0)].setText(str(row[0]))
                  self.lab_cafe2[(0,0)].setText(str(row[1]))
                  self.button_cafe2[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b18=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=18")               
               for row in self.b18:
                  self.button_cafe2[(0,1)].setText(str(row[0]))
                  self.lab_cafe2[(0,1)].setText(str(row[1]))
                  self.button_cafe2[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b19=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=19")               
               for row in self.b19:
                  self.button_cafe2[(0,2)].setText(str(row[0]))
                  self.lab_cafe2[(0,2)].setText(str(row[1]))
                  self.button_cafe2[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b20=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=20")               
               for row in self.b20:
                  self.button_cafe2[(0,3)].setText(str(row[0]))
                  self.lab_cafe2[(0,3)].setText(str(row[1]))
                  self.button_cafe2[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b21=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=21")               
               for row in self.b21:
                  self.button_cafe2[(1,0)].setText(str(row[0]))
                  self.lab_cafe2[(1,0)].setText(str(row[1]))
                  self.button_cafe2[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b22=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=22")               
               for row in self.b22:
                  self.button_cafe2[(1,1)].setText(str(row[0]))
                  self.lab_cafe2[(1,1)].setText(str(row[1]))
                  self.button_cafe2[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b23=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=23")               
               for row in self.b23:
                  self.button_cafe2[(1,2)].setText(str(row[0]))
                  self.lab_cafe2[(1,2)].setText(str(row[1]))
                  self.button_cafe2[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b24=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=24")               
               for row in self.b24:
                  self.button_cafe2[(1,3)].setText(str(row[0]))
                  self.lab_cafe2[(1,3)].setText(str(row[1]))
                  self.button_cafe2[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b25=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=25")               
               for row in self.b25:
                  self.button_cafe2[(2,0)].setText(str(row[0]))
                  self.lab_cafe2[(2,0)].setText(str(row[1]))
                  self.button_cafe2[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b26=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=26")               
               for row in self.b26:
                  self.button_cafe2[(2,1)].setText(str(row[0]))
                  self.lab_cafe2[(2,1)].setText(str(row[1]))
                  self.button_cafe2[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b27=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=27")               
               for row in self.b27:
                  self.button_cafe2[(2,2)].setText(str(row[0]))
                  self.lab_cafe2[(2,2)].setText(str(row[1]))
                  self.button_cafe2[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b28=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=28")               
               for row in self.b28:
                  self.button_cafe2[(2,3)].setText(str(row[0]))
                  self.lab_cafe2[(2,3)].setText(str(row[1]))
                  self.button_cafe2[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b29=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=29")               
               for row in self.b29:
                  self.button_cafe2[(3,0)].setText(str(row[0]))
                  self.lab_cafe2[(3,0)].setText(str(row[1]))
                  self.button_cafe2[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b30=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=30")               
               for row in self.b30:
                  self.button_cafe2[(3,1)].setText(str(row[0]))
                  self.lab_cafe2[(3,1)].setText(str(row[1]))
                  self.button_cafe2[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b31=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=31")               
               for row in self.b31:
                  self.button_cafe2[(3,2)].setText(str(row[0]))
                  self.lab_cafe2[(3,2)].setText(str(row[1]))
                  self.button_cafe2[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b32=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=32")               
               for row in self.b32:
                  self.button_cafe2[(3,3)].setText(str(row[0]))
                  self.lab_cafe2[(3,3)].setText(str(row[1]))
                  self.button_cafe2[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe2[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 3
               self.b33=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=33")               
               for row in self.b33:
                  self.button_cafe3[(0,0)].setText(str(row[0]))
                  self.lab_cafe3[(0,0)].setText(str(row[1]))
                  self.button_cafe3[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b34=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=34")               
               for row in self.b34:
                  self.button_cafe3[(0,1)].setText(str(row[0]))
                  self.lab_cafe3[(0,1)].setText(str(row[1]))
                  self.button_cafe3[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b35=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=35")               
               for row in self.b35:
                  self.button_cafe3[(0,2)].setText(str(row[0]))
                  self.lab_cafe3[(0,2)].setText(str(row[1]))
                  self.button_cafe3[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b36=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=36")               
               for row in self.b36:
                  self.button_cafe3[(0,3)].setText(str(row[0]))
                  self.lab_cafe3[(0,3)].setText(str(row[1]))
                  self.button_cafe3[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b37=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=37")               
               for row in self.b37:
                  self.button_cafe3[(1,0)].setText(str(row[0]))
                  self.lab_cafe3[(1,0)].setText(str(row[1]))
                  self.button_cafe3[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b38=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=38")               
               for row in self.b38:
                  self.button_cafe3[(1,1)].setText(str(row[0]))
                  self.lab_cafe3[(1,1)].setText(str(row[1]))
                  self.button_cafe3[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b39=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=39")               
               for row in self.b39:
                  self.button_cafe3[(1,2)].setText(str(row[0]))
                  self.lab_cafe3[(1,2)].setText(str(row[1]))
                  self.button_cafe3[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b40=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=40")               
               for row in self.b40:
                  self.button_cafe3[(1,3)].setText(str(row[0]))
                  self.lab_cafe3[(1,3)].setText(str(row[1]))
                  self.button_cafe3[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b41=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=41")               
               for row in self.b41:
                  self.button_cafe3[(2,0)].setText(str(row[0]))
                  self.lab_cafe3[(2,0)].setText(str(row[1]))
                  self.button_cafe3[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b42=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=42")               
               for row in self.b42:
                  self.button_cafe3[(2,1)].setText(str(row[0]))
                  self.lab_cafe3[(2,1)].setText(str(row[1]))
                  self.button_cafe3[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b43=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=43")               
               for row in self.b43:
                  self.button_cafe3[(2,2)].setText(str(row[0]))
                  self.lab_cafe3[(2,2)].setText(str(row[1]))
                  self.button_cafe3[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b44=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=44")               
               for row in self.b44:
                  self.button_cafe3[(2,3)].setText(str(row[0]))
                  self.lab_cafe3[(2,3)].setText(str(row[1]))
                  self.button_cafe3[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b45=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=45")               
               for row in self.b45:
                  self.button_cafe3[(3,0)].setText(str(row[0]))
                  self.lab_cafe3[(3,0)].setText(str(row[1]))
                  self.button_cafe3[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b46=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=46")               
               for row in self.b46:
                  self.button_cafe3[(3,1)].setText(str(row[0]))
                  self.lab_cafe3[(3,1)].setText(str(row[1]))
                  self.button_cafe3[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b47=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=47")               
               for row in self.b47:
                  self.button_cafe3[(3,2)].setText(str(row[0]))
                  self.lab_cafe3[(3,2)].setText(str(row[1]))
                  self.button_cafe3[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b48=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=48")               
               for row in self.b48:
                  self.button_cafe3[(3,3)].setText(str(row[0]))
                  self.lab_cafe3[(3,3)].setText(str(row[1]))
                  self.button_cafe3[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe3[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 4
               self.b49=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=49")               
               for row in self.b49:
                  self.button_cafe4[(0,0)].setText(str(row[0]))
                  self.lab_cafe4[(0,0)].setText(str(row[1]))
                  self.button_cafe4[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b50=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=50")           
               for row in self.b50:
                  self.button_cafe4[(0,1)].setText(str(row[0]))
                  self.lab_cafe4[(0,1)].setText(str(row[1]))
                  self.button_cafe4[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b51=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=51")               
               for row in self.b51:
                  self.button_cafe4[(0,2)].setText(str(row[0]))
                  self.lab_cafe4[(0,2)].setText(str(row[1]))
                  self.button_cafe4[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b52=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=52")               
               for row in self.b52:
                  self.button_cafe4[(0,3)].setText(str(row[0]))
                  self.lab_cafe4[(0,3)].setText(str(row[1]))
                  self.button_cafe4[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b53=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=53")               
               for row in self.b53:
                  self.button_cafe4[(1,0)].setText(str(row[0]))
                  self.lab_cafe4[(1,0)].setText(str(row[1]))
                  self.button_cafe4[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b54=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=54")               
               for row in self.b54:
                  self.button_cafe4[(1,1)].setText(str(row[0]))
                  self.lab_cafe4[(1,1)].setText(str(row[1]))
                  self.button_cafe4[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b55=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=55")               
               for row in self.b55:
                  self.button_cafe4[(1,2)].setText(str(row[0]))
                  self.lab_cafe4[(1,2)].setText(str(row[1]))
                  self.button_cafe4[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b56=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=56")               
               for row in self.b56:
                  self.button_cafe4[(1,3)].setText(str(row[0]))
                  self.lab_cafe4[(1,3)].setText(str(row[1]))
                  self.button_cafe4[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b57=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=57")               
               for row in self.b57:
                  self.button_cafe4[(2,0)].setText(str(row[0]))
                  self.lab_cafe4[(2,0)].setText(str(row[1]))
                  self.button_cafe4[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b58=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=58")               
               for row in self.b58:
                  self.button_cafe4[(2,1)].setText(str(row[0]))
                  self.lab_cafe4[(2,1)].setText(str(row[1]))
                  self.button_cafe4[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b59=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=59")               
               for row in self.b59:
                  self.button_cafe4[(2,2)].setText(str(row[0]))
                  self.lab_cafe4[(2,2)].setText(str(row[1]))
                  self.button_cafe4[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b60=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=60")               
               for row in self.b60:
                  self.button_cafe4[(2,3)].setText(str(row[0]))
                  self.lab_cafe4[(2,3)].setText(str(row[1]))
                  self.button_cafe4[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b61=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=61")               
               for row in self.b61:
                  self.button_cafe4[(3,0)].setText(str(row[0]))
                  self.lab_cafe4[(3,0)].setText(str(row[1]))
                  self.button_cafe4[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b62=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=62")               
               for row in self.b62:
                  self.button_cafe4[(3,1)].setText(str(row[0]))
                  self.lab_cafe4[(3,1)].setText(str(row[1]))
                  self.button_cafe4[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b63=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=63")               
               for row in self.b63:
                  self.button_cafe4[(3,2)].setText(str(row[0]))
                  self.lab_cafe4[(3,2)].setText(str(row[1]))
                  self.button_cafe4[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b64=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=64")               
               for row in self.b64:
                  self.button_cafe4[(3,3)].setText(str(row[0]))
                  self.lab_cafe4[(3,3)].setText(str(row[1]))
                  self.button_cafe4[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe4[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 5
               self.b65=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=65")               
               for row in self.b65:
                  self.button_cafe5[(0,0)].setText(str(row[0]))
                  self.lab_cafe5[(0,0)].setText(str(row[1]))
                  self.button_cafe5[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b66=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=66")             
               for row in self.b66:
                  self.button_cafe5[(0,1)].setText(str(row[0]))
                  self.lab_cafe5[(0,1)].setText(str(row[1]))
                  self.button_cafe5[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b67=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=67")               
               for row in self.b67:
                  self.button_cafe5[(0,2)].setText(str(row[0]))
                  self.lab_cafe5[(0,2)].setText(str(row[1]))
                  self.button_cafe5[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b68=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=68")               
               for row in self.b68:
                  self.button_cafe5[(0,3)].setText(str(row[0]))
                  self.lab_cafe5[(0,3)].setText(str(row[1]))
                  self.button_cafe5[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b69=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=69")               
               for row in self.b69:
                  self.button_cafe5[(1,0)].setText(str(row[0]))
                  self.lab_cafe5[(1,0)].setText(str(row[1]))
                  self.button_cafe5[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b70=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=70")               
               for row in self.b70:
                  self.button_cafe5[(1,1)].setText(str(row[0]))
                  self.lab_cafe5[(1,1)].setText(str(row[1]))
                  self.button_cafe5[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b71=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=71")               
               for row in self.b71:
                  self.button_cafe5[(1,2)].setText(str(row[0]))
                  self.lab_cafe5[(1,2)].setText(str(row[1]))
                  self.button_cafe5[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b72=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=72")               
               for row in self.b72:
                  self.button_cafe5[(1,3)].setText(str(row[0]))
                  self.lab_cafe5[(1,3)].setText(str(row[1]))
                  self.button_cafe5[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b73=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=73")               
               for row in self.b73:
                  self.button_cafe5[(2,0)].setText(str(row[0]))
                  self.lab_cafe5[(2,0)].setText(str(row[1]))
                  self.button_cafe5[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b74=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=74")               
               for row in self.b74:
                  self.button_cafe5[(2,1)].setText(str(row[0]))
                  self.lab_cafe5[(2,1)].setText(str(row[1]))
                  self.button_cafe5[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b75=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=75")               
               for row in self.b75:
                  self.button_cafe5[(2,2)].setText(str(row[0]))
                  self.lab_cafe5[(2,2)].setText(str(row[1]))
                  self.button_cafe5[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b76=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=76")               
               for row in self.b76:
                  self.button_cafe5[(2,3)].setText(str(row[0]))
                  self.lab_cafe5[(2,3)].setText(str(row[1]))
                  self.button_cafe5[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b77=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=77")               
               for row in self.b77:
                  self.button_cafe5[(3,0)].setText(str(row[0]))
                  self.lab_cafe5[(3,0)].setText(str(row[1]))
                  self.button_cafe5[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b78=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=78")               
               for row in self.b78:
                  self.button_cafe5[(3,1)].setText(str(row[0]))
                  self.lab_cafe5[(3,1)].setText(str(row[1]))
                  self.button_cafe5[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b79=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=79")               
               for row in self.b79:
                  self.button_cafe5[(3,2)].setText(str(row[0]))
                  self.lab_cafe5[(3,2)].setText(str(row[1]))
                  self.button_cafe5[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b80=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=80")               
               for row in self.b80:
                  self.button_cafe5[(3,3)].setText(str(row[0]))
                  self.lab_cafe5[(3,3)].setText(str(row[1]))
                  self.button_cafe5[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe5[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 6
               self.b81=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=81")               
               for row in self.b81:
                  self.button_cafe6[(0,0)].setText(str(row[0]))
                  self.lab_cafe6[(0,0)].setText(str(row[1]))
                  self.button_cafe6[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b82=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=82")               
               for row in self.b82:
                  self.button_cafe6[(0,1)].setText(str(row[0]))
                  self.lab_cafe6[(0,1)].setText(str(row[1]))
                  self.button_cafe6[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b83=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=83")               
               for row in self.b83:
                  self.button_cafe6[(0,2)].setText(str(row[0]))
                  self.lab_cafe6[(0,2)].setText(str(row[1]))
                  self.button_cafe6[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b84=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=84")               
               for row in self.b84:
                  self.button_cafe6[(0,3)].setText(str(row[0]))
                  self.lab_cafe6[(0,3)].setText(str(row[1]))
                  self.button_cafe6[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b85=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=85")               
               for row in self.b85:
                  self.button_cafe6[(1,0)].setText(str(row[0]))
                  self.lab_cafe6[(1,0)].setText(str(row[1]))
                  self.button_cafe6[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b86=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=86")               
               for row in self.b86:
                  self.button_cafe6[(1,1)].setText(str(row[0]))
                  self.lab_cafe6[(1,1)].setText(str(row[1]))
                  self.button_cafe6[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b87=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=87")               
               for row in self.b87:
                  self.button_cafe6[(1,2)].setText(str(row[0]))
                  self.lab_cafe6[(1,2)].setText(str(row[1]))
                  self.button_cafe6[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b88=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=88")               
               for row in self.b88:
                  self.button_cafe6[(1,3)].setText(str(row[0]))
                  self.lab_cafe6[(1,3)].setText(str(row[1]))
                  self.button_cafe6[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b89=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=89")               
               for row in self.b89:
                  self.button_cafe6[(2,0)].setText(str(row[0]))
                  self.lab_cafe6[(2,0)].setText(str(row[1]))
                  self.button_cafe6[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b90=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=90")               
               for row in self.b90:
                  self.button_cafe6[(2,1)].setText(str(row[0]))
                  self.lab_cafe6[(2,1)].setText(str(row[1]))
                  self.button_cafe6[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b91=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=91")               
               for row in self.b91:
                  self.button_cafe6[(2,2)].setText(str(row[0]))
                  self.lab_cafe6[(2,2)].setText(str(row[1]))
                  self.button_cafe6[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b92=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=92")               
               for row in self.b92:
                  self.button_cafe6[(2,3)].setText(str(row[0]))
                  self.lab_cafe6[(2,3)].setText(str(row[1]))
                  self.button_cafe6[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b93=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=93")               
               for row in self.b93:
                  self.button_cafe6[(3,0)].setText(str(row[0]))
                  self.lab_cafe6[(3,0)].setText(str(row[1]))
                  self.button_cafe6[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b94=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=94")               
               for row in self.b94:
                  self.button_cafe6[(3,1)].setText(str(row[0]))
                  self.lab_cafe6[(3,1)].setText(str(row[1]))
                  self.button_cafe6[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b95=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=95")               
               for row in self.b95:
                  self.button_cafe6[(3,2)].setText(str(row[0]))
                  self.lab_cafe6[(3,2)].setText(str(row[1]))
                  self.button_cafe6[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b96=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=96")               
               for row in self.b96:
                  self.button_cafe6[(3,3)].setText(str(row[0]))
                  self.lab_cafe6[(3,3)].setText(str(row[1]))
                  self.button_cafe6[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe6[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 7
               self.b97=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=97")               
               for row in self.b97:
                  self.button_cafe7[(0,0)].setText(str(row[0]))
                  self.lab_cafe7[(0,0)].setText(str(row[1]))
                  self.button_cafe7[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b98=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=98")               
               for row in self.b98:
                  self.button_cafe7[(0,1)].setText(str(row[0]))
                  self.lab_cafe7[(0,1)].setText(str(row[1]))
                  self.button_cafe7[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b99=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=99")               
               for row in self.b99:
                  self.button_cafe7[(0,2)].setText(str(row[0]))
                  self.lab_cafe7[(0,2)].setText(str(row[1]))
                  self.button_cafe7[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b100=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=100")               
               for row in self.b100:
                  self.button_cafe7[(0,3)].setText(str(row[0]))
                  self.lab_cafe7[(0,3)].setText(str(row[1]))
                  self.button_cafe7[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b101=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=101")               
               for row in self.b101:
                  self.button_cafe7[(1,0)].setText(str(row[0]))
                  self.lab_cafe7[(1,0)].setText(str(row[1]))
                  self.button_cafe7[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b102=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=102")               
               for row in self.b101:
                  self.button_cafe7[(1,1)].setText(str(row[0]))
                  self.lab_cafe7[(1,1)].setText(str(row[1]))
                  self.button_cafe7[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b103=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=103")               
               for row in self.b103:
                  self.button_cafe7[(1,2)].setText(str(row[0]))
                  self.lab_cafe7[(1,2)].setText(str(row[1]))
                  self.button_cafe7[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b104=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=104")               
               for row in self.b104:
                  self.button_cafe7[(1,3)].setText(str(row[0]))
                  self.lab_cafe7[(1,3)].setText(str(row[1]))
                  self.button_cafe7[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b105=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=105")               
               for row in self.b105:
                  self.button_cafe7[(2,0)].setText(str(row[0]))
                  self.lab_cafe7[(2,0)].setText(str(row[1]))
                  self.button_cafe7[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b106=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=106")               
               for row in self.b106:
                  self.button_cafe7[(2,1)].setText(str(row[0]))
                  self.lab_cafe7[(2,1)].setText(str(row[1]))
                  self.button_cafe7[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b107=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=107")               
               for row in self.b107:
                  self.button_cafe7[(2,2)].setText(str(row[0]))
                  self.lab_cafe7[(2,2)].setText(str(row[1]))
                  self.button_cafe7[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b108=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=108")               
               for row in self.b108:
                  self.button_cafe7[(2,3)].setText(str(row[0]))
                  self.lab_cafe7[(2,3)].setText(str(row[1]))
                  self.button_cafe7[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b109=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=109")               
               for row in self.b109:
                  self.button_cafe7[(3,0)].setText(str(row[0]))
                  self.lab_cafe7[(3,0)].setText(str(row[1]))
                  self.button_cafe7[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b110=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=110")               
               for row in self.b110:
                  self.button_cafe7[(3,1)].setText(str(row[0]))
                  self.lab_cafe7[(3,1)].setText(str(row[1]))
                  self.button_cafe7[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b111=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=111")               
               for row in self.b111:
                  self.button_cafe7[(3,2)].setText(str(row[0]))
                  self.lab_cafe7[(3,2)].setText(str(row[1]))
                  self.button_cafe7[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b112=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=112")               
               for row in self.b112:
                  self.button_cafe7[(3,3)].setText(str(row[0]))
                  self.lab_cafe7[(3,3)].setText(str(row[1]))
                  self.button_cafe7[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe7[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 8
               self.b113=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=113")               
               for row in self.b113:
                  self.button_cafe8[(0,0)].setText(str(row[0]))
                  self.lab_cafe8[(0,0)].setText(str(row[1]))
                  self.button_cafe8[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b114=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=114")           
               for row in self.b114:
                  self.button_cafe8[(0,1)].setText(str(row[0]))
                  self.lab_cafe8[(0,1)].setText(str(row[1]))
                  self.button_cafe8[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b115=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=115")               
               for row in self.b115:
                  self.button_cafe8[(0,2)].setText(str(row[0]))
                  self.lab_cafe8[(0,2)].setText(str(row[1]))
                  self.button_cafe8[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b116=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=116")               
               for row in self.b116:
                  self.button_cafe8[(0,3)].setText(str(row[0]))
                  self.lab_cafe8[(0,3)].setText(str(row[1]))
                  self.button_cafe8[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b117=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=117")               
               for row in self.b117:
                  self.button_cafe8[(1,0)].setText(str(row[0]))
                  self.lab_cafe8[(1,0)].setText(str(row[1]))
                  self.button_cafe8[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b118=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=118")               
               for row in self.b118:
                  self.button_cafe8[(1,1)].setText(str(row[0]))
                  self.lab_cafe8[(1,1)].setText(str(row[1]))
                  self.button_cafe8[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b119=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=119")               
               for row in self.b119:
                  self.button_cafe8[(1,2)].setText(str(row[0]))
                  self.lab_cafe8[(1,2)].setText(str(row[1]))
                  self.button_cafe8[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b120=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=120")               
               for row in self.b120:
                  self.button_cafe4[(1,3)].setText(str(row[0]))
                  self.lab_cafe8[(1,3)].setText(str(row[1]))
                  self.button_cafe8[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b121=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=121")               
               for row in self.b121:
                  self.button_cafe8[(2,0)].setText(str(row[0]))
                  self.lab_cafe8[(2,0)].setText(str(row[1]))
                  self.button_cafe8[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b122=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=122")               
               for row in self.b122:
                  self.button_cafe8[(2,1)].setText(str(row[0]))
                  self.lab_cafe8[(2,1)].setText(str(row[1]))
                  self.button_cafe8[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b123=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=123")               
               for row in self.b123:
                  self.button_cafe8[(2,2)].setText(str(row[0]))
                  self.lab_cafe8[(2,2)].setText(str(row[1]))
                  self.button_cafe8[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b124=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=124")               
               for row in self.b124:
                  self.button_cafe8[(2,3)].setText(str(row[0]))
                  self.lab_cafe8[(2,3)].setText(str(row[1]))
                  self.button_cafe8[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b125=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=125")               
               for row in self.b125:
                  self.button_cafe8[(3,0)].setText(str(row[0]))
                  self.lab_cafe8[(3,0)].setText(str(row[1]))
                  self.button_cafe8[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b126=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=126")               
               for row in self.b126:
                  self.button_cafe8[(3,1)].setText(str(row[0]))
                  self.lab_cafe8[(3,1)].setText(str(row[1]))
                  self.button_cafe8[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b127=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=127")               
               for row in self.b127:
                  self.button_cafe8[(3,2)].setText(str(row[0]))
                  self.lab_cafe8[(3,2)].setText(str(row[1]))
                  self.button_cafe8[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b128=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM cafes WHERE rowid=128")               
               for row in self.b128:
                  self.button_cafe8[(3,3)].setText(str(row[0]))
                  self.lab_cafe8[(3,3)].setText(str(row[1]))
                  self.button_cafe8[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_cafe8[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))

               #====================== REFRESH PLATS ==#
               #=======================================#
               #________PAGE 1
               self.b1=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=1")               
               for row in self.b1:
                  self.button_plat1[(0,0)].setText(str(row[0]))
                  self.lab_plat1[(0,0)].setText(str(row[1]))
                  self.button_plat1[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b2=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=2")             
               for row in self.b2:
                  self.button_plat1[(0,1)].setText(str(row[0]))
                  self.lab_plat1[(0,1)].setText(str(row[1]))
                  self.button_plat1[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b3=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=3")               
               for row in self.b3:
                  self.button_plat1[(0,2)].setText(str(row[0]))
                  self.lab_plat1[(0,2)].setText(str(row[1]))
                  self.button_plat1[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b4=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=4")               
               for row in self.b4:
                  self.button_plat1[(0,3)].setText(str(row[0]))
                  self.lab_plat1[(0,3)].setText(str(row[1]))
                  self.button_plat1[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b5=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=5")               
               for row in self.b5:
                  self.button_plat1[(1,0)].setText(str(row[0]))
                  self.lab_plat1[(1,0)].setText(str(row[1]))
                  self.button_plat1[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b6=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=6")               
               for row in self.b6:
                  self.button_plat1[(1,1)].setText(str(row[0]))
                  self.lab_plat1[(1,1)].setText(str(row[1]))
                  self.button_plat1[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b7=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=7")               
               for row in self.b7:
                  self.button_plat1[(1,2)].setText(str(row[0]))
                  self.lab_plat1[(1,2)].setText(str(row[1]))
                  self.button_plat1[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b8=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=8")               
               for row in self.b8:
                  self.button_plat1[(1,3)].setText(str(row[0]))
                  self.lab_plat1[(1,3)].setText(str(row[1]))
                  self.button_plat1[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b9=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=9")               
               for row in self.b9:
                  self.button_plat1[(2,0)].setText(str(row[0]))
                  self.lab_plat1[(2,0)].setText(str(row[1]))
                  self.button_plat1[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b10=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=10")               
               for row in self.b10:
                  self.button_plat1[(2,1)].setText(str(row[0]))
                  self.lab_plat1[(2,1)].setText(str(row[1]))
                  self.button_plat1[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b11=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=11")               
               for row in self.b11:
                  self.button_plat1[(2,2)].setText(str(row[0]))
                  self.lab_plat1[(2,2)].setText(str(row[1]))
                  self.button_plat1[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b12=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=12")               
               for row in self.b12:
                  self.button_plat1[(2,3)].setText(str(row[0]))
                  self.lab_plat1[(2,3)].setText(str(row[1]))
                  self.button_plat1[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b13=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=13")               
               for row in self.b13:
                  self.button_plat1[(3,0)].setText(str(row[0]))
                  self.lab_plat1[(3,0)].setText(str(row[1]))
                  self.button_plat1[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b14=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=14")               
               for row in self.b14:
                  self.button_plat1[(3,1)].setText(str(row[0]))
                  self.lab_plat1[(3,1)].setText(str(row[1]))
                  self.button_plat1[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b15=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=15")               
               for row in self.b15:
                  self.button_plat1[(3,2)].setText(str(row[0]))
                  self.lab_plat1[(3,2)].setText(str(row[1]))
                  self.button_plat1[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b16=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=16")               
               for row in self.b16:
                  self.button_plat1[(3,3)].setText(str(row[0]))
                  self.lab_plat1[(3,3)].setText(str(row[1]))
                  self.button_plat1[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat1[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 2
               self.b17=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=17")               
               for row in self.b17:
                  self.button_plat2[(0,0)].setText(str(row[0]))
                  self.lab_plat2[(0,0)].setText(str(row[1]))
                  self.button_plat2[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b18=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=18")               
               for row in self.b18:
                  self.button_plat2[(0,1)].setText(str(row[0]))
                  self.lab_plat2[(0,1)].setText(str(row[1]))
                  self.button_plat2[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b19=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=19")               
               for row in self.b19:
                  self.button_plat2[(0,2)].setText(str(row[0]))
                  self.lab_plat2[(0,2)].setText(str(row[1]))
                  self.button_plat2[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b20=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=20")               
               for row in self.b20:
                  self.button_plat2[(0,3)].setText(str(row[0]))
                  self.lab_plat2[(0,3)].setText(str(row[1]))
                  self.button_plat2[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b21=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=21")               
               for row in self.b21:
                  self.button_plat2[(1,0)].setText(str(row[0]))
                  self.lab_plat2[(1,0)].setText(str(row[1]))
                  self.button_plat2[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b22=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=22")               
               for row in self.b22:
                  self.button_plat2[(1,1)].setText(str(row[0]))
                  self.lab_plat2[(1,1)].setText(str(row[1]))
                  self.button_plat2[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b23=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=23")               
               for row in self.b23:
                  self.button_plat2[(1,2)].setText(str(row[0]))
                  self.lab_plat2[(1,2)].setText(str(row[1]))
                  self.button_plat2[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b24=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=24")               
               for row in self.b24:
                  self.button_plat2[(1,3)].setText(str(row[0]))
                  self.lab_plat2[(1,3)].setText(str(row[1]))
                  self.button_plat2[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b25=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=25")               
               for row in self.b25:
                  self.button_plat2[(2,0)].setText(str(row[0]))
                  self.lab_plat2[(2,0)].setText(str(row[1]))
                  self.button_plat2[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b26=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=26")               
               for row in self.b26:
                  self.button_plat2[(2,1)].setText(str(row[0]))
                  self.lab_plat2[(2,1)].setText(str(row[1]))
                  self.button_plat2[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b27=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=27")               
               for row in self.b27:
                  self.button_plat2[(2,2)].setText(str(row[0]))
                  self.lab_plat2[(2,2)].setText(str(row[1]))
                  self.button_plat2[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b28=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=28")               
               for row in self.b28:
                  self.button_plat2[(2,3)].setText(str(row[0]))
                  self.lab_plat2[(2,3)].setText(str(row[1]))
                  self.button_plat2[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b29=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=29")               
               for row in self.b29:
                  self.button_plat2[(3,0)].setText(str(row[0]))
                  self.lab_plat2[(3,0)].setText(str(row[1]))
                  self.button_plat2[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b30=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=30")               
               for row in self.b30:
                  self.button_plat2[(3,1)].setText(str(row[0]))
                  self.lab_plat2[(3,1)].setText(str(row[1]))
                  self.button_plat2[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b31=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=31")               
               for row in self.b31:
                  self.button_plat2[(3,2)].setText(str(row[0]))
                  self.lab_plat2[(3,2)].setText(str(row[1]))
                  self.button_plat2[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b32=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=32")               
               for row in self.b32:
                  self.button_plat2[(3,3)].setText(str(row[0]))
                  self.lab_plat2[(3,3)].setText(str(row[1]))
                  self.button_plat2[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat2[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 3
               self.b33=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=33")               
               for row in self.b33:
                  self.button_plat3[(0,0)].setText(str(row[0]))
                  self.lab_plat3[(0,0)].setText(str(row[1]))
                  self.button_plat3[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b34=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=34")               
               for row in self.b34:
                  self.button_plat3[(0,1)].setText(str(row[0]))
                  self.lab_plat3[(0,1)].setText(str(row[1]))
                  self.button_plat3[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b35=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=35")               
               for row in self.b35:
                  self.button_plat3[(0,2)].setText(str(row[0]))
                  self.lab_plat3[(0,2)].setText(str(row[1]))
                  self.button_plat3[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b36=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=36")               
               for row in self.b36:
                  self.button_plat3[(0,3)].setText(str(row[0]))
                  self.lab_plat3[(0,3)].setText(str(row[1]))
                  self.button_plat3[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b37=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=37")               
               for row in self.b37:
                  self.button_plat3[(1,0)].setText(str(row[0]))
                  self.lab_plat3[(1,0)].setText(str(row[1]))
                  self.button_plat3[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b38=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=38")               
               for row in self.b38:
                  self.button_plat3[(1,1)].setText(str(row[0]))
                  self.lab_plat3[(1,1)].setText(str(row[1]))
                  self.button_plat3[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b39=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=39")               
               for row in self.b39:
                  self.button_plat3[(1,2)].setText(str(row[0]))
                  self.lab_plat3[(1,2)].setText(str(row[1]))
                  self.button_plat3[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b40=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=40")               
               for row in self.b40:
                  self.button_plat3[(1,3)].setText(str(row[0]))
                  self.lab_plat3[(1,3)].setText(str(row[1]))
                  self.button_plat3[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b41=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=41")               
               for row in self.b41:
                  self.button_plat3[(2,0)].setText(str(row[0]))
                  self.lab_plat3[(2,0)].setText(str(row[1]))
                  self.button_plat3[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b42=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=42")               
               for row in self.b42:
                  self.button_plat3[(2,1)].setText(str(row[0]))
                  self.lab_plat3[(2,1)].setText(str(row[1]))
                  self.button_plat3[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b43=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=43")               
               for row in self.b43:
                  self.button_plat3[(2,2)].setText(str(row[0]))
                  self.lab_plat3[(2,2)].setText(str(row[1]))
                  self.button_plat3[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b44=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=44")               
               for row in self.b44:
                  self.button_plat3[(2,3)].setText(str(row[0]))
                  self.lab_plat3[(2,3)].setText(str(row[1]))
                  self.button_plat3[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b45=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=45")               
               for row in self.b45:
                  self.button_plat3[(3,0)].setText(str(row[0]))
                  self.lab_plat3[(3,0)].setText(str(row[1]))
                  self.button_plat3[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b46=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=46")               
               for row in self.b46:
                  self.button_plat3[(3,1)].setText(str(row[0]))
                  self.lab_plat3[(3,1)].setText(str(row[1]))
                  self.button_plat3[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b47=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=47")               
               for row in self.b47:
                  self.button_plat3[(3,2)].setText(str(row[0]))
                  self.lab_plat3[(3,2)].setText(str(row[1]))
                  self.button_plat3[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b48=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=48")               
               for row in self.b48:
                  self.button_plat3[(3,3)].setText(str(row[0]))
                  self.lab_plat3[(3,3)].setText(str(row[1]))
                  self.button_plat3[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat3[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 4
               self.b49=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=49")               
               for row in self.b49:
                  self.button_plat4[(0,0)].setText(str(row[0]))
                  self.lab_plat4[(0,0)].setText(str(row[1]))
                  self.button_plat4[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b50=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=50")           
               for row in self.b50:
                  self.button_plat4[(0,1)].setText(str(row[0]))
                  self.lab_plat4[(0,1)].setText(str(row[1]))
                  self.button_plat4[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b51=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=51")               
               for row in self.b51:
                  self.button_plat4[(0,2)].setText(str(row[0]))
                  self.lab_plat4[(0,2)].setText(str(row[1]))
                  self.button_plat4[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b52=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=52")               
               for row in self.b52:
                  self.button_plat4[(0,3)].setText(str(row[0]))
                  self.lab_plat4[(0,3)].setText(str(row[1]))
                  self.button_plat4[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b53=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=53")               
               for row in self.b53:
                  self.button_plat4[(1,0)].setText(str(row[0]))
                  self.lab_plat4[(1,0)].setText(str(row[1]))
                  self.button_plat4[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b54=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=54")               
               for row in self.b54:
                  self.button_plat4[(1,1)].setText(str(row[0]))
                  self.lab_plat4[(1,1)].setText(str(row[1]))
                  self.button_plat4[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b55=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=55")               
               for row in self.b55:
                  self.button_plat4[(1,2)].setText(str(row[0]))
                  self.lab_plat4[(1,2)].setText(str(row[1]))
                  self.button_plat4[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b56=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=56")               
               for row in self.b56:
                  self.button_plat4[(1,3)].setText(str(row[0]))
                  self.lab_plat4[(1,3)].setText(str(row[1]))
                  self.button_plat4[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b57=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=57")               
               for row in self.b57:
                  self.button_plat4[(2,0)].setText(str(row[0]))
                  self.lab_plat4[(2,0)].setText(str(row[1]))
                  self.button_plat4[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b58=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=58")               
               for row in self.b58:
                  self.button_plat4[(2,1)].setText(str(row[0]))
                  self.lab_plat4[(2,1)].setText(str(row[1]))
                  self.button_plat4[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b59=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=59")               
               for row in self.b59:
                  self.button_plat4[(2,2)].setText(str(row[0]))
                  self.lab_plat4[(2,2)].setText(str(row[1]))
                  self.button_plat4[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b60=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=60")               
               for row in self.b60:
                  self.button_plat4[(2,3)].setText(str(row[0]))
                  self.lab_plat4[(2,3)].setText(str(row[1]))
                  self.button_plat4[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b61=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=61")               
               for row in self.b61:
                  self.button_plat4[(3,0)].setText(str(row[0]))
                  self.lab_plat4[(3,0)].setText(str(row[1]))
                  self.button_plat4[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b62=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=62")               
               for row in self.b62:
                  self.button_plat4[(3,1)].setText(str(row[0]))
                  self.lab_plat4[(3,1)].setText(str(row[1]))
                  self.button_plat4[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b63=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=63")               
               for row in self.b63:
                  self.button_plat4[(3,2)].setText(str(row[0]))
                  self.lab_plat4[(3,2)].setText(str(row[1]))
                  self.button_plat4[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b64=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=64")               
               for row in self.b64:
                  self.button_plat4[(3,3)].setText(str(row[0]))
                  self.lab_plat4[(3,3)].setText(str(row[1]))
                  self.button_plat4[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat4[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 5
               self.b65=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=65")               
               for row in self.b65:
                  self.button_plat5[(0,0)].setText(str(row[0]))
                  self.lab_plat5[(0,0)].setText(str(row[1]))
                  self.button_plat5[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b66=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=66")             
               for row in self.b66:
                  self.button_plat5[(0,1)].setText(str(row[0]))
                  self.lab_plat5[(0,1)].setText(str(row[1]))
                  self.button_plat5[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b67=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=67")               
               for row in self.b67:
                  self.button_plat5[(0,2)].setText(str(row[0]))
                  self.lab_plat5[(0,2)].setText(str(row[1]))
                  self.button_plat5[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b68=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=68")               
               for row in self.b68:
                  self.button_plat5[(0,3)].setText(str(row[0]))
                  self.lab_plat5[(0,3)].setText(str(row[1]))
                  self.button_plat5[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b69=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=69")               
               for row in self.b69:
                  self.button_plat5[(1,0)].setText(str(row[0]))
                  self.lab_plat5[(1,0)].setText(str(row[1]))
                  self.button_plat5[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b70=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=70")               
               for row in self.b70:
                  self.button_plat5[(1,1)].setText(str(row[0]))
                  self.lab_plat5[(1,1)].setText(str(row[1]))
                  self.button_plat5[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b71=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=71")               
               for row in self.b71:
                  self.button_plat5[(1,2)].setText(str(row[0]))
                  self.lab_plat5[(1,2)].setText(str(row[1]))
                  self.button_plat5[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b72=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=72")               
               for row in self.b72:
                  self.button_plat5[(1,3)].setText(str(row[0]))
                  self.lab_plat5[(1,3)].setText(str(row[1]))
                  self.button_plat5[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b73=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=73")               
               for row in self.b73:
                  self.button_plat5[(2,0)].setText(str(row[0]))
                  self.lab_plat5[(2,0)].setText(str(row[1]))
                  self.button_plat5[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b74=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=74")               
               for row in self.b74:
                  self.button_plat5[(2,1)].setText(str(row[0]))
                  self.lab_plat5[(2,1)].setText(str(row[1]))
                  self.button_plat5[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b75=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=75")               
               for row in self.b75:
                  self.button_plat5[(2,2)].setText(str(row[0]))
                  self.lab_plat5[(2,2)].setText(str(row[1]))
                  self.button_plat5[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b76=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=76")               
               for row in self.b76:
                  self.button_plat5[(2,3)].setText(str(row[0]))
                  self.lab_plat5[(2,3)].setText(str(row[1]))
                  self.button_plat5[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b77=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=77")               
               for row in self.b77:
                  self.button_plat5[(3,0)].setText(str(row[0]))
                  self.lab_plat5[(3,0)].setText(str(row[1]))
                  self.button_plat5[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b78=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=78")               
               for row in self.b78:
                  self.button_plat5[(3,1)].setText(str(row[0]))
                  self.lab_plat5[(3,1)].setText(str(row[1]))
                  self.button_plat5[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b79=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=79")               
               for row in self.b79:
                  self.button_plat5[(3,2)].setText(str(row[0]))
                  self.lab_plat5[(3,2)].setText(str(row[1]))
                  self.button_plat5[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b80=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=80")               
               for row in self.b80:
                  self.button_plat5[(3,3)].setText(str(row[0]))
                  self.lab_plat5[(3,3)].setText(str(row[1]))
                  self.button_plat5[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat5[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 6
               self.b81=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=81")               
               for row in self.b81:
                  self.button_plat6[(0,0)].setText(str(row[0]))
                  self.lab_plat6[(0,0)].setText(str(row[1]))
                  self.button_plat6[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b82=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=82")               
               for row in self.b82:
                  self.button_plat6[(0,1)].setText(str(row[0]))
                  self.lab_plat6[(0,1)].setText(str(row[1]))
                  self.button_plat6[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b83=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=83")               
               for row in self.b83:
                  self.button_plat6[(0,2)].setText(str(row[0]))
                  self.lab_plat6[(0,2)].setText(str(row[1]))
                  self.button_plat6[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b84=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=84")               
               for row in self.b84:
                  self.button_plat6[(0,3)].setText(str(row[0]))
                  self.lab_plat6[(0,3)].setText(str(row[1]))
                  self.button_plat6[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b85=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=85")               
               for row in self.b85:
                  self.button_plat6[(1,0)].setText(str(row[0]))
                  self.lab_plat6[(1,0)].setText(str(row[1]))
                  self.button_plat6[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b86=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=86")               
               for row in self.b86:
                  self.button_plat6[(1,1)].setText(str(row[0]))
                  self.lab_plat6[(1,1)].setText(str(row[1]))
                  self.button_plat6[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b87=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=87")               
               for row in self.b87:
                  self.button_plat6[(1,2)].setText(str(row[0]))
                  self.lab_plat6[(1,2)].setText(str(row[1]))
                  self.button_plat6[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b88=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=88")               
               for row in self.b88:
                  self.button_plat6[(1,3)].setText(str(row[0]))
                  self.lab_plat6[(1,3)].setText(str(row[1]))
                  self.button_plat6[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b89=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=89")               
               for row in self.b89:
                  self.button_plat6[(2,0)].setText(str(row[0]))
                  self.lab_plat6[(2,0)].setText(str(row[1]))
                  self.button_plat6[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b90=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=90")               
               for row in self.b90:
                  self.button_plat6[(2,1)].setText(str(row[0]))
                  self.lab_plat6[(2,1)].setText(str(row[1]))
                  self.button_plat6[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b91=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=91")               
               for row in self.b91:
                  self.button_plat6[(2,2)].setText(str(row[0]))
                  self.lab_plat6[(2,2)].setText(str(row[1]))
                  self.button_plat6[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b92=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=92")               
               for row in self.b92:
                  self.button_plat6[(2,3)].setText(str(row[0]))
                  self.lab_plat6[(2,3)].setText(str(row[1]))
                  self.button_plat6[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b93=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=93")               
               for row in self.b93:
                  self.button_plat6[(3,0)].setText(str(row[0]))
                  self.lab_plat6[(3,0)].setText(str(row[1]))
                  self.button_plat6[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b94=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=94")               
               for row in self.b94:
                  self.button_plat6[(3,1)].setText(str(row[0]))
                  self.lab_plat6[(3,1)].setText(str(row[1]))
                  self.button_plat6[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b95=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=95")               
               for row in self.b95:
                  self.button_plat6[(3,2)].setText(str(row[0]))
                  self.lab_plat6[(3,2)].setText(str(row[1]))
                  self.button_plat6[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b96=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=96")               
               for row in self.b96:
                  self.button_plat6[(3,3)].setText(str(row[0]))
                  self.lab_plat6[(3,3)].setText(str(row[1]))
                  self.button_plat6[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat6[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 7
               self.b97=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=97")               
               for row in self.b97:
                  self.button_plat7[(0,0)].setText(str(row[0]))
                  self.lab_plat7[(0,0)].setText(str(row[1]))
                  self.button_plat7[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b98=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=98")               
               for row in self.b98:
                  self.button_plat7[(0,1)].setText(str(row[0]))
                  self.lab_plat7[(0,1)].setText(str(row[1]))
                  self.button_plat7[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b99=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=99")               
               for row in self.b99:
                  self.button_plat7[(0,2)].setText(str(row[0]))
                  self.lab_plat7[(0,2)].setText(str(row[1]))
                  self.button_plat7[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b100=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=100")               
               for row in self.b100:
                  self.button_plat7[(0,3)].setText(str(row[0]))
                  self.lab_plat7[(0,3)].setText(str(row[1]))
                  self.button_plat7[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b101=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=101")               
               for row in self.b101:
                  self.button_plat7[(1,0)].setText(str(row[0]))
                  self.lab_plat7[(1,0)].setText(str(row[1]))
                  self.button_plat7[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b102=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=102")               
               for row in self.b101:
                  self.button_plat7[(1,1)].setText(str(row[0]))
                  self.lab_plat7[(1,1)].setText(str(row[1]))
                  self.button_plat7[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b103=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=103")               
               for row in self.b103:
                  self.button_plat7[(1,2)].setText(str(row[0]))
                  self.lab_plat7[(1,2)].setText(str(row[1]))
                  self.button_plat7[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b104=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=104")               
               for row in self.b104:
                  self.button_plat7[(1,3)].setText(str(row[0]))
                  self.lab_plat7[(1,3)].setText(str(row[1]))
                  self.button_plat7[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b105=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=105")               
               for row in self.b105:
                  self.button_plat7[(2,0)].setText(str(row[0]))
                  self.lab_plat7[(2,0)].setText(str(row[1]))
                  self.button_plat7[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b106=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=106")               
               for row in self.b106:
                  self.button_plat7[(2,1)].setText(str(row[0]))
                  self.lab_plat7[(2,1)].setText(str(row[1]))
                  self.button_plat7[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b107=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=107")               
               for row in self.b107:
                  self.button_plat7[(2,2)].setText(str(row[0]))
                  self.lab_plat7[(2,2)].setText(str(row[1]))
                  self.button_plat7[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b108=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=108")               
               for row in self.b108:
                  self.button_plat7[(2,3)].setText(str(row[0]))
                  self.lab_plat7[(2,3)].setText(str(row[1]))
                  self.button_plat7[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b109=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=109")               
               for row in self.b109:
                  self.button_plat7[(3,0)].setText(str(row[0]))
                  self.lab_plat7[(3,0)].setText(str(row[1]))
                  self.button_plat7[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b110=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=110")               
               for row in self.b110:
                  self.button_plat7[(3,1)].setText(str(row[0]))
                  self.lab_plat7[(3,1)].setText(str(row[1]))
                  self.button_plat7[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b111=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=111")               
               for row in self.b111:
                  self.button_plat7[(3,2)].setText(str(row[0]))
                  self.lab_plat7[(3,2)].setText(str(row[1]))
                  self.button_plat7[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b112=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=112")               
               for row in self.b112:
                  self.button_plat7[(3,3)].setText(str(row[0]))
                  self.lab_plat7[(3,3)].setText(str(row[1]))
                  self.button_plat7[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat7[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 8
               self.b113=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=113")               
               for row in self.b113:
                  self.button_plat8[(0,0)].setText(str(row[0]))
                  self.lab_plat8[(0,0)].setText(str(row[1]))
                  self.button_plat8[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b114=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=114")           
               for row in self.b114:
                  self.button_plat8[(0,1)].setText(str(row[0]))
                  self.lab_plat8[(0,1)].setText(str(row[1]))
                  self.button_plat8[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b115=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=115")               
               for row in self.b115:
                  self.button_plat8[(0,2)].setText(str(row[0]))
                  self.lab_plat8[(0,2)].setText(str(row[1]))
                  self.button_plat8[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b116=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=116")               
               for row in self.b116:
                  self.button_plat8[(0,3)].setText(str(row[0]))
                  self.lab_plat8[(0,3)].setText(str(row[1]))
                  self.button_plat8[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b117=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=117")               
               for row in self.b117:
                  self.button_plat8[(1,0)].setText(str(row[0]))
                  self.lab_plat8[(1,0)].setText(str(row[1]))
                  self.button_plat8[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b118=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=118")               
               for row in self.b118:
                  self.button_plat8[(1,1)].setText(str(row[0]))
                  self.lab_plat8[(1,1)].setText(str(row[1]))
                  self.button_plat8[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b119=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=119")               
               for row in self.b119:
                  self.button_plat8[(1,2)].setText(str(row[0]))
                  self.lab_plat8[(1,2)].setText(str(row[1]))
                  self.button_plat8[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b120=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=120")               
               for row in self.b120:
                  self.button_plat4[(1,3)].setText(str(row[0]))
                  self.lab_plat8[(1,3)].setText(str(row[1]))
                  self.button_plat8[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b121=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=121")               
               for row in self.b121:
                  self.button_plat8[(2,0)].setText(str(row[0]))
                  self.lab_plat8[(2,0)].setText(str(row[1]))
                  self.button_plat8[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b122=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=122")               
               for row in self.b122:
                  self.button_plat8[(2,1)].setText(str(row[0]))
                  self.lab_plat8[(2,1)].setText(str(row[1]))
                  self.button_plat8[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b123=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=123")               
               for row in self.b123:
                  self.button_plat8[(2,2)].setText(str(row[0]))
                  self.lab_plat8[(2,2)].setText(str(row[1]))
                  self.button_plat8[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b124=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=124")               
               for row in self.b124:
                  self.button_plat8[(2,3)].setText(str(row[0]))
                  self.lab_plat8[(2,3)].setText(str(row[1]))
                  self.button_plat8[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b125=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=125")               
               for row in self.b125:
                  self.button_plat8[(3,0)].setText(str(row[0]))
                  self.lab_plat8[(3,0)].setText(str(row[1]))
                  self.button_plat8[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b126=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=126")               
               for row in self.b126:
                  self.button_plat8[(3,1)].setText(str(row[0]))
                  self.lab_plat8[(3,1)].setText(str(row[1]))
                  self.button_plat8[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b127=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=127")               
               for row in self.b127:
                  self.button_plat8[(3,2)].setText(str(row[0]))
                  self.lab_plat8[(3,2)].setText(str(row[1]))
                  self.button_plat8[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b128=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM plats WHERE rowid=128")               
               for row in self.b128:
                  self.button_plat8[(3,3)].setText(str(row[0]))
                  self.lab_plat8[(3,3)].setText(str(row[1]))
                  self.button_plat8[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_plat8[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.bdd.commit()

               #====================== REFRESH LAB ==#
               #=====================================#
               for x in range(4):
                  for y in range(4):
                     #====================== BOISSONS
                     self.lab_boisson1[(x,y)].adjustSize()

                     #====================== DESSERTS
                     self.lab_dessert1[(x,y)].adjustSize()
                     self.lab_dessert2[(x,y)].adjustSize()
                     self.lab_dessert3[(x,y)].adjustSize()
                     self.lab_dessert4[(x,y)].adjustSize()
                     self.lab_dessert5[(x,y)].adjustSize()
                     self.lab_dessert6[(x,y)].adjustSize()
                     self.lab_dessert7[(x,y)].adjustSize()
                     self.lab_dessert8[(x,y)].adjustSize()

                     #====================== CAFES
                     self.lab_cafe1[(x,y)].adjustSize()
                     self.lab_cafe2[(x,y)].adjustSize()
                     self.lab_cafe3[(x,y)].adjustSize()
                     self.lab_cafe4[(x,y)].adjustSize()
                     self.lab_cafe5[(x,y)].adjustSize()
                     self.lab_cafe6[(x,y)].adjustSize()
                     self.lab_cafe7[(x,y)].adjustSize()
                     self.lab_cafe8[(x,y)].adjustSize()

                     #====================== PLATS
                     self.lab_plat1[(x,y)].adjustSize()
                     self.lab_plat2[(x,y)].adjustSize()
                     self.lab_plat3[(x,y)].adjustSize()
                     self.lab_plat4[(x,y)].adjustSize()
                     self.lab_plat5[(x,y)].adjustSize()
                     self.lab_plat6[(x,y)].adjustSize()
                     self.lab_plat7[(x,y)].adjustSize()
                     self.lab_plat8[(x,y)].adjustSize()
                  
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass
      
   def get_data(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd and self.zone_title.text()=='BOISSONS':
               self.cursor=self.bdd.cursor()
               self.sql1=self.cursor.execute("""SELECT COUNT(*) FROM boissons """)             
               for row in self.sql1:
                  if self.id_produit.value()> int(row[0]):
                     self.nom_produit.setText("")
                     self.qte_produit.setValue(0)
                     self.prix_produit.setValue(0)
                     self.photo=""
                     self.cat_produit.setCurrentText("")
                     self.code_produit.setText("")
                     self.reduction_produit.setValue(0)
                  else:
                     self.sql2=self.cursor.execute("""SELECT nom,quantite,prix,photo,categorie,code_produit,reduction
                                                      FROM boissons WHERE rowid={0}""".format(str(self.id_produit.value())))             
                     for row in self.sql2:
                        self.nom_produit.setText(row[0])
                        self.qte_produit.setValue(int(row[1]))
                        self.prix_produit.setValue(float(row[2]))
                        self.photo=row[3]
                        self.cat_produit.setCurrentText(str(row[4]))
                        self.code_produit.setText(row[5])
                        self.reduction_produit.setValue(int(row[6]))
               self.bdd.commit()
               self.refresh_data()
            elif self.bdd and self.zone_title.text()=='DESSERTS':
               self.cursor=self.bdd.cursor()
               self.sql1=self.cursor.execute("""SELECT COUNT(*) FROM desserts """)             
               for row in self.sql1:
                  if self.id_produit.value()> int(row[0]):
                     self.nom_produit.setText("")
                     self.qte_produit.setValue(0)
                     self.prix_produit.setValue(0)
                     self.photo=""
                     self.cat_produit.setCurrentText("")
                     self.code_produit.setText("")
                     self.reduction_produit.setValue(0)
                  else:
                     self.sql2=self.cursor.execute("""SELECT nom,quantite,prix,photo,categorie,code_produit,reduction
                                                      FROM desserts WHERE rowid={0}""".format(str(self.id_produit.value())))             
                     for row in self.sql2:
                        self.nom_produit.setText(row[0])
                        self.qte_produit.setValue(int(row[1]))
                        self.prix_produit.setValue(float(row[2]))
                        self.photo=row[3]
                        self.cat_produit.setCurrentText(str(row[4]))
                        self.code_produit.setText(row[5])
                        self.reduction_produit.setValue(int(row[6]))
               self.bdd.commit()
               self.refresh_data()
            elif self.bdd and self.zone_title.text()=='CAFES':
               self.cursor=self.bdd.cursor()
               self.sql1=self.cursor.execute("""SELECT COUNT(*) FROM cafes """)             
               for row in self.sql1:
                  if self.id_produit.value()> int(row[0]):
                     self.nom_produit.setText("")
                     self.qte_produit.setValue(0)
                     self.prix_produit.setValue(0)
                     self.photo=""
                     self.cat_produit.setCurrentText("")
                     self.code_produit.setText("")
                     self.reduction_produit.setValue(0)
                  else:
                     self.sql2=self.cursor.execute("""SELECT nom,quantite,prix,photo,categorie,code_produit,reduction
                                                      FROM cafes WHERE rowid={0}""".format(str(self.id_produit.value())))             
                     for row in self.sql2:
                        self.nom_produit.setText(row[0])
                        self.qte_produit.setValue(int(row[1]))
                        self.prix_produit.setValue(float(row[2]))
                        self.photo=row[3]
                        self.cat_produit.setCurrentText(str(row[4]))
                        self.code_produit.setText(row[5])
                        self.reduction_produit.setValue(int(row[6]))
               self.bdd.commit()
               self.refresh_data()
            elif self.bdd and self.zone_title.text()=='PLATS':
               self.cursor=self.bdd.cursor()
               self.sql1=self.cursor.execute("""SELECT COUNT(*) FROM plats """)             
               for row in self.sql1:
                  if self.id_produit.value()> int(row[0]):
                     self.nom_produit.setText("")
                     self.qte_produit.setValue(0)
                     self.prix_produit.setValue(0)
                     self.photo=""
                     self.cat_produit.setCurrentText("")
                     self.code_produit.setText("")
                     self.reduction_produit.setValue(0)
                  else:
                     self.sql2=self.cursor.execute("""SELECT nom,quantite,prix,photo,categorie,code_produit,reduction
                                                      FROM plats WHERE rowid={0}""".format(str(self.id_produit.value())))             
                     for row in self.sql2:
                        self.nom_produit.setText(row[0])
                        self.qte_produit.setValue(int(row[1]))
                        self.prix_produit.setValue(float(row[2]))
                        self.photo=row[3]
                        self.cat_produit.setCurrentText(str(row[4]))
                        self.code_produit.setText(row[5])
                        self.reduction_produit.setValue(int(row[6]))
               self.bdd.commit()
               self.refresh_data()
            else:
               pass

   
   def add_data(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd and self.zone_title.text()=='BOISSONS':
               try:
                  self.index1=[]
                  self.ui="""{0}""".format(str(uuid.uuid4()).split('-')[0])
                  self.set_date= """{0}-{1}-{2}/{3}:{4}:{5}""".format(str(datetime.datetime.utcnow().day),
                                                                          str(datetime.datetime.utcnow().month),
                                                                          str(datetime.datetime.utcnow().year),
                                                                          str(datetime.datetime.utcnow().hour),
                                                                          str(datetime.datetime.utcnow().minute),
                                                                          str(datetime.datetime.utcnow().second))
                  self.cursor=self.bdd.cursor()

                  self.cursor.execute("""INSERT INTO boissons (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                           is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                    (self.id_produit.value(),
                                     self.nom_produit.text(),
                                     self.qte_produit.value(),
                                     self.prix_produit.value(),
                                     self.photo,
                                     self.cat_produit.currentText(),
                                     self.ui,
                                     self.set_date,
                                     self.reduction_produit.value(),
                                     "0","0","0","0","0"))

                  #==== MISE A JOUR ID PRODUIT
                  self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                   rownum,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                                   is_added,is_ordered,is_processed,is_shipped,is_paid FROM boissons""")
                  for i in self.s_ss:
                     self.index1.append(i)

                  self.cursor.execute("DELETE FROM boissons")
                  
                  self.cursor.executemany("""INSERT INTO boissons
                                            (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                            is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1)
               
                  self.bdd.commit()
                  self.refresh_data()
                  QMessageBox.information(self,str(self.app_name),'BOISSON AJOUTE AVEC SUCCES')
                  
               except:
                  self.bdd.rollback();self.refresh_all()
                  QMessageBox.information(self,str(self.app_name),"BOISSON NON AJOUTE\nUNE ERREUR S'EST PRODUITE")
                  
            elif self.bdd and self.zone_title.text()=='DESSERTS':
               try:
                  self.index1=[]
                  self.ui="""{0}""".format(str(uuid.uuid4()).split('-')[0])
                  self.set_date= """{0}-{1}-{2}/{3}:{4}:{5}""".format(str(datetime.datetime.utcnow().day),
                                                                          str(datetime.datetime.utcnow().month),
                                                                          str(datetime.datetime.utcnow().year),
                                                                          str(datetime.datetime.utcnow().hour),
                                                                          str(datetime.datetime.utcnow().minute),
                                                                          str(datetime.datetime.utcnow().second))
                  self.cursor=self.bdd.cursor()

                  self.cursor.execute("""INSERT INTO desserts (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                        is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                    (self.id_produit.value(),
                                     self.nom_produit.text(),
                                     self.qte_produit.value(),
                                     self.prix_produit.value(),
                                     self.photo,
                                     self.cat_produit.currentText(),
                                     self.ui,
                                     self.set_date,
                                     self.reduction_produit.value(),
                                     "0","0","0","0","0"))

                  #==== MISE A JOUR ID PRODUIT
                  self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                   rownum,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                                   is_added,is_ordered,is_processed,is_shipped,is_paid FROM desserts""")
                  for i in self.s_ss:
                     self.index1.append(i)

                  self.cursor.execute("DELETE FROM desserts")
                  
                  self.cursor.executemany("""INSERT INTO desserts
                                            (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                            is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1)               
                  self.bdd.commit()
                  self.refresh_data()
                  QMessageBox.information(self,str(self.app_name),'DESSERT AJOUTE AVEC SUCCES')
                  
               except:
                  self.bdd.rollback();self.refresh_all()
                  QMessageBox.information(self,str(self.app_name),"DESSERT NON AJOUTE\nUNE ERREUR S'EST PRODUITE")

            elif self.bdd and self.zone_title.text()=='CAFES':
               try:
                  self.index1=[]
                  self.ui="""{0}""".format(str(uuid.uuid4()).split('-')[0])
                  self.set_date= """{0}-{1}-{2}/{3}:{4}:{5}""".format(str(datetime.datetime.utcnow().day),
                                                                          str(datetime.datetime.utcnow().month),
                                                                          str(datetime.datetime.utcnow().year),
                                                                          str(datetime.datetime.utcnow().hour),
                                                                          str(datetime.datetime.utcnow().minute),
                                                                          str(datetime.datetime.utcnow().second))
                  self.cursor=self.bdd.cursor()

                  self.cursor.execute("""INSERT INTO cafes (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                       is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                    (self.id_produit.value(),
                                     self.nom_produit.text(),
                                     self.qte_produit.value(),
                                     self.prix_produit.value(),
                                     self.photo,
                                     self.cat_produit.currentText(),
                                     self.ui,
                                     self.set_date,
                                     self.reduction_produit.value(),
                                     "0","0","0","0","0"))

                  #==== MISE A JOUR ID PRODUIT
                  self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                   rownum,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                                   is_added,is_ordered,is_processed,is_shipped,is_paid FROM cafes""")
                  for i in self.s_ss:
                     self.index1.append(i)

                  self.cursor.execute("DELETE FROM cafes")
                  
                  self.cursor.executemany("""INSERT INTO cafes
                                            (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                            is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1) 
               
                  self.bdd.commit()
                  self.refresh_data()
                  QMessageBox.information(self,str(self.app_name),'CAFE AJOUTE AVEC SUCCES')
                  
               except:
                  self.bdd.rollback();self.refresh_all()
                  QMessageBox.information(self,str(self.app_name),"CAFE NON AJOUTE\nUNE ERREUR S'EST PRODUITE")

            elif self.bdd and self.zone_title.text()=='PLATS':
               try:
                  self.index1=[]
                  self.ui="""{0}""".format(str(uuid.uuid4()).split('-')[0])
                  self.set_date= """{0}-{1}-{2}/{3}:{4}:{5}""".format(str(datetime.datetime.utcnow().day),
                                                                          str(datetime.datetime.utcnow().month),
                                                                          str(datetime.datetime.utcnow().year),
                                                                          str(datetime.datetime.utcnow().hour),
                                                                          str(datetime.datetime.utcnow().minute),
                                                                          str(datetime.datetime.utcnow().second))
                  self.cursor=self.bdd.cursor()

                  self.cursor.execute("""INSERT INTO plats (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                       is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                    (self.id_produit.value(),
                                     self.nom_produit.text(),
                                     self.qte_produit.value(),
                                     self.prix_produit.value(),
                                     self.photo,
                                     self.cat_produit.currentText(),
                                     self.ui,
                                     self.set_date,
                                     self.reduction_produit.value(),
                                     "0","0","0","0","0"))

                  #==== MISE A JOUR ID PRODUIT
                  self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                   rownum,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                                   is_added,is_ordered,is_processed,is_shipped,is_paid FROM plats""")
                  for i in self.s_ss:
                     self.index1.append(i)

                  self.cursor.execute("DELETE FROM plats")
                  
                  self.cursor.executemany("""INSERT INTO plats
                                            (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                            is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1) 
               
                  self.bdd.commit()
                  self.refresh_data()
                  QMessageBox.information(self,str(self.app_name),'PLAT AJOUTE AVEC SUCCES')
                  
               except:
                  self.bdd.rollback();self.refresh_all()
                  QMessageBox.information(self,str(self.app_name),"PLAT NON AJOUTE\nUNE ERREUR S'EST PRODUITE")              
            else:
               pass
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass
               

   def modify_data(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd and self.zone_title.text()=='BOISSONS':
               try:
                  self.cursor=self.bdd.cursor()
                  self.cursor.execute(""" UPDATE boissons SET nom=?,quantite=?,prix=?,photo=?,categorie=?,reduction=?
                                          WHERE code_produit= {0}""".format("'"+str(self.code_produit.text())+"'"),
                                      (self.nom_produit.text(),
                                       self.qte_produit.value(),
                                       self.prix_produit.value(),
                                       self.photo,
                                       self.cat_produit.currentText(),
                                       self.reduction_produit.value()))

                  self.bdd.commit()
                  self.refresh_data()
                  QMessageBox.information(self,str(self.app_name),'BOISSON MODIFIE AVEC SUCCES')
                  
               except:
                  self.bdd.rollback();self.refresh_all()
                  QMessageBox.information(self,str(self.app_name),"BOISSON NON MODIFIE\nUNE ERREUR S'EST PRODUITE")
            elif self.bdd and self.zone_title.text()=='DESSERTS':
               try:
                  self.cursor=self.bdd.cursor()
                  self.cursor.execute(""" UPDATE desserts SET nom=?,quantite=?,prix=?,photo=?,categorie=?,reduction=?
                                          WHERE code_produit= {0}""".format("'"+str(self.code_produit.text())+"'"),
                                      (self.nom_produit.text(),
                                       self.qte_produit.value(),
                                       self.prix_produit.value(),
                                       self.photo,
                                       self.cat_produit.currentText(),
                                       self.reduction_produit.value()))

                  self.bdd.commit()
                  self.refresh_data()
                  QMessageBox.information(self,str(self.app_name),'DESSERT MODIFIE AVEC SUCCES')
                  
               except:
                  self.bdd.rollback();self.refresh_all()
                  QMessageBox.information(self,str(self.app_name),"DESSERT NON MODIFIE\nUNE ERREUR S'EST PRODUITE")            
            elif self.bdd and self.zone_title.text()=='CAFES':
               try:
                  self.cursor=self.bdd.cursor()
                  self.cursor.execute(""" UPDATE cafes SET nom=?,quantite=?,prix=?,photo=?,categorie=?,reduction=?
                                          WHERE code_produit= {0}""".format("'"+str(self.code_produit.text())+"'"),
                                      (self.nom_produit.text(),
                                       self.qte_produit.value(),
                                       self.prix_produit.value(),
                                       self.photo,
                                       self.cat_produit.currentText(),
                                       self.reduction_produit.value()))

                  self.bdd.commit()
                  self.refresh_data()
                  QMessageBox.information(self,str(self.app_name),'CAFE MODIFIE AVEC SUCCES')
                  
               except:
                  self.bdd.rollback();self.refresh_all()
                  QMessageBox.information(self,str(self.app_name),"CAFE NON MODIFIE\nUNE ERREUR S'EST PRODUITE")
            elif self.bdd and self.zone_title.text()=='PLATS':
               try:
                  self.cursor=self.bdd.cursor()
                  self.cursor.execute(""" UPDATE plats SET nom=?,quantite=?,prix=?,photo=?,categorie=?,reduction=?
                                          WHERE code_produit= {0}""".format("'"+str(self.code_produit.text())+"'"),
                                      (self.nom_produit.text(),
                                       self.qte_produit.value(),
                                       self.prix_produit.value(),
                                       self.photo,
                                       self.cat_produit.currentText(),
                                       self.reduction_produit.value()))

                  self.bdd.commit()
                  self.refresh_data()
                  QMessageBox.information(self,str(self.app_name),'PLAT MODIFIE AVEC SUCCES')
                  
               except:
                  self.bdd.rollback();self.refresh_all()
                  QMessageBox.information(self,str(self.app_name),"PLAT NON MODIFIE\nUNE ERREUR S'EST PRODUITE")               
            else:
               pass
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass

   def remove_data(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd and self.zone_title.text()=='BOISSONS':
               try:
                  self.index1=[]
                  self.nom_produit.setText('')
                  self.qte_produit.setValue(0)
                  self.prix_produit.setValue(0)
                  self.photo=''
                  self.cat_produit.setCurrentText('')
                  self.cursor=self.bdd.cursor()
                  self.cursor.execute("DELETE FROM boissons WHERE code_produit={0}".format("'"+str(self.code_produit.text())+"'"))
                  
                  #==== MISE A JOUR ID PRODUIT
                  self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                   rownum,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                                   is_added,is_ordered,is_processed,is_shipped,is_paid FROM boissons""")
                  for i in self.s_ss:
                     self.index1.append(i)

                  self.cursor.execute("DELETE FROM boissons")
                  
                  self.cursor.executemany("""INSERT INTO boissons
                                            (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                            is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1)                        
                           
                  self.bdd.commit()
                  self.refresh_data()
                  QMessageBox.information(self,str(self.app_name),'BOISSON RETIRE AVEC SUCCES')
               except:
                  self.bdd.rollback();self.refresh_all()
                  QMessageBox.information(self,str(self.app_name),"BOISSON NON RETIRE\nUNE ERREUR S'EST PRODUITE")
            elif self.bdd and self.zone_title.text()=='DESSERTS':
               try:
                  self.index1=[]
                  self.nom_produit.setText('')
                  self.qte_produit.setValue(0)
                  self.prix_produit.setValue(0)
                  self.photo=''
                  self.cat_produit.setCurrentText('')
                  self.cursor=self.bdd.cursor()
                  self.cursor.execute("DELETE FROM desserts WHERE code_produit={0}".format("'"+str(self.code_produit.text())+"'"))
                  
                  #==== MISE A JOUR ID PRODUIT
                  self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                   rownum,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                                   is_added,is_ordered,is_processed,is_shipped,is_paid FROM desserts""")
                  for i in self.s_ss:
                     self.index1.append(i)

                  self.cursor.execute("DELETE FROM desserts")
                  
                  self.cursor.executemany("""INSERT INTO desserts
                                            (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                            is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1)                      
                  self.bdd.commit()
                  self.refresh_data()
                  QMessageBox.information(self,str(self.app_name),'DESSERT RETIRE AVEC SUCCES')
               except:
                  self.bdd.rollback();self.refresh_all()
                  QMessageBox.information(self,str(self.app_name),"DESSERT NON RETIRE\nUNE ERREUR S'EST PRODUITE")
            elif self.bdd and self.zone_title.text()=='CAFES':
               try:
                  self.index1=[]
                  self.nom_produit.setText('')
                  self.qte_produit.setValue(0)
                  self.prix_produit.setValue(0)
                  self.photo=''
                  self.cat_produit.setCurrentText('')
                  self.cursor=self.bdd.cursor()
                  self.cursor.execute("DELETE FROM cafes WHERE code_produit={0}".format("'"+str(self.code_produit.text())+"'"))
                  
                  #==== MISE A JOUR ID PRODUIT
                  self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                   rownum,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                                   is_added,is_ordered,is_processed,is_shipped,is_paid FROM cafes""")
                  for i in self.s_ss:
                     self.index1.append(i)

                  self.cursor.execute("DELETE FROM cafes")
                  
                  self.cursor.executemany("""INSERT INTO cafes
                                            (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                            is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1)   
                           
                  self.bdd.commit()
                  self.refresh_data()
                  QMessageBox.information(self,str(self.app_name),'BOISSONS RETIRE AVEC SUCCES')
               except:
                  self.bdd.rollback();self.refresh_all()
                  QMessageBox.information(self,str(self.app_name),"BOISSONS NON RETIRE\nUNE ERREUR S'EST PRODUITE")
            elif self.bdd and self.zone_title.text()=='DESSERTS':
               try:
                  self.index1=[]
                  self.nom_produit.setText('')
                  self.qte_produit.setValue(0)
                  self.prix_produit.setValue(0)
                  self.photo=''
                  self.cat_produit.setCurrentText('')
                  self.cursor=self.bdd.cursor()

                  self.id_x=list(eval(self.id_x_produit.text()))

                  if len(self.id_x)==2:
                     self.cursor.execute("""DELETE FROM desserts WHERE rowid IN ({0},{1})""".format(int(self.id_x[0]),int(self.id_x[1])))
                  elif len(self.id_x)==3:
                     self.cursor.execute("""DELETE FROM desserts WHERE rowid IN ({0},{1},{2}) """.format(int(self.id_x[0]),int(self.id_x[1])
                                                                                                       ,int(self.id_x[2])))
                  elif len(self.id_x)==4:
                     self.cursor.execute("""DELETE FROM desserts WHERE rowid IN ({0},{1},{2},{3})""".format(int(self.id_x[0]),int(self.id_x[1])
                                                                                                       ,int(self.id_x[2]),int(self.id_x[3])))
                  elif len(self.id_x)==5:
                     self.cursor.execute("""DELETE FROM desserts WHERE rowid IN ({0},{1},{2},{3},{4}) """.format(int(self.id_x[0]),int(self.id_x[1])
                                                                                                       ,int(self.id_x[2]),int(self.id_x[3])
                                                                                                       ,int(self.id_x[4])))
                  elif len(self.id_x)==6:
                     self.cursor.execute("""DELETE FROM desserts WHERE rowid IN ({0},{1},{2},{3},{4}
                                                                  ,{5})""".format(int(self.id_x[0]),int(self.id_x[1])
                                                                                                       ,int(self.id_x[2]),int(self.id_x[3])
                                                                                                       ,int(self.id_x[4]),int(self.id_x[5])))
                  elif len(self.id_x)==7:
                     self.cursor.execute("""DELETE FROM desserts WHERE rowid IN ({0},{1},{2},{3},{4}
                                                                  ,{5},{6})""".format(int(self.id_x[0]),int(self.id_x[1])
                                                                                                       ,int(self.id_x[2]),int(self.id_x[3])
                                                                                                       ,int(self.id_x[4]),int(self.id_x[5])
                                                                                                       ,int(self.id_x[6])))
                  elif len(self.id_x)==8:
                     self.cursor.execute("""DELETE FROM desserts WHERE rowid IN ({0},{1},{2},{3},{4}
                                                                  ,{5},{6},{7})""".format(int(self.id_x[0]),int(self.id_x[1])
                                                                                                       ,int(self.id_x[2]),int(self.id_x[3])
                                                                                                       ,int(self.id_x[4]),int(self.id_x[5])
                                                                                                       ,int(self.id_x[6]),int(self.id_x[7])))
                  elif len(self.id_x)==9:
                     self.cursor.execute("""DELETE FROM desserts WHERE rowid IN ({0},{1},{2},{3},{4}
                                                                  ,{5},{6},{7},{8}) """.format(int(self.id_x[0]),int(self.id_x[1])
                                                                                                       ,int(self.id_x[2]),int(self.id_x[3])
                                                                                                       ,int(self.id_x[4]),int(self.id_x[5])
                                                                                                       ,int(self.id_x[6]),int(self.id_x[7])
                                                                                                       ,int(self.id_x[8])))
                  elif len(self.id_x)==10:
                     self.cursor.execute("""DELETE FROM desserts WHERE rowid IN ({0},{1},{2},{3},{4}
                                                                  ,{5},{6},{7},{8},{9}) """.format(int(self.id_x[0]),int(self.id_x[1])
                                                                                                       ,int(self.id_x[2]),int(self.id_x[3])
                                                                                                       ,int(self.id_x[4]),int(self.id_x[5])
                                                                                                       ,int(self.id_x[6]),int(self.id_x[7])
                                                                                                       ,int(self.id_x[8]),int(self.id_x[9])))
                  
                  #==== MISE A JOUR ID PRODUIT
                  self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                   rownum,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                                   is_added,is_ordered,is_processed,is_shipped,is_paid FROM desserts""")
                  for i in self.s_ss:
                     self.index1.append(i)

                  self.cursor.execute("DELETE FROM desserts")
                  
                  self.cursor.executemany("""INSERT INTO desserts
                                            (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                            is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1)    
                           
                  self.bdd.commit()
                  self.refresh_data()
                  QMessageBox.information(self,str(self.app_name),'PLATS RETIRE AVEC SUCCES')
               except:
                  self.bdd.rollback();self.refresh_all()
                  QMessageBox.information(self,str(self.app_name),"PLATS NON RETIRE\nUNE ERREUR S'EST PRODUITE")
                               
            else:
               pass
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass

   

   #_____________________________________ FOR CATEGORIES
   
   def selection_cat(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.s_qs=self.cursor.execute("SELECT id FROM categories WHERE categorie={0}".format(str(self.nom_cat.text())))
               for i in self.s_qs:
                  self.id_produit.setValue(i[0])

               self.bdd.commit()


   def refresh_cat(self):
      self.index1=[]
      self.group=[]
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()

               #==== MISE A JOUR ID DANS LA TABLE CATEGORIE
               self.s_ss=self.cursor.execute("SELECT row_number() OVER (ORDER BY categorie) rownum,categorie FROM categories")
               for i in self.s_ss:
                  
                  self.index1.append(i)
                  self.group.append(i[1])
                  self.cat_produit.clear()
                  self.cat_produit.addItems(self.group)

               self.cursor.execute("DELETE FROM categories")
               self.cursor.executemany("""INSERT INTO categories (id,categorie) VALUES (?,?)""",self.index1)
                                             
               self.bdd.commit()

   def add_cat(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.cursor.execute("INSERT INTO categories ( categorie ) VALUES ({0}) ".format("'"+str(self.nom_cat.text())+"'"))
               self.bdd.commit()
               QMessageBox.information(self,str(self.app_name),'CATEGORIE AJOUTE AVEC SUCCES')
               self.refresh_cat()
                  

   def remove_cat(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.cursor.execute("DELETE FROM categories WHERE categorie={0}".format("'"+str(self.cat_produit.currentText())+"'"))
               self.bdd.commit()
               QMessageBox.information(self,str(self.app_name),'CATEGORIE RETIRE AVEC SUCCES')
               self.refresh_cat()

   """

   #_________________________________________DRAG MAIN WINDOW EVENTS BEGINNING
   def mousePressEvent(self, event):
      if event.button() == Qt.LeftButton:
         self.offset = event.pos()
      else:
         self.offset = None
         super().mousePressEvent(event)
         
   def mouseMoveEvent(self, event):
      if self.offset is not None and event.buttons() == Qt.LeftButton:
         self.move(self.pos() + event.pos() - self.offset)
      else:
         self.offset = None
         super().mouseMoveEvent(event)
         
   def mouseReleaseEvent(self, event):
      self.offset = None
      super().mouseReleaseEvent(event)
   #_________________________________________DRAG MAIN WINDOW EVENTS END"""

if __name__=='__main__':
   app=QApplication(sys.argv)
   app.setStyle('plastique')
   screen=Stock()   
   screen.show()
   sys.exit(app.exec_())
