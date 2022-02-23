#####################################
# IZI TOC V1.0 by Edan_Zoung
#####################################

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import sys
import sqlite3

from panier import Panier
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

class Dash(QMainWindow):
   def __init__(self):
      super().__init__()
      self.width=1200
      self.height=600
      self.set=0
      self.cart=0
      self.cart_price=0
      self.type=''
      self.app_name=name_app

      
      
      # this will hide the title bar
      #self.setWindowFlag(Qt.FramelessWindowHint)
      self.offset = None
      self.setGeometry(100,100,self.width,self.height)
      self.setWindowTitle('RESTAURANT')
      self.setStyleSheet("""
                          QMainWindow{ background-color:#000;color:#fff;
                             background-image: url("assets/background2.jpg"); 
                             background-repeat: no-repeat; 
                             background-position: center;}
                          QMessageBox{ background-color:#fff
                          }
                         """)
      #self.setFixedSize(self.width,self.height)
      self.setWindowOpacity(1)
      #self._row=0

      self.list_boisson_size=100
      self.list_dessert_size=100
      self.list_cafe_size=100
      self.list_plat_size=100

      self.button_boisson1={}
      self.button_boisson2={}
      self.button_boisson3={}
      self.button_boisson4={}
      self.button_boisson5={}
      self.button_boisson6={}
      self.button_boisson7={}
      self.button_boisson8={}
      self.lab_boisson1={}
      self.lab_boisson2={}
      self.lab_boisson3={}
      self.lab_boisson4={}
      self.lab_boisson5={}
      self.lab_boisson6={}
      self.lab_boisson7={}
      self.lab_boisson8={}

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
      self.refresh_boisson()
      #self._row=self._row
      self.refresh_dessert()
      self.refresh_cafe()
      self.refresh_plat()
      self.refresh_cart()
      self.showMaximized()
      
      
   def widgets(self):
      #______________________________________________INTERFACE  VENTES BEGINNING
      self.x=0
      self.y=0
      self.w_size_b=100
      self.h_size_b=100
      self.icon_size=80
      self.button_vente1={}
      self.button_vente2={}
      self.button_vente3={}
      self.button_vente4={}
      self.lab_vente1={}
      self.lab_vente2={}
      self.lab_vente3={}
      self.lab_vente4={}

      #_______TITLE PRODUITS ZONE
      self.zone_title=QLabel('BOISSONS',self)
      self.zone_title.setStyleSheet("""
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:20pt;
                                  font-weight:bold;
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
      self.btn_boisson.move(505,20)
      self.btn_boisson.resize(80,30)
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
      self.btn_dessert.move(605,20)
      self.btn_dessert.resize(80,30)
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
      self.btn_cafe.move(705,20)
      self.btn_cafe.resize(80,30)
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
      self.btn_plat.move(805,20)
      self.btn_plat.resize(80,30)


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
      self.boisson1.resize(400,800)

      
      for i in range(4):
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

      #_________BOISSON PAGE 2
      self.boisson2=QWidget()
      self.boisson2.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)

      self.boisson2.move(5,5)
      self.boisson2.resize(400,400)


      for i in range(4):
          for j in range(4):
              self.button_boisson2[(i,j)]=QToolButton(self.boisson2)
              self.button_boisson2[(i,j)].setStyleSheet("""
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
              self.button_boisson2[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_boisson2[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_boisson2[(i,j)].resize(100,100)
              self.lab_boisson2[(i,j)]=QLabel(self.boisson2)
              self.lab_boisson2[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_boisson2[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_boisson2[(i,j)].adjustSize()


      #_________BOISSON PAGE 3
      self.boisson3=QWidget()
      self.boisson3.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.boisson3.move(5,5)
      self.boisson3.resize(400,400)

      for i in range(4):
          for j in range(4):
              self.button_boisson3[(i,j)]=QToolButton(self.boisson3)
              self.button_boisson3[(i,j)].setStyleSheet("""
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
              self.button_boisson3[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_boisson3[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_boisson3[(i,j)].resize(100,100)
              self.lab_boisson3[(i,j)]=QLabel(self.boisson3)
              self.lab_boisson3[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_boisson3[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_boisson3[(i,j)].adjustSize()


      #_________BOISSON PAGE 4
      self.boisson4=QWidget()
      self.boisson4.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.boisson4.move(5,5)
      self.boisson4.resize(400,400)

      for i in range(4):
          for j in range(4):
              self.button_boisson4[(i,j)]=QToolButton(self.boisson4)
              self.button_boisson4[(i,j)].setStyleSheet("""
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
              self.button_boisson4[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_boisson4[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_boisson4[(i,j)].resize(100,100)
              self.lab_boisson4[(i,j)]=QLabel(self.boisson4)
              self.lab_boisson4[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_boisson4[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_boisson4[(i,j)].adjustSize()


      #_________BOISSON PAGE 5
      self.boisson5=QWidget()
      self.boisson5.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.boisson5.move(5,5)
      self.boisson5.resize(400,400)

      for i in range(4):
          for j in range(4):
              self.button_boisson5[(i,j)]=QToolButton(self.boisson5)
              self.button_boisson5[(i,j)].setStyleSheet("""
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
              self.button_boisson5[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_boisson5[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_boisson5[(i,j)].resize(100,100)
              self.lab_boisson5[(i,j)]=QLabel(self.boisson5)
              self.lab_boisson5[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_boisson5[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_boisson5[(i,j)].adjustSize()


      #_________BOISSON PAGE 6
      self.boisson6=QWidget()
      self.boisson6.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.boisson6.move(5,5)
      self.boisson6.resize(400,400)

      for i in range(4):
          for j in range(4):
              self.button_boisson6[(i,j)]=QToolButton(self.boisson6)
              self.button_boisson6[(i,j)].setStyleSheet("""
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
              self.button_boisson6[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_boisson6[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_boisson6[(i,j)].resize(100,100)
              self.lab_boisson6[(i,j)]=QLabel(self.boisson6)
              self.lab_boisson6[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_boisson6[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_boisson6[(i,j)].adjustSize()



      #_________BOISSON PAGE 7
      self.boisson7=QWidget()
      self.boisson7.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.boisson7.move(5,5)
      self.boisson7.resize(400,400)

      for i in range(4):
          for j in range(4):
              self.button_boisson7[(i,j)]=QToolButton(self.boisson7)
              self.button_boisson7[(i,j)].setStyleSheet("""
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
              self.button_boisson7[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_boisson7[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_boisson7[(i,j)].resize(100,100)
              self.lab_boisson7[(i,j)]=QLabel(self.boisson7)
              self.lab_boisson7[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_boisson7[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_boisson7[(i,j)].adjustSize()



      #_________BOISSON PAGE 8
      self.boisson8=QWidget()
      self.boisson8.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.boisson8.move(5,5)
      self.boisson8.resize(400,400)


      for i in range(4):
          for j in range(4):
              self.button_boisson8[(i,j)]=QToolButton(self.boisson8)
              self.button_boisson8[(i,j)].setStyleSheet("""
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
              self.button_boisson8[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_boisson8[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_boisson8[(i,j)].resize(100,100)
              self.lab_boisson8[(i,j)]=QLabel(self.boisson8)
              self.lab_boisson8[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_boisson8[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_boisson8[(i,j)].adjustSize()


      self.data_boisson=[self.boisson1,self.boisson2,self.boisson3,self.boisson4,self.boisson5,self.boisson6,self.boisson7,self.boisson8]

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

          self.item1.setSizeHint(QSize(0,400))
         
          self.list_boisson.addItem(self.item1)
          self.list_boisson.setItemWidget(self.item1,self.item_widget1)
      
         
      
      self.lab_boisson1[(0,0)].move(self.x,self.y)
      self.lab_boisson1[(0,1)].move(self.x+100,self.y)
      self.lab_boisson1[(0,2)].move(self.x+200,self.y)
      self.lab_boisson1[(0,3)].move(self.x+300,self.y)
      self.lab_boisson1[(1,0)].move(self.x,self.y+100)
      self.lab_boisson1[(1,1)].move(self.x+100,self.y+100)
      self.lab_boisson1[(1,2)].move(self.x+200,self.y+100)
      self.lab_boisson1[(1,3)].move(self.x+300,self.y+100)
      self.lab_boisson1[(2,0)].move(self.x,self.y+200)
      self.lab_boisson1[(2,1)].move(self.x+100,self.y+200)
      self.lab_boisson1[(2,2)].move(self.x+200,self.y+200)
      self.lab_boisson1[(2,3)].move(self.x+300,self.y+200)
      self.lab_boisson1[(3,0)].move(self.x,self.y+300)
      self.lab_boisson1[(3,1)].move(self.x+100,self.y+300)
      self.lab_boisson1[(3,2)].move(self.x+200,self.y+300)
      self.lab_boisson1[(3,3)].move(self.x+300,self.y+300)
      
      self.button_boisson1[(0,0)].move(self.x,self.y)
      self.button_boisson1[(0,1)].move(self.x+100,self.y)
      self.button_boisson1[(0,2)].move(self.x+200,self.y)
      self.button_boisson1[(0,3)].move(self.x+300,self.y)
      self.button_boisson1[(1,0)].move(self.x,self.y+100)
      self.button_boisson1[(1,1)].move(self.x+100,self.y+100)
      self.button_boisson1[(1,2)].move(self.x+200,self.y+100)
      self.button_boisson1[(1,3)].move(self.x+300,self.y+100)
      self.button_boisson1[(2,0)].move(self.x,self.y+200)
      self.button_boisson1[(2,1)].move(self.x+100,self.y+200)
      self.button_boisson1[(2,2)].move(self.x+200,self.y+200)
      self.button_boisson1[(2,3)].move(self.x+300,self.y+200)
      self.button_boisson1[(3,0)].move(self.x,self.y+300)
      self.button_boisson1[(3,1)].move(self.x+100,self.y+300)
      self.button_boisson1[(3,2)].move(self.x+200,self.y+300)
      self.button_boisson1[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 2
      
      self.lab_boisson2[(0,0)].move(self.x,self.y)
      self.lab_boisson2[(0,1)].move(self.x+100,self.y)
      self.lab_boisson2[(0,2)].move(self.x+200,self.y)
      self.lab_boisson2[(0,3)].move(self.x+300,self.y)
      self.lab_boisson2[(1,0)].move(self.x,self.y+100)
      self.lab_boisson2[(1,1)].move(self.x+100,self.y+100)
      self.lab_boisson2[(1,2)].move(self.x+200,self.y+100)
      self.lab_boisson2[(1,3)].move(self.x+300,self.y+100)
      self.lab_boisson2[(2,0)].move(self.x,self.y+200)
      self.lab_boisson2[(2,1)].move(self.x+100,self.y+200)
      self.lab_boisson2[(2,2)].move(self.x+200,self.y+200)
      self.lab_boisson2[(2,3)].move(self.x+300,self.y+200)
      self.lab_boisson2[(3,0)].move(self.x,self.y+300)
      self.lab_boisson2[(3,1)].move(self.x+100,self.y+300)
      self.lab_boisson2[(3,2)].move(self.x+200,self.y+300)
      self.lab_boisson2[(3,3)].move(self.x+300,self.y+300)
      
      self.button_boisson2[(0,0)].move(self.x,self.y)
      self.button_boisson2[(0,1)].move(self.x+100,self.y)
      self.button_boisson2[(0,2)].move(self.x+200,self.y)
      self.button_boisson2[(0,3)].move(self.x+300,self.y)
      self.button_boisson2[(1,0)].move(self.x,self.y+100)
      self.button_boisson2[(1,1)].move(self.x+100,self.y+100)
      self.button_boisson2[(1,2)].move(self.x+200,self.y+100)
      self.button_boisson2[(1,3)].move(self.x+300,self.y+100)
      self.button_boisson2[(2,0)].move(self.x,self.y+200)
      self.button_boisson2[(2,1)].move(self.x+100,self.y+200)
      self.button_boisson2[(2,2)].move(self.x+200,self.y+200)
      self.button_boisson2[(2,3)].move(self.x+300,self.y+200)
      self.button_boisson2[(3,0)].move(self.x,self.y+300)
      self.button_boisson2[(3,1)].move(self.x+100,self.y+300)
      self.button_boisson2[(3,2)].move(self.x+200,self.y+300)
      self.button_boisson2[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 3

      self.lab_boisson3[(0,0)].move(self.x,self.y)
      self.lab_boisson3[(0,1)].move(self.x+100,self.y)
      self.lab_boisson3[(0,2)].move(self.x+200,self.y)
      self.lab_boisson3[(0,3)].move(self.x+300,self.y)
      self.lab_boisson3[(1,0)].move(self.x,self.y+100)
      self.lab_boisson3[(1,1)].move(self.x+100,self.y+100)
      self.lab_boisson3[(1,2)].move(self.x+200,self.y+100)
      self.lab_boisson3[(1,3)].move(self.x+300,self.y+100)
      self.lab_boisson3[(2,0)].move(self.x,self.y+200)
      self.lab_boisson3[(2,1)].move(self.x+100,self.y+200)
      self.lab_boisson3[(2,2)].move(self.x+200,self.y+200)
      self.lab_boisson3[(2,3)].move(self.x+300,self.y+200)
      self.lab_boisson3[(3,0)].move(self.x,self.y+300)
      self.lab_boisson3[(3,1)].move(self.x+100,self.y+300)
      self.lab_boisson3[(3,2)].move(self.x+200,self.y+300)
      self.lab_boisson3[(3,3)].move(self.x+300,self.y+300)

      self.button_boisson3[(0,0)].move(self.x,self.y)
      self.button_boisson3[(0,1)].move(self.x+100,self.y)
      self.button_boisson3[(0,2)].move(self.x+200,self.y)
      self.button_boisson3[(0,3)].move(self.x+300,self.y)
      self.button_boisson3[(1,0)].move(self.x,self.y+100)
      self.button_boisson3[(1,1)].move(self.x+100,self.y+100)
      self.button_boisson3[(1,2)].move(self.x+200,self.y+100)
      self.button_boisson3[(1,3)].move(self.x+300,self.y+100)
      self.button_boisson3[(2,0)].move(self.x,self.y+200)
      self.button_boisson3[(2,1)].move(self.x+100,self.y+200)
      self.button_boisson3[(2,2)].move(self.x+200,self.y+200)
      self.button_boisson3[(2,3)].move(self.x+300,self.y+200)
      self.button_boisson3[(3,0)].move(self.x,self.y+300)
      self.button_boisson3[(3,1)].move(self.x+100,self.y+300)
      self.button_boisson3[(3,2)].move(self.x+200,self.y+300)
      self.button_boisson3[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 4

      self.lab_boisson4[(0,0)].move(self.x,self.y)
      self.lab_boisson4[(0,1)].move(self.x+100,self.y)
      self.lab_boisson4[(0,2)].move(self.x+200,self.y)
      self.lab_boisson4[(0,3)].move(self.x+300,self.y)
      self.lab_boisson4[(1,0)].move(self.x,self.y+100)
      self.lab_boisson4[(1,1)].move(self.x+100,self.y+100)
      self.lab_boisson4[(1,2)].move(self.x+200,self.y+100)
      self.lab_boisson4[(1,3)].move(self.x+300,self.y+100)
      self.lab_boisson4[(2,0)].move(self.x,self.y+200)
      self.lab_boisson4[(2,1)].move(self.x+100,self.y+200)
      self.lab_boisson4[(2,2)].move(self.x+200,self.y+200)
      self.lab_boisson4[(2,3)].move(self.x+300,self.y+200)
      self.lab_boisson4[(3,0)].move(self.x,self.y+300)
      self.lab_boisson4[(3,1)].move(self.x+100,self.y+300)
      self.lab_boisson4[(3,2)].move(self.x+200,self.y+300)
      self.lab_boisson4[(3,3)].move(self.x+300,self.y+300)

      self.button_boisson4[(0,0)].move(self.x,self.y)
      self.button_boisson4[(0,1)].move(self.x+100,self.y)
      self.button_boisson4[(0,2)].move(self.x+200,self.y)
      self.button_boisson4[(0,3)].move(self.x+300,self.y)
      self.button_boisson4[(1,0)].move(self.x,self.y+100)
      self.button_boisson4[(1,1)].move(self.x+100,self.y+100)
      self.button_boisson4[(1,2)].move(self.x+200,self.y+100)
      self.button_boisson4[(1,3)].move(self.x+300,self.y+100)
      self.button_boisson4[(2,0)].move(self.x,self.y+200)
      self.button_boisson4[(2,1)].move(self.x+100,self.y+200)
      self.button_boisson4[(2,2)].move(self.x+200,self.y+200)
      self.button_boisson4[(2,3)].move(self.x+300,self.y+200)
      self.button_boisson4[(3,0)].move(self.x,self.y+300)
      self.button_boisson4[(3,1)].move(self.x+100,self.y+300)
      self.button_boisson4[(3,2)].move(self.x+200,self.y+300)
      self.button_boisson4[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 5

      self.lab_boisson5[(0,0)].move(self.x,self.y)
      self.lab_boisson5[(0,1)].move(self.x+100,self.y)
      self.lab_boisson5[(0,2)].move(self.x+200,self.y)
      self.lab_boisson5[(0,3)].move(self.x+300,self.y)
      self.lab_boisson5[(1,0)].move(self.x,self.y+100)
      self.lab_boisson5[(1,1)].move(self.x+100,self.y+100)
      self.lab_boisson5[(1,2)].move(self.x+200,self.y+100)
      self.lab_boisson5[(1,3)].move(self.x+300,self.y+100)
      self.lab_boisson5[(2,0)].move(self.x,self.y+200)
      self.lab_boisson5[(2,1)].move(self.x+100,self.y+200)
      self.lab_boisson5[(2,2)].move(self.x+200,self.y+200)
      self.lab_boisson5[(2,3)].move(self.x+300,self.y+200)
      self.lab_boisson5[(3,0)].move(self.x,self.y+300)
      self.lab_boisson5[(3,1)].move(self.x+100,self.y+300)
      self.lab_boisson5[(3,2)].move(self.x+200,self.y+300)
      self.lab_boisson5[(3,3)].move(self.x+300,self.y+300)

      self.button_boisson5[(0,0)].move(self.x,self.y)
      self.button_boisson5[(0,1)].move(self.x+100,self.y)
      self.button_boisson5[(0,2)].move(self.x+200,self.y)
      self.button_boisson5[(0,3)].move(self.x+300,self.y)
      self.button_boisson5[(1,0)].move(self.x,self.y+100)
      self.button_boisson5[(1,1)].move(self.x+100,self.y+100)
      self.button_boisson5[(1,2)].move(self.x+200,self.y+100)
      self.button_boisson5[(1,3)].move(self.x+300,self.y+100)
      self.button_boisson5[(2,0)].move(self.x,self.y+200)
      self.button_boisson5[(2,1)].move(self.x+100,self.y+200)
      self.button_boisson5[(2,2)].move(self.x+200,self.y+200)
      self.button_boisson5[(2,3)].move(self.x+300,self.y+200)
      self.button_boisson5[(3,0)].move(self.x,self.y+300)
      self.button_boisson5[(3,1)].move(self.x+100,self.y+300)
      self.button_boisson5[(3,2)].move(self.x+200,self.y+300)
      self.button_boisson5[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 6

      self.lab_boisson6[(0,0)].move(self.x,self.y)
      self.lab_boisson6[(0,1)].move(self.x+100,self.y)
      self.lab_boisson6[(0,2)].move(self.x+200,self.y)
      self.lab_boisson6[(0,3)].move(self.x+300,self.y)
      self.lab_boisson6[(1,0)].move(self.x,self.y+100)
      self.lab_boisson6[(1,1)].move(self.x+100,self.y+100)
      self.lab_boisson6[(1,2)].move(self.x+200,self.y+100)
      self.lab_boisson6[(1,3)].move(self.x+300,self.y+100)
      self.lab_boisson6[(2,0)].move(self.x,self.y+200)
      self.lab_boisson6[(2,1)].move(self.x+100,self.y+200)
      self.lab_boisson6[(2,2)].move(self.x+200,self.y+200)
      self.lab_boisson6[(2,3)].move(self.x+300,self.y+200)
      self.lab_boisson6[(3,0)].move(self.x,self.y+300)
      self.lab_boisson6[(3,1)].move(self.x+100,self.y+300)
      self.lab_boisson6[(3,2)].move(self.x+200,self.y+300)
      self.lab_boisson6[(3,3)].move(self.x+300,self.y+300)

      self.button_boisson6[(0,0)].move(self.x,self.y)
      self.button_boisson6[(0,1)].move(self.x+100,self.y)
      self.button_boisson6[(0,2)].move(self.x+200,self.y)
      self.button_boisson6[(0,3)].move(self.x+300,self.y)
      self.button_boisson6[(1,0)].move(self.x,self.y+100)
      self.button_boisson6[(1,1)].move(self.x+100,self.y+100)
      self.button_boisson6[(1,2)].move(self.x+200,self.y+100)
      self.button_boisson6[(1,3)].move(self.x+300,self.y+100)
      self.button_boisson6[(2,0)].move(self.x,self.y+200)
      self.button_boisson6[(2,1)].move(self.x+100,self.y+200)
      self.button_boisson6[(2,2)].move(self.x+200,self.y+200)
      self.button_boisson6[(2,3)].move(self.x+300,self.y+200)
      self.button_boisson6[(3,0)].move(self.x,self.y+300)
      self.button_boisson6[(3,1)].move(self.x+100,self.y+300)
      self.button_boisson6[(3,2)].move(self.x+200,self.y+300)
      self.button_boisson6[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 7

      self.lab_boisson7[(0,0)].move(self.x,self.y)
      self.lab_boisson7[(0,1)].move(self.x+100,self.y)
      self.lab_boisson7[(0,2)].move(self.x+200,self.y)
      self.lab_boisson7[(0,3)].move(self.x+300,self.y)
      self.lab_boisson7[(1,0)].move(self.x,self.y+100)
      self.lab_boisson7[(1,1)].move(self.x+100,self.y+100)
      self.lab_boisson7[(1,2)].move(self.x+200,self.y+100)
      self.lab_boisson7[(1,3)].move(self.x+300,self.y+100)
      self.lab_boisson7[(2,0)].move(self.x,self.y+200)
      self.lab_boisson7[(2,1)].move(self.x+100,self.y+200)
      self.lab_boisson7[(2,2)].move(self.x+200,self.y+200)
      self.lab_boisson7[(2,3)].move(self.x+300,self.y+200)
      self.lab_boisson7[(3,0)].move(self.x,self.y+300)
      self.lab_boisson7[(3,1)].move(self.x+100,self.y+300)
      self.lab_boisson7[(3,2)].move(self.x+200,self.y+300)
      self.lab_boisson7[(3,3)].move(self.x+300,self.y+300)

      self.button_boisson7[(0,0)].move(self.x,self.y)
      self.button_boisson7[(0,1)].move(self.x+100,self.y)
      self.button_boisson7[(0,2)].move(self.x+200,self.y)
      self.button_boisson7[(0,3)].move(self.x+300,self.y)
      self.button_boisson7[(1,0)].move(self.x,self.y+100)
      self.button_boisson7[(1,1)].move(self.x+100,self.y+100)
      self.button_boisson7[(1,2)].move(self.x+200,self.y+100)
      self.button_boisson7[(1,3)].move(self.x+300,self.y+100)
      self.button_boisson7[(2,0)].move(self.x,self.y+200)
      self.button_boisson7[(2,1)].move(self.x+100,self.y+200)
      self.button_boisson7[(2,2)].move(self.x+200,self.y+200)
      self.button_boisson7[(2,3)].move(self.x+300,self.y+200)
      self.button_boisson7[(3,0)].move(self.x,self.y+300)
      self.button_boisson7[(3,1)].move(self.x+100,self.y+300)
      self.button_boisson7[(3,2)].move(self.x+200,self.y+300)
      self.button_boisson7[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 8

      self.lab_boisson8[(0,0)].move(self.x,self.y)
      self.lab_boisson8[(0,1)].move(self.x+100,self.y)
      self.lab_boisson8[(0,2)].move(self.x+200,self.y)
      self.lab_boisson8[(0,3)].move(self.x+300,self.y)
      self.lab_boisson8[(1,0)].move(self.x,self.y+100)
      self.lab_boisson8[(1,1)].move(self.x+100,self.y+100)
      self.lab_boisson8[(1,2)].move(self.x+200,self.y+100)
      self.lab_boisson8[(1,3)].move(self.x+300,self.y+100)
      self.lab_boisson8[(2,0)].move(self.x,self.y+200)
      self.lab_boisson8[(2,1)].move(self.x+100,self.y+200)
      self.lab_boisson8[(2,2)].move(self.x+200,self.y+200)
      self.lab_boisson8[(2,3)].move(self.x+300,self.y+200)
      self.lab_boisson8[(3,0)].move(self.x,self.y+300)
      self.lab_boisson8[(3,1)].move(self.x+100,self.y+300)
      self.lab_boisson8[(3,2)].move(self.x+200,self.y+300)
      self.lab_boisson8[(3,3)].move(self.x+300,self.y+300)
      self.button_boisson8[(0,0)].move(self.x,self.y)
      self.button_boisson8[(0,1)].move(self.x+100,self.y)
      self.button_boisson8[(0,2)].move(self.x+200,self.y)
      self.button_boisson8[(0,3)].move(self.x+300,self.y)
      self.button_boisson8[(1,0)].move(self.x,self.y+100)
      self.button_boisson8[(1,1)].move(self.x+100,self.y+100)
      self.button_boisson8[(1,2)].move(self.x+200,self.y+100)
      self.button_boisson8[(1,3)].move(self.x+300,self.y+100)
      self.button_boisson8[(2,0)].move(self.x,self.y+200)
      self.button_boisson8[(2,1)].move(self.x+100,self.y+200)
      self.button_boisson8[(2,2)].move(self.x+200,self.y+200)
      self.button_boisson8[(2,3)].move(self.x+300,self.y+200)
      self.button_boisson8[(3,0)].move(self.x,self.y+300)
      self.button_boisson8[(3,1)].move(self.x+100,self.y+300)
      self.button_boisson8[(3,2)].move(self.x+200,self.y+300)
      self.button_boisson8[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++ buttons events +++++++++++++++++++++++++++++++++ DE 1 A 4

      self.button_boisson1[(0,0)].clicked.connect(self.selection_boisson1)
      self.button_boisson1[(0,1)].clicked.connect(self.selection_boisson2)
      self.button_boisson1[(0,2)].clicked.connect(self.selection_boisson3)
      self.button_boisson1[(0,3)].clicked.connect(self.selection_boisson4)
      self.button_boisson1[(1,0)].clicked.connect(self.selection_boisson5)
      self.button_boisson1[(1,1)].clicked.connect(self.selection_boisson6)
      self.button_boisson1[(1,2)].clicked.connect(self.selection_boisson7)
      self.button_boisson1[(1,3)].clicked.connect(self.selection_boisson8)
      self.button_boisson1[(2,0)].clicked.connect(self.selection_boisson9)
      self.button_boisson1[(2,1)].clicked.connect(self.selection_boisson10)
      self.button_boisson1[(2,2)].clicked.connect(self.selection_boisson11)
      self.button_boisson1[(2,3)].clicked.connect(self.selection_boisson12)
      self.button_boisson1[(3,0)].clicked.connect(self.selection_boisson13)
      self.button_boisson1[(3,1)].clicked.connect(self.selection_boisson14)
      self.button_boisson1[(3,2)].clicked.connect(self.selection_boisson15)
      self.button_boisson1[(3,3)].clicked.connect(self.selection_boisson16)

      self.button_boisson2[(0,0)].clicked.connect(self.selection_boisson17)
      self.button_boisson2[(0,1)].clicked.connect(self.selection_boisson18)
      self.button_boisson2[(0,2)].clicked.connect(self.selection_boisson19)
      self.button_boisson2[(0,3)].clicked.connect(self.selection_boisson20)
      self.button_boisson2[(1,0)].clicked.connect(self.selection_boisson21)
      self.button_boisson2[(1,1)].clicked.connect(self.selection_boisson22)
      self.button_boisson2[(1,2)].clicked.connect(self.selection_boisson23)
      self.button_boisson2[(1,3)].clicked.connect(self.selection_boisson24)
      self.button_boisson2[(2,0)].clicked.connect(self.selection_boisson25)
      self.button_boisson2[(2,1)].clicked.connect(self.selection_boisson26)
      self.button_boisson2[(2,2)].clicked.connect(self.selection_boisson27)
      self.button_boisson2[(2,3)].clicked.connect(self.selection_boisson28)
      self.button_boisson2[(3,0)].clicked.connect(self.selection_boisson29)
      self.button_boisson2[(3,1)].clicked.connect(self.selection_boisson30)
      self.button_boisson2[(3,2)].clicked.connect(self.selection_boisson31)
      self.button_boisson2[(3,3)].clicked.connect(self.selection_boisson32)

      self.button_boisson3[(0,0)].clicked.connect(self.selection_boisson33)
      self.button_boisson3[(0,1)].clicked.connect(self.selection_boisson34)
      self.button_boisson3[(0,2)].clicked.connect(self.selection_boisson35)
      self.button_boisson3[(0,3)].clicked.connect(self.selection_boisson36)
      self.button_boisson3[(1,0)].clicked.connect(self.selection_boisson37)
      self.button_boisson3[(1,1)].clicked.connect(self.selection_boisson38)
      self.button_boisson3[(1,2)].clicked.connect(self.selection_boisson39)
      self.button_boisson3[(1,3)].clicked.connect(self.selection_boisson40)
      self.button_boisson3[(2,0)].clicked.connect(self.selection_boisson41)
      self.button_boisson3[(2,1)].clicked.connect(self.selection_boisson42)
      self.button_boisson3[(2,2)].clicked.connect(self.selection_boisson43)
      self.button_boisson3[(2,3)].clicked.connect(self.selection_boisson44)
      self.button_boisson3[(3,0)].clicked.connect(self.selection_boisson45)
      self.button_boisson3[(3,1)].clicked.connect(self.selection_boisson46)
      self.button_boisson3[(3,2)].clicked.connect(self.selection_boisson47)
      self.button_boisson3[(3,3)].clicked.connect(self.selection_boisson48)

      self.button_boisson4[(0,0)].clicked.connect(self.selection_boisson49)
      self.button_boisson4[(0,1)].clicked.connect(self.selection_boisson50)
      self.button_boisson4[(0,2)].clicked.connect(self.selection_boisson51)
      self.button_boisson4[(0,3)].clicked.connect(self.selection_boisson52)
      self.button_boisson4[(1,0)].clicked.connect(self.selection_boisson53)
      self.button_boisson4[(1,1)].clicked.connect(self.selection_boisson54)
      self.button_boisson4[(1,2)].clicked.connect(self.selection_boisson55)
      self.button_boisson4[(1,3)].clicked.connect(self.selection_boisson56)
      self.button_boisson4[(2,0)].clicked.connect(self.selection_boisson57)
      self.button_boisson4[(2,1)].clicked.connect(self.selection_boisson58)
      self.button_boisson4[(2,2)].clicked.connect(self.selection_boisson59)
      self.button_boisson4[(2,3)].clicked.connect(self.selection_boisson60)
      self.button_boisson4[(3,0)].clicked.connect(self.selection_boisson61)
      self.button_boisson4[(3,1)].clicked.connect(self.selection_boisson62)
      self.button_boisson4[(3,2)].clicked.connect(self.selection_boisson63)
      self.button_boisson4[(3,3)].clicked.connect(self.selection_boisson64)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ DE 5 A 8

      self.button_boisson5[(0,0)].clicked.connect(self.selection_boisson65)
      self.button_boisson5[(0,1)].clicked.connect(self.selection_boisson66)
      self.button_boisson5[(0,2)].clicked.connect(self.selection_boisson67)
      self.button_boisson5[(0,3)].clicked.connect(self.selection_boisson68)
      self.button_boisson5[(1,0)].clicked.connect(self.selection_boisson69)
      self.button_boisson5[(1,1)].clicked.connect(self.selection_boisson70)
      self.button_boisson5[(1,2)].clicked.connect(self.selection_boisson71)
      self.button_boisson5[(1,3)].clicked.connect(self.selection_boisson72)
      self.button_boisson5[(2,0)].clicked.connect(self.selection_boisson73)
      self.button_boisson5[(2,1)].clicked.connect(self.selection_boisson74)
      self.button_boisson5[(2,2)].clicked.connect(self.selection_boisson75)
      self.button_boisson5[(2,3)].clicked.connect(self.selection_boisson76)
      self.button_boisson5[(3,0)].clicked.connect(self.selection_boisson77)
      self.button_boisson5[(3,1)].clicked.connect(self.selection_boisson78)
      self.button_boisson5[(3,2)].clicked.connect(self.selection_boisson79)
      self.button_boisson5[(3,3)].clicked.connect(self.selection_boisson80)

      self.button_boisson6[(0,0)].clicked.connect(self.selection_boisson81)
      self.button_boisson6[(0,1)].clicked.connect(self.selection_boisson82)
      self.button_boisson6[(0,2)].clicked.connect(self.selection_boisson83)
      self.button_boisson6[(0,3)].clicked.connect(self.selection_boisson84)
      self.button_boisson6[(1,0)].clicked.connect(self.selection_boisson85)
      self.button_boisson6[(1,1)].clicked.connect(self.selection_boisson86)
      self.button_boisson6[(1,2)].clicked.connect(self.selection_boisson87)
      self.button_boisson6[(1,3)].clicked.connect(self.selection_boisson88)
      self.button_boisson6[(2,0)].clicked.connect(self.selection_boisson89)
      self.button_boisson6[(2,1)].clicked.connect(self.selection_boisson90)
      self.button_boisson6[(2,2)].clicked.connect(self.selection_boisson91)
      self.button_boisson6[(2,3)].clicked.connect(self.selection_boisson92)
      self.button_boisson6[(3,0)].clicked.connect(self.selection_boisson93)
      self.button_boisson6[(3,1)].clicked.connect(self.selection_boisson94)
      self.button_boisson6[(3,2)].clicked.connect(self.selection_boisson95)
      self.button_boisson6[(3,3)].clicked.connect(self.selection_boisson96)

      self.button_boisson7[(0,0)].clicked.connect(self.selection_boisson97)
      self.button_boisson7[(0,1)].clicked.connect(self.selection_boisson98)
      self.button_boisson7[(0,2)].clicked.connect(self.selection_boisson99)
      self.button_boisson7[(0,3)].clicked.connect(self.selection_boisson100)
      self.button_boisson7[(1,0)].clicked.connect(self.selection_boisson101)
      self.button_boisson7[(1,1)].clicked.connect(self.selection_boisson102)
      self.button_boisson7[(1,2)].clicked.connect(self.selection_boisson103)
      self.button_boisson7[(1,3)].clicked.connect(self.selection_boisson104)
      self.button_boisson7[(2,0)].clicked.connect(self.selection_boisson105)
      self.button_boisson7[(2,1)].clicked.connect(self.selection_boisson106)
      self.button_boisson7[(2,2)].clicked.connect(self.selection_boisson107)
      self.button_boisson7[(2,3)].clicked.connect(self.selection_boisson108)
      self.button_boisson7[(3,0)].clicked.connect(self.selection_boisson109)
      self.button_boisson7[(3,1)].clicked.connect(self.selection_boisson110)
      self.button_boisson7[(3,2)].clicked.connect(self.selection_boisson111)
      self.button_boisson7[(3,3)].clicked.connect(self.selection_boisson112)

      self.button_boisson8[(0,0)].clicked.connect(self.selection_boisson113)
      self.button_boisson8[(0,1)].clicked.connect(self.selection_boisson114)
      self.button_boisson8[(0,2)].clicked.connect(self.selection_boisson115)
      self.button_boisson8[(0,3)].clicked.connect(self.selection_boisson116)
      self.button_boisson8[(1,0)].clicked.connect(self.selection_boisson117)
      self.button_boisson8[(1,1)].clicked.connect(self.selection_boisson118)
      self.button_boisson8[(1,2)].clicked.connect(self.selection_boisson119)
      self.button_boisson8[(1,3)].clicked.connect(self.selection_boisson120)
      self.button_boisson8[(2,0)].clicked.connect(self.selection_boisson121)
      self.button_boisson8[(2,1)].clicked.connect(self.selection_boisson122)
      self.button_boisson8[(2,2)].clicked.connect(self.selection_boisson123)
      self.button_boisson8[(2,3)].clicked.connect(self.selection_boisson124)
      self.button_boisson8[(3,0)].clicked.connect(self.selection_boisson125)
      self.button_boisson8[(3,1)].clicked.connect(self.selection_boisson126)
      self.button_boisson8[(3,2)].clicked.connect(self.selection_boisson127)
      self.button_boisson8[(3,3)].clicked.connect(self.selection_boisson128)


      

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

      self.button_cafe1[(0,0)].clicked.connect(self.selection_cafe1)
      self.button_cafe1[(0,1)].clicked.connect(self.selection_cafe2)
      self.button_cafe1[(0,2)].clicked.connect(self.selection_cafe3)
      self.button_cafe1[(0,3)].clicked.connect(self.selection_cafe4)
      self.button_cafe1[(1,0)].clicked.connect(self.selection_cafe5)
      self.button_cafe1[(1,1)].clicked.connect(self.selection_cafe6)
      self.button_cafe1[(1,2)].clicked.connect(self.selection_cafe7)
      self.button_cafe1[(1,3)].clicked.connect(self.selection_cafe8)
      self.button_cafe1[(2,0)].clicked.connect(self.selection_cafe9)
      self.button_cafe1[(2,1)].clicked.connect(self.selection_cafe10)
      self.button_cafe1[(2,2)].clicked.connect(self.selection_cafe11)
      self.button_cafe1[(2,3)].clicked.connect(self.selection_cafe12)
      self.button_cafe1[(3,0)].clicked.connect(self.selection_cafe13)
      self.button_cafe1[(3,1)].clicked.connect(self.selection_cafe14)
      self.button_cafe1[(3,2)].clicked.connect(self.selection_cafe15)
      self.button_cafe1[(3,3)].clicked.connect(self.selection_cafe16)

      self.button_cafe2[(0,0)].clicked.connect(self.selection_cafe17)
      self.button_cafe2[(0,1)].clicked.connect(self.selection_cafe18)
      self.button_cafe2[(0,2)].clicked.connect(self.selection_cafe19)
      self.button_cafe2[(0,3)].clicked.connect(self.selection_cafe20)
      self.button_cafe2[(1,0)].clicked.connect(self.selection_cafe21)
      self.button_cafe2[(1,1)].clicked.connect(self.selection_cafe22)
      self.button_cafe2[(1,2)].clicked.connect(self.selection_cafe23)
      self.button_cafe2[(1,3)].clicked.connect(self.selection_cafe24)
      self.button_cafe2[(2,0)].clicked.connect(self.selection_cafe25)
      self.button_cafe2[(2,1)].clicked.connect(self.selection_cafe26)
      self.button_cafe2[(2,2)].clicked.connect(self.selection_cafe27)
      self.button_cafe2[(2,3)].clicked.connect(self.selection_cafe28)
      self.button_cafe2[(3,0)].clicked.connect(self.selection_cafe29)
      self.button_cafe2[(3,1)].clicked.connect(self.selection_cafe30)
      self.button_cafe2[(3,2)].clicked.connect(self.selection_cafe31)
      self.button_cafe2[(3,3)].clicked.connect(self.selection_cafe32)

      self.button_cafe3[(0,0)].clicked.connect(self.selection_cafe33)
      self.button_cafe3[(0,1)].clicked.connect(self.selection_cafe34)
      self.button_cafe3[(0,2)].clicked.connect(self.selection_cafe35)
      self.button_cafe3[(0,3)].clicked.connect(self.selection_cafe36)
      self.button_cafe3[(1,0)].clicked.connect(self.selection_cafe37)
      self.button_cafe3[(1,1)].clicked.connect(self.selection_cafe38)
      self.button_cafe3[(1,2)].clicked.connect(self.selection_cafe39)
      self.button_cafe3[(1,3)].clicked.connect(self.selection_cafe40)
      self.button_cafe3[(2,0)].clicked.connect(self.selection_cafe41)
      self.button_cafe3[(2,1)].clicked.connect(self.selection_cafe42)
      self.button_cafe3[(2,2)].clicked.connect(self.selection_cafe43)
      self.button_cafe3[(2,3)].clicked.connect(self.selection_cafe44)
      self.button_cafe3[(3,0)].clicked.connect(self.selection_cafe45)
      self.button_cafe3[(3,1)].clicked.connect(self.selection_cafe46)
      self.button_cafe3[(3,2)].clicked.connect(self.selection_cafe47)
      self.button_cafe3[(3,3)].clicked.connect(self.selection_cafe48)

      self.button_cafe4[(0,0)].clicked.connect(self.selection_cafe49)
      self.button_cafe4[(0,1)].clicked.connect(self.selection_cafe50)
      self.button_cafe4[(0,2)].clicked.connect(self.selection_cafe51)
      self.button_cafe4[(0,3)].clicked.connect(self.selection_cafe52)
      self.button_cafe4[(1,0)].clicked.connect(self.selection_cafe53)
      self.button_cafe4[(1,1)].clicked.connect(self.selection_cafe54)
      self.button_cafe4[(1,2)].clicked.connect(self.selection_cafe55)
      self.button_cafe4[(1,3)].clicked.connect(self.selection_cafe56)
      self.button_cafe4[(2,0)].clicked.connect(self.selection_cafe57)
      self.button_cafe4[(2,1)].clicked.connect(self.selection_cafe58)
      self.button_cafe4[(2,2)].clicked.connect(self.selection_cafe59)
      self.button_cafe4[(2,3)].clicked.connect(self.selection_cafe60)
      self.button_cafe4[(3,0)].clicked.connect(self.selection_cafe61)
      self.button_cafe4[(3,1)].clicked.connect(self.selection_cafe62)
      self.button_cafe4[(3,2)].clicked.connect(self.selection_cafe63)
      self.button_cafe4[(3,3)].clicked.connect(self.selection_cafe64)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ DE 5 A 8

      self.button_cafe5[(0,0)].clicked.connect(self.selection_cafe65)
      self.button_cafe5[(0,1)].clicked.connect(self.selection_cafe66)
      self.button_cafe5[(0,2)].clicked.connect(self.selection_cafe67)
      self.button_cafe5[(0,3)].clicked.connect(self.selection_cafe68)
      self.button_cafe5[(1,0)].clicked.connect(self.selection_cafe69)
      self.button_cafe5[(1,1)].clicked.connect(self.selection_cafe70)
      self.button_cafe5[(1,2)].clicked.connect(self.selection_cafe71)
      self.button_cafe5[(1,3)].clicked.connect(self.selection_cafe72)
      self.button_cafe5[(2,0)].clicked.connect(self.selection_cafe73)
      self.button_cafe5[(2,1)].clicked.connect(self.selection_cafe74)
      self.button_cafe5[(2,2)].clicked.connect(self.selection_cafe75)
      self.button_cafe5[(2,3)].clicked.connect(self.selection_cafe76)
      self.button_cafe5[(3,0)].clicked.connect(self.selection_cafe77)
      self.button_cafe5[(3,1)].clicked.connect(self.selection_cafe78)
      self.button_cafe5[(3,2)].clicked.connect(self.selection_cafe79)
      self.button_cafe5[(3,3)].clicked.connect(self.selection_cafe80)

      self.button_cafe6[(0,0)].clicked.connect(self.selection_cafe81)
      self.button_cafe6[(0,1)].clicked.connect(self.selection_cafe82)
      self.button_cafe6[(0,2)].clicked.connect(self.selection_cafe83)
      self.button_cafe6[(0,3)].clicked.connect(self.selection_cafe84)
      self.button_cafe6[(1,0)].clicked.connect(self.selection_cafe85)
      self.button_cafe6[(1,1)].clicked.connect(self.selection_cafe86)
      self.button_cafe6[(1,2)].clicked.connect(self.selection_cafe87)
      self.button_cafe6[(1,3)].clicked.connect(self.selection_cafe88)
      self.button_cafe6[(2,0)].clicked.connect(self.selection_cafe89)
      self.button_cafe6[(2,1)].clicked.connect(self.selection_cafe90)
      self.button_cafe6[(2,2)].clicked.connect(self.selection_cafe91)
      self.button_cafe6[(2,3)].clicked.connect(self.selection_cafe92)
      self.button_cafe6[(3,0)].clicked.connect(self.selection_cafe93)
      self.button_cafe6[(3,1)].clicked.connect(self.selection_cafe94)
      self.button_cafe6[(3,2)].clicked.connect(self.selection_cafe95)
      self.button_cafe6[(3,3)].clicked.connect(self.selection_cafe96)

      self.button_cafe7[(0,0)].clicked.connect(self.selection_cafe97)
      self.button_cafe7[(0,1)].clicked.connect(self.selection_cafe98)
      self.button_cafe7[(0,2)].clicked.connect(self.selection_cafe99)
      self.button_cafe7[(0,3)].clicked.connect(self.selection_cafe100)
      self.button_cafe7[(1,0)].clicked.connect(self.selection_cafe101)
      self.button_cafe7[(1,1)].clicked.connect(self.selection_cafe102)
      self.button_cafe7[(1,2)].clicked.connect(self.selection_cafe103)
      self.button_cafe7[(1,3)].clicked.connect(self.selection_cafe104)
      self.button_cafe7[(2,0)].clicked.connect(self.selection_cafe105)
      self.button_cafe7[(2,1)].clicked.connect(self.selection_cafe106)
      self.button_cafe7[(2,2)].clicked.connect(self.selection_cafe107)
      self.button_cafe7[(2,3)].clicked.connect(self.selection_cafe108)
      self.button_cafe7[(3,0)].clicked.connect(self.selection_cafe109)
      self.button_cafe7[(3,1)].clicked.connect(self.selection_cafe110)
      self.button_cafe7[(3,2)].clicked.connect(self.selection_cafe111)
      self.button_cafe7[(3,3)].clicked.connect(self.selection_cafe112)

      self.button_cafe8[(0,0)].clicked.connect(self.selection_cafe113)
      self.button_cafe8[(0,1)].clicked.connect(self.selection_cafe114)
      self.button_cafe8[(0,2)].clicked.connect(self.selection_cafe115)
      self.button_cafe8[(0,3)].clicked.connect(self.selection_cafe116)
      self.button_cafe8[(1,0)].clicked.connect(self.selection_cafe117)
      self.button_cafe8[(1,1)].clicked.connect(self.selection_cafe118)
      self.button_cafe8[(1,2)].clicked.connect(self.selection_cafe119)
      self.button_cafe8[(1,3)].clicked.connect(self.selection_cafe120)
      self.button_cafe8[(2,0)].clicked.connect(self.selection_cafe121)
      self.button_cafe8[(2,1)].clicked.connect(self.selection_cafe122)
      self.button_cafe8[(2,2)].clicked.connect(self.selection_cafe123)
      self.button_cafe8[(2,3)].clicked.connect(self.selection_cafe124)
      self.button_cafe8[(3,0)].clicked.connect(self.selection_cafe125)
      self.button_cafe8[(3,1)].clicked.connect(self.selection_cafe126)
      self.button_cafe8[(3,2)].clicked.connect(self.selection_cafe127)
      self.button_cafe8[(3,3)].clicked.connect(self.selection_cafe128)


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

      self.button_dessert1[(0,0)].clicked.connect(self.selection_dessert1)
      self.button_dessert1[(0,1)].clicked.connect(self.selection_dessert2)
      self.button_dessert1[(0,2)].clicked.connect(self.selection_dessert3)
      self.button_dessert1[(0,3)].clicked.connect(self.selection_dessert4)
      self.button_dessert1[(1,0)].clicked.connect(self.selection_dessert5)
      self.button_dessert1[(1,1)].clicked.connect(self.selection_dessert6)
      self.button_dessert1[(1,2)].clicked.connect(self.selection_dessert7)
      self.button_dessert1[(1,3)].clicked.connect(self.selection_dessert8)
      self.button_dessert1[(2,0)].clicked.connect(self.selection_dessert9)
      self.button_dessert1[(2,1)].clicked.connect(self.selection_dessert10)
      self.button_dessert1[(2,2)].clicked.connect(self.selection_dessert11)
      self.button_dessert1[(2,3)].clicked.connect(self.selection_dessert12)
      self.button_dessert1[(3,0)].clicked.connect(self.selection_dessert13)
      self.button_dessert1[(3,1)].clicked.connect(self.selection_dessert14)
      self.button_dessert1[(3,2)].clicked.connect(self.selection_dessert15)
      self.button_dessert1[(3,3)].clicked.connect(self.selection_dessert16)

      self.button_dessert2[(0,0)].clicked.connect(self.selection_dessert17)
      self.button_dessert2[(0,1)].clicked.connect(self.selection_dessert18)
      self.button_dessert2[(0,2)].clicked.connect(self.selection_dessert19)
      self.button_dessert2[(0,3)].clicked.connect(self.selection_dessert20)
      self.button_dessert2[(1,0)].clicked.connect(self.selection_dessert21)
      self.button_dessert2[(1,1)].clicked.connect(self.selection_dessert22)
      self.button_dessert2[(1,2)].clicked.connect(self.selection_dessert23)
      self.button_dessert2[(1,3)].clicked.connect(self.selection_dessert24)
      self.button_dessert2[(2,0)].clicked.connect(self.selection_dessert25)
      self.button_dessert2[(2,1)].clicked.connect(self.selection_dessert26)
      self.button_dessert2[(2,2)].clicked.connect(self.selection_dessert27)
      self.button_dessert2[(2,3)].clicked.connect(self.selection_dessert28)
      self.button_dessert2[(3,0)].clicked.connect(self.selection_dessert29)
      self.button_dessert2[(3,1)].clicked.connect(self.selection_dessert30)
      self.button_dessert2[(3,2)].clicked.connect(self.selection_dessert31)
      self.button_dessert2[(3,3)].clicked.connect(self.selection_dessert32)

      self.button_dessert3[(0,0)].clicked.connect(self.selection_dessert33)
      self.button_dessert3[(0,1)].clicked.connect(self.selection_dessert34)
      self.button_dessert3[(0,2)].clicked.connect(self.selection_dessert35)
      self.button_dessert3[(0,3)].clicked.connect(self.selection_dessert36)
      self.button_dessert3[(1,0)].clicked.connect(self.selection_dessert37)
      self.button_dessert3[(1,1)].clicked.connect(self.selection_dessert38)
      self.button_dessert3[(1,2)].clicked.connect(self.selection_dessert39)
      self.button_dessert3[(1,3)].clicked.connect(self.selection_dessert40)
      self.button_dessert3[(2,0)].clicked.connect(self.selection_dessert41)
      self.button_dessert3[(2,1)].clicked.connect(self.selection_dessert42)
      self.button_dessert3[(2,2)].clicked.connect(self.selection_dessert43)
      self.button_dessert3[(2,3)].clicked.connect(self.selection_dessert44)
      self.button_dessert3[(3,0)].clicked.connect(self.selection_dessert45)
      self.button_dessert3[(3,1)].clicked.connect(self.selection_dessert46)
      self.button_dessert3[(3,2)].clicked.connect(self.selection_dessert47)
      self.button_dessert3[(3,3)].clicked.connect(self.selection_dessert48)

      self.button_dessert4[(0,0)].clicked.connect(self.selection_dessert49)
      self.button_dessert4[(0,1)].clicked.connect(self.selection_dessert50)
      self.button_dessert4[(0,2)].clicked.connect(self.selection_dessert51)
      self.button_dessert4[(0,3)].clicked.connect(self.selection_dessert52)
      self.button_dessert4[(1,0)].clicked.connect(self.selection_dessert53)
      self.button_dessert4[(1,1)].clicked.connect(self.selection_dessert54)
      self.button_dessert4[(1,2)].clicked.connect(self.selection_dessert55)
      self.button_dessert4[(1,3)].clicked.connect(self.selection_dessert56)
      self.button_dessert4[(2,0)].clicked.connect(self.selection_dessert57)
      self.button_dessert4[(2,1)].clicked.connect(self.selection_dessert58)
      self.button_dessert4[(2,2)].clicked.connect(self.selection_dessert59)
      self.button_dessert4[(2,3)].clicked.connect(self.selection_dessert60)
      self.button_dessert4[(3,0)].clicked.connect(self.selection_dessert61)
      self.button_dessert4[(3,1)].clicked.connect(self.selection_dessert62)
      self.button_dessert4[(3,2)].clicked.connect(self.selection_dessert63)
      self.button_dessert4[(3,3)].clicked.connect(self.selection_dessert64)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ DE 5 A 8

      self.button_dessert5[(0,0)].clicked.connect(self.selection_dessert65)
      self.button_dessert5[(0,1)].clicked.connect(self.selection_dessert66)
      self.button_dessert5[(0,2)].clicked.connect(self.selection_dessert67)
      self.button_dessert5[(0,3)].clicked.connect(self.selection_dessert68)
      self.button_dessert5[(1,0)].clicked.connect(self.selection_dessert69)
      self.button_dessert5[(1,1)].clicked.connect(self.selection_dessert70)
      self.button_dessert5[(1,2)].clicked.connect(self.selection_dessert71)
      self.button_dessert5[(1,3)].clicked.connect(self.selection_dessert72)
      self.button_dessert5[(2,0)].clicked.connect(self.selection_dessert73)
      self.button_dessert5[(2,1)].clicked.connect(self.selection_dessert74)
      self.button_dessert5[(2,2)].clicked.connect(self.selection_dessert75)
      self.button_dessert5[(2,3)].clicked.connect(self.selection_dessert76)
      self.button_dessert5[(3,0)].clicked.connect(self.selection_dessert77)
      self.button_dessert5[(3,1)].clicked.connect(self.selection_dessert78)
      self.button_dessert5[(3,2)].clicked.connect(self.selection_dessert79)
      self.button_dessert5[(3,3)].clicked.connect(self.selection_dessert80)

      self.button_dessert6[(0,0)].clicked.connect(self.selection_dessert81)
      self.button_dessert6[(0,1)].clicked.connect(self.selection_dessert82)
      self.button_dessert6[(0,2)].clicked.connect(self.selection_dessert83)
      self.button_dessert6[(0,3)].clicked.connect(self.selection_dessert84)
      self.button_dessert6[(1,0)].clicked.connect(self.selection_dessert85)
      self.button_dessert6[(1,1)].clicked.connect(self.selection_dessert86)
      self.button_dessert6[(1,2)].clicked.connect(self.selection_dessert87)
      self.button_dessert6[(1,3)].clicked.connect(self.selection_dessert88)
      self.button_dessert6[(2,0)].clicked.connect(self.selection_dessert89)
      self.button_dessert6[(2,1)].clicked.connect(self.selection_dessert90)
      self.button_dessert6[(2,2)].clicked.connect(self.selection_dessert91)
      self.button_dessert6[(2,3)].clicked.connect(self.selection_dessert92)
      self.button_dessert6[(3,0)].clicked.connect(self.selection_dessert93)
      self.button_dessert6[(3,1)].clicked.connect(self.selection_dessert94)
      self.button_dessert6[(3,2)].clicked.connect(self.selection_dessert95)
      self.button_dessert6[(3,3)].clicked.connect(self.selection_dessert96)

      self.button_dessert7[(0,0)].clicked.connect(self.selection_dessert97)
      self.button_dessert7[(0,1)].clicked.connect(self.selection_dessert98)
      self.button_dessert7[(0,2)].clicked.connect(self.selection_dessert99)
      self.button_dessert7[(0,3)].clicked.connect(self.selection_dessert100)
      self.button_dessert7[(1,0)].clicked.connect(self.selection_dessert101)
      self.button_dessert7[(1,1)].clicked.connect(self.selection_dessert102)
      self.button_dessert7[(1,2)].clicked.connect(self.selection_dessert103)
      self.button_dessert7[(1,3)].clicked.connect(self.selection_dessert104)
      self.button_dessert7[(2,0)].clicked.connect(self.selection_dessert105)
      self.button_dessert7[(2,1)].clicked.connect(self.selection_dessert106)
      self.button_dessert7[(2,2)].clicked.connect(self.selection_dessert107)
      self.button_dessert7[(2,3)].clicked.connect(self.selection_dessert108)
      self.button_dessert7[(3,0)].clicked.connect(self.selection_dessert109)
      self.button_dessert7[(3,1)].clicked.connect(self.selection_dessert110)
      self.button_dessert7[(3,2)].clicked.connect(self.selection_dessert111)
      self.button_dessert7[(3,3)].clicked.connect(self.selection_dessert112)

      self.button_dessert8[(0,0)].clicked.connect(self.selection_dessert113)
      self.button_dessert8[(0,1)].clicked.connect(self.selection_dessert114)
      self.button_dessert8[(0,2)].clicked.connect(self.selection_dessert115)
      self.button_dessert8[(0,3)].clicked.connect(self.selection_dessert116)
      self.button_dessert8[(1,0)].clicked.connect(self.selection_dessert117)
      self.button_dessert8[(1,1)].clicked.connect(self.selection_dessert118)
      self.button_dessert8[(1,2)].clicked.connect(self.selection_dessert119)
      self.button_dessert8[(1,3)].clicked.connect(self.selection_dessert120)
      self.button_dessert8[(2,0)].clicked.connect(self.selection_dessert121)
      self.button_dessert8[(2,1)].clicked.connect(self.selection_dessert122)
      self.button_dessert8[(2,2)].clicked.connect(self.selection_dessert123)
      self.button_dessert8[(2,3)].clicked.connect(self.selection_dessert124)
      self.button_dessert8[(3,0)].clicked.connect(self.selection_dessert125)
      self.button_dessert8[(3,1)].clicked.connect(self.selection_dessert126)
      self.button_dessert8[(3,2)].clicked.connect(self.selection_dessert127)
      self.button_dessert8[(3,3)].clicked.connect(self.selection_dessert128)

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

      self.button_plat1[(0,0)].clicked.connect(self.selection_plat1)
      self.button_plat1[(0,1)].clicked.connect(self.selection_plat2)
      self.button_plat1[(0,2)].clicked.connect(self.selection_plat3)
      self.button_plat1[(0,3)].clicked.connect(self.selection_plat4)
      self.button_plat1[(1,0)].clicked.connect(self.selection_plat5)
      self.button_plat1[(1,1)].clicked.connect(self.selection_plat6)
      self.button_plat1[(1,2)].clicked.connect(self.selection_plat7)
      self.button_plat1[(1,3)].clicked.connect(self.selection_plat8)
      self.button_plat1[(2,0)].clicked.connect(self.selection_plat9)
      self.button_plat1[(2,1)].clicked.connect(self.selection_plat10)
      self.button_plat1[(2,2)].clicked.connect(self.selection_plat11)
      self.button_plat1[(2,3)].clicked.connect(self.selection_plat12)
      self.button_plat1[(3,0)].clicked.connect(self.selection_plat13)
      self.button_plat1[(3,1)].clicked.connect(self.selection_plat14)
      self.button_plat1[(3,2)].clicked.connect(self.selection_plat15)
      self.button_plat1[(3,3)].clicked.connect(self.selection_plat16)

      self.button_plat2[(0,0)].clicked.connect(self.selection_plat17)
      self.button_plat2[(0,1)].clicked.connect(self.selection_plat18)
      self.button_plat2[(0,2)].clicked.connect(self.selection_plat19)
      self.button_plat2[(0,3)].clicked.connect(self.selection_plat20)
      self.button_plat2[(1,0)].clicked.connect(self.selection_plat21)
      self.button_plat2[(1,1)].clicked.connect(self.selection_plat22)
      self.button_plat2[(1,2)].clicked.connect(self.selection_plat23)
      self.button_plat2[(1,3)].clicked.connect(self.selection_plat24)
      self.button_plat2[(2,0)].clicked.connect(self.selection_plat25)
      self.button_plat2[(2,1)].clicked.connect(self.selection_plat26)
      self.button_plat2[(2,2)].clicked.connect(self.selection_plat27)
      self.button_plat2[(2,3)].clicked.connect(self.selection_plat28)
      self.button_plat2[(3,0)].clicked.connect(self.selection_plat29)
      self.button_plat2[(3,1)].clicked.connect(self.selection_plat30)
      self.button_plat2[(3,2)].clicked.connect(self.selection_plat31)
      self.button_plat2[(3,3)].clicked.connect(self.selection_plat32)

      self.button_plat3[(0,0)].clicked.connect(self.selection_plat33)
      self.button_plat3[(0,1)].clicked.connect(self.selection_plat34)
      self.button_plat3[(0,2)].clicked.connect(self.selection_plat35)
      self.button_plat3[(0,3)].clicked.connect(self.selection_plat36)
      self.button_plat3[(1,0)].clicked.connect(self.selection_plat37)
      self.button_plat3[(1,1)].clicked.connect(self.selection_plat38)
      self.button_plat3[(1,2)].clicked.connect(self.selection_plat39)
      self.button_plat3[(1,3)].clicked.connect(self.selection_plat40)
      self.button_plat3[(2,0)].clicked.connect(self.selection_plat41)
      self.button_plat3[(2,1)].clicked.connect(self.selection_plat42)
      self.button_plat3[(2,2)].clicked.connect(self.selection_plat43)
      self.button_plat3[(2,3)].clicked.connect(self.selection_plat44)
      self.button_plat3[(3,0)].clicked.connect(self.selection_plat45)
      self.button_plat3[(3,1)].clicked.connect(self.selection_plat46)
      self.button_plat3[(3,2)].clicked.connect(self.selection_plat47)
      self.button_plat3[(3,3)].clicked.connect(self.selection_plat48)

      self.button_plat4[(0,0)].clicked.connect(self.selection_plat49)
      self.button_plat4[(0,1)].clicked.connect(self.selection_plat50)
      self.button_plat4[(0,2)].clicked.connect(self.selection_plat51)
      self.button_plat4[(0,3)].clicked.connect(self.selection_plat52)
      self.button_plat4[(1,0)].clicked.connect(self.selection_plat53)
      self.button_plat4[(1,1)].clicked.connect(self.selection_plat54)
      self.button_plat4[(1,2)].clicked.connect(self.selection_plat55)
      self.button_plat4[(1,3)].clicked.connect(self.selection_plat56)
      self.button_plat4[(2,0)].clicked.connect(self.selection_plat57)
      self.button_plat4[(2,1)].clicked.connect(self.selection_plat58)
      self.button_plat4[(2,2)].clicked.connect(self.selection_plat59)
      self.button_plat4[(2,3)].clicked.connect(self.selection_plat60)
      self.button_plat4[(3,0)].clicked.connect(self.selection_plat61)
      self.button_plat4[(3,1)].clicked.connect(self.selection_plat62)
      self.button_plat4[(3,2)].clicked.connect(self.selection_plat63)
      self.button_plat4[(3,3)].clicked.connect(self.selection_plat64)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ DE 5 A 8

      self.button_plat5[(0,0)].clicked.connect(self.selection_plat65)
      self.button_plat5[(0,1)].clicked.connect(self.selection_plat66)
      self.button_plat5[(0,2)].clicked.connect(self.selection_plat67)
      self.button_plat5[(0,3)].clicked.connect(self.selection_plat68)
      self.button_plat5[(1,0)].clicked.connect(self.selection_plat69)
      self.button_plat5[(1,1)].clicked.connect(self.selection_plat70)
      self.button_plat5[(1,2)].clicked.connect(self.selection_plat71)
      self.button_plat5[(1,3)].clicked.connect(self.selection_plat72)
      self.button_plat5[(2,0)].clicked.connect(self.selection_plat73)
      self.button_plat5[(2,1)].clicked.connect(self.selection_plat74)
      self.button_plat5[(2,2)].clicked.connect(self.selection_plat75)
      self.button_plat5[(2,3)].clicked.connect(self.selection_plat76)
      self.button_plat5[(3,0)].clicked.connect(self.selection_plat77)
      self.button_plat5[(3,1)].clicked.connect(self.selection_plat78)
      self.button_plat5[(3,2)].clicked.connect(self.selection_plat79)
      self.button_plat5[(3,3)].clicked.connect(self.selection_plat80)

      self.button_plat6[(0,0)].clicked.connect(self.selection_plat81)
      self.button_plat6[(0,1)].clicked.connect(self.selection_plat82)
      self.button_plat6[(0,2)].clicked.connect(self.selection_plat83)
      self.button_plat6[(0,3)].clicked.connect(self.selection_plat84)
      self.button_plat6[(1,0)].clicked.connect(self.selection_plat85)
      self.button_plat6[(1,1)].clicked.connect(self.selection_plat86)
      self.button_plat6[(1,2)].clicked.connect(self.selection_plat87)
      self.button_plat6[(1,3)].clicked.connect(self.selection_plat88)
      self.button_plat6[(2,0)].clicked.connect(self.selection_plat89)
      self.button_plat6[(2,1)].clicked.connect(self.selection_plat90)
      self.button_plat6[(2,2)].clicked.connect(self.selection_plat91)
      self.button_plat6[(2,3)].clicked.connect(self.selection_plat92)
      self.button_plat6[(3,0)].clicked.connect(self.selection_plat93)
      self.button_plat6[(3,1)].clicked.connect(self.selection_plat94)
      self.button_plat6[(3,2)].clicked.connect(self.selection_plat95)
      self.button_plat6[(3,3)].clicked.connect(self.selection_plat96)

      self.button_plat7[(0,0)].clicked.connect(self.selection_plat97)
      self.button_plat7[(0,1)].clicked.connect(self.selection_plat98)
      self.button_plat7[(0,2)].clicked.connect(self.selection_plat99)
      self.button_plat7[(0,3)].clicked.connect(self.selection_plat100)
      self.button_plat7[(1,0)].clicked.connect(self.selection_plat101)
      self.button_plat7[(1,1)].clicked.connect(self.selection_plat102)
      self.button_plat7[(1,2)].clicked.connect(self.selection_plat103)
      self.button_plat7[(1,3)].clicked.connect(self.selection_plat104)
      self.button_plat7[(2,0)].clicked.connect(self.selection_plat105)
      self.button_plat7[(2,1)].clicked.connect(self.selection_plat106)
      self.button_plat7[(2,2)].clicked.connect(self.selection_plat107)
      self.button_plat7[(2,3)].clicked.connect(self.selection_plat108)
      self.button_plat7[(3,0)].clicked.connect(self.selection_plat109)
      self.button_plat7[(3,1)].clicked.connect(self.selection_plat110)
      self.button_plat7[(3,2)].clicked.connect(self.selection_plat111)
      self.button_plat7[(3,3)].clicked.connect(self.selection_plat112)

      self.button_plat8[(0,0)].clicked.connect(self.selection_plat113)
      self.button_plat8[(0,1)].clicked.connect(self.selection_plat114)
      self.button_plat8[(0,2)].clicked.connect(self.selection_plat115)
      self.button_plat8[(0,3)].clicked.connect(self.selection_plat116)
      self.button_plat8[(1,0)].clicked.connect(self.selection_plat117)
      self.button_plat8[(1,1)].clicked.connect(self.selection_plat118)
      self.button_plat8[(1,2)].clicked.connect(self.selection_plat119)
      self.button_plat8[(1,3)].clicked.connect(self.selection_plat120)
      self.button_plat8[(2,0)].clicked.connect(self.selection_plat121)
      self.button_plat8[(2,1)].clicked.connect(self.selection_plat122)
      self.button_plat8[(2,2)].clicked.connect(self.selection_plat123)
      self.button_plat8[(2,3)].clicked.connect(self.selection_plat124)
      self.button_plat8[(3,0)].clicked.connect(self.selection_plat125)
      self.button_plat8[(3,1)].clicked.connect(self.selection_plat126)
      self.button_plat8[(3,2)].clicked.connect(self.selection_plat127)
      self.button_plat8[(3,3)].clicked.connect(self.selection_plat128)
      
      #================================================================================================#
      #================================================================================================#
      #============================================= PLATS ============================================#
      #================================================================================================#

      

      #================================================================================================#
      #================================================================================================#
      #========================================== DASHBOARD 1 =========================================#
      #================================================================================================#
      self.dash_vente=QFrame(self)
      self.dash_vente.setStyleSheet("""
                                background-color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:10px;
                                border-bottom-right-radius:10px;border-top-right-radius:0px
                                """)
      self.dash_vente.move(500,295)
      self.dash_vente.resize(390,200)

      #____________________________________FRAME BTN VIEW

      self.btn_view_frame=QFrame(self)            
      self.btn_view_frame.setStyleSheet("""border-style:solid;border-width:1px;border-color:#000;
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;
                                  border-top-left-radius:10px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:10px
                            """)
      self.btn_view_frame.move(500,50)
      self.btn_view_frame.resize(390,250)
      
      #=====BTN VIEW
      self.btn_view=QToolButton(self.btn_view_frame)
      self.btn_view.setStyleSheet("""
                                  QToolButton::pressed{background-color :transparent;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;
                                  border-top-left-radius:10px;border-bottom-left-radius:0px;
                                  border-bottom-right-radius:0px;border-top-right-radius:10px}
                                  QToolButton::!pressed{border-style:solid;border-width:3px;border-color:#000;
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:30pt;
                                  font-weight:bold;
                                  border-top-left-radius:10px;border-bottom-left-radius:0px;
                                  border-bottom-right-radius:0px;border-top-right-radius:10px}
                                  QToolButton::hover{background-color :transparent;color:crimson;border-style:solid;
                                  border-width:3px;border-color:#000;font-family: Time;font-style:italic;font-size:30pt;
                                  font-weight:bold;
                                  border-top-left-radius:10px;border-bottom-left-radius:0px;
                                  border-bottom-right-radius:0px;border-top-right-radius:10px}
                                """)
      
      self.btn_view.setIconSize(QSize(300,800))
      self.btn_view.move(0,0)
      self.btn_view.resize(390,250)
      self.btn_view.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
      self.btn_view.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_view.clicked.connect(self.add_item)


      #_______ID PANIER
      self.id_lab_panier=QLabel('ID PANIER',self.dash_vente)
      self.id_lab_panier.setStyleSheet("""
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold
                                  """)
      self.id_lab_panier.move(5,10)
      self.id_lab_panier.resize(100,20)

      self.id_panier=QSpinBox(self.dash_vente)
      self.id_panier.setStyleSheet("""
                                  background-color:#1b1b1c;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.id_panier.setMaximum(1000000)
      self.id_panier.setAlignment(Qt.AlignCenter)
      self.id_panier.setValue(1)
      self.id_panier.setEnabled(False)
      self.id_panier.move(5,30)
      self.id_panier.resize(150,20)

      #_______ID PRODUIT
      self.id_lab_produit=QLabel('ID PRODUIT',self.dash_vente)
      self.id_lab_produit.setStyleSheet("""
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold
                                  """)
      self.id_lab_produit.move(5,50)
      self.id_lab_produit.resize(100,20)

      self.id_produit=QSpinBox(self.dash_vente)
      self.id_produit.setStyleSheet("""
                                  background-color:#1b1b1c;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.id_produit.setMaximum(1000000)
      self.id_produit.setAlignment(Qt.AlignCenter)
      self.id_produit.setValue(1)
      self.id_produit.setEnabled(False)
      self.id_produit.move(5,70)
      self.id_produit.resize(150,20)

      #_______CODE PRODUIT
      self.code_lab=QLabel('CODE PRODUIT',self.dash_vente)
      self.code_lab.setStyleSheet("""
                                   background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold
                                  """)
      self.code_lab.move(5,90)
      self.code_lab.resize(100,20)

      self.code_produit=QLineEdit(self.dash_vente)
      self.code_produit.setStyleSheet("""
                                  background-color:#1b1b1c;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.code_produit.setAlignment(Qt.AlignCenter)
      self.code_produit.setEnabled(False)
      self.code_produit.move(5,110)
      self.code_produit.resize(150,20)

      #_______NOM
      self.nom_lab_vente=QLabel('PRODUIT',self.dash_vente)
      self.nom_lab_vente.setStyleSheet("""
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.nom_lab_vente.move(225,10)
      self.nom_lab_vente.resize(100,20)

      self.nom_vente=QLineEdit(self.dash_vente)
      self.nom_vente.setStyleSheet("""
                                  background-color:#1b1b1c;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.nom_vente.setAlignment(Qt.AlignCenter)
      self.nom_vente.move(225,30)
      self.nom_vente.resize(150,20)
      self.nom_vente.setEnabled(False)

      #_______QUANTITES
      self.qte_lab_vente=QLabel('STOCK DISPONIBLE',self.dash_vente)
      self.qte_lab_vente.setStyleSheet("""
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.qte_lab_vente.move(225,50)
      self.qte_lab_vente.resize(200,20)

      self.qte_vente=QSpinBox(self.dash_vente)
      self.qte_vente.setStyleSheet("""
                                  background-color:#1b1b1c;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.qte_vente.setAlignment(Qt.AlignCenter)
      self.qte_vente.setMinimum(0)
      self.qte_vente.setMaximum(1000000)
      self.qte_vente.move(225,70)
      self.qte_vente.resize(150,20)
      self.qte_vente.setEnabled(False)

      #_______PRIX
      self.prix_lab_vente=QLabel('PRIX UNITAIRE',self.dash_vente)
      self.prix_lab_vente.setStyleSheet("""
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.prix_lab_vente.move(225,90)
      self.prix_lab_vente.resize(200,20)

      self.prix_vente=QDoubleSpinBox(self.dash_vente)
      self.prix_vente.setStyleSheet("""
                                  background-color:#1b1b1c;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.prix_vente.setAlignment(Qt.AlignCenter)
      self.prix_vente.setMinimum(0)
      self.prix_vente.setMaximum(1000000)
      self.prix_vente.move(225,110)
      self.prix_vente.resize(150,20)
      self.prix_vente.setEnabled(False)

      


      #_________________________________________RAFRAICHIR

      self.btn_refresh=QPushButton('RAFRAICHIR',self.dash_vente)
      self.btn_refresh.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_refresh.clicked.connect(self.refresh_cart)
      self.btn_refresh.move(5,135)
      self.btn_refresh.resize(150,20)

      #_________________________________________RESET CART

      self.btn_reset_cart=QPushButton('VIDER LE PANIER',self.dash_vente)
      self.btn_reset_cart.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_reset_cart.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_reset_cart.clicked.connect(self.reset_cart)
      self.btn_reset_cart.move(225,135)
      self.btn_reset_cart.resize(150,20)
      

      #================================================================================================#
      #================================================================================================#
      #========================================== DASHBOARD 2 =========================================#
      #================================================================================================#
      self.dash2_vente=QFrame(self)
      self.dash2_vente.setStyleSheet("""
                                background-color:#1b1b1c;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-radius:0px
                                """)
      
      self.dash2_vente.move(500,455)
      self.dash2_vente.resize(690,130)


      

      #_______ ZONE FIDELISATION
      self.title_zone_client=QLabel('FIDELISATION CLIENTELE',self.dash2_vente)
      self.title_zone_client.setStyleSheet("""
                                  background-color:transparent;color:crimson;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.title_zone_client.move(30,10)
      self.title_zone_client.resize(200,30)
      """

      #_______CODE PROMOTION
      self.lab_code_promo=QLabel('CODE PROMOTION',self.dash2_vente)
      self.lab_code_promo.setStyleSheet(\"""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  \""")
      self.lab_code_promo.move(10,60)
      self.lab_code_promo.resize(150,30)

      self.code_promo=QLineEdit(self.dash2_vente)
      self.code_promo.setStyleSheet(\"""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  \""")

      self.code_promo.move(10,90)
      self.code_promo.resize(150,30)
      """

      #_______REDUCTION
      self.lab_reduction=QLabel('REDUCTION',self.dash2_vente)
      self.lab_reduction.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.lab_reduction.move(30,60)
      self.lab_reduction.resize(200,30)

      self.reduction_produit=QSpinBox(self.dash2_vente)
      self.reduction_produit.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.reduction_produit.setAlignment(Qt.AlignCenter)
      self.reduction_produit.move(30,90)
      self.reduction_produit.resize(150,30)
      self.reduction_produit.setEnabled(False)

      #_______TOTAL A PAYER
      self.lab_btn_total=QLabel('TOTAL A PAYER',self.dash2_vente)
      self.lab_btn_total.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.lab_btn_total.move(220,60)
      self.lab_btn_total.resize(200,30)

      self.btn_total=QLineEdit(self.dash2_vente)
      self.btn_total.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.btn_total.setAlignment(Qt.AlignCenter)
      self.btn_total.move(220,90)
      self.btn_total.resize(150,30)
      self.btn_total.setEnabled(False)

      #================================================================================================#
      #================================================================================================#
      #========================================== DASHBOARD 3 =========================================#
      #================================================================================================#
      self.dash3_vente=QFrame(self)
      self.dash3_vente.setStyleSheet("""
                                background-color:transparent;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-radius:0px
                                """)
      
      self.dash3_vente.move(900,50)
      self.dash3_vente.resize(290,450)

      #_______PANIER LISTE

      self.list_panier=QListWidget(self.dash3_vente)
      self.list_panier.setStyleSheet("""
                                  QListWidget::item:selected{border-style:solid;border-width:3px;border-color:#000;
                                  background-color:crimson;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-style:solid;border-size:20px;border-color:crimson;border-radius:0px}
                                  
                                  QListWidget::item:!selected{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:0px}
                                  """)
      self.list_panier.move(0,0)
      self.list_panier.resize(290,300)
      
      self.list_panier.itemClicked.connect(self.selection_item)

      
      #_______TOTAL VENTE
      self.lab_total_vente=QLabel('TOTAL DANS LE PANIER ',self.dash3_vente)
      self.lab_total_vente.setStyleSheet("""
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.lab_total_vente.move(70,300)
      self.lab_total_vente.resize(200,30)

      self.total_vente=QLineEdit(self.dash3_vente)
      self.total_vente.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.total_vente.setAlignment(Qt.AlignCenter)
      self.total_vente.move(70,350)
      self.total_vente.resize(150,30)
      self.total_vente.setEnabled(False)
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
      #self.btn_reduire.clicked.connect(self.remove_x_produit)
      self.btn_reduire.move(1090,10)
      self.btn_reduire.resize(80,20)"""

      #=====BTN CART
      self.btn_cart=QToolButton(self)
      self.btn_cart.setStyleSheet("""
                                  QToolButton::pressed{background-color :#1b1b1c;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#1b1b1c;color:#fff;font-family: Time;font-style:italic;font-size:15pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::hover{background-color :#1b1b1c;color:#fff;border-style:solid;
                                  border-width:3px;border-color:#e3128c;font-family: Time;font-style:italic;font-size:15pt;
                                  font-weight:bold;border-radius:10px}
                                """)
      
      self.btn_cart.setIconSize(QSize(100,200))
      self.btn_cart.move(1000,475)
      self.btn_cart.resize(180,100)
      self.btn_cart.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
      self.btn_cart.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_cart.clicked.connect(self.shop)
      self.btn_cart.setIcon(QIcon('png/sell.png'))
      self.btn_cart.setIconSize(QSize(110,110))
      #self.btn_cart.setText('PANIER')

      #_______cart count
      self.cart_count=QLabel(self)
      self.cart_count.setStyleSheet("""
                                  background-color:#1b1b1c;color:#fff;font-family: Time;font-style:italic;font-size:15pt;
                                  font-weight:bold;border-radius:10px
                                  """)
      self.cart_count.move(1080,478)
      self.cart_count.resize(80,20)
      #self.cart_count.hide()

      
      
      
   #================================================================================================#
   #================================================================================================#
   #============================================ FUNCTIONS =========================================#
   #================================================================================================#
   def shop(self):
      self.screen=Panier()
      self.screen.show()

   def close(self):
      self.question=QMessageBox.question(self,str(self.app_name),'VOUS VOULEZ QUITTER ?',QMessageBox.Yes,QMessageBox.No)
      if self.question==QMessageBox.Yes:
         os._exit(0)
      else:
         pass
   
         
   def reset_cart(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  self.question=QMessageBox.question(self,str(self.app_name),'VOULEZ VOUS VIDER LE PANIER ?',QMessageBox.Yes,QMessageBox.No)
                  if self.question==QMessageBox.Yes:
                     self.cursor=self.bdd.cursor()
                     
                     self.sq1=self.cursor.execute("SELECT COUNT(*) FROM panier")
                     for i in self.sq1:
                        if int(i[0])>0:

                           self.cursor.execute("SELECT code_produit,type,id_produit FROM panier")
                           self.rr=self.cursor.fetchall()
                           for i in self.rr:
                              if 'BOISSON' in i[1]:
                                 self.cursor.execute("""UPDATE boissons SET quantite = quantite + (SELECT quantite FROM panier
                                          WHERE code_produit={0} AND type='BOISSON') WHERE code_produit={1} """.format("'"+str(i[0])+"'","'"+str(i[0])+"'"))
                                 self.bdd.commit()
                              elif 'DESSERT' in i[1]:
                                 self.cursor.execute("""UPDATE desserts SET quantite = quantite + (SELECT quantite FROM panier
                                          WHERE code_produit={0} AND type='DESSERT') WHERE code_produit={1} """.format("'"+str(i[0])+"'","'"+str(i[0])+"'"))
                                 self.bdd.commit()
                              elif 'CAFE' in i[1]:
                                 self.cursor.execute("""UPDATE cafes SET quantite = quantite + (SELECT quantite FROM panier
                                          WHERE code_produit={0} AND type='CAFE') WHERE code_produit={1} """.format("'"+str(i[0])+"'","'"+str(i[0])+"'"))
                                 self.bdd.commit()
                              elif 'PLAT' in i[1]:
                                 self.cursor.execute("""UPDATE plats SET quantite = quantite + (SELECT quantite FROM panier
                                          WHERE code_produit={0} AND type='PLAT') WHERE code_produit={1} """.format("'"+str(i[0])+"'","'"+str(i[0])+"'"))
                                 self.bdd.commit()
                              else:
                                 self.bdd.roolback()
                                 QMessageBox.information(self,str(self.app_name),"AUCUN PRODUIT \n DISPONIBLE DANS LE PANIER")
                                 
                              
                           self.cursor.execute("DELETE FROM panier")
                           self.bdd.commit()
                           QMessageBox.information(self,str(self.app_name),'PANIER VIDE AVEC SUCCES')
                           
                           self.list_panier.clear()
                           self.cart_price=0
                           self.cart=0
                           self.cart_count.setText(str(self.cart))
                           self.total_vente.setText(str(self.cart_price))
                        else:
                           QMessageBox.information(self,str(self.app_name),"AUCUN PRODUIT \n DISPONIBLE DANS LE PANIER")
                        
                     self.bdd.commit()
                     self.refresh_all()
               except:
                  self.bdd.roolback()
                  QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")
              
       
   def refresh_all(self):
      if self.zone_title.text()=='BOISSONS':
         self.refresh_boisson()
      elif self.zone_title.text()=='DESSERTS':
         self.refresh_dessert()
      elif self.zone_title.text()=='CAFES':
         self.refresh_cafe()
      elif self.zone_title.text()=='PLATS':
         self.refresh_plat()
         

   def refresh_cart(self):
      try:
         self.index1=[]
         self.double_index=[]
         self.selection=[]
         self.bdd=sqlite3.connect('restaurant.bd')
         self.cursor=self.bdd.cursor()

         #==== MISE A JOUR QUANTITE ET PRIX DANS LE PANIER
         self.sql=self.cursor.execute(""" SELECT SUM(panier.quantite),SUM(panier.quantite*panier.prix),
                                          SUM((panier.quantite*panier.prix)-((panier.quantite*panier.prix)*panier.reduction/100))                                          
                                          FROM panier """)
         for c in self.sql:
            if c[0] is not None:
               self.cart=c[0]
               self.cart_count.setText(str(self.cart))
               self.cart_price=c[1]
               self.total_vente.setText(str(self.cart_price))
               self.btn_total.setText(str(c[2]))
            else :
               self.cart_count.setText('0')
               self.total_vente.setText('0')
               self.btn_total.setText('0')

         #==== MISE A JOUR ID PANIER 
         self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                rownum,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,datetime,reduction,is_added,is_ordered,
                                is_processed,is_shipped,is_paid FROM panier""")
         for i in self.s_ss:
            self.index1.append(i)

         self.cursor.execute("DELETE FROM panier")            
         self.cursor.executemany("""INSERT INTO panier
                                   (id,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,datetime,reduction,is_added,is_ordered,
                                is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1)

         #==== MISE A JOUR APERCU PANIER( LISTE PRODUIT AJOUTE )
         self.list_panier.clear()
         self.cursor.execute("SELECT * FROM panier")
         self.records=self.cursor.fetchall()
         for r in self.records:
            self.list_produit=("NOM: ------ " + str(r[1]) + " \n " +
                               "QUANTITE: ------ " + str(r[2]) + " \n " +
                               "PRIX: ------ " + str(r[3]) + " FCFA")
            
            #====FRAME WIDGET
            self.choose1=QFrame(self.list_panier)
            self.choose1.setStyleSheet("""
                                background-color:#490063;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;border-radius:25px
                                """)
            self.label1 = QLabel(self.list_produit,self.choose1)
                              
            self.layout = QHBoxLayout(self.choose1)
            self.layout.addWidget(self.label1)
            self.setLayout(self.layout)
            
            self.item = QListWidgetItem(self.list_panier)         
            self.item_widget = self.choose1        
            self.item.setSizeHint(self.item_widget.sizeHint())
            
            self.list_panier.addItem(self.item)
            self.list_panier.setItemWidget(self.item,self.item_widget)

         self.bdd.commit()
         self.refresh_all()
      except:
         self.bdd.rollback()
         QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")

       
   def selection_item(self):
      try:
         self.panier1=[]
         self.bdd=sqlite3.connect('restaurant.bd')
         self.cursor=self.bdd.cursor()
         
         #==== ID PANIER MISE A JOUR
         self.id_panier.setValue(int(self.list_panier.currentRow())+1)

         #==== MISE A JOUR QUANTITE ET PRIX DANS LE PANIER
         self.sql=self.cursor.execute(""" SELECT SUM(panier.quantite),SUM(panier.quantite*panier.prix),
                                          SUM((panier.quantite*panier.prix)-((panier.quantite*panier.prix)*panier.reduction/100))                                          
                                          FROM panier """)
         for c in self.sql:
            if c[0] is not None:
               self.cart=c[0]
               self.cart_count.setText(str(self.cart))
               self.cart_price=c[1]
               self.total_vente.setText(str(self.cart_price))
               self.btn_total.setText(str(c[2]))
            else :
               self.cart_count.setText('0')
               self.total_vente.setText('0')
               self.btn_total.setText('0')

         #==== SELECTION ARTICLE DANS LE PANIER
         self.s_sq=self.cursor.execute("SELECT row_number() OVER (ORDER BY id) rownum,nom,quantite,prix,id_produit,type,photo,code_produit,reduction FROM panier")
         for i in self.s_sq:
            self.panier1.append(i)
            if len(self.panier1)==int(self.list_panier.count()):
               #print(self.panier1)
               self.type=str(self.panier1[int(self.list_panier.currentRow())][5])
               self.nom_vente.setText(str(self.panier1[int(self.list_panier.currentRow())][1]))
               self.prix_vente.setValue(float(self.panier1[int(self.list_panier.currentRow())][3]))
               self.id_produit.setValue(int(self.panier1[int(self.list_panier.currentRow())][4]))                  
               self.btn_view.setIcon(QIcon(str(self.panier1[int(self.list_panier.currentRow())][6])))
               self.code_produit.setText(str(self.panier1[int(self.list_panier.currentRow())][7]))
               self.reduction_produit.setValue(int(self.panier1[int(self.list_panier.currentRow())][8]))
               if self.type=='BOISSON':
                  self.cursor.execute("""SELECT quantite FROM boissons
                                                  WHERE code_produit={0}""".format("'"+str(self.code_produit.text())+"'"))
                  self.sq1=self.cursor.fetchone()
                  for c in self.sq1:
                     self.qte_vente.setValue(int(c))
                  self.bdd.commit()
               if self.type=='DESSERT':
                  self.cursor.execute("""SELECT quantite FROM desserts
                                                  WHERE code_produit={0}""".format("'"+str(self.code_produit.text())+"'"))
                  self.sq2=self.cursor.fetchone()
                  for c in self.sq2:
                     self.qte_vente.setValue(int(c))
                  self.bdd.commit()
               if self.type=='CAFE':
                  self.cursor.execute("""SELECT quantite FROM cafes
                                                  WHERE code_produit={0}""".format("'"+str(self.code_produit.text())+"'"))
                  self.sq3=self.cursor.fetchone()
                  for c in self.sq3:
                     self.qte_vente.setValue(int(c))
                  self.bdd.commit()
               if self.type=='PLAT':
                  self.cursor.execute("""SELECT quantite FROM plats
                                                  WHERE code_produit={0}""".format("'"+str(self.code_produit.text())+"'"))
                  self.sq4=self.cursor.fetchone()
                  for c in self.sq4:
                     self.qte_vente.setValue(int(c))
                  self.bdd.commit()
                     
         self.bdd.commit()
         self.refresh_all()
      
      except:
         self.bdd.rollback()
         QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")

   def add_item(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:               
               self.cursor=self.bdd.cursor()
               if self.qte_vente.value() >0 and self.zone_title.text()=='BOISSONS':
                  try:
                     self.index1=[]
                     self.set_date= """{0}-{1}-{2}/{3}:{4}:{5}""".format(str(datetime.datetime.utcnow().day),
                                                              str(datetime.datetime.utcnow().month),
                                                              str(datetime.datetime.utcnow().year),
                                                              str(datetime.datetime.utcnow().hour),
                                                              str(datetime.datetime.utcnow().minute),
                                                              str(datetime.datetime.utcnow().second))

                     #==== VERIFICATION PRODUIT EXISTANT AND AJOUT
                     self.cursor.execute("""SELECT id,nom,quantite,prix,photo FROM panier
                                            WHERE id_produit={0} AND type='BOISSON'""".format(str(self.id_produit.value())))
                     self._result=self.cursor.fetchone()
                     if self._result is not None:
                        self.cursor.execute(""" UPDATE panier SET quantite=quantite+1
                                            WHERE id_produit={0} AND type='BOISSON'""".format(str(self.id_produit.value())))
                        self.cursor.execute(""" UPDATE boissons SET quantite = quantite-1 WHERE id={0} """.format(self.id_produit.value()))
                        self.bdd.commit()
                     else:
                        #==== INSERTION ARTICLE DANS LE PANIER
                        self.cursor.execute("""INSERT INTO panier (nom,quantite,prix,id_produit,type,datetime,is_added,is_ordered,
                                            is_processed,is_shipped,is_paid,code_produit,photo,reduction,categorie)
                                            VALUES (?,?,?,?,?,?,?,?,?,?,?""" +
                                            ",(SELECT code_produit FROM boissons WHERE id=" + str(self.id_produit.value()) + ")" +
                                            ",(SELECT photo FROM boissons WHERE id=" + str(self.id_produit.value()) + ")" +
                                            ",(SELECT reduction FROM boissons WHERE id=" + str(self.id_produit.value()) + ")" +
                                            ",(SELECT categorie FROM boissons WHERE id=" + str(self.id_produit.value()) + ") )",
                                            (str(self.nom_vente.text()),'1',str(self.prix_vente.value()),
                                             str(self.id_produit.value()),'BOISSON',self.set_date,'1','0','0','0','0'))
                        
                        self.cursor.execute(""" UPDATE boissons SET quantite = quantite-1 WHERE id={0} """.format(self.id_produit.value()))
                        self.bdd.commit()
                     

                     #==== MISE A JOUR ID PANIER 
                     self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                            rownum,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,datetime,reduction,is_added,is_ordered,
                                            is_processed,is_shipped,is_paid FROM panier""")
                     for i in self.s_ss:
                        self.index1.append(i)

                     self.cursor.execute("DELETE FROM panier")            
                     self.cursor.executemany("""INSERT INTO panier
                                               (id,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,datetime,reduction,is_added,is_ordered,
                                            is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1)
                     
                     self.list_panier.clear()
                     self.cursor.execute("SELECT * FROM panier")
                     self.records=self.cursor.fetchall()
                     for r in self.records:
                        self.list_produit=("NOM: ------ " + str(r[1]) + " \n " +
                                           "QUANTITE: ------ " + str(r[2]) + " \n " +
                                           "PRIX: ------ " + str(r[3]) + " FCFA")
                        
                        #====FRAME WIDGET
                        self.choose1=QFrame(self.list_panier)
                        self.choose1.setStyleSheet("""
                             background-color:#490063;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                             font-weight:bold;border-radius:25px
                             """)
                        self.label1 = QLabel(self.list_produit,self.choose1)
                                          
                        self.layout = QHBoxLayout(self.choose1)
                        self.layout.addWidget(self.label1)
                        self.setLayout(self.layout)
                        
                        self.item = QListWidgetItem(self.list_panier)         
                        self.item_widget = self.choose1        
                        self.item.setSizeHint(self.item_widget.sizeHint())
                        
                        self.list_panier.addItem(self.item)
                        self.list_panier.setItemWidget(self.item,self.item_widget)
                        
                     
                     self.bdd.commit()
                     self.refresh_all()
                     self.refresh_cart()
                     self.cart_count.show()
                  except:
                     self.bdd.roolback()
                     QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")
                  
               elif self.qte_vente.value() >0 and self.zone_title.text()=='DESSERTS':
                  try:
                     self.index1=[]
                     self.set_date= """{0}-{1}-{2}/{3}:{4}:{5}""".format(str(datetime.datetime.utcnow().day),
                                                              str(datetime.datetime.utcnow().month),
                                                              str(datetime.datetime.utcnow().year),
                                                              str(datetime.datetime.utcnow().hour),
                                                              str(datetime.datetime.utcnow().minute),
                                                              str(datetime.datetime.utcnow().second))

                     #==== VERIFICATION PRODUIT EXISTANT AND AJOUT
                     self.cursor.execute("""SELECT id,nom,quantite,prix,photo FROM panier
                                            WHERE id_produit={0} AND type='DESSERT'""".format(str(self.id_produit.value())))
                     self._result=self.cursor.fetchone()
                     if self._result is not None:
                        self.cursor.execute(""" UPDATE panier SET quantite=quantite+1
                                            WHERE id_produit={0} AND type='DESSERT'""".format(str(self.id_produit.value())))
                        self.cursor.execute(""" UPDATE desserts SET quantite = quantite-1 WHERE id={0} """.format(self.id_produit.value()))
                        self.bdd.commit()
                     else:
                        #==== INSERTION ARTICLE DANS LE PANIER
                        self.cursor.execute("""INSERT INTO panier (nom,quantite,prix,id_produit,type,datetime,is_added,is_ordered,
                                            is_processed,is_shipped,is_paid,code_produit,photo,reduction,categorie)
                                            VALUES (?,?,?,?,?,?,?,?,?,?,?""" +
                                            ",(SELECT code_produit FROM desserts WHERE id=" + str(self.id_produit.value()) + ")" +
                                            ",(SELECT photo FROM desserts WHERE id=" + str(self.id_produit.value()) + ")" +
                                            ",(SELECT reduction FROM desserts WHERE id=" + str(self.id_produit.value()) + ")" +
                                            ",(SELECT categorie FROM desserts WHERE id=" + str(self.id_produit.value()) + ") )",
                                            (str(self.nom_vente.text()),'1',str(self.prix_vente.value()),
                                             str(self.id_produit.value()),'DESSERT',self.set_date,'1','0','0','0','0'))
                        
                        self.cursor.execute(""" UPDATE desserts SET quantite = quantite-1 WHERE id={0} """.format(self.id_produit.value()))
                        self.bdd.commit()
                     

                     #==== MISE A JOUR ID PANIER 
                     self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                            rownum,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,datetime,reduction,is_added,is_ordered,
                                            is_processed,is_shipped,is_paid FROM panier""")
                     for i in self.s_ss:
                        self.index1.append(i)

                     self.cursor.execute("DELETE FROM panier")            
                     self.cursor.executemany("""INSERT INTO panier
                                               (id,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,datetime,reduction,is_added,is_ordered,
                                            is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1)

                     self.list_panier.clear()
                     self.cursor.execute("SELECT * FROM panier")
                     self.records=self.cursor.fetchall()
                     for r in self.records:
                        self.list_produit=("NOM: ------ " + str(r[1]) + " \n " +
                                           "QUANTITE: ------ " + str(r[2]) + " \n " +
                                           "PRIX: ------ " + str(r[3]) + " FCFA")
                        
                        #====FRAME WIDGET
                        self.choose1=QFrame(self.list_panier)
                        self.choose1.setStyleSheet("""
                             background-color:#490063;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                             font-weight:bold;border-radius:25px
                             """)
                        self.label1 = QLabel(self.list_produit,self.choose1)
                                          
                        self.layout = QHBoxLayout(self.choose1)
                        self.layout.addWidget(self.label1)
                        self.setLayout(self.layout)
                        
                        self.item = QListWidgetItem(self.list_panier)         
                        self.item_widget = self.choose1        
                        self.item.setSizeHint(self.item_widget.sizeHint())
                        
                        self.list_panier.addItem(self.item)
                        self.list_panier.setItemWidget(self.item,self.item_widget)
                        
                     self.bdd.commit()
                     self.refresh_all()
                     self.refresh_cart()
                     self.cart_count.show()
                  except:
                     self.bdd.roolback()
                     QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")

               elif self.qte_vente.value() >0 and self.zone_title.text()=='CAFES':
                  try:
                     self.index1=[]
                     self.set_date= """{0}-{1}-{2}/{3}:{4}:{5}""".format(str(datetime.datetime.utcnow().day),
                                                              str(datetime.datetime.utcnow().month),
                                                              str(datetime.datetime.utcnow().year),
                                                              str(datetime.datetime.utcnow().hour),
                                                              str(datetime.datetime.utcnow().minute),
                                                              str(datetime.datetime.utcnow().second))

                     #==== VERIFICATION PRODUIT EXISTANT AND AJOUT
                     self.cursor.execute("""SELECT id,nom,quantite,prix,photo FROM panier
                                            WHERE id_produit={0} AND type='CAFE'""".format(str(self.id_produit.value())))
                     self._result=self.cursor.fetchone()
                     if self._result is not None:
                        self.cursor.execute(""" UPDATE panier SET quantite=quantite+1
                                            WHERE id_produit={0} AND type='CAFE'""".format(str(self.id_produit.value())))
                        self.cursor.execute(""" UPDATE cafes SET quantite = quantite-1 WHERE id={0} """.format(self.id_produit.value()))
                        self.bdd.commit()
                     else:
                        #==== INSERTION ARTICLE DANS LE PANIER
                        self.cursor.execute("""INSERT INTO panier (nom,quantite,prix,id_produit,type,datetime,is_added,is_ordered,
                                            is_processed,is_shipped,is_paid,code_produit,photo,reduction,categorie)
                                            VALUES (?,?,?,?,?,?,?,?,?,?,?""" +
                                            ",(SELECT code_produit FROM cafes WHERE id=" + str(self.id_produit.value()) + ")" +
                                            ",(SELECT photo FROM cafes WHERE id=" + str(self.id_produit.value()) + ")" +
                                            ",(SELECT reduction FROM cafes WHERE id=" + str(self.id_produit.value()) + ")" +
                                            ",(SELECT categorie FROM cafes WHERE id=" + str(self.id_produit.value()) + ") )",
                                            (str(self.nom_vente.text()),'1',str(self.prix_vente.value()),
                                             str(self.id_produit.value()),'CAFE',self.set_date,'1','0','0','0','0'))
                        
                        self.cursor.execute(""" UPDATE cafes SET quantite = quantite-1 WHERE id={0} """.format(self.id_produit.value()))
                        self.bdd.commit()
                     

                     #==== MISE A JOUR ID PANIER 
                     self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                            rownum,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,datetime,reduction,is_added,is_ordered,
                                            is_processed,is_shipped,is_paid FROM panier""")
                     for i in self.s_ss:
                        self.index1.append(i)

                     self.cursor.execute("DELETE FROM panier")            
                     self.cursor.executemany("""INSERT INTO panier
                                               (id,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,datetime,reduction,is_added,is_ordered,
                                            is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1)

                     self.list_panier.clear()
                     self.cursor.execute("SELECT * FROM panier")
                     self.records=self.cursor.fetchall()
                     for r in self.records:
                        self.list_produit=("NOM: ------ " + str(r[1]) + " \n " +
                                           "QUANTITE: ------ " + str(r[2]) + " \n " +
                                           "PRIX: ------ " + str(r[3]) + " FCFA")
                        
                        #====FRAME WIDGET
                        self.choose1=QFrame(self.list_panier)
                        self.choose1.setStyleSheet("""
                             background-color:#490063;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                             font-weight:bold;border-radius:25px
                             """)
                        self.label1 = QLabel(self.list_produit,self.choose1)                                          
                        self.layout = QHBoxLayout(self.choose1)
                        self.layout.addWidget(self.label1)
                        self.setLayout(self.layout)                        
                        self.item = QListWidgetItem(self.list_panier)         
                        self.item_widget = self.choose1        
                        self.item.setSizeHint(self.item_widget.sizeHint())
                        
                        self.list_panier.addItem(self.item)
                        self.list_panier.setItemWidget(self.item,self.item_widget)

                     self.bdd.commit()
                     self.refresh_all()
                     self.refresh_cart()
                     self.cart_count.show()
                  except:
                     self.bdd.roolback()
                     QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")
                  
               elif self.qte_vente.value() >0 and self.zone_title.text()=='PLATS':
                  try:
                     self.index1=[]
                     self.set_date= """{0}-{1}-{2}/{3}:{4}:{5}""".format(str(datetime.datetime.utcnow().day),
                                                              str(datetime.datetime.utcnow().month),
                                                              str(datetime.datetime.utcnow().year),
                                                              str(datetime.datetime.utcnow().hour),
                                                              str(datetime.datetime.utcnow().minute),
                                                              str(datetime.datetime.utcnow().second))

                     #==== VERIFICATION PRODUIT EXISTANT AND AJOUT
                     self.cursor.execute("""SELECT id,nom,quantite,prix,photo FROM panier
                                            WHERE id_produit={0} AND type='PLAT'""".format(str(self.id_produit.value())))
                     self._result=self.cursor.fetchone()
                     if self._result is not None:
                        self.cursor.execute(""" UPDATE panier SET quantite=quantite+1
                                            WHERE id_produit={0} AND type='PLAT'""".format(str(self.id_produit.value())))
                        self.cursor.execute(""" UPDATE plats SET quantite = quantite-1 WHERE id={0} """.format(self.id_produit.value()))
                        self.bdd.commit()
                     else:
                         #==== INSERTION ARTICLE DANS LE PANIER
                        self.cursor.execute("""INSERT INTO panier (nom,quantite,prix,id_produit,type,datetime,is_added,is_ordered,
                                            is_processed,is_shipped,is_paid,code_produit,photo,reduction,categorie)
                                            VALUES (?,?,?,?,?,?,?,?,?,?,?""" +
                                            ",(SELECT code_produit FROM plats WHERE id=" + str(self.id_produit.value()) + ")" +
                                            ",(SELECT photo FROM plats WHERE id=" + str(self.id_produit.value()) + ")" +
                                            ",(SELECT reduction FROM plats WHERE id=" + str(self.id_produit.value()) + ")" +
                                            ",(SELECT categorie FROM plats WHERE id=" + str(self.id_produit.value()) + ") )",
                                            (str(self.nom_vente.text()),'1',str(self.prix_vente.value()),
                                             str(self.id_produit.value()),'PLAT',self.set_date,'1','0','0','0','0'))
                        
                        self.cursor.execute(""" UPDATE plats SET quantite = quantite-1 WHERE id={0} """.format(self.id_produit.value()))
                        self.bdd.commit()
                     

                     #==== MISE A JOUR ID PANIER
                     self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                      rownum,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,datetime,reduction
                                                      FROM panier""")
                     for i in self.s_ss:
                        self.index1.append(i)

                     self.cursor.execute("DELETE FROM panier")            
                     self.cursor.executemany("""INSERT INTO panier
                                               (id,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,datetime,reduction)
                                                VALUES (?,?,?,?,?,?,?,?,?,?,?)""",self.index1)
                        
                     self.list_panier.clear()

                     self.cursor.execute("SELECT * FROM panier")
                     self.records=self.cursor.fetchall()
                     for r in self.records:
                        self.list_produit=("NOM: ------ " + str(r[1]) + " \n " +
                                           "QUANTITE: ------ " + str(r[2]) + " \n " +
                                           "PRIX: ------ " + str(r[3]) + " FCFA")
                        
                        #====FRAME WIDGET
                        self.choose1=QFrame(self.list_panier)
                        self.choose1.setStyleSheet("""
                             background-color:#490063;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                             font-weight:bold;border-radius:25px
                             """)
                        self.label1 = QLabel(self.list_produit,self.choose1)
                                          
                        self.layout = QHBoxLayout(self.choose1)
                        self.layout.addWidget(self.label1)
                        self.setLayout(self.layout)
                        
                        self.item = QListWidgetItem(self.list_panier)         
                        self.item_widget = self.choose1        
                        self.item.setSizeHint(self.item_widget.sizeHint())
                        
                        self.list_panier.addItem(self.item)
                        self.list_panier.setItemWidget(self.item,self.item_widget)
                        
                     self.bdd.commit()
                     self.refresh_all()
                     self.refresh_cart()
                     self.cart_count.show()
                  except:
                     self.bdd.roolback()
                     QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")
               else:
                  QMessageBox.information(self,str(self.app_name),'STOCK {0} EPUISE\n\nREAPPROVISIONNER ET REESSAYER'.format(self.nom_vente.text()))

            else:
               QMessageBox.information(self,str(self.app_name),'BASE DE DONNEE NON CONNECTEE')

   #====== SELECTION boissons                    
   def selection_boisson1(self):
      self.id_produit.setValue(1)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(0,0)].icon()))
      self.button_boisson1[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson2(self):
      self.id_produit.setValue(2)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(0,1)].icon()))
      self.button_boisson1[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson3(self):
      self.id_produit.setValue(3)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(0,2)].icon()))
      self.button_boisson1[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson4(self):
      self.id_produit.setValue(4)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(0,3)].icon()))
      self.button_boisson1[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson5(self):
      self.id_produit.setValue(5)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(1,0)].icon()))
      self.button_boisson1[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson6(self):
      self.id_produit.setValue(6)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(1,1)].icon()))
      self.button_boisson1[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson7(self):
      self.id_produit.setValue(7)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(1,2)].icon()))
      self.button_boisson1[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson8(self):
      self.id_produit.setValue(8)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(1,3)].icon()))
      self.button_boisson1[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson9(self):
      self.id_produit.setValue(9)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(2,0)].icon()))
      self.button_boisson1[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson10(self):
      self.id_produit.setValue(10)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(2,1)].icon()))
      self.button_boisson1[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson11(self):
      self.id_produit.setValue(11)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(2,2)].icon()))
      self.button_boisson1[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson12(self):
      self.id_produit.setValue(12)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(2,3)].icon()))
      self.button_boisson1[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson13(self):
      self.id_produit.setValue(13)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(3,0)].icon()))
      self.button_boisson1[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson14(self):
      self.id_produit.setValue(14)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(3,1)].icon()))
      self.button_boisson1[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson15(self):
      self.id_produit.setValue(15)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(3,2)].icon()))
      self.button_boisson1[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson16(self):
      self.id_produit.setValue(16)
      self.btn_view.setIcon(QIcon(self.button_boisson1[(3,3)].icon()))
      self.button_boisson1[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson17(self):
      self.id_produit.setValue(17)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(0,0)].icon()))
      self.button_boisson2[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson18(self):
      self.id_produit.setValue(18)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(0,1)].icon()))
      self.button_boisson2[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson19(self):
      self.id_produit.setValue(19)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(0,2)].icon()))
      self.button_boisson2[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson20(self):
      self.id_produit.setValue(20)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(0,3)].icon()))
      self.button_boisson2[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson21(self):
      self.id_produit.setValue(21)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(1,0)].icon()))
      self.button_boisson2[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson22(self):
      self.id_produit.setValue(22)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(1,1)].icon()))
      self.button_boisson2[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson23(self):
      self.id_produit.setValue(23)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(1,2)].icon()))
      self.button_boisson2[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson24(self):
      self.id_produit.setValue(24)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(1,3)].icon()))
      self.button_boisson2[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson25(self):
      self.id_produit.setValue(25)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(2,0)].icon()))
      self.button_boisson2[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson26(self):
      self.id_produit.setValue(26)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(2,1)].icon()))
      self.button_boisson2[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson27(self):
      self.id_produit.setValue(27)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(2,2)].icon()))
      self.button_boisson2[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson28(self):
      self.id_produit.setValue(28)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(2,3)].icon()))
      self.button_boisson2[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson29(self):
      self.id_produit.setValue(29)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(3,0)].icon()))
      self.button_boisson2[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson30(self):
      self.id_produit.setValue(30)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(3,1)].icon()))
      self.button_boisson2[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson31(self):
      self.id_produit.setValue(31)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(3,2)].icon()))
      self.button_boisson2[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson32(self):
      self.id_produit.setValue(32)
      self.btn_view.setIcon(QIcon(self.button_boisson2[(3,3)].icon()))
      self.button_boisson2[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson33(self):
      self.id_produit.setValue(33)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(0,0)].icon()))
      self.button_boisson3[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson34(self):
      self.id_produit.setValue(34)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(0,1)].icon()))
      self.button_boisson3[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson35(self):
      self.id_produit.setValue(35)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(0,2)].icon()))
      self.button_boisson3[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson36(self):
      self.id_produit.setValue(36)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(0,3)].icon()))
      self.button_boisson3[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson37(self):
      self.id_produit.setValue(37)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(1,0)].icon()))
      self.button_boisson3[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson38(self):
      self.id_produit.setValue(38)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(1,1)].icon()))
      self.button_boisson3[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson39(self):
      self.id_produit.setValue(39)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(1,2)].icon()))
      self.button_boisson3[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson40(self):
      self.id_produit.setValue(40)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(1,3)].icon()))
      self.button_boisson3[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson41(self):
      self.id_produit.setValue(41)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(2,0)].icon()))
      self.button_boisson3[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson42(self):
      self.id_produit.setValue(42)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(2,1)].icon()))
      self.button_boisson3[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson43(self):
      self.id_produit.setValue(43)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(2,2)].icon()))
      self.button_boisson3[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson44(self):
      self.id_produit.setValue(44)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(2,3)].icon()))
      self.button_boisson3[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson45(self):
      self.id_produit.setValue(45)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(3,0)].icon()))
      self.button_boisson3[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson46(self):
      self.id_produit.setValue(46)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(3,1)].icon()))
      self.button_boisson3[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson47(self):
      self.id_produit.setValue(47)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(3,2)].icon()))
      self.button_boisson3[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson48(self):
      self.id_produit.setValue(48)
      self.btn_view.setIcon(QIcon(self.button_boisson3[(3,3)].icon()))
      self.button_boisson3[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson49(self):
      self.id_produit.setValue(49)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(0,0)].icon()))
      self.button_boisson4[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson50(self):
      self.id_produit.setValue(50)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(0,1)].icon()))
      self.button_boisson4[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson51(self):
      self.id_produit.setValue(51)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(0,2)].icon()))
      self.button_boisson4[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson52(self):
      self.id_produit.setValue(52)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(0,3)].icon()))
      self.button_boisson4[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson53(self):
      self.id_produit.setValue(53)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(1,0)].icon()))
      self.button_boisson4[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson54(self):
      self.id_produit.setValue(54)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(1,1)].icon()))
      self.button_boisson4[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson55(self):
      self.id_produit.setValue(55)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(1,2)].icon()))
      self.button_boisson4[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson56(self):
      self.id_produit.setValue(56)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(1,3)].icon()))
      self.button_boisson4[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson57(self):
      self.id_produit.setValue(57)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(2,0)].icon()))
      self.button_boisson4[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson58(self):
      self.id_produit.setValue(58)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(2,1)].icon()))
      self.button_boisson4[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson59(self):
      self.id_produit.setValue(59)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(2,2)].icon()))
      self.button_boisson4[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson60(self):
      self.id_produit.setValue(60)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(2,3)].icon()))
      self.button_boisson4[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson61(self):
      self.id_produit.setValue(61)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(3,0)].icon()))
      self.button_boisson4[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson62(self):
      self.id_produit.setValue(62)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(3,1)].icon()))
      self.button_boisson4[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson63(self):
      self.id_produit.setValue(63)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(3,2)].icon()))
      self.button_boisson4[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson64(self):
      self.id_produit.setValue(64)
      self.btn_view.setIcon(QIcon(self.button_boisson4[(3,3)].icon()))
      self.button_boisson4[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson65(self):
      self.id_produit.setValue(65)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(0,0)].icon()))
      self.button_boisson5[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson66(self):
      self.id_produit.setValue(66)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(0,1)].icon()))
      self.button_boisson5[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson67(self):
      self.id_produit.setValue(67)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(0,2)].icon()))
      self.button_boisson5[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson68(self):
      self.id_produit.setValue(68)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(0,3)].icon()))
      self.button_boisson5[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson69(self):
      self.id_produit.setValue(69)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(1,0)].icon()))
      self.button_boisson5[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson70(self):
      self.id_produit.setValue(70)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(1,1)].icon()))
      self.button_boisson5[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson71(self):
      self.id_produit.setValue(71)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(1,2)].icon()))
      self.button_boisson5[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson72(self):
      self.id_produit.setValue(72)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(1,3)].icon()))
      self.button_boisson5[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson73(self):
      self.id_produit.setValue(73)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(2,0)].icon()))
      self.button_boisson5[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson74(self):
      self.id_produit.setValue(74)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(2,1)].icon()))
      self.button_boisson5[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson75(self):
      self.id_produit.setValue(75)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(2,2)].icon()))
      self.button_boisson5[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson76(self):
      self.id_produit.setValue(76)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(2,3)].icon()))
      self.button_boisson5[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson77(self):
      self.id_produit.setValue(77)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(3,0)].icon()))
      self.button_boisson5[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson78(self):
      self.id_produit.setValue(78)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(3,1)].icon()))
      self.button_boisson5[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson79(self):
      self.id_produit.setValue(79)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(3,2)].icon()))
      self.button_boisson5[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson80(self):
      self.id_produit.setValue(80)
      self.btn_view.setIcon(QIcon(self.button_boisson5[(3,3)].icon()))
      self.button_boisson5[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson81(self):
      self.id_produit.setValue(81)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(0,0)].icon()))
      self.button_boisson6[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson82(self):
      self.id_produit.setValue(82)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(0,1)].icon()))
      self.button_boisson6[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson83(self):
      self.id_produit.setValue(83)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(0,2)].icon()))
      self.button_boisson6[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson84(self):
      self.id_produit.setValue(84)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(0,3)].icon()))
      self.button_boisson6[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson85(self):
      self.id_produit.setValue(85)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(1,0)].icon()))
      self.button_boisson6[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson86(self):
      self.id_produit.setValue(86)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(1,1)].icon()))
      self.button_boisson6[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson87(self):
      self.id_produit.setValue(87)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(1,2)].icon()))
      self.button_boisson6[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson88(self):
      self.id_produit.setValue(88)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(1,3)].icon()))
      self.button_boisson6[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson89(self):
      self.id_produit.setValue(89)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(2,0)].icon()))
      self.button_boisson6[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson90(self):
      self.id_produit.setValue(90)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(2,1)].icon()))
      self.button_boisson6[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson91(self):
      self.id_produit.setValue(91)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(2,2)].icon()))
      self.button_boisson6[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson92(self):
      self.id_produit.setValue(92)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(2,3)].icon()))
      self.button_boisson6[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson93(self):
      self.id_produit.setValue(93)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(3,0)].icon()))
      self.button_boisson6[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson94(self):
      self.id_produit.setValue(94)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(3,1)].icon()))
      self.button_boisson6[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson95(self):
      self.id_produit.setValue(95)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(3,2)].icon()))
      self.button_boisson6[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson96(self):
      self.id_produit.setValue(96)
      self.btn_view.setIcon(QIcon(self.button_boisson6[(3,3)].icon()))
      self.button_boisson6[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson97(self):
      self.id_produit.setValue(97)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(0,0)].icon()))
      self.button_boisson7[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson98(self):
      self.id_produit.setValue(98)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(0,1)].icon()))
      self.button_boisson7[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()     
   def selection_boisson99(self):
      self.id_produit.setValue(99)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(0,2)].icon()))
      self.button_boisson7[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson100(self):
      self.id_produit.setValue(100)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(0,3)].icon()))
      self.button_boisson7[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson101(self):
      self.id_produit.setValue(101)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(1,0)].icon()))
      self.button_boisson7[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson102(self):
      self.id_produit.setValue(102)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(1,1)].icon()))
      self.button_boisson7[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson103(self):
      self.id_produit.setValue(103)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(1,2)].icon()))
      self.button_boisson7[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson104(self):
      self.id_produit.setValue(104)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(1,3)].icon()))
      self.button_boisson7[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson105(self):
      self.id_produit.setValue(105)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(2,0)].icon()))
      self.button_boisson7[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson106(self):
      self.id_produit.setValue(106)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(2,1)].icon()))
      self.button_boisson7[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson107(self):
      self.id_produit.setValue(107)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(2,2)].icon()))
      self.button_boisson7[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson108(self):
      self.id_produit.setValue(108)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(2,3)].icon()))
      self.button_boisson7[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson109(self):
      self.id_produit.setValue(109)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(3,0)].icon()))
      self.button_boisson7[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson110(self):
      self.id_produit.setValue(110)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(3,1)].icon()))
      self.button_boisson7[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson111(self):
      self.id_produit.setValue(111)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(3,2)].icon()))
      self.button_boisson7[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson112(self):
      self.id_produit.setValue(112)
      self.btn_view.setIcon(QIcon(self.button_boisson7[(3,3)].icon()))
      self.button_boisson7[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson113(self):
      self.id_produit.setValue(113)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(0,0)].icon()))
      self.button_boisson8[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson114(self):
      self.id_produit.setValue(114)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(0,1)].icon()))
      self.button_boisson8[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson115(self):
      self.id_produit.setValue(115)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(0,2)].icon()))
      self.button_boisson8[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson116(self):
      self.id_produit.setValue(116)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(0,3)].icon()))
      self.button_boisson8[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson117(self):
      self.id_produit.setValue(117)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(1,0)].icon()))
      self.button_boisson8[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson118(self):
      self.id_produit.setValue(118)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(1,1)].icon()))
      self.button_boisson8[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson119(self):
      self.id_produit.setValue(119)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(1,2)].icon()))
      self.button_boisson8[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson120(self):
      self.id_produit.setValue(120)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(1,3)].icon()))
      self.button_boisson8[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson121(self):
      self.id_produit.setValue(121)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(2,0)].icon()))
      self.button_boisson8[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson122(self):
      self.id_produit.setValue(122)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(2,1)].icon()))
      self.button_boisson8[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson123(self):
      self.id_produit.setValue(123)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(2,2)].icon()))
      self.button_boisson8[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson124(self):
      self.id_produit.setValue(124)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(2,3)].icon()))
      self.button_boisson8[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson125(self):
      self.id_produit.setValue(125)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(3,0)].icon()))
      self.button_boisson8[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson126(self):
      self.id_produit.setValue(126)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(3,1)].icon()))
      self.button_boisson8[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson127(self):
      self.id_produit.setValue(127)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(3,2)].icon()))
      self.button_boisson8[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()
   def selection_boisson128(self):
      self.id_produit.setValue(128)
      self.btn_view.setIcon(QIcon(self.button_boisson8[(3,3)].icon()))
      self.button_boisson8[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_boisson()

   #====== SELECTION desserts                    
   def selection_dessert1(self):
      self.id_produit.setValue(1)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(0,0)].icon()))
      self.button_dessert1[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert2(self):
      self.id_produit.setValue(2)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(0,1)].icon()))
      self.button_dessert1[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert3(self):
      self.id_produit.setValue(3)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(0,2)].icon()))
      self.button_dessert1[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert4(self):
      self.id_produit.setValue(4)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(0,3)].icon()))
      self.button_dessert1[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert5(self):
      self.id_produit.setValue(5)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(1,0)].icon()))
      self.button_dessert1[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert6(self):
      self.id_produit.setValue(6)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(1,1)].icon()))
      self.button_dessert1[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert7(self):
      self.id_produit.setValue(7)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(1,2)].icon()))
      self.button_dessert1[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert8(self):
      self.id_produit.setValue(8)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(1,3)].icon()))
      self.button_dessert1[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert9(self):
      self.id_produit.setValue(9)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(2,0)].icon()))
      self.button_dessert1[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert10(self):
      self.id_produit.setValue(10)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(2,1)].icon()))
      self.button_dessert1[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert11(self):
      self.id_produit.setValue(11)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(2,2)].icon()))
      self.button_dessert1[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert12(self):
      self.id_produit.setValue(12)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(2,3)].icon()))
      self.button_dessert1[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert13(self):
      self.id_produit.setValue(13)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(3,0)].icon()))
      self.button_dessert1[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert14(self):
      self.id_produit.setValue(14)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(3,1)].icon()))
      self.button_dessert1[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert15(self):
      self.id_produit.setValue(15)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(3,2)].icon()))
      self.button_dessert1[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert16(self):
      self.id_produit.setValue(16)
      self.btn_view.setIcon(QIcon(self.button_dessert1[(3,3)].icon()))
      self.button_dessert1[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert17(self):
      self.id_produit.setValue(17)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(0,0)].icon()))
      self.button_dessert2[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert18(self):
      self.id_produit.setValue(18)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(0,1)].icon()))
      self.button_dessert2[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert19(self):
      self.id_produit.setValue(19)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(0,2)].icon()))
      self.button_dessert2[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert20(self):
      self.id_produit.setValue(20)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(0,3)].icon()))
      self.button_dessert2[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert21(self):
      self.id_produit.setValue(21)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(1,0)].icon()))
      self.button_dessert2[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert22(self):
      self.id_produit.setValue(22)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(1,1)].icon()))
      self.button_dessert2[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert23(self):
      self.id_produit.setValue(23)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(1,2)].icon()))
      self.button_dessert2[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert24(self):
      self.id_produit.setValue(24)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(1,3)].icon()))
      self.button_dessert2[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert25(self):
      self.id_produit.setValue(25)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(2,0)].icon()))
      self.button_dessert2[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert26(self):
      self.id_produit.setValue(26)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(2,1)].icon()))
      self.button_dessert2[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert27(self):
      self.id_produit.setValue(27)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(2,2)].icon()))
      self.button_dessert2[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert28(self):
      self.id_produit.setValue(28)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(2,3)].icon()))
      self.button_dessert2[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert29(self):
      self.id_produit.setValue(29)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(3,0)].icon()))
      self.button_dessert2[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert30(self):
      self.id_produit.setValue(30)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(3,1)].icon()))
      self.button_dessert2[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert31(self):
      self.id_produit.setValue(31)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(3,2)].icon()))
      self.button_dessert2[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert32(self):
      self.id_produit.setValue(32)
      self.btn_view.setIcon(QIcon(self.button_dessert2[(3,3)].icon()))
      self.button_dessert2[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert33(self):
      self.id_produit.setValue(33)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(0,0)].icon()))
      self.button_dessert3[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert34(self):
      self.id_produit.setValue(34)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(0,1)].icon()))
      self.button_dessert3[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert35(self):
      self.id_produit.setValue(35)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(0,2)].icon()))
      self.button_dessert3[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert36(self):
      self.id_produit.setValue(36)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(0,3)].icon()))
      self.button_dessert3[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert37(self):
      self.id_produit.setValue(37)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(1,0)].icon()))
      self.button_dessert3[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert38(self):
      self.id_produit.setValue(38)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(1,1)].icon()))
      self.button_dessert3[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert39(self):
      self.id_produit.setValue(39)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(1,2)].icon()))
      self.button_dessert3[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert40(self):
      self.id_produit.setValue(40)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(1,3)].icon()))
      self.button_dessert3[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert41(self):
      self.id_produit.setValue(41)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(2,0)].icon()))
      self.button_dessert3[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert42(self):
      self.id_produit.setValue(42)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(2,1)].icon()))
      self.button_dessert3[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert43(self):
      self.id_produit.setValue(43)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(2,2)].icon()))
      self.button_dessert3[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert44(self):
      self.id_produit.setValue(44)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(2,3)].icon()))
      self.button_dessert3[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert45(self):
      self.id_produit.setValue(45)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(3,0)].icon()))
      self.button_dessert3[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert46(self):
      self.id_produit.setValue(46)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(3,1)].icon()))
      self.button_dessert3[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert47(self):
      self.id_produit.setValue(47)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(3,2)].icon()))
      self.button_dessert3[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert48(self):
      self.id_produit.setValue(48)
      self.btn_view.setIcon(QIcon(self.button_dessert3[(3,3)].icon()))
      self.button_dessert3[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert49(self):
      self.id_produit.setValue(49)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(0,0)].icon()))
      self.button_dessert4[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert50(self):
      self.id_produit.setValue(50)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(0,1)].icon()))
      self.button_dessert4[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert51(self):
      self.id_produit.setValue(51)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(0,2)].icon()))
      self.button_dessert4[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert52(self):
      self.id_produit.setValue(52)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(0,3)].icon()))
      self.button_dessert4[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert53(self):
      self.id_produit.setValue(53)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(1,0)].icon()))
      self.button_dessert4[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert54(self):
      self.id_produit.setValue(54)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(1,1)].icon()))
      self.button_dessert4[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert55(self):
      self.id_produit.setValue(55)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(1,2)].icon()))
      self.button_dessert4[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert56(self):
      self.id_produit.setValue(56)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(1,3)].icon()))
      self.button_dessert4[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert57(self):
      self.id_produit.setValue(57)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(2,0)].icon()))
      self.button_dessert4[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert58(self):
      self.id_produit.setValue(58)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(2,1)].icon()))
      self.button_dessert4[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert59(self):
      self.id_produit.setValue(59)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(2,2)].icon()))
      self.button_dessert4[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert60(self):
      self.id_produit.setValue(60)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(2,3)].icon()))
      self.button_dessert4[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert61(self):
      self.id_produit.setValue(61)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(3,0)].icon()))
      self.button_dessert4[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert62(self):
      self.id_produit.setValue(62)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(3,1)].icon()))
      self.button_dessert4[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert63(self):
      self.id_produit.setValue(63)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(3,2)].icon()))
      self.button_dessert4[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert64(self):
      self.id_produit.setValue(64)
      self.btn_view.setIcon(QIcon(self.button_dessert4[(3,3)].icon()))
      self.button_dessert4[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert65(self):
      self.id_produit.setValue(65)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(0,0)].icon()))
      self.button_dessert5[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert66(self):
      self.id_produit.setValue(66)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(0,1)].icon()))
      self.button_dessert5[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert67(self):
      self.id_produit.setValue(67)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(0,2)].icon()))
      self.button_dessert5[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert68(self):
      self.id_produit.setValue(68)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(0,3)].icon()))
      self.button_dessert5[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert69(self):
      self.id_produit.setValue(69)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(1,0)].icon()))
      self.button_dessert5[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert70(self):
      self.id_produit.setValue(70)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(1,1)].icon()))
      self.button_dessert5[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert71(self):
      self.id_produit.setValue(71)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(1,2)].icon()))
      self.button_dessert5[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert72(self):
      self.id_produit.setValue(72)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(1,3)].icon()))
      self.button_dessert5[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert73(self):
      self.id_produit.setValue(73)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(2,0)].icon()))
      self.button_dessert5[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert74(self):
      self.id_produit.setValue(74)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(2,1)].icon()))
      self.button_dessert5[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert75(self):
      self.id_produit.setValue(75)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(2,2)].icon()))
      self.button_dessert5[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert76(self):
      self.id_produit.setValue(76)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(2,3)].icon()))
      self.button_dessert5[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert77(self):
      self.id_produit.setValue(77)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(3,0)].icon()))
      self.button_dessert5[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert78(self):
      self.id_produit.setValue(78)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(3,1)].icon()))
      self.button_dessert5[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert79(self):
      self.id_produit.setValue(79)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(3,2)].icon()))
      self.button_dessert5[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert80(self):
      self.id_produit.setValue(80)
      self.btn_view.setIcon(QIcon(self.button_dessert5[(3,3)].icon()))
      self.button_dessert5[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert81(self):
      self.id_produit.setValue(81)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(0,0)].icon()))
      self.button_dessert6[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert82(self):
      self.id_produit.setValue(82)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(0,1)].icon()))
      self.button_dessert6[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert83(self):
      self.id_produit.setValue(83)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(0,2)].icon()))
      self.button_dessert6[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert84(self):
      self.id_produit.setValue(84)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(0,3)].icon()))
      self.button_dessert6[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert85(self):
      self.id_produit.setValue(85)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(1,0)].icon()))
      self.button_dessert6[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert86(self):
      self.id_produit.setValue(86)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(1,1)].icon()))
      self.button_dessert6[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert87(self):
      self.id_produit.setValue(87)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(1,2)].icon()))
      self.button_dessert6[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert88(self):
      self.id_produit.setValue(88)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(1,3)].icon()))
      self.button_dessert6[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert89(self):
      self.id_produit.setValue(89)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(2,0)].icon()))
      self.button_dessert6[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert90(self):
      self.id_produit.setValue(90)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(2,1)].icon()))
      self.button_dessert6[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert91(self):
      self.id_produit.setValue(91)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(2,2)].icon()))
      self.button_dessert6[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert92(self):
      self.id_produit.setValue(92)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(2,3)].icon()))
      self.button_dessert6[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert93(self):
      self.id_produit.setValue(93)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(3,0)].icon()))
      self.button_dessert6[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert94(self):
      self.id_produit.setValue(94)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(3,1)].icon()))
      self.button_dessert6[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert95(self):
      self.id_produit.setValue(95)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(3,2)].icon()))
      self.button_dessert6[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert96(self):
      self.id_produit.setValue(96)
      self.btn_view.setIcon(QIcon(self.button_dessert6[(3,3)].icon()))
      self.button_dessert6[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert97(self):
      self.id_produit.setValue(97)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(0,0)].icon()))
      self.button_dessert7[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert98(self):
      self.id_produit.setValue(98)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(0,1)].icon()))
      self.button_dessert7[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()     
   def selection_dessert99(self):
      self.id_produit.setValue(99)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(0,2)].icon()))
      self.button_dessert7[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert100(self):
      self.id_produit.setValue(100)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(0,3)].icon()))
      self.button_dessert7[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert101(self):
      self.id_produit.setValue(101)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(1,0)].icon()))
      self.button_dessert7[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert102(self):
      self.id_produit.setValue(102)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(1,1)].icon()))
      self.button_dessert7[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert103(self):
      self.id_produit.setValue(103)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(1,2)].icon()))
      self.button_dessert7[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert104(self):
      self.id_produit.setValue(104)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(1,3)].icon()))
      self.button_dessert7[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert105(self):
      self.id_produit.setValue(105)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(2,0)].icon()))
      self.button_dessert7[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert106(self):
      self.id_produit.setValue(106)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(2,1)].icon()))
      self.button_dessert7[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert107(self):
      self.id_produit.setValue(107)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(2,2)].icon()))
      self.button_dessert7[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert108(self):
      self.id_produit.setValue(108)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(2,3)].icon()))
      self.button_dessert7[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert109(self):
      self.id_produit.setValue(109)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(3,0)].icon()))
      self.button_dessert7[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert110(self):
      self.id_produit.setValue(110)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(3,1)].icon()))
      self.button_dessert7[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert111(self):
      self.id_produit.setValue(111)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(3,2)].icon()))
      self.button_dessert7[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert112(self):
      self.id_produit.setValue(112)
      self.btn_view.setIcon(QIcon(self.button_dessert7[(3,3)].icon()))
      self.button_dessert7[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert113(self):
      self.id_produit.setValue(113)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(0,0)].icon()))
      self.button_dessert8[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert114(self):
      self.id_produit.setValue(114)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(0,1)].icon()))
      self.button_dessert8[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert115(self):
      self.id_produit.setValue(115)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(0,2)].icon()))
      self.button_dessert8[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert116(self):
      self.id_produit.setValue(116)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(0,3)].icon()))
      self.button_dessert8[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert117(self):
      self.id_produit.setValue(117)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(1,0)].icon()))
      self.button_dessert8[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert118(self):
      self.id_produit.setValue(118)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(1,1)].icon()))
      self.button_dessert8[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert119(self):
      self.id_produit.setValue(119)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(1,2)].icon()))
      self.button_dessert8[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert120(self):
      self.id_produit.setValue(120)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(1,3)].icon()))
      self.button_dessert8[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert121(self):
      self.id_produit.setValue(121)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(2,0)].icon()))
      self.button_dessert8[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert122(self):
      self.id_produit.setValue(122)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(2,1)].icon()))
      self.button_dessert8[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert123(self):
      self.id_produit.setValue(123)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(2,2)].icon()))
      self.button_dessert8[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert124(self):
      self.id_produit.setValue(124)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(2,3)].icon()))
      self.button_dessert8[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert125(self):
      self.id_produit.setValue(125)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(3,0)].icon()))
      self.button_dessert8[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert126(self):
      self.id_produit.setValue(126)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(3,1)].icon()))
      self.button_dessert8[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert127(self):
      self.id_produit.setValue(127)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(3,2)].icon()))
      self.button_dessert8[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()
   def selection_dessert128(self):
      self.id_produit.setValue(128)
      self.btn_view.setIcon(QIcon(self.button_dessert8[(3,3)].icon()))
      self.button_dessert8[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_dessert()

   #====== SELECTION cafes                    
   def selection_cafe1(self):
      self.id_produit.setValue(1)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(0,0)].icon()))
      self.button_cafe1[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe2(self):
      self.id_produit.setValue(2)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(0,1)].icon()))
      self.button_cafe1[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe3(self):
      self.id_produit.setValue(3)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(0,2)].icon()))
      self.button_cafe1[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe4(self):
      self.id_produit.setValue(4)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(0,3)].icon()))
      self.button_cafe1[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe5(self):
      self.id_produit.setValue(5)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(1,0)].icon()))
      self.button_cafe1[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe6(self):
      self.id_produit.setValue(6)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(1,1)].icon()))
      self.button_cafe1[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe7(self):
      self.id_produit.setValue(7)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(1,2)].icon()))
      self.button_cafe1[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe8(self):
      self.id_produit.setValue(8)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(1,3)].icon()))
      self.button_cafe1[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe9(self):
      self.id_produit.setValue(9)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(2,0)].icon()))
      self.button_cafe1[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe10(self):
      self.id_produit.setValue(10)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(2,1)].icon()))
      self.button_cafe1[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe11(self):
      self.id_produit.setValue(11)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(2,2)].icon()))
      self.button_cafe1[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe12(self):
      self.id_produit.setValue(12)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(2,3)].icon()))
      self.button_cafe1[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe13(self):
      self.id_produit.setValue(13)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(3,0)].icon()))
      self.button_cafe1[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe14(self):
      self.id_produit.setValue(14)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(3,1)].icon()))
      self.button_cafe1[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe15(self):
      self.id_produit.setValue(15)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(3,2)].icon()))
      self.button_cafe1[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe16(self):
      self.id_produit.setValue(16)
      self.btn_view.setIcon(QIcon(self.button_cafe1[(3,3)].icon()))
      self.button_cafe1[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe17(self):
      self.id_produit.setValue(17)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(0,0)].icon()))
      self.button_cafe2[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe18(self):
      self.id_produit.setValue(18)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(0,1)].icon()))
      self.button_cafe2[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe19(self):
      self.id_produit.setValue(19)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(0,2)].icon()))
      self.button_cafe2[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe20(self):
      self.id_produit.setValue(20)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(0,3)].icon()))
      self.button_cafe2[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe21(self):
      self.id_produit.setValue(21)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(1,0)].icon()))
      self.button_cafe2[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe22(self):
      self.id_produit.setValue(22)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(1,1)].icon()))
      self.button_cafe2[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe23(self):
      self.id_produit.setValue(23)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(1,2)].icon()))
      self.button_cafe2[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe24(self):
      self.id_produit.setValue(24)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(1,3)].icon()))
      self.button_cafe2[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe25(self):
      self.id_produit.setValue(25)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(2,0)].icon()))
      self.button_cafe2[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe26(self):
      self.id_produit.setValue(26)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(2,1)].icon()))
      self.button_cafe2[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe27(self):
      self.id_produit.setValue(27)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(2,2)].icon()))
      self.button_cafe2[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe28(self):
      self.id_produit.setValue(28)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(2,3)].icon()))
      self.button_cafe2[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe29(self):
      self.id_produit.setValue(29)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(3,0)].icon()))
      self.button_cafe2[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe30(self):
      self.id_produit.setValue(30)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(3,1)].icon()))
      self.button_cafe2[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe31(self):
      self.id_produit.setValue(31)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(3,2)].icon()))
      self.button_cafe2[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe32(self):
      self.id_produit.setValue(32)
      self.btn_view.setIcon(QIcon(self.button_cafe2[(3,3)].icon()))
      self.button_cafe2[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe33(self):
      self.id_produit.setValue(33)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(0,0)].icon()))
      self.button_cafe3[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe34(self):
      self.id_produit.setValue(34)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(0,1)].icon()))
      self.button_cafe3[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe35(self):
      self.id_produit.setValue(35)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(0,2)].icon()))
      self.button_cafe3[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe36(self):
      self.id_produit.setValue(36)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(0,3)].icon()))
      self.button_cafe3[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe37(self):
      self.id_produit.setValue(37)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(1,0)].icon()))
      self.button_cafe3[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe38(self):
      self.id_produit.setValue(38)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(1,1)].icon()))
      self.button_cafe3[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe39(self):
      self.id_produit.setValue(39)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(1,2)].icon()))
      self.button_cafe3[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe40(self):
      self.id_produit.setValue(40)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(1,3)].icon()))
      self.button_cafe3[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe41(self):
      self.id_produit.setValue(41)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(2,0)].icon()))
      self.button_cafe3[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe42(self):
      self.id_produit.setValue(42)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(2,1)].icon()))
      self.button_cafe3[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe43(self):
      self.id_produit.setValue(43)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(2,2)].icon()))
      self.button_cafe3[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe44(self):
      self.id_produit.setValue(44)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(2,3)].icon()))
      self.button_cafe3[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe45(self):
      self.id_produit.setValue(45)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(3,0)].icon()))
      self.button_cafe3[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe46(self):
      self.id_produit.setValue(46)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(3,1)].icon()))
      self.button_cafe3[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe47(self):
      self.id_produit.setValue(47)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(3,2)].icon()))
      self.button_cafe3[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe48(self):
      self.id_produit.setValue(48)
      self.btn_view.setIcon(QIcon(self.button_cafe3[(3,3)].icon()))
      self.button_cafe3[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe49(self):
      self.id_produit.setValue(49)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(0,0)].icon()))
      self.button_cafe4[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe50(self):
      self.id_produit.setValue(50)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(0,1)].icon()))
      self.button_cafe4[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe51(self):
      self.id_produit.setValue(51)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(0,2)].icon()))
      self.button_cafe4[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe52(self):
      self.id_produit.setValue(52)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(0,3)].icon()))
      self.button_cafe4[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe53(self):
      self.id_produit.setValue(53)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(1,0)].icon()))
      self.button_cafe4[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe54(self):
      self.id_produit.setValue(54)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(1,1)].icon()))
      self.button_cafe4[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe55(self):
      self.id_produit.setValue(55)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(1,2)].icon()))
      self.button_cafe4[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe56(self):
      self.id_produit.setValue(56)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(1,3)].icon()))
      self.button_cafe4[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe57(self):
      self.id_produit.setValue(57)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(2,0)].icon()))
      self.button_cafe4[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe58(self):
      self.id_produit.setValue(58)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(2,1)].icon()))
      self.button_cafe4[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe59(self):
      self.id_produit.setValue(59)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(2,2)].icon()))
      self.button_cafe4[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe60(self):
      self.id_produit.setValue(60)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(2,3)].icon()))
      self.button_cafe4[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe61(self):
      self.id_produit.setValue(61)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(3,0)].icon()))
      self.button_cafe4[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe62(self):
      self.id_produit.setValue(62)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(3,1)].icon()))
      self.button_cafe4[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe63(self):
      self.id_produit.setValue(63)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(3,2)].icon()))
      self.button_cafe4[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe64(self):
      self.id_produit.setValue(64)
      self.btn_view.setIcon(QIcon(self.button_cafe4[(3,3)].icon()))
      self.button_cafe4[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe65(self):
      self.id_produit.setValue(65)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(0,0)].icon()))
      self.button_cafe5[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe66(self):
      self.id_produit.setValue(66)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(0,1)].icon()))
      self.button_cafe5[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe67(self):
      self.id_produit.setValue(67)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(0,2)].icon()))
      self.button_cafe5[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe68(self):
      self.id_produit.setValue(68)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(0,3)].icon()))
      self.button_cafe5[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe69(self):
      self.id_produit.setValue(69)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(1,0)].icon()))
      self.button_cafe5[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe70(self):
      self.id_produit.setValue(70)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(1,1)].icon()))
      self.button_cafe5[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe71(self):
      self.id_produit.setValue(71)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(1,2)].icon()))
      self.button_cafe5[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe72(self):
      self.id_produit.setValue(72)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(1,3)].icon()))
      self.button_cafe5[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe73(self):
      self.id_produit.setValue(73)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(2,0)].icon()))
      self.button_cafe5[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe74(self):
      self.id_produit.setValue(74)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(2,1)].icon()))
      self.button_cafe5[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe75(self):
      self.id_produit.setValue(75)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(2,2)].icon()))
      self.button_cafe5[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe76(self):
      self.id_produit.setValue(76)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(2,3)].icon()))
      self.button_cafe5[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe77(self):
      self.id_produit.setValue(77)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(3,0)].icon()))
      self.button_cafe5[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe78(self):
      self.id_produit.setValue(78)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(3,1)].icon()))
      self.button_cafe5[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe79(self):
      self.id_produit.setValue(79)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(3,2)].icon()))
      self.button_cafe5[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe80(self):
      self.id_produit.setValue(80)
      self.btn_view.setIcon(QIcon(self.button_cafe5[(3,3)].icon()))
      self.button_cafe5[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe81(self):
      self.id_produit.setValue(81)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(0,0)].icon()))
      self.button_cafe6[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe82(self):
      self.id_produit.setValue(82)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(0,1)].icon()))
      self.button_cafe6[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe83(self):
      self.id_produit.setValue(83)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(0,2)].icon()))
      self.button_cafe6[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe84(self):
      self.id_produit.setValue(84)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(0,3)].icon()))
      self.button_cafe6[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe85(self):
      self.id_produit.setValue(85)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(1,0)].icon()))
      self.button_cafe6[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe86(self):
      self.id_produit.setValue(86)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(1,1)].icon()))
      self.button_cafe6[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe87(self):
      self.id_produit.setValue(87)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(1,2)].icon()))
      self.button_cafe6[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe88(self):
      self.id_produit.setValue(88)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(1,3)].icon()))
      self.button_cafe6[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe89(self):
      self.id_produit.setValue(89)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(2,0)].icon()))
      self.button_cafe6[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe90(self):
      self.id_produit.setValue(90)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(2,1)].icon()))
      self.button_cafe6[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe91(self):
      self.id_produit.setValue(91)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(2,2)].icon()))
      self.button_cafe6[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe92(self):
      self.id_produit.setValue(92)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(2,3)].icon()))
      self.button_cafe6[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe93(self):
      self.id_produit.setValue(93)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(3,0)].icon()))
      self.button_cafe6[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe94(self):
      self.id_produit.setValue(94)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(3,1)].icon()))
      self.button_cafe6[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe95(self):
      self.id_produit.setValue(95)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(3,2)].icon()))
      self.button_cafe6[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe96(self):
      self.id_produit.setValue(96)
      self.btn_view.setIcon(QIcon(self.button_cafe6[(3,3)].icon()))
      self.button_cafe6[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe97(self):
      self.id_produit.setValue(97)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(0,0)].icon()))
      self.button_cafe7[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe98(self):
      self.id_produit.setValue(98)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(0,1)].icon()))
      self.button_cafe7[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()     
   def selection_cafe99(self):
      self.id_produit.setValue(99)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(0,2)].icon()))
      self.button_cafe7[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe100(self):
      self.id_produit.setValue(100)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(0,3)].icon()))
      self.button_cafe7[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe101(self):
      self.id_produit.setValue(101)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(1,0)].icon()))
      self.button_cafe7[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe102(self):
      self.id_produit.setValue(102)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(1,1)].icon()))
      self.button_cafe7[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe103(self):
      self.id_produit.setValue(103)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(1,2)].icon()))
      self.button_cafe7[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe104(self):
      self.id_produit.setValue(104)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(1,3)].icon()))
      self.button_cafe7[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe105(self):
      self.id_produit.setValue(105)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(2,0)].icon()))
      self.button_cafe7[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe106(self):
      self.id_produit.setValue(106)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(2,1)].icon()))
      self.button_cafe7[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe107(self):
      self.id_produit.setValue(107)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(2,2)].icon()))
      self.button_cafe7[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe108(self):
      self.id_produit.setValue(108)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(2,3)].icon()))
      self.button_cafe7[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe109(self):
      self.id_produit.setValue(109)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(3,0)].icon()))
      self.button_cafe7[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe110(self):
      self.id_produit.setValue(110)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(3,1)].icon()))
      self.button_cafe7[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe111(self):
      self.id_produit.setValue(111)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(3,2)].icon()))
      self.button_cafe7[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe112(self):
      self.id_produit.setValue(112)
      self.btn_view.setIcon(QIcon(self.button_cafe7[(3,3)].icon()))
      self.button_cafe7[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe113(self):
      self.id_produit.setValue(113)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(0,0)].icon()))
      self.button_cafe8[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe114(self):
      self.id_produit.setValue(114)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(0,1)].icon()))
      self.button_cafe8[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe115(self):
      self.id_produit.setValue(115)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(0,2)].icon()))
      self.button_cafe8[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe116(self):
      self.id_produit.setValue(116)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(0,3)].icon()))
      self.button_cafe8[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe117(self):
      self.id_produit.setValue(117)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(1,0)].icon()))
      self.button_cafe8[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe118(self):
      self.id_produit.setValue(118)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(1,1)].icon()))
      self.button_cafe8[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe119(self):
      self.id_produit.setValue(119)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(1,2)].icon()))
      self.button_cafe8[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe120(self):
      self.id_produit.setValue(120)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(1,3)].icon()))
      self.button_cafe8[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe121(self):
      self.id_produit.setValue(121)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(2,0)].icon()))
      self.button_cafe8[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe122(self):
      self.id_produit.setValue(122)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(2,1)].icon()))
      self.button_cafe8[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe123(self):
      self.id_produit.setValue(123)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(2,2)].icon()))
      self.button_cafe8[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe124(self):
      self.id_produit.setValue(124)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(2,3)].icon()))
      self.button_cafe8[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe125(self):
      self.id_produit.setValue(125)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(3,0)].icon()))
      self.button_cafe8[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe126(self):
      self.id_produit.setValue(126)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(3,1)].icon()))
      self.button_cafe8[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe127(self):
      self.id_produit.setValue(127)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(3,2)].icon()))
      self.button_cafe8[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()
   def selection_cafe128(self):
      self.id_produit.setValue(128)
      self.btn_view.setIcon(QIcon(self.button_cafe8[(3,3)].icon()))
      self.button_cafe8[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_cafe()

   #====== SELECTION plats                    
   def selection_plat1(self):
      self.id_produit.setValue(1)
      self.btn_view.setIcon(QIcon(self.button_plat1[(0,0)].icon()))
      self.button_plat1[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat2(self):
      self.id_produit.setValue(2)
      self.btn_view.setIcon(QIcon(self.button_plat1[(0,1)].icon()))
      self.button_plat1[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat3(self):
      self.id_produit.setValue(3)
      self.btn_view.setIcon(QIcon(self.button_plat1[(0,2)].icon()))
      self.button_plat1[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat4(self):
      self.id_produit.setValue(4)
      self.btn_view.setIcon(QIcon(self.button_plat1[(0,3)].icon()))
      self.button_plat1[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat5(self):
      self.id_produit.setValue(5)
      self.btn_view.setIcon(QIcon(self.button_plat1[(1,0)].icon()))
      self.button_plat1[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat6(self):
      self.id_produit.setValue(6)
      self.btn_view.setIcon(QIcon(self.button_plat1[(1,1)].icon()))
      self.button_plat1[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat7(self):
      self.id_produit.setValue(7)
      self.btn_view.setIcon(QIcon(self.button_plat1[(1,2)].icon()))
      self.button_plat1[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat8(self):
      self.id_produit.setValue(8)
      self.btn_view.setIcon(QIcon(self.button_plat1[(1,3)].icon()))
      self.button_plat1[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat9(self):
      self.id_produit.setValue(9)
      self.btn_view.setIcon(QIcon(self.button_plat1[(2,0)].icon()))
      self.button_plat1[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat10(self):
      self.id_produit.setValue(10)
      self.btn_view.setIcon(QIcon(self.button_plat1[(2,1)].icon()))
      self.button_plat1[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat11(self):
      self.id_produit.setValue(11)
      self.btn_view.setIcon(QIcon(self.button_plat1[(2,2)].icon()))
      self.button_plat1[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat12(self):
      self.id_produit.setValue(12)
      self.btn_view.setIcon(QIcon(self.button_plat1[(2,3)].icon()))
      self.button_plat1[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat13(self):
      self.id_produit.setValue(13)
      self.btn_view.setIcon(QIcon(self.button_plat1[(3,0)].icon()))
      self.button_plat1[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat14(self):
      self.id_produit.setValue(14)
      self.btn_view.setIcon(QIcon(self.button_plat1[(3,1)].icon()))
      self.button_plat1[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat15(self):
      self.id_produit.setValue(15)
      self.btn_view.setIcon(QIcon(self.button_plat1[(3,2)].icon()))
      self.button_plat1[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat16(self):
      self.id_produit.setValue(16)
      self.btn_view.setIcon(QIcon(self.button_plat1[(3,3)].icon()))
      self.button_plat1[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat17(self):
      self.id_produit.setValue(17)
      self.btn_view.setIcon(QIcon(self.button_plat2[(0,0)].icon()))
      self.button_plat2[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat18(self):
      self.id_produit.setValue(18)
      self.btn_view.setIcon(QIcon(self.button_plat2[(0,1)].icon()))
      self.button_plat2[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat19(self):
      self.id_produit.setValue(19)
      self.btn_view.setIcon(QIcon(self.button_plat2[(0,2)].icon()))
      self.button_plat2[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat20(self):
      self.id_produit.setValue(20)
      self.btn_view.setIcon(QIcon(self.button_plat2[(0,3)].icon()))
      self.button_plat2[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat21(self):
      self.id_produit.setValue(21)
      self.btn_view.setIcon(QIcon(self.button_plat2[(1,0)].icon()))
      self.button_plat2[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat22(self):
      self.id_produit.setValue(22)
      self.btn_view.setIcon(QIcon(self.button_plat2[(1,1)].icon()))
      self.button_plat2[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat23(self):
      self.id_produit.setValue(23)
      self.btn_view.setIcon(QIcon(self.button_plat2[(1,2)].icon()))
      self.button_plat2[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat24(self):
      self.id_produit.setValue(24)
      self.btn_view.setIcon(QIcon(self.button_plat2[(1,3)].icon()))
      self.button_plat2[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat25(self):
      self.id_produit.setValue(25)
      self.btn_view.setIcon(QIcon(self.button_plat2[(2,0)].icon()))
      self.button_plat2[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat26(self):
      self.id_produit.setValue(26)
      self.btn_view.setIcon(QIcon(self.button_plat2[(2,1)].icon()))
      self.button_plat2[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat27(self):
      self.id_produit.setValue(27)
      self.btn_view.setIcon(QIcon(self.button_plat2[(2,2)].icon()))
      self.button_plat2[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat28(self):
      self.id_produit.setValue(28)
      self.btn_view.setIcon(QIcon(self.button_plat2[(2,3)].icon()))
      self.button_plat2[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat29(self):
      self.id_produit.setValue(29)
      self.btn_view.setIcon(QIcon(self.button_plat2[(3,0)].icon()))
      self.button_plat2[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat30(self):
      self.id_produit.setValue(30)
      self.btn_view.setIcon(QIcon(self.button_plat2[(3,1)].icon()))
      self.button_plat2[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat31(self):
      self.id_produit.setValue(31)
      self.btn_view.setIcon(QIcon(self.button_plat2[(3,2)].icon()))
      self.button_plat2[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat32(self):
      self.id_produit.setValue(32)
      self.btn_view.setIcon(QIcon(self.button_plat2[(3,3)].icon()))
      self.button_plat2[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat33(self):
      self.id_produit.setValue(33)
      self.btn_view.setIcon(QIcon(self.button_plat3[(0,0)].icon()))
      self.button_plat3[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat34(self):
      self.id_produit.setValue(34)
      self.btn_view.setIcon(QIcon(self.button_plat3[(0,1)].icon()))
      self.button_plat3[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat35(self):
      self.id_produit.setValue(35)
      self.btn_view.setIcon(QIcon(self.button_plat3[(0,2)].icon()))
      self.button_plat3[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat36(self):
      self.id_produit.setValue(36)
      self.btn_view.setIcon(QIcon(self.button_plat3[(0,3)].icon()))
      self.button_plat3[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat37(self):
      self.id_produit.setValue(37)
      self.btn_view.setIcon(QIcon(self.button_plat3[(1,0)].icon()))
      self.button_plat3[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat38(self):
      self.id_produit.setValue(38)
      self.btn_view.setIcon(QIcon(self.button_plat3[(1,1)].icon()))
      self.button_plat3[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat39(self):
      self.id_produit.setValue(39)
      self.btn_view.setIcon(QIcon(self.button_plat3[(1,2)].icon()))
      self.button_plat3[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat40(self):
      self.id_produit.setValue(40)
      self.btn_view.setIcon(QIcon(self.button_plat3[(1,3)].icon()))
      self.button_plat3[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat41(self):
      self.id_produit.setValue(41)
      self.btn_view.setIcon(QIcon(self.button_plat3[(2,0)].icon()))
      self.button_plat3[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat42(self):
      self.id_produit.setValue(42)
      self.btn_view.setIcon(QIcon(self.button_plat3[(2,1)].icon()))
      self.button_plat3[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat43(self):
      self.id_produit.setValue(43)
      self.btn_view.setIcon(QIcon(self.button_plat3[(2,2)].icon()))
      self.button_plat3[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat44(self):
      self.id_produit.setValue(44)
      self.btn_view.setIcon(QIcon(self.button_plat3[(2,3)].icon()))
      self.button_plat3[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat45(self):
      self.id_produit.setValue(45)
      self.btn_view.setIcon(QIcon(self.button_plat3[(3,0)].icon()))
      self.button_plat3[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat46(self):
      self.id_produit.setValue(46)
      self.btn_view.setIcon(QIcon(self.button_plat3[(3,1)].icon()))
      self.button_plat3[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat47(self):
      self.id_produit.setValue(47)
      self.btn_view.setIcon(QIcon(self.button_plat3[(3,2)].icon()))
      self.button_plat3[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat48(self):
      self.id_produit.setValue(48)
      self.btn_view.setIcon(QIcon(self.button_plat3[(3,3)].icon()))
      self.button_plat3[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat49(self):
      self.id_produit.setValue(49)
      self.btn_view.setIcon(QIcon(self.button_plat4[(0,0)].icon()))
      self.button_plat4[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat50(self):
      self.id_produit.setValue(50)
      self.btn_view.setIcon(QIcon(self.button_plat4[(0,1)].icon()))
      self.button_plat4[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat51(self):
      self.id_produit.setValue(51)
      self.btn_view.setIcon(QIcon(self.button_plat4[(0,2)].icon()))
      self.button_plat4[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat52(self):
      self.id_produit.setValue(52)
      self.btn_view.setIcon(QIcon(self.button_plat4[(0,3)].icon()))
      self.button_plat4[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat53(self):
      self.id_produit.setValue(53)
      self.btn_view.setIcon(QIcon(self.button_plat4[(1,0)].icon()))
      self.button_plat4[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat54(self):
      self.id_produit.setValue(54)
      self.btn_view.setIcon(QIcon(self.button_plat4[(1,1)].icon()))
      self.button_plat4[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat55(self):
      self.id_produit.setValue(55)
      self.btn_view.setIcon(QIcon(self.button_plat4[(1,2)].icon()))
      self.button_plat4[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat56(self):
      self.id_produit.setValue(56)
      self.btn_view.setIcon(QIcon(self.button_plat4[(1,3)].icon()))
      self.button_plat4[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat57(self):
      self.id_produit.setValue(57)
      self.btn_view.setIcon(QIcon(self.button_plat4[(2,0)].icon()))
      self.button_plat4[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat58(self):
      self.id_produit.setValue(58)
      self.btn_view.setIcon(QIcon(self.button_plat4[(2,1)].icon()))
      self.button_plat4[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat59(self):
      self.id_produit.setValue(59)
      self.btn_view.setIcon(QIcon(self.button_plat4[(2,2)].icon()))
      self.button_plat4[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat60(self):
      self.id_produit.setValue(60)
      self.btn_view.setIcon(QIcon(self.button_plat4[(2,3)].icon()))
      self.button_plat4[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat61(self):
      self.id_produit.setValue(61)
      self.btn_view.setIcon(QIcon(self.button_plat4[(3,0)].icon()))
      self.button_plat4[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat62(self):
      self.id_produit.setValue(62)
      self.btn_view.setIcon(QIcon(self.button_plat4[(3,1)].icon()))
      self.button_plat4[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat63(self):
      self.id_produit.setValue(63)
      self.btn_view.setIcon(QIcon(self.button_plat4[(3,2)].icon()))
      self.button_plat4[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat64(self):
      self.id_produit.setValue(64)
      self.btn_view.setIcon(QIcon(self.button_plat4[(3,3)].icon()))
      self.button_plat4[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat65(self):
      self.id_produit.setValue(65)
      self.btn_view.setIcon(QIcon(self.button_plat5[(0,0)].icon()))
      self.button_plat5[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat66(self):
      self.id_produit.setValue(66)
      self.btn_view.setIcon(QIcon(self.button_plat5[(0,1)].icon()))
      self.button_plat5[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat67(self):
      self.id_produit.setValue(67)
      self.btn_view.setIcon(QIcon(self.button_plat5[(0,2)].icon()))
      self.button_plat5[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat68(self):
      self.id_produit.setValue(68)
      self.btn_view.setIcon(QIcon(self.button_plat5[(0,3)].icon()))
      self.button_plat5[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat69(self):
      self.id_produit.setValue(69)
      self.btn_view.setIcon(QIcon(self.button_plat5[(1,0)].icon()))
      self.button_plat5[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat70(self):
      self.id_produit.setValue(70)
      self.btn_view.setIcon(QIcon(self.button_plat5[(1,1)].icon()))
      self.button_plat5[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat71(self):
      self.id_produit.setValue(71)
      self.btn_view.setIcon(QIcon(self.button_plat5[(1,2)].icon()))
      self.button_plat5[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat72(self):
      self.id_produit.setValue(72)
      self.btn_view.setIcon(QIcon(self.button_plat5[(1,3)].icon()))
      self.button_plat5[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat73(self):
      self.id_produit.setValue(73)
      self.btn_view.setIcon(QIcon(self.button_plat5[(2,0)].icon()))
      self.button_plat5[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat74(self):
      self.id_produit.setValue(74)
      self.btn_view.setIcon(QIcon(self.button_plat5[(2,1)].icon()))
      self.button_plat5[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat75(self):
      self.id_produit.setValue(75)
      self.btn_view.setIcon(QIcon(self.button_plat5[(2,2)].icon()))
      self.button_plat5[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat76(self):
      self.id_produit.setValue(76)
      self.btn_view.setIcon(QIcon(self.button_plat5[(2,3)].icon()))
      self.button_plat5[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat77(self):
      self.id_produit.setValue(77)
      self.btn_view.setIcon(QIcon(self.button_plat5[(3,0)].icon()))
      self.button_plat5[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat78(self):
      self.id_produit.setValue(78)
      self.btn_view.setIcon(QIcon(self.button_plat5[(3,1)].icon()))
      self.button_plat5[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat79(self):
      self.id_produit.setValue(79)
      self.btn_view.setIcon(QIcon(self.button_plat5[(3,2)].icon()))
      self.button_plat5[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat80(self):
      self.id_produit.setValue(80)
      self.btn_view.setIcon(QIcon(self.button_plat5[(3,3)].icon()))
      self.button_plat5[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat81(self):
      self.id_produit.setValue(81)
      self.btn_view.setIcon(QIcon(self.button_plat6[(0,0)].icon()))
      self.button_plat6[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat82(self):
      self.id_produit.setValue(82)
      self.btn_view.setIcon(QIcon(self.button_plat6[(0,1)].icon()))
      self.button_plat6[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat83(self):
      self.id_produit.setValue(83)
      self.btn_view.setIcon(QIcon(self.button_plat6[(0,2)].icon()))
      self.button_plat6[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat84(self):
      self.id_produit.setValue(84)
      self.btn_view.setIcon(QIcon(self.button_plat6[(0,3)].icon()))
      self.button_plat6[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat85(self):
      self.id_produit.setValue(85)
      self.btn_view.setIcon(QIcon(self.button_plat6[(1,0)].icon()))
      self.button_plat6[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat86(self):
      self.id_produit.setValue(86)
      self.btn_view.setIcon(QIcon(self.button_plat6[(1,1)].icon()))
      self.button_plat6[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat87(self):
      self.id_produit.setValue(87)
      self.btn_view.setIcon(QIcon(self.button_plat6[(1,2)].icon()))
      self.button_plat6[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat88(self):
      self.id_produit.setValue(88)
      self.btn_view.setIcon(QIcon(self.button_plat6[(1,3)].icon()))
      self.button_plat6[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat89(self):
      self.id_produit.setValue(89)
      self.btn_view.setIcon(QIcon(self.button_plat6[(2,0)].icon()))
      self.button_plat6[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat90(self):
      self.id_produit.setValue(90)
      self.btn_view.setIcon(QIcon(self.button_plat6[(2,1)].icon()))
      self.button_plat6[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat91(self):
      self.id_produit.setValue(91)
      self.btn_view.setIcon(QIcon(self.button_plat6[(2,2)].icon()))
      self.button_plat6[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat92(self):
      self.id_produit.setValue(92)
      self.btn_view.setIcon(QIcon(self.button_plat6[(2,3)].icon()))
      self.button_plat6[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat93(self):
      self.id_produit.setValue(93)
      self.btn_view.setIcon(QIcon(self.button_plat6[(3,0)].icon()))
      self.button_plat6[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat94(self):
      self.id_produit.setValue(94)
      self.btn_view.setIcon(QIcon(self.button_plat6[(3,1)].icon()))
      self.button_plat6[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat95(self):
      self.id_produit.setValue(95)
      self.btn_view.setIcon(QIcon(self.button_plat6[(3,2)].icon()))
      self.button_plat6[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat96(self):
      self.id_produit.setValue(96)
      self.btn_view.setIcon(QIcon(self.button_plat6[(3,3)].icon()))
      self.button_plat6[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat97(self):
      self.id_produit.setValue(97)
      self.btn_view.setIcon(QIcon(self.button_plat7[(0,0)].icon()))
      self.button_plat7[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat98(self):
      self.id_produit.setValue(98)
      self.btn_view.setIcon(QIcon(self.button_plat7[(0,1)].icon()))
      self.button_plat7[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()     
   def selection_plat99(self):
      self.id_produit.setValue(99)
      self.btn_view.setIcon(QIcon(self.button_plat7[(0,2)].icon()))
      self.button_plat7[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat100(self):
      self.id_produit.setValue(100)
      self.btn_view.setIcon(QIcon(self.button_plat7[(0,3)].icon()))
      self.button_plat7[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat101(self):
      self.id_produit.setValue(101)
      self.btn_view.setIcon(QIcon(self.button_plat7[(1,0)].icon()))
      self.button_plat7[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat102(self):
      self.id_produit.setValue(102)
      self.btn_view.setIcon(QIcon(self.button_plat7[(1,1)].icon()))
      self.button_plat7[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat103(self):
      self.id_produit.setValue(103)
      self.btn_view.setIcon(QIcon(self.button_plat7[(1,2)].icon()))
      self.button_plat7[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat104(self):
      self.id_produit.setValue(104)
      self.btn_view.setIcon(QIcon(self.button_plat7[(1,3)].icon()))
      self.button_plat7[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat105(self):
      self.id_produit.setValue(105)
      self.btn_view.setIcon(QIcon(self.button_plat7[(2,0)].icon()))
      self.button_plat7[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat106(self):
      self.id_produit.setValue(106)
      self.btn_view.setIcon(QIcon(self.button_plat7[(2,1)].icon()))
      self.button_plat7[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat107(self):
      self.id_produit.setValue(107)
      self.btn_view.setIcon(QIcon(self.button_plat7[(2,2)].icon()))
      self.button_plat7[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat108(self):
      self.id_produit.setValue(108)
      self.btn_view.setIcon(QIcon(self.button_plat7[(2,3)].icon()))
      self.button_plat7[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat109(self):
      self.id_produit.setValue(109)
      self.btn_view.setIcon(QIcon(self.button_plat7[(3,0)].icon()))
      self.button_plat7[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat110(self):
      self.id_produit.setValue(110)
      self.btn_view.setIcon(QIcon(self.button_plat7[(3,1)].icon()))
      self.button_plat7[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat111(self):
      self.id_produit.setValue(111)
      self.btn_view.setIcon(QIcon(self.button_plat7[(3,2)].icon()))
      self.button_plat7[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat112(self):
      self.id_produit.setValue(112)
      self.btn_view.setIcon(QIcon(self.button_plat7[(3,3)].icon()))
      self.button_plat7[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat113(self):
      self.id_produit.setValue(113)
      self.btn_view.setIcon(QIcon(self.button_plat8[(0,0)].icon()))
      self.button_plat8[(0,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat114(self):
      self.id_produit.setValue(114)
      self.btn_view.setIcon(QIcon(self.button_plat8[(0,1)].icon()))
      self.button_plat8[(0,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat115(self):
      self.id_produit.setValue(115)
      self.btn_view.setIcon(QIcon(self.button_plat8[(0,2)].icon()))
      self.button_plat8[(0,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat116(self):
      self.id_produit.setValue(116)
      self.btn_view.setIcon(QIcon(self.button_plat8[(0,3)].icon()))
      self.button_plat8[(0,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat117(self):
      self.id_produit.setValue(117)
      self.btn_view.setIcon(QIcon(self.button_plat8[(1,0)].icon()))
      self.button_plat8[(1,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat118(self):
      self.id_produit.setValue(118)
      self.btn_view.setIcon(QIcon(self.button_plat8[(1,1)].icon()))
      self.button_plat8[(1,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat119(self):
      self.id_produit.setValue(119)
      self.btn_view.setIcon(QIcon(self.button_plat8[(1,2)].icon()))
      self.button_plat8[(1,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat120(self):
      self.id_produit.setValue(120)
      self.btn_view.setIcon(QIcon(self.button_plat8[(1,3)].icon()))
      self.button_plat8[(1,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat121(self):
      self.id_produit.setValue(121)
      self.btn_view.setIcon(QIcon(self.button_plat8[(2,0)].icon()))
      self.button_plat8[(2,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat122(self):
      self.id_produit.setValue(122)
      self.btn_view.setIcon(QIcon(self.button_plat8[(2,1)].icon()))
      self.button_plat8[(2,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat123(self):
      self.id_produit.setValue(123)
      self.btn_view.setIcon(QIcon(self.button_plat8[(2,2)].icon()))
      self.button_plat8[(2,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat124(self):
      self.id_produit.setValue(124)
      self.btn_view.setIcon(QIcon(self.button_plat8[(2,3)].icon()))
      self.button_plat8[(2,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat125(self):
      self.id_produit.setValue(125)
      self.btn_view.setIcon(QIcon(self.button_plat8[(3,0)].icon()))
      self.button_plat8[(3,0)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat126(self):
      self.id_produit.setValue(126)
      self.btn_view.setIcon(QIcon(self.button_plat8[(3,1)].icon()))
      self.button_plat8[(3,1)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat127(self):
      self.id_produit.setValue(127)
      self.btn_view.setIcon(QIcon(self.button_plat8[(3,2)].icon()))
      self.button_plat8[(3,2)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   def selection_plat128(self):
      self.id_produit.setValue(128)
      self.btn_view.setIcon(QIcon(self.button_plat8[(3,3)].icon()))
      self.button_plat8[(3,3)].setFocus()
      self.btn_view_frame.show()
      self.information_plat()
   
   def refresh_boisson(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.cursor.execute("""SELECT COUNT(*) FROM boissons """)
               self._result=self.cursor.fetchone()
               self._row=int(self._result[0])
               
               self.list_boisson_size=self.list_boisson.count()-(self.list_boisson.count()-self._row)
               
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
               #________PAGE 2
               self.b17=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=17")               
               for row in self.b17:
                  self.button_boisson2[(0,0)].setText(str(row[0]))
                  self.lab_boisson2[(0,0)].setText(str(row[1]))
                  self.button_boisson2[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b18=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=18")               
               for row in self.b18:
                  self.button_boisson2[(0,1)].setText(str(row[0]))
                  self.lab_boisson2[(0,1)].setText(str(row[1]))
                  self.button_boisson2[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b19=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=19")               
               for row in self.b19:
                  self.button_boisson2[(0,2)].setText(str(row[0]))
                  self.lab_boisson2[(0,2)].setText(str(row[1]))
                  self.button_boisson2[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b20=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=20")               
               for row in self.b20:
                  self.button_boisson2[(0,3)].setText(str(row[0]))
                  self.lab_boisson2[(0,3)].setText(str(row[1]))
                  self.button_boisson2[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b21=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=21")               
               for row in self.b21:
                  self.button_boisson2[(1,0)].setText(str(row[0]))
                  self.lab_boisson2[(1,0)].setText(str(row[1]))
                  self.button_boisson2[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b22=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=22")               
               for row in self.b22:
                  self.button_boisson2[(1,1)].setText(str(row[0]))
                  self.lab_boisson2[(1,1)].setText(str(row[1]))
                  self.button_boisson2[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b23=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=23")               
               for row in self.b23:
                  self.button_boisson2[(1,2)].setText(str(row[0]))
                  self.lab_boisson2[(1,2)].setText(str(row[1]))
                  self.button_boisson2[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b24=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=24")               
               for row in self.b24:
                  self.button_boisson2[(1,3)].setText(str(row[0]))
                  self.lab_boisson2[(1,3)].setText(str(row[1]))
                  self.button_boisson2[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b25=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=25")               
               for row in self.b25:
                  self.button_boisson2[(2,0)].setText(str(row[0]))
                  self.lab_boisson2[(2,0)].setText(str(row[1]))
                  self.button_boisson2[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b26=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=26")               
               for row in self.b26:
                  self.button_boisson2[(2,1)].setText(str(row[0]))
                  self.lab_boisson2[(2,1)].setText(str(row[1]))
                  self.button_boisson2[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b27=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=27")               
               for row in self.b27:
                  self.button_boisson2[(2,2)].setText(str(row[0]))
                  self.lab_boisson2[(2,2)].setText(str(row[1]))
                  self.button_boisson2[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b28=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=28")               
               for row in self.b28:
                  self.button_boisson2[(2,3)].setText(str(row[0]))
                  self.lab_boisson2[(2,3)].setText(str(row[1]))
                  self.button_boisson2[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b29=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=29")               
               for row in self.b29:
                  self.button_boisson2[(3,0)].setText(str(row[0]))
                  self.lab_boisson2[(3,0)].setText(str(row[1]))
                  self.button_boisson2[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b30=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=30")               
               for row in self.b30:
                  self.button_boisson2[(3,1)].setText(str(row[0]))
                  self.lab_boisson2[(3,1)].setText(str(row[1]))
                  self.button_boisson2[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b31=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=31")               
               for row in self.b31:
                  self.button_boisson2[(3,2)].setText(str(row[0]))
                  self.lab_boisson2[(3,2)].setText(str(row[1]))
                  self.button_boisson2[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b32=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=32")               
               for row in self.b32:
                  self.button_boisson2[(3,3)].setText(str(row[0]))
                  self.lab_boisson2[(3,3)].setText(str(row[1]))
                  self.button_boisson2[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson2[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 3
               self.b33=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=33")               
               for row in self.b33:
                  self.button_boisson3[(0,0)].setText(str(row[0]))
                  self.lab_boisson3[(0,0)].setText(str(row[1]))
                  self.button_boisson3[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b34=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=34")               
               for row in self.b34:
                  self.button_boisson3[(0,1)].setText(str(row[0]))
                  self.lab_boisson3[(0,1)].setText(str(row[1]))
                  self.button_boisson3[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b35=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=35")               
               for row in self.b35:
                  self.button_boisson3[(0,2)].setText(str(row[0]))
                  self.lab_boisson3[(0,2)].setText(str(row[1]))
                  self.button_boisson3[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b36=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=36")               
               for row in self.b36:
                  self.button_boisson3[(0,3)].setText(str(row[0]))
                  self.lab_boisson3[(0,3)].setText(str(row[1]))
                  self.button_boisson3[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b37=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=37")               
               for row in self.b37:
                  self.button_boisson3[(1,0)].setText(str(row[0]))
                  self.lab_boisson3[(1,0)].setText(str(row[1]))
                  self.button_boisson3[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b38=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=38")               
               for row in self.b38:
                  self.button_boisson3[(1,1)].setText(str(row[0]))
                  self.lab_boisson3[(1,1)].setText(str(row[1]))
                  self.button_boisson3[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b39=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=39")               
               for row in self.b39:
                  self.button_boisson3[(1,2)].setText(str(row[0]))
                  self.lab_boisson3[(1,2)].setText(str(row[1]))
                  self.button_boisson3[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b40=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=40")               
               for row in self.b40:
                  self.button_boisson3[(1,3)].setText(str(row[0]))
                  self.lab_boisson3[(1,3)].setText(str(row[1]))
                  self.button_boisson3[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b41=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=41")               
               for row in self.b41:
                  self.button_boisson3[(2,0)].setText(str(row[0]))
                  self.lab_boisson3[(2,0)].setText(str(row[1]))
                  self.button_boisson3[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b42=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=42")               
               for row in self.b42:
                  self.button_boisson3[(2,1)].setText(str(row[0]))
                  self.lab_boisson3[(2,1)].setText(str(row[1]))
                  self.button_boisson3[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b43=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=43")               
               for row in self.b43:
                  self.button_boisson3[(2,2)].setText(str(row[0]))
                  self.lab_boisson3[(2,2)].setText(str(row[1]))
                  self.button_boisson3[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b44=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=44")               
               for row in self.b44:
                  self.button_boisson3[(2,3)].setText(str(row[0]))
                  self.lab_boisson3[(2,3)].setText(str(row[1]))
                  self.button_boisson3[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b45=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=45")               
               for row in self.b45:
                  self.button_boisson3[(3,0)].setText(str(row[0]))
                  self.lab_boisson3[(3,0)].setText(str(row[1]))
                  self.button_boisson3[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b46=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=46")               
               for row in self.b46:
                  self.button_boisson3[(3,1)].setText(str(row[0]))
                  self.lab_boisson3[(3,1)].setText(str(row[1]))
                  self.button_boisson3[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b47=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=47")               
               for row in self.b47:
                  self.button_boisson3[(3,2)].setText(str(row[0]))
                  self.lab_boisson3[(3,2)].setText(str(row[1]))
                  self.button_boisson3[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b48=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=48")               
               for row in self.b48:
                  self.button_boisson3[(3,3)].setText(str(row[0]))
                  self.lab_boisson3[(3,3)].setText(str(row[1]))
                  self.button_boisson3[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson3[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 4
               self.b49=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=49")               
               for row in self.b49:
                  self.button_boisson4[(0,0)].setText(str(row[0]))
                  self.lab_boisson4[(0,0)].setText(str(row[1]))
                  self.button_boisson4[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b50=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=50")           
               for row in self.b50:
                  self.button_boisson4[(0,1)].setText(str(row[0]))
                  self.lab_boisson4[(0,1)].setText(str(row[1]))
                  self.button_boisson4[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b51=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=51")               
               for row in self.b51:
                  self.button_boisson4[(0,2)].setText(str(row[0]))
                  self.lab_boisson4[(0,2)].setText(str(row[1]))
                  self.button_boisson4[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b52=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=52")               
               for row in self.b52:
                  self.button_boisson4[(0,3)].setText(str(row[0]))
                  self.lab_boisson4[(0,3)].setText(str(row[1]))
                  self.button_boisson4[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b53=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=53")               
               for row in self.b53:
                  self.button_boisson4[(1,0)].setText(str(row[0]))
                  self.lab_boisson4[(1,0)].setText(str(row[1]))
                  self.button_boisson4[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b54=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=54")               
               for row in self.b54:
                  self.button_boisson4[(1,1)].setText(str(row[0]))
                  self.lab_boisson4[(1,1)].setText(str(row[1]))
                  self.button_boisson4[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b55=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=55")               
               for row in self.b55:
                  self.button_boisson4[(1,2)].setText(str(row[0]))
                  self.lab_boisson4[(1,2)].setText(str(row[1]))
                  self.button_boisson4[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b56=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=56")               
               for row in self.b56:
                  self.button_boisson4[(1,3)].setText(str(row[0]))
                  self.lab_boisson4[(1,3)].setText(str(row[1]))
                  self.button_boisson4[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b57=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=57")               
               for row in self.b57:
                  self.button_boisson4[(2,0)].setText(str(row[0]))
                  self.lab_boisson4[(2,0)].setText(str(row[1]))
                  self.button_boisson4[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b58=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=58")               
               for row in self.b58:
                  self.button_boisson4[(2,1)].setText(str(row[0]))
                  self.lab_boisson4[(2,1)].setText(str(row[1]))
                  self.button_boisson4[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b59=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=59")               
               for row in self.b59:
                  self.button_boisson4[(2,2)].setText(str(row[0]))
                  self.lab_boisson4[(2,2)].setText(str(row[1]))
                  self.button_boisson4[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b60=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=60")               
               for row in self.b60:
                  self.button_boisson4[(2,3)].setText(str(row[0]))
                  self.lab_boisson4[(2,3)].setText(str(row[1]))
                  self.button_boisson4[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b61=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=61")               
               for row in self.b61:
                  self.button_boisson4[(3,0)].setText(str(row[0]))
                  self.lab_boisson4[(3,0)].setText(str(row[1]))
                  self.button_boisson4[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b62=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=62")               
               for row in self.b62:
                  self.button_boisson4[(3,1)].setText(str(row[0]))
                  self.lab_boisson4[(3,1)].setText(str(row[1]))
                  self.button_boisson4[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b63=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=63")               
               for row in self.b63:
                  self.button_boisson4[(3,2)].setText(str(row[0]))
                  self.lab_boisson4[(3,2)].setText(str(row[1]))
                  self.button_boisson4[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b64=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=64")               
               for row in self.b64:
                  self.button_boisson4[(3,3)].setText(str(row[0]))
                  self.lab_boisson4[(3,3)].setText(str(row[1]))
                  self.button_boisson4[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson4[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 5
               self.b65=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=65")               
               for row in self.b65:
                  self.button_boisson5[(0,0)].setText(str(row[0]))
                  self.lab_boisson5[(0,0)].setText(str(row[1]))
                  self.button_boisson5[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b66=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=66")             
               for row in self.b66:
                  self.button_boisson5[(0,1)].setText(str(row[0]))
                  self.lab_boisson5[(0,1)].setText(str(row[1]))
                  self.button_boisson5[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b67=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=67")               
               for row in self.b67:
                  self.button_boisson5[(0,2)].setText(str(row[0]))
                  self.lab_boisson5[(0,2)].setText(str(row[1]))
                  self.button_boisson5[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b68=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=68")               
               for row in self.b68:
                  self.button_boisson5[(0,3)].setText(str(row[0]))
                  self.lab_boisson5[(0,3)].setText(str(row[1]))
                  self.button_boisson5[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b69=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=69")               
               for row in self.b69:
                  self.button_boisson5[(1,0)].setText(str(row[0]))
                  self.lab_boisson5[(1,0)].setText(str(row[1]))
                  self.button_boisson5[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b70=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=70")               
               for row in self.b70:
                  self.button_boisson5[(1,1)].setText(str(row[0]))
                  self.lab_boisson5[(1,1)].setText(str(row[1]))
                  self.button_boisson5[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b71=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=71")               
               for row in self.b71:
                  self.button_boisson5[(1,2)].setText(str(row[0]))
                  self.lab_boisson5[(1,2)].setText(str(row[1]))
                  self.button_boisson5[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b72=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=72")               
               for row in self.b72:
                  self.button_boisson5[(1,3)].setText(str(row[0]))
                  self.lab_boisson5[(1,3)].setText(str(row[1]))
                  self.button_boisson5[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b73=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=73")               
               for row in self.b73:
                  self.button_boisson5[(2,0)].setText(str(row[0]))
                  self.lab_boisson5[(2,0)].setText(str(row[1]))
                  self.button_boisson5[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b74=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=74")               
               for row in self.b74:
                  self.button_boisson5[(2,1)].setText(str(row[0]))
                  self.lab_boisson5[(2,1)].setText(str(row[1]))
                  self.button_boisson5[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b75=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=75")               
               for row in self.b75:
                  self.button_boisson5[(2,2)].setText(str(row[0]))
                  self.lab_boisson5[(2,2)].setText(str(row[1]))
                  self.button_boisson5[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b76=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=76")               
               for row in self.b76:
                  self.button_boisson5[(2,3)].setText(str(row[0]))
                  self.lab_boisson5[(2,3)].setText(str(row[1]))
                  self.button_boisson5[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b77=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=77")               
               for row in self.b77:
                  self.button_boisson5[(3,0)].setText(str(row[0]))
                  self.lab_boisson5[(3,0)].setText(str(row[1]))
                  self.button_boisson5[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b78=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=78")               
               for row in self.b78:
                  self.button_boisson5[(3,1)].setText(str(row[0]))
                  self.lab_boisson5[(3,1)].setText(str(row[1]))
                  self.button_boisson5[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b79=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=79")               
               for row in self.b79:
                  self.button_boisson5[(3,2)].setText(str(row[0]))
                  self.lab_boisson5[(3,2)].setText(str(row[1]))
                  self.button_boisson5[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b80=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=80")               
               for row in self.b80:
                  self.button_boisson5[(3,3)].setText(str(row[0]))
                  self.lab_boisson5[(3,3)].setText(str(row[1]))
                  self.button_boisson5[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson5[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 6
               self.b81=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=81")               
               for row in self.b81:
                  self.button_boisson6[(0,0)].setText(str(row[0]))
                  self.lab_boisson6[(0,0)].setText(str(row[1]))
                  self.button_boisson6[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b82=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=82")               
               for row in self.b82:
                  self.button_boisson6[(0,1)].setText(str(row[0]))
                  self.lab_boisson6[(0,1)].setText(str(row[1]))
                  self.button_boisson6[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b83=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=83")               
               for row in self.b83:
                  self.button_boisson6[(0,2)].setText(str(row[0]))
                  self.lab_boisson6[(0,2)].setText(str(row[1]))
                  self.button_boisson6[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b84=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=84")               
               for row in self.b84:
                  self.button_boisson6[(0,3)].setText(str(row[0]))
                  self.lab_boisson6[(0,3)].setText(str(row[1]))
                  self.button_boisson6[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b85=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=85")               
               for row in self.b85:
                  self.button_boisson6[(1,0)].setText(str(row[0]))
                  self.lab_boisson6[(1,0)].setText(str(row[1]))
                  self.button_boisson6[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b86=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=86")               
               for row in self.b86:
                  self.button_boisson6[(1,1)].setText(str(row[0]))
                  self.lab_boisson6[(1,1)].setText(str(row[1]))
                  self.button_boisson6[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b87=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=87")               
               for row in self.b87:
                  self.button_boisson6[(1,2)].setText(str(row[0]))
                  self.lab_boisson6[(1,2)].setText(str(row[1]))
                  self.button_boisson6[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b88=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=88")               
               for row in self.b88:
                  self.button_boisson6[(1,3)].setText(str(row[0]))
                  self.lab_boisson6[(1,3)].setText(str(row[1]))
                  self.button_boisson6[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b89=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=89")               
               for row in self.b89:
                  self.button_boisson6[(2,0)].setText(str(row[0]))
                  self.lab_boisson6[(2,0)].setText(str(row[1]))
                  self.button_boisson6[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b90=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=90")               
               for row in self.b90:
                  self.button_boisson6[(2,1)].setText(str(row[0]))
                  self.lab_boisson6[(2,1)].setText(str(row[1]))
                  self.button_boisson6[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b91=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=91")               
               for row in self.b91:
                  self.button_boisson6[(2,2)].setText(str(row[0]))
                  self.lab_boisson6[(2,2)].setText(str(row[1]))
                  self.button_boisson6[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b92=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=92")               
               for row in self.b92:
                  self.button_boisson6[(2,3)].setText(str(row[0]))
                  self.lab_boisson6[(2,3)].setText(str(row[1]))
                  self.button_boisson6[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b93=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=93")               
               for row in self.b93:
                  self.button_boisson6[(3,0)].setText(str(row[0]))
                  self.lab_boisson6[(3,0)].setText(str(row[1]))
                  self.button_boisson6[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b94=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=94")               
               for row in self.b94:
                  self.button_boisson6[(3,1)].setText(str(row[0]))
                  self.lab_boisson6[(3,1)].setText(str(row[1]))
                  self.button_boisson6[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b95=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=95")               
               for row in self.b95:
                  self.button_boisson6[(3,2)].setText(str(row[0]))
                  self.lab_boisson6[(3,2)].setText(str(row[1]))
                  self.button_boisson6[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b96=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=96")               
               for row in self.b96:
                  self.button_boisson6[(3,3)].setText(str(row[0]))
                  self.lab_boisson6[(3,3)].setText(str(row[1]))
                  self.button_boisson6[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson6[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 7
               self.b97=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=97")               
               for row in self.b97:
                  self.button_boisson7[(0,0)].setText(str(row[0]))
                  self.lab_boisson7[(0,0)].setText(str(row[1]))
                  self.button_boisson7[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b98=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=98")               
               for row in self.b98:
                  self.button_boisson7[(0,1)].setText(str(row[0]))
                  self.lab_boisson7[(0,1)].setText(str(row[1]))
                  self.button_boisson7[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b99=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=99")               
               for row in self.b99:
                  self.button_boisson7[(0,2)].setText(str(row[0]))
                  self.lab_boisson7[(0,2)].setText(str(row[1]))
                  self.button_boisson7[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b100=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=100")               
               for row in self.b100:
                  self.button_boisson7[(0,3)].setText(str(row[0]))
                  self.lab_boisson7[(0,3)].setText(str(row[1]))
                  self.button_boisson7[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b101=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=101")               
               for row in self.b101:
                  self.button_boisson7[(1,0)].setText(str(row[0]))
                  self.lab_boisson7[(1,0)].setText(str(row[1]))
                  self.button_boisson7[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b102=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=102")               
               for row in self.b101:
                  self.button_boisson7[(1,1)].setText(str(row[0]))
                  self.lab_boisson7[(1,1)].setText(str(row[1]))
                  self.button_boisson7[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b103=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=103")               
               for row in self.b103:
                  self.button_boisson7[(1,2)].setText(str(row[0]))
                  self.lab_boisson7[(1,2)].setText(str(row[1]))
                  self.button_boisson7[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b104=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=104")               
               for row in self.b104:
                  self.button_boisson7[(1,3)].setText(str(row[0]))
                  self.lab_boisson7[(1,3)].setText(str(row[1]))
                  self.button_boisson7[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b105=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=105")               
               for row in self.b105:
                  self.button_boisson7[(2,0)].setText(str(row[0]))
                  self.lab_boisson7[(2,0)].setText(str(row[1]))
                  self.button_boisson7[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b106=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=106")               
               for row in self.b106:
                  self.button_boisson7[(2,1)].setText(str(row[0]))
                  self.lab_boisson7[(2,1)].setText(str(row[1]))
                  self.button_boisson7[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b107=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=107")               
               for row in self.b107:
                  self.button_boisson7[(2,2)].setText(str(row[0]))
                  self.lab_boisson7[(2,2)].setText(str(row[1]))
                  self.button_boisson7[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b108=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=108")               
               for row in self.b108:
                  self.button_boisson7[(2,3)].setText(str(row[0]))
                  self.lab_boisson7[(2,3)].setText(str(row[1]))
                  self.button_boisson7[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b109=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=109")               
               for row in self.b109:
                  self.button_boisson7[(3,0)].setText(str(row[0]))
                  self.lab_boisson7[(3,0)].setText(str(row[1]))
                  self.button_boisson7[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b110=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=110")               
               for row in self.b110:
                  self.button_boisson7[(3,1)].setText(str(row[0]))
                  self.lab_boisson7[(3,1)].setText(str(row[1]))
                  self.button_boisson7[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b111=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=111")               
               for row in self.b111:
                  self.button_boisson7[(3,2)].setText(str(row[0]))
                  self.lab_boisson7[(3,2)].setText(str(row[1]))
                  self.button_boisson7[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b112=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=112")               
               for row in self.b112:
                  self.button_boisson7[(3,3)].setText(str(row[0]))
                  self.lab_boisson7[(3,3)].setText(str(row[1]))
                  self.button_boisson7[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson7[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 8
               self.b113=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=113")               
               for row in self.b113:
                  self.button_boisson8[(0,0)].setText(str(row[0]))
                  self.lab_boisson8[(0,0)].setText(str(row[1]))
                  self.button_boisson8[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b114=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=114")           
               for row in self.b114:
                  self.button_boisson8[(0,1)].setText(str(row[0]))
                  self.lab_boisson8[(0,1)].setText(str(row[1]))
                  self.button_boisson8[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b115=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=115")               
               for row in self.b115:
                  self.button_boisson8[(0,2)].setText(str(row[0]))
                  self.lab_boisson8[(0,2)].setText(str(row[1]))
                  self.button_boisson8[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b116=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=116")               
               for row in self.b116:
                  self.button_boisson8[(0,3)].setText(str(row[0]))
                  self.lab_boisson8[(0,3)].setText(str(row[1]))
                  self.button_boisson8[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b117=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=117")               
               for row in self.b117:
                  self.button_boisson8[(1,0)].setText(str(row[0]))
                  self.lab_boisson8[(1,0)].setText(str(row[1]))
                  self.button_boisson8[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b118=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=118")               
               for row in self.b118:
                  self.button_boisson8[(1,1)].setText(str(row[0]))
                  self.lab_boisson8[(1,1)].setText(str(row[1]))
                  self.button_boisson8[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b119=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=119")               
               for row in self.b119:
                  self.button_boisson8[(1,2)].setText(str(row[0]))
                  self.lab_boisson8[(1,2)].setText(str(row[1]))
                  self.button_boisson8[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b120=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=120")               
               for row in self.b120:
                  self.button_boisson4[(1,3)].setText(str(row[0]))
                  self.lab_boisson8[(1,3)].setText(str(row[1]))
                  self.button_boisson8[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b121=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=121")               
               for row in self.b121:
                  self.button_boisson8[(2,0)].setText(str(row[0]))
                  self.lab_boisson8[(2,0)].setText(str(row[1]))
                  self.button_boisson8[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b122=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=122")               
               for row in self.b122:
                  self.button_boisson8[(2,1)].setText(str(row[0]))
                  self.lab_boisson8[(2,1)].setText(str(row[1]))
                  self.button_boisson8[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b123=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=123")               
               for row in self.b123:
                  self.button_boisson8[(2,2)].setText(str(row[0]))
                  self.lab_boisson8[(2,2)].setText(str(row[1]))
                  self.button_boisson8[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b124=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=124")               
               for row in self.b124:
                  self.button_boisson8[(2,3)].setText(str(row[0]))
                  self.lab_boisson8[(2,3)].setText(str(row[1]))
                  self.button_boisson8[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b125=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=125")               
               for row in self.b125:
                  self.button_boisson8[(3,0)].setText(str(row[0]))
                  self.lab_boisson8[(3,0)].setText(str(row[1]))
                  self.button_boisson8[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b126=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=126")               
               for row in self.b126:
                  self.button_boisson8[(3,1)].setText(str(row[0]))
                  self.lab_boisson8[(3,1)].setText(str(row[1]))
                  self.button_boisson8[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b127=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=127")               
               for row in self.b127:
                  self.button_boisson8[(3,2)].setText(str(row[0]))
                  self.lab_boisson8[(3,2)].setText(str(row[1]))
                  self.button_boisson8[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b128=self.cursor.execute("SELECT nom,quantite,photo,prix,categorie FROM boissons WHERE rowid=128")               
               for row in self.b128:
                  self.button_boisson8[(3,3)].setText(str(row[0]))
                  self.lab_boisson8[(3,3)].setText(str(row[1]))
                  self.button_boisson8[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_boisson8[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))

               self.bdd.commit()

               #====================== REFRESH LAB ==#
               #=====================================#
               for x in range(4):
                  for y in range(4):
                     #====================== BOISSONS
                     self.lab_boisson1[(x,y)].adjustSize()
                     self.lab_boisson2[(x,y)].adjustSize()
                     self.lab_boisson3[(x,y)].adjustSize()
                     self.lab_boisson4[(x,y)].adjustSize()
                     self.lab_boisson5[(x,y)].adjustSize()
                     self.lab_boisson6[(x,y)].adjustSize()
                     self.lab_boisson7[(x,y)].adjustSize()
                     self.lab_boisson8[(x,y)].adjustSize()
                  
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass

   def refresh_dessert(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.cursor.execute("""SELECT COUNT(*) FROM desserts """)
               self._result=self.cursor.fetchone()
               self._row=int(self._result[0])
               
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
                        
               self.bdd.commit()
                  
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass

   def refresh_cafe(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.cursor.execute("""SELECT COUNT(*) FROM cafes """)
               self._result=self.cursor.fetchone()
               self._row=int(self._result[0])
               
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
                        
               self.bdd.commit()
                  
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass

   def refresh_plat(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.cursor.execute("""SELECT COUNT(*) FROM plats """)
               self._result=self.cursor.fetchone()
               self._row=int(self._result[0])
               
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
                        
               self.bdd.commit()
                  
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass

   def boissons_page(self):
      self.zone_title.setText('BOISSONS')
      self.refresh_all()
      self.list_panier.show()
      self.refresh_cart()
      
      self.nom_vente.setText('')
      self.qte_vente.setValue(0)
      self.prix_vente.setValue(0)
      self.photo=''
      self.code_produit.setText('')
      self.reduction_produit.setValue(0)
      
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
      self.list_panier.show()
      self.refresh_cart()

      self.nom_vente.setText('')
      self.qte_vente.setValue(0)
      self.prix_vente.setValue(0)
      self.photo=''
      self.code_produit.setText('')
      self.reduction_produit.setValue(0)
      
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
      self.list_panier.show()
      self.refresh_cart()

      self.nom_vente.setText('')
      self.qte_vente.setValue(0)
      self.prix_vente.setValue(0)
      self.photo=''
      self.code_produit.setText('')
      self.reduction_produit.setValue(0)
      
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
      self.list_panier.show()
      self.refresh_cart()

      self.nom_vente.setText('')
      self.qte_vente.setValue(0)
      self.prix_vente.setValue(0)
      self.photo=''
      self.code_produit.setText('')
      self.reduction_produit.setValue(0)
      
      #BOISSONS
      self.list_boisson.hide()
      #DESSERTS
      self.list_dessert.hide()
      #CAFES
      self.list_cafe.hide()
      #PLATS
      self.list_plat.show()
   
      
   def information_boisson(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.sql1=self.cursor.execute("""SELECT COUNT(*) FROM boissons """)             
               for row in self.sql1:
                  if self.id_produit.value()> int(row[0]):
                     self.nom_vente.setText('')
                     self.qte_vente.setValue(0)
                     self.prix_vente.setValue(0)
                     self.photo=''
                     self.code_produit.setText('')
                     self.reduction_produit.setValue(0)
                  else:
                     self.sql2=self.cursor.execute("""SELECT nom,quantite,prix,photo,categorie,code_produit,reduction FROM boissons
                                                      WHERE rowid={0}""".format(str(self.id_produit.value())))             
                     for row in self.sql2:
                        self.nom_vente.setText(row[0])
                        self.qte_vente.setValue(int(row[1]))
                        self.prix_vente.setValue(float(row[2]))
                        self.photo=row[3]
                        self.code_produit.setText(row[5])
                        self.reduction_produit.setValue(int(row[6]))
               self.bdd.commit()
            else:
               pass
     
   def information_dessert(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.sql1=self.cursor.execute("""SELECT COUNT(*) FROM desserts """)             
               for row in self.sql1:
                  if self.id_produit.value()> int(row[0]):
                     self.nom_vente.setText('')
                     self.qte_vente.setValue(0)
                     self.prix_vente.setValue(0)
                     self.photo=''
                     self.code_produit.setText('')
                     self.reduction_produit.setValue(0)
                  else:
                     self.sql2=self.cursor.execute("""SELECT nom,quantite,prix,photo,categorie,code_produit,reduction FROM desserts
                                                      WHERE rowid={0}""".format(str(self.id_produit.value())))             
                     for row in self.sql2:
                        self.nom_vente.setText(row[0])
                        self.qte_vente.setValue(int(row[1]))
                        self.prix_vente.setValue(float(row[2]))
                        self.photo=row[3]
                        self.code_produit.setText(row[5])
                        self.reduction_produit.setValue(int(row[6]))           
               self.bdd.commit()
            else:
               pass

   def information_cafe(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.sql1=self.cursor.execute("""SELECT COUNT(*) FROM cafes """)             
               for row in self.sql1:
                  if self.id_produit.value()> int(row[0]):
                     self.nom_vente.setText('')
                     self.qte_vente.setValue(0)
                     self.prix_vente.setValue(0)
                     self.photo=''
                     self.code_produit.setText('')
                     self.reduction_produit.setValue(0)
                  else:
                     self.sql2=self.cursor.execute("""SELECT nom,quantite,prix,photo,categorie,code_produit,reduction FROM cafes
                                                      WHERE rowid={0}""".format(str(self.id_produit.value())))             
                     for row in self.sql2:
                        self.nom_vente.setText(row[0])
                        self.qte_vente.setValue(int(row[1]))
                        self.prix_vente.setValue(float(row[2]))
                        self.photo=row[3]
                        self.code_produit.setText(row[5])
                        self.reduction_produit.setValue(int(row[6]))         
               self.bdd.commit()
            else:
               pass

   def information_plat(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.sql1=self.cursor.execute("""SELECT COUNT(*) FROM plats """)             
               for row in self.sql1:
                  if self.id_produit.value()> int(row[0]):
                     self.nom_vente.setText('')
                     self.qte_vente.setValue(0)
                     self.prix_vente.setValue(0)
                     self.photo=''
                     self.code_produit.setText('')
                     self.reduction_produit.setValue(0)
                  else:
                     self.sql2=self.cursor.execute("""SELECT nom,quantite,prix,photo,categorie,code_produit,reduction FROM plats
                                                      WHERE rowid={0}""".format(str(self.id_produit.value())))             
                     for row in self.sql2:
                        self.nom_vente.setText(row[0])
                        self.qte_vente.setValue(int(row[1]))
                        self.prix_vente.setValue(float(row[2]))
                        self.photo=row[3]
                        self.code_produit.setText(row[5])
                        self.reduction_produit.setValue(int(row[6]))             
               self.bdd.commit()
            else:
               pass
            
   
      
   """
   #_________________________________________DRAP MAIN WINDOW EVENTS BEGINNING
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
   #_________________________________________DRAP MAIN WINDOW EVENTS END"""

if __name__=='__main__':
   app=QApplication(sys.argv)
   app.setStyle('vista')
   screen=Dash()   
   screen.show()
   sys.exit(app.exec_())
