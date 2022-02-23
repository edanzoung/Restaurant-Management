#####################################
# IZI TOC V1.0 by Edan_Zoung
#####################################

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import sys
import sqlite3
#♣from paiement import Paiement
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

class Commande(QMainWindow):
   def __init__(self):
      super().__init__()
      self.width=1200
      self.height=600
      self.set=0
      self.photo=''
      self.app_name=name_app
      #this will hide the title bar
      #self.setWindowFlag(Qt.FramelessWindowHint)
      self.offset = None
      self.setGeometry(100,100,self.width,self.height)
      self.setWindowTitle('COMMANDES')  
      self.setStyleSheet("""
                         QMainWindow{ background-color:#000;color:#fff;
                             background: url("assets/background7.jpg"); 
                             background-repeat: no-repeat; 
                             background-position: center;}
                          QMessageBox{ background-color:#fff}
                         """)
      #self.setFixedSize(self.width,self.height)
      self.setWindowOpacity(1)

      self.id_client=0
      self.group=None

      self.x=0
      self.y=0
      self.w_size_b=100
      self.h_size_b=100
      self.icon_size=80
      self.button_commande1={}
      self.button_commande2={}
      self.button_commande3={}
      self.button_commande4={}
      self.button_commande5={}
      self.button_commande6={}
      self.button_commande7={}
      self.button_commande8={}
      self.lab_commande1={}
      self.lab_commande2={}
      self.lab_commande3={}
      self.lab_commande4={}
      self.lab_commande5={}
      self.lab_commande6={}
      self.lab_commande7={}
      self.lab_commande8={}
      self.lab_validate1={}
      self.lab_validate2={}
      self.lab_validate3={}
      self.lab_validate4={}
      self.lab_validate5={}
      self.lab_validate6={}
      self.lab_validate7={}
      self.lab_validate8={}
      
      self.widgets()
      self.refresh_commande()
      self.showMaximized()
   def widgets(self):
      #______________________________________________INTERFACE  PRODUITS BEGINNING

      #_________PANIER PAGE 1
      self.commande1=QWidget()
      self.commande1.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.commande1.move(5,5)
      self.commande1.resize(400,400)
      for i in range(4):
          for j in range(4):            
              self.button_commande1[(i,j)]=QToolButton(self.commande1)
              self.button_commande1[(i,j)].setStyleSheet("""
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
              self.button_commande1[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_commande1[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_commande1[(i,j)].resize(100,100)

              self.lab_commande1[(i,j)]=QLabel(self.commande1)
              self.lab_commande1[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_commande1[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_commande1[(i,j)].adjustSize()

              self.lab_validate1[(i,j)]=QLabel(self.commande1)
              self.lab_validate1[(i,j)].setStyleSheet("""background-color:transparent;color:#fff;
                             background-repeat: no-repeat; 
                             background-position: center""")
              self.lab_validate1[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_validate1[(i,j)].resize(50,50)
              self.pixmap = QPixmap('png/check1.png').scaled(50,50)
              self.lab_validate1[(i,j)].setPixmap(self.pixmap)

      #_________PANIER PAGE 2

      self.commande2=QWidget()
      self.commande2.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.commande2.move(5,5)
      self.commande2.resize(400,400)
      for i in range(4):
          for j in range(4):            
              self.button_commande2[(i,j)]=QToolButton(self.commande2)
              self.button_commande2[(i,j)].setStyleSheet("""
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
              self.button_commande2[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_commande2[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_commande2[(i,j)].resize(100,100)
              self.lab_commande2[(i,j)]=QLabel(self.commande2)
              self.lab_commande2[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_commande2[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_commande2[(i,j)].adjustSize()

      #_________PANIER PAGE 3
      
      self.commande3=QWidget()
      self.commande3.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.commande3.move(5,5)
      self.commande3.resize(400,400)
      for i in range(4):
          for j in range(4):            
              self.button_commande3[(i,j)]=QToolButton(self.commande3)
              self.button_commande3[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#e3128c;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_commande3[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_commande3[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_commande3[(i,j)].resize(100,100)
              self.lab_commande3[(i,j)]=QLabel(self.commande3)
              self.lab_commande3[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_commande3[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_commande3[(i,j)].adjustSize()

      #_________PANIER PAGE 4
      
      self.commande4=QWidget()
      self.commande4.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.commande4.move(5,5)
      self.commande4.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_commande4[(i,j)]=QToolButton(self.commande4)
              self.button_commande4[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#e3128c;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_commande4[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_commande4[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_commande4[(i,j)].resize(100,100)
              self.lab_commande4[(i,j)]=QLabel(self.commande4)
              self.lab_commande4[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_commande4[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_commande4[(i,j)].adjustSize()

      #_________PANIER PAGE 5
      
      self.commande5=QWidget()
      self.commande5.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.commande5.move(5,5)
      self.commande5.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_commande5[(i,j)]=QToolButton(self.commande5)
              self.button_commande5[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#e3128c;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_commande5[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_commande5[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_commande5[(i,j)].resize(100,100)
              self.lab_commande5[(i,j)]=QLabel(self.commande5)
              self.lab_commande5[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_commande5[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_commande5[(i,j)].adjustSize()

      #_________PANIER PAGE 6
      
      self.commande6=QWidget()
      self.commande6.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.commande6.move(5,5)
      self.commande6.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_commande6[(i,j)]=QToolButton(self.commande6)
              self.button_commande6[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#e3128c;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_commande6[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_commande6[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_commande6[(i,j)].resize(100,100)
              self.lab_commande6[(i,j)]=QLabel(self.commande6)
              self.lab_commande6[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_commande6[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_commande6[(i,j)].adjustSize()

      #_________PANIER PAGE 7
      
      self.commande7=QWidget()
      self.commande7.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.commande7.move(5,5)
      self.commande7.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_commande7[(i,j)]=QToolButton(self.commande7)
              self.button_commande7[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#e3128c;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_commande7[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_commande7[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_commande7[(i,j)].resize(100,100)
              self.lab_commande7[(i,j)]=QLabel(self.commande7)
              self.lab_commande7[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_commande7[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_commande7[(i,j)].adjustSize()

      #_________PANIER PAGE 8
      
      self.commande8=QWidget()
      self.commande8.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.commande8.move(5,5)
      self.commande8.resize(400,400)    
      for i in range(4):
          for j in range(4):            
              self.button_commande8[(i,j)]=QToolButton(self.commande8)
              self.button_commande8[(i,j)].setStyleSheet("""
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
                                  border-width:3px;border-color:#e3128c;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_commande8[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_commande8[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_commande8[(i,j)].resize(100,100)
              self.lab_commande8[(i,j)]=QLabel(self.commande8)
              self.lab_commande8[(i,j)].setStyleSheet("""
                                   background-color :#6603a3;color:#fff;
                                  font-family: Time;font-style:normal;font-size:10pt;
                                  font-weight:bold;border-radius:5px                                  
                                """)
              self.lab_commande8[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.lab_commande8[(i,j)].adjustSize()


      self.data_commande=[self.commande1,self.commande2,self.commande3,self.commande4,self.commande5,self.commande6,self.commande7,self.commande8]

      self.list_commande=QListWidget(self)
      self.list_commande.setGeometry(50,50,425,430)
      self.list_commande.setStyleSheet("""
                                  background-color:#00f;color:#000

                                  QListWidget::item:selected{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-style:solid;border-size:20px;border-color:#fff;border-radius:0px}
                                  
                                  QListWidget::item:!selected{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:0px}
                                  """)

      for i in self.data_commande:

          self.list_commande_frame=QFrame(self.list_commande)
          self.list_commande_frame.setStyleSheet("""
                                  background-color:#ff0;color:#000
                                  """)
         
          self.layout_commande = QVBoxLayout(self.list_commande_frame)
          self.layout_commande.setContentsMargins(0,0,0,0)
          self.layout_commande.setSpacing(20)
          self.layout_commande.addWidget(i)
          self.setLayout(self.layout_commande)
      
          self.item = QListWidgetItem(self.list_commande)         
          self.item_widget = self.list_commande_frame     

          self.item.setSizeHint(QSize(0,400))
         
          self.list_commande.addItem(self.item)
          self.list_commande.setItemWidget(self.item,self.item_widget)
          

      self.lab_commande1[(0,0)].move(self.x,self.y)
      self.lab_commande1[(0,1)].move(self.x+100,self.y)
      self.lab_commande1[(0,2)].move(self.x+200,self.y)
      self.lab_commande1[(0,3)].move(self.x+300,self.y)
      self.lab_commande1[(1,0)].move(self.x,self.y+100)
      self.lab_commande1[(1,1)].move(self.x+100,self.y+100)
      self.lab_commande1[(1,2)].move(self.x+200,self.y+100)
      self.lab_commande1[(1,3)].move(self.x+300,self.y+100)
      self.lab_commande1[(2,0)].move(self.x,self.y+200)
      self.lab_commande1[(2,1)].move(self.x+100,self.y+200)
      self.lab_commande1[(2,2)].move(self.x+200,self.y+200)
      self.lab_commande1[(2,3)].move(self.x+300,self.y+200)
      self.lab_commande1[(3,0)].move(self.x,self.y+300)
      self.lab_commande1[(3,1)].move(self.x+100,self.y+300)
      self.lab_commande1[(3,2)].move(self.x+200,self.y+300)
      self.lab_commande1[(3,3)].move(self.x+300,self.y+300)

      self.lab_validate1[(0,0)].move(self.x,self.y+50)
      self.lab_validate1[(0,1)].move(self.x+100,self.y+50)
      self.lab_validate1[(0,2)].move(self.x+200,self.y+50)
      self.lab_validate1[(0,3)].move(self.x+300,self.y+50)
      self.lab_validate1[(1,0)].move(self.x,self.y+150)
      self.lab_validate1[(1,1)].move(self.x+100,self.y+150)
      self.lab_validate1[(1,2)].move(self.x+200,self.y+150)
      self.lab_validate1[(1,3)].move(self.x+300,self.y+150)
      self.lab_validate1[(2,0)].move(self.x,self.y+250)
      self.lab_validate1[(2,1)].move(self.x+100,self.y+250)
      self.lab_validate1[(2,2)].move(self.x+200,self.y+250)
      self.lab_validate1[(2,3)].move(self.x+300,self.y+250)
      self.lab_validate1[(3,0)].move(self.x,self.y+350)
      self.lab_validate1[(3,1)].move(self.x+100,self.y+350)
      self.lab_validate1[(3,2)].move(self.x+200,self.y+350)
      self.lab_validate1[(3,3)].move(self.x+300,self.y+350)

      self.lab_validate1[(0,0)].hide()
      self.lab_validate1[(0,1)].hide()
      self.lab_validate1[(0,2)].hide()
      self.lab_validate1[(0,3)].hide()
      self.lab_validate1[(1,0)].hide()
      self.lab_validate1[(1,1)].hide()
      self.lab_validate1[(1,2)].hide()
      self.lab_validate1[(1,3)].hide()
      self.lab_validate1[(2,0)].hide()
      self.lab_validate1[(2,1)].hide()
      self.lab_validate1[(2,2)].hide()
      self.lab_validate1[(2,3)].hide()
      self.lab_validate1[(3,0)].hide()
      self.lab_validate1[(3,1)].hide()
      self.lab_validate1[(3,2)].hide()
      self.lab_validate1[(3,3)].hide()
      
      self.button_commande1[(0,0)].move(self.x,self.y)
      self.button_commande1[(0,1)].move(self.x+100,self.y)
      self.button_commande1[(0,2)].move(self.x+200,self.y)
      self.button_commande1[(0,3)].move(self.x+300,self.y)
      self.button_commande1[(1,0)].move(self.x,self.y+100)
      self.button_commande1[(1,1)].move(self.x+100,self.y+100)
      self.button_commande1[(1,2)].move(self.x+200,self.y+100)
      self.button_commande1[(1,3)].move(self.x+300,self.y+100)
      self.button_commande1[(2,0)].move(self.x,self.y+200)
      self.button_commande1[(2,1)].move(self.x+100,self.y+200)
      self.button_commande1[(2,2)].move(self.x+200,self.y+200)
      self.button_commande1[(2,3)].move(self.x+300,self.y+200)
      self.button_commande1[(3,0)].move(self.x,self.y+300)
      self.button_commande1[(3,1)].move(self.x+100,self.y+300)
      self.button_commande1[(3,2)].move(self.x+200,self.y+300)
      self.button_commande1[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 2
      
      self.lab_commande2[(0,0)].move(self.x,self.y)
      self.lab_commande2[(0,1)].move(self.x+100,self.y)
      self.lab_commande2[(0,2)].move(self.x+200,self.y)
      self.lab_commande2[(0,3)].move(self.x+300,self.y)
      self.lab_commande2[(1,0)].move(self.x,self.y+100)
      self.lab_commande2[(1,1)].move(self.x+100,self.y+100)
      self.lab_commande2[(1,2)].move(self.x+200,self.y+100)
      self.lab_commande2[(1,3)].move(self.x+300,self.y+100)
      self.lab_commande2[(2,0)].move(self.x,self.y+200)
      self.lab_commande2[(2,1)].move(self.x+100,self.y+200)
      self.lab_commande2[(2,2)].move(self.x+200,self.y+200)
      self.lab_commande2[(2,3)].move(self.x+300,self.y+200)
      self.lab_commande2[(3,0)].move(self.x,self.y+300)
      self.lab_commande2[(3,1)].move(self.x+100,self.y+300)
      self.lab_commande2[(3,2)].move(self.x+200,self.y+300)
      self.lab_commande2[(3,3)].move(self.x+300,self.y+300)
      
      self.button_commande2[(0,0)].move(self.x,self.y)
      self.button_commande2[(0,1)].move(self.x+100,self.y)
      self.button_commande2[(0,2)].move(self.x+200,self.y)
      self.button_commande2[(0,3)].move(self.x+300,self.y)
      self.button_commande2[(1,0)].move(self.x,self.y+100)
      self.button_commande2[(1,1)].move(self.x+100,self.y+100)
      self.button_commande2[(1,2)].move(self.x+200,self.y+100)
      self.button_commande2[(1,3)].move(self.x+300,self.y+100)
      self.button_commande2[(2,0)].move(self.x,self.y+200)
      self.button_commande2[(2,1)].move(self.x+100,self.y+200)
      self.button_commande2[(2,2)].move(self.x+200,self.y+200)
      self.button_commande2[(2,3)].move(self.x+300,self.y+200)
      self.button_commande2[(3,0)].move(self.x,self.y+300)
      self.button_commande2[(3,1)].move(self.x+100,self.y+300)
      self.button_commande2[(3,2)].move(self.x+200,self.y+300)
      self.button_commande2[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 3

      self.lab_commande3[(0,0)].move(self.x,self.y)
      self.lab_commande3[(0,1)].move(self.x+100,self.y)
      self.lab_commande3[(0,2)].move(self.x+200,self.y)
      self.lab_commande3[(0,3)].move(self.x+300,self.y)
      self.lab_commande3[(1,0)].move(self.x,self.y+100)
      self.lab_commande3[(1,1)].move(self.x+100,self.y+100)
      self.lab_commande3[(1,2)].move(self.x+200,self.y+100)
      self.lab_commande3[(1,3)].move(self.x+300,self.y+100)
      self.lab_commande3[(2,0)].move(self.x,self.y+200)
      self.lab_commande3[(2,1)].move(self.x+100,self.y+200)
      self.lab_commande3[(2,2)].move(self.x+200,self.y+200)
      self.lab_commande3[(2,3)].move(self.x+300,self.y+200)
      self.lab_commande3[(3,0)].move(self.x,self.y+300)
      self.lab_commande3[(3,1)].move(self.x+100,self.y+300)
      self.lab_commande3[(3,2)].move(self.x+200,self.y+300)
      self.lab_commande3[(3,3)].move(self.x+300,self.y+300)

      self.button_commande3[(0,0)].move(self.x,self.y)
      self.button_commande3[(0,1)].move(self.x+100,self.y)
      self.button_commande3[(0,2)].move(self.x+200,self.y)
      self.button_commande3[(0,3)].move(self.x+300,self.y)
      self.button_commande3[(1,0)].move(self.x,self.y+100)
      self.button_commande3[(1,1)].move(self.x+100,self.y+100)
      self.button_commande3[(1,2)].move(self.x+200,self.y+100)
      self.button_commande3[(1,3)].move(self.x+300,self.y+100)
      self.button_commande3[(2,0)].move(self.x,self.y+200)
      self.button_commande3[(2,1)].move(self.x+100,self.y+200)
      self.button_commande3[(2,2)].move(self.x+200,self.y+200)
      self.button_commande3[(2,3)].move(self.x+300,self.y+200)
      self.button_commande3[(3,0)].move(self.x,self.y+300)
      self.button_commande3[(3,1)].move(self.x+100,self.y+300)
      self.button_commande3[(3,2)].move(self.x+200,self.y+300)
      self.button_commande3[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 4

      self.lab_commande4[(0,0)].move(self.x,self.y)
      self.lab_commande4[(0,1)].move(self.x+100,self.y)
      self.lab_commande4[(0,2)].move(self.x+200,self.y)
      self.lab_commande4[(0,3)].move(self.x+300,self.y)
      self.lab_commande4[(1,0)].move(self.x,self.y+100)
      self.lab_commande4[(1,1)].move(self.x+100,self.y+100)
      self.lab_commande4[(1,2)].move(self.x+200,self.y+100)
      self.lab_commande4[(1,3)].move(self.x+300,self.y+100)
      self.lab_commande4[(2,0)].move(self.x,self.y+200)
      self.lab_commande4[(2,1)].move(self.x+100,self.y+200)
      self.lab_commande4[(2,2)].move(self.x+200,self.y+200)
      self.lab_commande4[(2,3)].move(self.x+300,self.y+200)
      self.lab_commande4[(3,0)].move(self.x,self.y+300)
      self.lab_commande4[(3,1)].move(self.x+100,self.y+300)
      self.lab_commande4[(3,2)].move(self.x+200,self.y+300)
      self.lab_commande4[(3,3)].move(self.x+300,self.y+300)

      self.button_commande4[(0,0)].move(self.x,self.y)
      self.button_commande4[(0,1)].move(self.x+100,self.y)
      self.button_commande4[(0,2)].move(self.x+200,self.y)
      self.button_commande4[(0,3)].move(self.x+300,self.y)
      self.button_commande4[(1,0)].move(self.x,self.y+100)
      self.button_commande4[(1,1)].move(self.x+100,self.y+100)
      self.button_commande4[(1,2)].move(self.x+200,self.y+100)
      self.button_commande4[(1,3)].move(self.x+300,self.y+100)
      self.button_commande4[(2,0)].move(self.x,self.y+200)
      self.button_commande4[(2,1)].move(self.x+100,self.y+200)
      self.button_commande4[(2,2)].move(self.x+200,self.y+200)
      self.button_commande4[(2,3)].move(self.x+300,self.y+200)
      self.button_commande4[(3,0)].move(self.x,self.y+300)
      self.button_commande4[(3,1)].move(self.x+100,self.y+300)
      self.button_commande4[(3,2)].move(self.x+200,self.y+300)
      self.button_commande4[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 5

      self.lab_commande5[(0,0)].move(self.x,self.y)
      self.lab_commande5[(0,1)].move(self.x+100,self.y)
      self.lab_commande5[(0,2)].move(self.x+200,self.y)
      self.lab_commande5[(0,3)].move(self.x+300,self.y)
      self.lab_commande5[(1,0)].move(self.x,self.y+100)
      self.lab_commande5[(1,1)].move(self.x+100,self.y+100)
      self.lab_commande5[(1,2)].move(self.x+200,self.y+100)
      self.lab_commande5[(1,3)].move(self.x+300,self.y+100)
      self.lab_commande5[(2,0)].move(self.x,self.y+200)
      self.lab_commande5[(2,1)].move(self.x+100,self.y+200)
      self.lab_commande5[(2,2)].move(self.x+200,self.y+200)
      self.lab_commande5[(2,3)].move(self.x+300,self.y+200)
      self.lab_commande5[(3,0)].move(self.x,self.y+300)
      self.lab_commande5[(3,1)].move(self.x+100,self.y+300)
      self.lab_commande5[(3,2)].move(self.x+200,self.y+300)
      self.lab_commande5[(3,3)].move(self.x+300,self.y+300)

      self.button_commande5[(0,0)].move(self.x,self.y)
      self.button_commande5[(0,1)].move(self.x+100,self.y)
      self.button_commande5[(0,2)].move(self.x+200,self.y)
      self.button_commande5[(0,3)].move(self.x+300,self.y)
      self.button_commande5[(1,0)].move(self.x,self.y+100)
      self.button_commande5[(1,1)].move(self.x+100,self.y+100)
      self.button_commande5[(1,2)].move(self.x+200,self.y+100)
      self.button_commande5[(1,3)].move(self.x+300,self.y+100)
      self.button_commande5[(2,0)].move(self.x,self.y+200)
      self.button_commande5[(2,1)].move(self.x+100,self.y+200)
      self.button_commande5[(2,2)].move(self.x+200,self.y+200)
      self.button_commande5[(2,3)].move(self.x+300,self.y+200)
      self.button_commande5[(3,0)].move(self.x,self.y+300)
      self.button_commande5[(3,1)].move(self.x+100,self.y+300)
      self.button_commande5[(3,2)].move(self.x+200,self.y+300)
      self.button_commande5[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 6

      self.lab_commande6[(0,0)].move(self.x,self.y)
      self.lab_commande6[(0,1)].move(self.x+100,self.y)
      self.lab_commande6[(0,2)].move(self.x+200,self.y)
      self.lab_commande6[(0,3)].move(self.x+300,self.y)
      self.lab_commande6[(1,0)].move(self.x,self.y+100)
      self.lab_commande6[(1,1)].move(self.x+100,self.y+100)
      self.lab_commande6[(1,2)].move(self.x+200,self.y+100)
      self.lab_commande6[(1,3)].move(self.x+300,self.y+100)
      self.lab_commande6[(2,0)].move(self.x,self.y+200)
      self.lab_commande6[(2,1)].move(self.x+100,self.y+200)
      self.lab_commande6[(2,2)].move(self.x+200,self.y+200)
      self.lab_commande6[(2,3)].move(self.x+300,self.y+200)
      self.lab_commande6[(3,0)].move(self.x,self.y+300)
      self.lab_commande6[(3,1)].move(self.x+100,self.y+300)
      self.lab_commande6[(3,2)].move(self.x+200,self.y+300)
      self.lab_commande6[(3,3)].move(self.x+300,self.y+300)

      self.button_commande6[(0,0)].move(self.x,self.y)
      self.button_commande6[(0,1)].move(self.x+100,self.y)
      self.button_commande6[(0,2)].move(self.x+200,self.y)
      self.button_commande6[(0,3)].move(self.x+300,self.y)
      self.button_commande6[(1,0)].move(self.x,self.y+100)
      self.button_commande6[(1,1)].move(self.x+100,self.y+100)
      self.button_commande6[(1,2)].move(self.x+200,self.y+100)
      self.button_commande6[(1,3)].move(self.x+300,self.y+100)
      self.button_commande6[(2,0)].move(self.x,self.y+200)
      self.button_commande6[(2,1)].move(self.x+100,self.y+200)
      self.button_commande6[(2,2)].move(self.x+200,self.y+200)
      self.button_commande6[(2,3)].move(self.x+300,self.y+200)
      self.button_commande6[(3,0)].move(self.x,self.y+300)
      self.button_commande6[(3,1)].move(self.x+100,self.y+300)
      self.button_commande6[(3,2)].move(self.x+200,self.y+300)
      self.button_commande6[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 7

      self.lab_commande7[(0,0)].move(self.x,self.y)
      self.lab_commande7[(0,1)].move(self.x+100,self.y)
      self.lab_commande7[(0,2)].move(self.x+200,self.y)
      self.lab_commande7[(0,3)].move(self.x+300,self.y)
      self.lab_commande7[(1,0)].move(self.x,self.y+100)
      self.lab_commande7[(1,1)].move(self.x+100,self.y+100)
      self.lab_commande7[(1,2)].move(self.x+200,self.y+100)
      self.lab_commande7[(1,3)].move(self.x+300,self.y+100)
      self.lab_commande7[(2,0)].move(self.x,self.y+200)
      self.lab_commande7[(2,1)].move(self.x+100,self.y+200)
      self.lab_commande7[(2,2)].move(self.x+200,self.y+200)
      self.lab_commande7[(2,3)].move(self.x+300,self.y+200)
      self.lab_commande7[(3,0)].move(self.x,self.y+300)
      self.lab_commande7[(3,1)].move(self.x+100,self.y+300)
      self.lab_commande7[(3,2)].move(self.x+200,self.y+300)
      self.lab_commande7[(3,3)].move(self.x+300,self.y+300)

      self.button_commande7[(0,0)].move(self.x,self.y)
      self.button_commande7[(0,1)].move(self.x+100,self.y)
      self.button_commande7[(0,2)].move(self.x+200,self.y)
      self.button_commande7[(0,3)].move(self.x+300,self.y)
      self.button_commande7[(1,0)].move(self.x,self.y+100)
      self.button_commande7[(1,1)].move(self.x+100,self.y+100)
      self.button_commande7[(1,2)].move(self.x+200,self.y+100)
      self.button_commande7[(1,3)].move(self.x+300,self.y+100)
      self.button_commande7[(2,0)].move(self.x,self.y+200)
      self.button_commande7[(2,1)].move(self.x+100,self.y+200)
      self.button_commande7[(2,2)].move(self.x+200,self.y+200)
      self.button_commande7[(2,3)].move(self.x+300,self.y+200)
      self.button_commande7[(3,0)].move(self.x,self.y+300)
      self.button_commande7[(3,1)].move(self.x+100,self.y+300)
      self.button_commande7[(3,2)].move(self.x+200,self.y+300)
      self.button_commande7[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ page 8

      self.lab_commande8[(0,0)].move(self.x,self.y)
      self.lab_commande8[(0,1)].move(self.x+100,self.y)
      self.lab_commande8[(0,2)].move(self.x+200,self.y)
      self.lab_commande8[(0,3)].move(self.x+300,self.y)
      self.lab_commande8[(1,0)].move(self.x,self.y+100)
      self.lab_commande8[(1,1)].move(self.x+100,self.y+100)
      self.lab_commande8[(1,2)].move(self.x+200,self.y+100)
      self.lab_commande8[(1,3)].move(self.x+300,self.y+100)
      self.lab_commande8[(2,0)].move(self.x,self.y+200)
      self.lab_commande8[(2,1)].move(self.x+100,self.y+200)
      self.lab_commande8[(2,2)].move(self.x+200,self.y+200)
      self.lab_commande8[(2,3)].move(self.x+300,self.y+200)
      self.lab_commande8[(3,0)].move(self.x,self.y+300)
      self.lab_commande8[(3,1)].move(self.x+100,self.y+300)
      self.lab_commande8[(3,2)].move(self.x+200,self.y+300)
      self.lab_commande8[(3,3)].move(self.x+300,self.y+300)
      self.button_commande8[(0,0)].move(self.x,self.y)
      self.button_commande8[(0,1)].move(self.x+100,self.y)
      self.button_commande8[(0,2)].move(self.x+200,self.y)
      self.button_commande8[(0,3)].move(self.x+300,self.y)
      self.button_commande8[(1,0)].move(self.x,self.y+100)
      self.button_commande8[(1,1)].move(self.x+100,self.y+100)
      self.button_commande8[(1,2)].move(self.x+200,self.y+100)
      self.button_commande8[(1,3)].move(self.x+300,self.y+100)
      self.button_commande8[(2,0)].move(self.x,self.y+200)
      self.button_commande8[(2,1)].move(self.x+100,self.y+200)
      self.button_commande8[(2,2)].move(self.x+200,self.y+200)
      self.button_commande8[(2,3)].move(self.x+300,self.y+200)
      self.button_commande8[(3,0)].move(self.x,self.y+300)
      self.button_commande8[(3,1)].move(self.x+100,self.y+300)
      self.button_commande8[(3,2)].move(self.x+200,self.y+300)
      self.button_commande8[(3,3)].move(self.x+300,self.y+300)

      #+++++++++++++++++++++++ buttons events +++++++++++++++++++++++++++++++++ DE 1 A 4

      self.button_commande1[(0,0)].clicked.connect(self.pp1)
      self.button_commande1[(0,1)].clicked.connect(self.pp2)
      self.button_commande1[(0,2)].clicked.connect(self.pp3)
      self.button_commande1[(0,3)].clicked.connect(self.pp4)
      self.button_commande1[(1,0)].clicked.connect(self.pp5)
      self.button_commande1[(1,1)].clicked.connect(self.pp6)
      self.button_commande1[(1,2)].clicked.connect(self.pp7)
      self.button_commande1[(1,3)].clicked.connect(self.pp8)
      self.button_commande1[(2,0)].clicked.connect(self.pp9)
      self.button_commande1[(2,1)].clicked.connect(self.pp10)
      self.button_commande1[(2,2)].clicked.connect(self.pp11)
      self.button_commande1[(2,3)].clicked.connect(self.pp12)
      self.button_commande1[(3,0)].clicked.connect(self.pp13)
      self.button_commande1[(3,1)].clicked.connect(self.pp14)
      self.button_commande1[(3,2)].clicked.connect(self.pp15)
      self.button_commande1[(3,3)].clicked.connect(self.pp16)

      self.button_commande2[(0,0)].clicked.connect(self._pp1)
      self.button_commande2[(0,1)].clicked.connect(self._pp2)
      self.button_commande2[(0,2)].clicked.connect(self._pp3)
      self.button_commande2[(0,3)].clicked.connect(self._pp4)
      self.button_commande2[(1,0)].clicked.connect(self._pp5)
      self.button_commande2[(1,1)].clicked.connect(self._pp6)
      self.button_commande2[(1,2)].clicked.connect(self._pp7)
      self.button_commande2[(1,3)].clicked.connect(self._pp8)
      self.button_commande2[(2,0)].clicked.connect(self._pp9)
      self.button_commande2[(2,1)].clicked.connect(self._pp10)
      self.button_commande2[(2,2)].clicked.connect(self._pp11)
      self.button_commande2[(2,3)].clicked.connect(self._pp12)
      self.button_commande2[(3,0)].clicked.connect(self._pp13)
      self.button_commande2[(3,1)].clicked.connect(self._pp14)
      self.button_commande2[(3,2)].clicked.connect(self._pp15)
      self.button_commande2[(3,3)].clicked.connect(self._pp16)

      self.button_commande3[(0,0)].clicked.connect(self.__pp1)
      self.button_commande3[(0,1)].clicked.connect(self.__pp2)
      self.button_commande3[(0,2)].clicked.connect(self.__pp3)
      self.button_commande3[(0,3)].clicked.connect(self.__pp4)
      self.button_commande3[(1,0)].clicked.connect(self.__pp5)
      self.button_commande3[(1,1)].clicked.connect(self.__pp6)
      self.button_commande3[(1,2)].clicked.connect(self.__pp7)
      self.button_commande3[(1,3)].clicked.connect(self.__pp8)
      self.button_commande3[(2,0)].clicked.connect(self.__pp9)
      self.button_commande3[(2,1)].clicked.connect(self.__pp10)
      self.button_commande3[(2,2)].clicked.connect(self.__pp11)
      self.button_commande3[(2,3)].clicked.connect(self.__pp12)
      self.button_commande3[(3,0)].clicked.connect(self.__pp13)
      self.button_commande3[(3,1)].clicked.connect(self.__pp14)
      self.button_commande3[(3,2)].clicked.connect(self.__pp15)
      self.button_commande3[(3,3)].clicked.connect(self.__pp16)

      self.button_commande4[(0,0)].clicked.connect(self.___pp1)
      self.button_commande4[(0,1)].clicked.connect(self.___pp2)
      self.button_commande4[(0,2)].clicked.connect(self.___pp3)
      self.button_commande4[(0,3)].clicked.connect(self.___pp4)
      self.button_commande4[(1,0)].clicked.connect(self.___pp5)
      self.button_commande4[(1,1)].clicked.connect(self.___pp6)
      self.button_commande4[(1,2)].clicked.connect(self.___pp7)
      self.button_commande4[(1,3)].clicked.connect(self.___pp8)
      self.button_commande4[(2,0)].clicked.connect(self.___pp9)
      self.button_commande4[(2,1)].clicked.connect(self.___pp10)
      self.button_commande4[(2,2)].clicked.connect(self.___pp11)
      self.button_commande4[(2,3)].clicked.connect(self.___pp12)
      self.button_commande4[(3,0)].clicked.connect(self.___pp13)
      self.button_commande4[(3,1)].clicked.connect(self.___pp14)
      self.button_commande4[(3,2)].clicked.connect(self.___pp15)
      self.button_commande4[(3,3)].clicked.connect(self.___pp16)
      #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ DE 5 A 8

      self.button_commande5[(0,0)].clicked.connect(self.p1)
      self.button_commande5[(0,1)].clicked.connect(self.p2)
      self.button_commande5[(0,2)].clicked.connect(self.p3)
      self.button_commande5[(0,3)].clicked.connect(self.p4)
      self.button_commande5[(1,0)].clicked.connect(self.p5)
      self.button_commande5[(1,1)].clicked.connect(self.p6)
      self.button_commande5[(1,2)].clicked.connect(self.p7)
      self.button_commande5[(1,3)].clicked.connect(self.p8)
      self.button_commande5[(2,0)].clicked.connect(self.p9)
      self.button_commande5[(2,1)].clicked.connect(self.p10)
      self.button_commande5[(2,2)].clicked.connect(self.p11)
      self.button_commande5[(2,3)].clicked.connect(self.p12)
      self.button_commande5[(3,0)].clicked.connect(self.p13)
      self.button_commande5[(3,1)].clicked.connect(self.p14)
      self.button_commande5[(3,2)].clicked.connect(self.p15)
      self.button_commande5[(3,3)].clicked.connect(self.p16)

      self.button_commande6[(0,0)].clicked.connect(self._p1)
      self.button_commande6[(0,1)].clicked.connect(self._p2)
      self.button_commande6[(0,2)].clicked.connect(self._p3)
      self.button_commande6[(0,3)].clicked.connect(self._p4)
      self.button_commande6[(1,0)].clicked.connect(self._p5)
      self.button_commande6[(1,1)].clicked.connect(self._p6)
      self.button_commande6[(1,2)].clicked.connect(self._p7)
      self.button_commande6[(1,3)].clicked.connect(self._p8)
      self.button_commande6[(2,0)].clicked.connect(self._p9)
      self.button_commande6[(2,1)].clicked.connect(self._p10)
      self.button_commande6[(2,2)].clicked.connect(self._p11)
      self.button_commande6[(2,3)].clicked.connect(self._p12)
      self.button_commande6[(3,0)].clicked.connect(self._p13)
      self.button_commande6[(3,1)].clicked.connect(self._p14)
      self.button_commande6[(3,2)].clicked.connect(self._p15)
      self.button_commande6[(3,3)].clicked.connect(self._p16)

      self.button_commande7[(0,0)].clicked.connect(self.__p1)
      self.button_commande7[(0,1)].clicked.connect(self.__p2)
      self.button_commande7[(0,2)].clicked.connect(self.__p3)
      self.button_commande7[(0,3)].clicked.connect(self.__p4)
      self.button_commande7[(1,0)].clicked.connect(self.__p5)
      self.button_commande7[(1,1)].clicked.connect(self.__p6)
      self.button_commande7[(1,2)].clicked.connect(self.__p7)
      self.button_commande7[(1,3)].clicked.connect(self.__p8)
      self.button_commande7[(2,0)].clicked.connect(self.__p9)
      self.button_commande7[(2,1)].clicked.connect(self.__p10)
      self.button_commande7[(2,2)].clicked.connect(self.__p11)
      self.button_commande7[(2,3)].clicked.connect(self.__p12)
      self.button_commande7[(3,0)].clicked.connect(self.__p13)
      self.button_commande7[(3,1)].clicked.connect(self.__p14)
      self.button_commande7[(3,2)].clicked.connect(self.__p15)
      self.button_commande7[(3,3)].clicked.connect(self.__p16)

      self.button_commande8[(0,0)].clicked.connect(self.___p1)
      self.button_commande8[(0,1)].clicked.connect(self.___p2)
      self.button_commande8[(0,2)].clicked.connect(self.___p3)
      self.button_commande8[(0,3)].clicked.connect(self.___p4)
      self.button_commande8[(1,0)].clicked.connect(self.___p5)
      self.button_commande8[(1,1)].clicked.connect(self.___p6)
      self.button_commande8[(1,2)].clicked.connect(self.___p7)
      self.button_commande8[(1,3)].clicked.connect(self.___p8)
      self.button_commande8[(2,0)].clicked.connect(self.___p9)
      self.button_commande8[(2,1)].clicked.connect(self.___p10)
      self.button_commande8[(2,2)].clicked.connect(self.___p11)
      self.button_commande8[(2,3)].clicked.connect(self.___p12)
      self.button_commande8[(3,0)].clicked.connect(self.___p13)
      self.button_commande8[(3,1)].clicked.connect(self.___p14)
      self.button_commande8[(3,2)].clicked.connect(self.___p15)
      self.button_commande8[(3,3)].clicked.connect(self.___p16)
      
      #_________________________________________
      #_________________________________________
      #_________________________________________DASHBOARD

      #_______TITLE
      self.title_lab=QLabel('COMMANDES',self)
      self.title_lab.setStyleSheet("""
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:20pt;
                                  font-weight:bold
                                  """)
      self.title_lab.move(150,10)
      self.title_lab.resize(200,30)


      #_________________________________________ Button 1

      self.btn_valider=QPushButton('VALIDER',self)
      self.btn_valider.setStyleSheet("""
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
      self.btn_valider.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_valider.clicked.connect(self.validate_commande)
      self.btn_valider.move(500,20)
      self.btn_valider.resize(105,30)
      #_________________________________________ Button 2

      self.btn_annuler=QPushButton('ANNULER',self)
      self.btn_annuler.setStyleSheet("""
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
      self.btn_annuler.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_annuler.clicked.connect(self.abort_commande)
      self.btn_annuler.move(615,20)
      self.btn_annuler.resize(105,30)
      #_________________________________________ Button 3

      self.btn_return=QPushButton('RETOURNER',self)
      self.btn_return.setStyleSheet("""
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
      self.btn_return.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_return.clicked.connect(self.return_commande)
      self.btn_return.move(730,20)
      self.btn_return.resize(105,30)
      #_________________________________________ Button 4

      self.btn_livraison=QPushButton('LIVRER',self)
      self.btn_livraison.setStyleSheet("""
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
      self.btn_livraison.setCursor(QCursor(Qt.PointingHandCursor))
      #self.btn_livraison.clicked.connect(self.refresh_commande)
      self.btn_livraison.move(845,20)
      self.btn_livraison.resize(105,30)


      #=============================================
      #=============================================
      #=============================================
      #=============================================

      self.dash3_vente=QFrame(self)
      self.dash3_vente.setStyleSheet("""
                                background-color:transparent;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-radius:0px
                                """)
      
      self.dash3_vente.move(950,50)
      self.dash3_vente.resize(290,600)

      #_______PANIER LISTE

      self.list_commande=QListWidget(self.dash3_vente)
      self.list_commande.setStyleSheet("""
                                  QListWidget::item:selected{border-style:solid;border-width:3px;border-color:#000;
                                  background-color:crimson;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-style:solid;border-size:20px;border-color:crimson;border-radius:0px}
                                  
                                  QListWidget::item:!selected{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:0px}
                                  """)
      self.list_commande.move(0,0)
      self.list_commande.resize(290,600)
      
      self.list_commande.itemClicked.connect(self.selection_item)

      
      

      #=============================================
      #=============================================
      #=============================================
      #=============================================


      
      
      
      self.dash=QFrame(self)
      self.dash.setStyleSheet("""
                                background-color:#1b1b1c;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:10px;border-bottom-left-radius:10px;
                                border-bottom-right-radius:10px;border-top-right-radius:10px
                                """)
      self.dash.move(50,500)
      self.dash.resize(900,150)

      #____________________________________FRAME BTN VIEW

      self.f1=QFrame(self)            
      self.f1.setStyleSheet("""border-style:solid;border-width:3px;border-color:#000;
                                  background-color:transparent;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:10px
                            """)
      self.f1.move(500,50)
      self.f1.resize(450,400)
      
      self.btn_view=QToolButton(self.f1)
      self.btn_view.setStyleSheet("""
                                  QToolButton::pressed{background-color :transparent;color:#000;border-style:solid;
                                  border-width:3px;border-color:#000;font-family: Time;font-style:italic;font-size:8pt;
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
      #self.btn_view.clicked.connect(self.select_photo_commande)

      #_________________________________________DATAS PRODUCT
      #_______NOM
      self.nom_lab=QLabel('NOM PRODUIT',self.dash)
      self.nom_lab.setStyleSheet("""
                                  background-color:transparent;color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.nom_lab.move(10,5)
      self.nom_lab.resize(150,20)

      self.nom_commande=QLineEdit(self.dash)
      self.nom_commande.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.nom_commande.setAlignment(Qt.AlignCenter)
      self.nom_commande.move(10,25)
      self.nom_commande.resize(150,20)
      self.nom_commande.setEnabled(False)

      #_______QUANTITES
      self.qte_lab=QLabel('QUANTITES',self.dash)
      self.qte_lab.setStyleSheet("""
                                  background-color:transparent;color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.qte_lab.move(10,50)
      self.qte_lab.resize(150,20)

      self.qte_commande=QSpinBox(self.dash)
      self.qte_commande.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.qte_commande.setAlignment(Qt.AlignCenter)
      self.qte_commande.setMinimum(0)
      self.qte_commande.setMaximum(1000000)
      self.qte_commande.move(10,70)
      self.qte_commande.resize(150,20)
      self.qte_commande.setEnabled(False)

      #_______PRIX
      self.prix_lab=QLabel('PRIX UNITAIRE',self.dash)
      self.prix_lab.setStyleSheet("""
                                  background-color:transparent;color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.prix_lab.move(10,100)
      self.prix_lab.resize(150,20)

      self.prix_commande=QDoubleSpinBox(self.dash)
      self.prix_commande.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.prix_commande.setAlignment(Qt.AlignCenter)
      self.prix_commande.setMinimum(0)
      self.prix_commande.setMaximum(1000000)
      self.prix_commande.move(10,120)
      self.prix_commande.resize(150,20)
      self.prix_commande.setEnabled(False)

      #_______NOM CLIENT
      self.nom_client_lab=QLabel('NOM CLIENT',self.dash)
      self.nom_client_lab.setStyleSheet("""
                                  background-color:transparent;color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.nom_client_lab.move(420,5)
      self.nom_client_lab.resize(200,20)

      self.nom_client=QLineEdit(self.dash)
      self.nom_client.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.nom_client.setAlignment(Qt.AlignCenter)
      self.nom_client.move(420,25)
      self.nom_client.resize(200,20)

      #_______CNIB CLIENT
      self.cnib_client_lab=QLabel('CNIB CLIENT',self.dash)
      self.cnib_client_lab.setStyleSheet("""
                                  background-color:transparent;color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.cnib_client_lab.move(420,50)
      self.cnib_client_lab.resize(200,20)

      self.cnib_client=QLineEdit(self.dash)
      self.cnib_client.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.cnib_client.setAlignment(Qt.AlignCenter)
      self.cnib_client.move(420,70)
      self.cnib_client.resize(200,20)

      #_______ADRESSE CLIENT
      self.adresse_client_lab=QLabel('ADRESSE CLIENT',self.dash)
      self.adresse_client_lab.setStyleSheet("""
                                  background-color:transparent;color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.adresse_client_lab.move(420,100)
      self.adresse_client_lab.resize(150,20)

      self.adresse_client=QLineEdit(self.dash)
      self.adresse_client.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.adresse_client.setAlignment(Qt.AlignCenter)
      self.adresse_client.move(420,120)
      self.adresse_client.resize(200,20)

      #_______TYPES
      self.cat_lab=QLabel('TYPES PRODUIT',self.dash)
      self.cat_lab.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold
                                  """)
      self.cat_lab.move(180,5)
      self.cat_lab.resize(100,20)

      self.cat_commande=QLineEdit(self.dash)
      self.cat_commande.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.cat_commande.setAlignment(Qt.AlignCenter)
      self.cat_commande.move(180,25)
      self.cat_commande.resize(100,20)
      self.cat_commande.setEnabled(False)
      #self.cat_commande.currentIndexChanged.connect(self.selection_cat)

      #_______ID PRODUIT
      self.id_lab_produit=QLabel('ID PRODUIT',self.dash)
      self.id_lab_produit.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold
                                  """)
      self.id_lab_produit.move(180,50)
      self.id_lab_produit.resize(100,20)

      self.id_produit=QSpinBox(self.dash)
      self.id_produit.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.id_produit.setMaximum(1000000)
      self.id_produit.setAlignment(Qt.AlignCenter)
      self.id_produit.setValue(1)
      self.id_produit.setEnabled(False)
      self.id_produit.move(180,70)
      self.id_produit.resize(100,20)

      #_______CODE PRODUIT
      self.code_lab=QLabel('CODE PRODUIT',self.dash)
      self.code_lab.setStyleSheet("""
                                   background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold
                                  """)
      self.code_lab.move(180,100)
      self.code_lab.resize(100,20)

      self.code_produit=QLineEdit(self.dash)
      self.code_produit.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.code_produit.setAlignment(Qt.AlignCenter)
      self.code_produit.setEnabled(False)
      self.code_produit.move(180,120)
      self.code_produit.resize(100,20)

      #_______ID COMMANDE
      self.id_lab=QLabel('ID COMMANDE',self.dash)
      self.id_lab.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold
                                  """)
      self.id_lab.move(300,5)
      self.id_lab.resize(100,20)

      self.id_commande=QSpinBox(self.dash)
      self.id_commande.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.id_commande.setMaximum(1000000)
      self.id_commande.setAlignment(Qt.AlignCenter)
      self.id_commande.setValue(1)
      self.id_commande.setEnabled(False)
      self.id_commande.move(300,25)
      self.id_commande.resize(100,20)

      #_______CODE COMMANDE
      self.code_commande_lab=QLabel('CODE COMMANDE',self.dash)
      self.code_commande_lab.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold
                                  """)
      self.code_commande_lab.move(300,50)
      self.code_commande_lab.resize(100,20)

      self.code_commande=QLineEdit(self.dash)
      self.code_commande.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.code_commande.setAlignment(Qt.AlignCenter)
      self.code_commande.setEnabled(False)
      self.code_commande.move(300,70)
      self.code_commande.resize(100,20)


      #_______REDUCTION
      self.reduction_lab=QLabel('REDUCTION',self.dash)
      self.reduction_lab.setStyleSheet("""
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold
                                  """)
      self.reduction_lab.move(300,100)
      self.reduction_lab.resize(100,20)

      self.reduction=QLineEdit(self.dash)
      self.reduction.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.reduction.setAlignment(Qt.AlignCenter)
      self.reduction.setEnabled(False)
      self.reduction.move(300,120)
      self.reduction.resize(100,20)

      self.btn_refresh=QPushButton('REFRESH',self.dash)
      self.btn_refresh.setStyleSheet("""
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
      self.btn_refresh.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_refresh.clicked.connect(self.refresh_commande)
      self.btn_refresh.move(640,5)
      self.btn_refresh.resize(105,20)

      self.btn_retirer=QPushButton('RETIRER',self.dash)
      self.btn_retirer.setStyleSheet("""
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
      self.btn_retirer.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_retirer.clicked.connect(self.retirer_produit)
      self.btn_retirer.move(750,5)
      self.btn_retirer.resize(105,20)

      #_______NUMERO TABLE
      self.lab_num_table=QLabel('NUMERO TABLE ',self.dash)
      self.lab_num_table.setStyleSheet("""
                                  background-color:transparent;color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.lab_num_table.move(640,50)
      self.lab_num_table.resize(100,20)

      self.num_table=QLineEdit(self.dash)
      self.num_table.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.num_table.setAlignment(Qt.AlignCenter)
      self.num_table.move(640,70)
      self.num_table.resize(100,20)
      self.num_table.setEnabled(False)

      #_______TOTAL COMMANDE
      self.lab_num_client=QLabel('TOTAL CLIENT ',self.dash)
      self.lab_num_client.setStyleSheet("""
                                  background-color:transparent;color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.lab_num_client.move(640,100)
      self.lab_num_client.resize(100,20)

      self.num_client=QLineEdit(self.dash)
      self.num_client.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.num_client.setAlignment(Qt.AlignCenter)
      self.num_client.move(640,120)
      self.num_client.resize(100,20)
      self.num_client.setEnabled(False)


      #=====BTN TOTAL A PAYER
      self.btn_total=QToolButton(self)
      self.btn_total.setStyleSheet("""
                                  QToolButton::pressed{background-color :#1b1b1c;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#1b1b1c;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::hover{background-color :#fff;color:#1b1b1c;border-style:solid;
                                  border-width:3px;border-color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:10px}
                                """)
      self.btn_total.move(50,700)
      self.btn_total.resize(600,85)
      self.btn_total.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
      self.btn_total.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_total.clicked.connect(self.refresh_commande)
      self.btn_total.setIcon(QIcon('png/argent.png'))
      self.btn_total.setIconSize(QSize(60,60))
      self.btn_total.setText("PRODUITS: 0 --- A PAYER: 0 FCFA")

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

      #______________________________________________INTERFACE  PRODUITS END
      self.list_commande.show()
      self.dash.show()

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

         
                  
   def pp1(self):
      if self.button_commande1[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(0,0)].icon()))
         self.btn_view.setText(str(self.button_commande1[(0,0)].text()))
         self.button_commande1[(0,0)].setFocus()
         self.f1.show();self.id_commande.setValue(1)
         self.information_commande()
   def pp2(self):
      if self.button_commande1[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(0,1)].icon()))
         self.btn_view.setText(str(self.button_commande1[(0,1)].text()))
         self.button_commande1[(0,1)].setFocus()
         self.f1.show();self.id_commande.setValue(2)
         self.information_commande()
   def pp3(self):
      if self.button_commande1[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(0,2)].icon()))
         self.btn_view.setText(str(self.button_commande1[(0,2)].text()))
         self.button_commande1[(0,2)].setFocus()
         self.f1.show();self.id_commande.setValue(3)
         self.information_commande()
   def pp4(self):
      if self.button_commande1[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(0,3)].icon()))
         self.btn_view.setText(str(self.button_commande1[(0,3)].text()))
         self.button_commande1[(0,3)].setFocus()
         self.f1.show();self.id_commande.setValue(4)
         self.information_commande()
   def pp5(self):
      if self.button_commande1[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(1,0)].icon()))
         self.btn_view.setText(str(self.button_commande1[(1,0)].text()))
         self.button_commande1[(1,0)].setFocus()
         self.f1.show();self.id_commande.setValue(5)
         self.information_commande()
   def pp6(self):
      if self.button_commande1[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(1,1)].icon()))
         self.btn_view.setText(str(self.button_commande1[(1,1)].text()))
         self.button_commande1[(1,1)].setFocus()
         self.f1.show();self.id_commande.setValue(6)
         self.information_commande()
   def pp7(self):
      if self.button_commande1[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(1,2)].icon()))
         self.btn_view.setText(str(self.button_commande1[(1,2)].text()))
         self.button_commande1[(1,2)].setFocus()
         self.f1.show();self.id_commande.setValue(7)
         self.information_commande()
   def pp8(self):
      if self.button_commande1[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(1,3)].icon()))
         self.btn_view.setText(str(self.button_commande1[(1,3)].text()))
         self.button_commande1[(1,3)].setFocus()
         self.f1.show();self.id_commande.setValue(8)
         self.information_commande()
   def pp9(self):
      if self.button_commande1[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(2,0)].icon()))
         self.btn_view.setText(str(self.button_commande1[(2,0)].text()))
         self.button_commande1[(2,0)].setFocus()
         self.f1.show();self.id_commande.setValue(9)
         self.information_commande()
   def pp10(self):
      if self.button_commande1[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(2,1)].icon()))
         self.btn_view.setText(str(self.button_commande1[(2,1)].text()))
         self.button_commande1[(2,1)].setFocus()
         self.f1.show();self.id_commande.setValue(10)
         self.information_commande()
   def pp11(self):
      if self.button_commande1[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(2,2)].icon()))
         self.btn_view.setText(str(self.button_commande1[(2,2)].text()))
         self.button_commande1[(2,2)].setFocus()
         self.f1.show();self.id_commande.setValue(11)
         self.information_commande()
   def pp12(self):
      if self.button_commande1[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(2,3)].icon()))
         self.btn_view.setText(str(self.button_commande1[(2,3)].text()))
         self.button_commande1[(2,3)].setFocus()
         self.f1.show();self.id_commande.setValue(12)
         self.information_commande()
   def pp13(self):
      if self.button_commande1[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(3,0)].icon()))
         self.btn_view.setText(str(self.button_commande1[(3,0)].text()))
         self.button_commande1[(3,0)].setFocus()
         self.f1.show();self.id_commande.setValue(13)
         self.information_commande()
   def pp14(self):
      if self.button_commande1[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(3,1)].icon()))
         self.btn_view.setText(str(self.button_commande1[(3,1)].text()))
         self.button_commande1[(3,1)].setFocus()
         self.f1.show();self.id_commande.setValue(14)
         self.information_commande()
   def pp15(self):
      if self.button_commande1[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(3,2)].icon()))
         self.btn_view.setText(str(self.button_commande1[(3,2)].text()))
         self.button_commande1[(3,2)].setFocus()
         self.f1.show();self.id_commande.setValue(15)
         self.information_commande()
   def pp16(self):
      if self.button_commande1[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande1[(3,3)].icon()))
         self.btn_view.setText(str(self.button_commande1[(3,3)].text()))
         self.button_commande1[(3,3)].setFocus()
         self.f1.show();self.id_commande.setValue(16)
         self.information_commande()
   def _pp1(self):
      if self.button_commande2[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(0,0)].icon()))
         self.btn_view.setText(str(self.button_commande2[(0,0)].text()))
         self.button_commande2[(0,0)].setFocus()
         self.f1.show();self.id_commande.setValue(17)
         self.information_commande()
   def _pp2(self):
      if self.button_commande2[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(0,1)].icon()))
         self.btn_view.setText(str(self.button_commande2[(0,1)].text()))
         self.button_commande2[(0,1)].setFocus()
         self.f1.show();self.id_commande.setValue(18)
         self.information_commande()
   def _pp3(self):
      if self.button_commande2[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(0,2)].icon()))
         self.btn_view.setText(str(self.button_commande2[(0,2)].text()))
         self.button_commande2[(0,2)].setFocus()
         self.f1.show();self.id_commande.setValue(19)
         self.information_commande()
   def _pp4(self):
      if self.button_commande2[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(0,3)].icon()))
         self.btn_view.setText(str(self.button_commande2[(0,3)].text()))
         self.button_commande2[(0,3)].setFocus()
         self.f1.show();self.id_commande.setValue(20)
         self.information_commande()
   def _pp5(self):
      if self.button_commande2[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(1,0)].icon()))
         self.btn_view.setText(str(self.button_commande2[(1,0)].text()))
         self.button_commande2[(1,0)].setFocus()
         self.f1.show();self.id_commande.setValue(21)
         self.information_commande()
   def _pp6(self):
      if self.button_commande2[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(1,1)].icon()))
         self.btn_view.setText(str(self.button_commande2[(1,1)].text()))
         self.button_commande2[(1,1)].setFocus()
         self.f1.show();self.id_commande.setValue(22)
         self.information_commande()
   def _pp7(self):
      if self.button_commande2[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(1,2)].icon()))
         self.btn_view.setText(str(self.button_commande2[(1,2)].text()))
         self.button_commande2[(1,2)].setFocus()
         self.f1.show();self.id_commande.setValue(23)
         self.information_commande()
   def _pp8(self):
      if self.button_commande2[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(1,3)].icon()))
         self.btn_view.setText(str(self.button_commande2[(1,3)].text()))
         self.button_commande2[(1,3)].setFocus()
         self.f1.show();self.id_commande.setValue(24)
         self.information_commande()
   def _pp9(self):
      if self.button_commande2[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(2,0)].icon()))
         self.btn_view.setText(str(self.button_commande2[(2,0)].text()))
         self.button_commande2[(2,0)].setFocus()
         self.f1.show();self.id_commande.setValue(25)
         self.information_commande()
   def _pp10(self):
      if self.button_commande2[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(2,1)].icon()))
         self.btn_view.setText(str(self.button_commande2[(2,1)].text()))
         self.button_commande2[(2,1)].setFocus()
         self.f1.show();self.id_commande.setValue(26)
         self.information_commande()
   def _pp11(self):
      if self.button_commande2[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(2,2)].icon()))
         self.btn_view.setText(str(self.button_commande2[(2,2)].text()))
         self.button_commande2[(2,2)].setFocus()
         self.f1.show();self.id_commande.setValue(27)
         self.information_commande()
   def _pp12(self):
      if self.button_commande2[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(2,3)].icon()))
         self.btn_view.setText(str(self.button_commande2[(2,3)].text()))
         self.button_commande2[(2,3)].setFocus()
         self.f1.show();self.id_commande.setValue(28)
         self.information_commande()
   def _pp13(self):
      if self.button_commande2[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(3,0)].icon()))
         self.btn_view.setText(str(self.button_commande2[(3,0)].text()))
         self.button_commande2[(3,0)].setFocus()
         self.f1.show();self.id_commande.setValue(29)
         self.information_commande()
   def _pp14(self):
      if self.button_commande2[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(3,1)].icon()))
         self.btn_view.setText(str(self.button_commande2[(3,1)].text()))
         self.button_commande2[(3,1)].setFocus()
         self.f1.show();self.id_commande.setValue(30)
         self.information_commande()
   def _pp15(self):
      if self.button_commande2[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(3,2)].icon()))
         self.btn_view.setText(str(self.button_commande2[(3,2)].text()))
         self.button_commande2[(3,2)].setFocus()
         self.f1.show();self.id_commande.setValue(31)
         self.information_commande()
   def _pp16(self):
      if self.button_commande2[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande2[(3,3)].icon()))
         self.btn_view.setText(str(self.button_commande2[(3,3)].text()))
         self.button_commande2[(3,3)].setFocus()
         self.f1.show();self.id_commande.setValue(32)
         self.information_commande()

   def __pp1(self):
      if self.button_commande3[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(0,0)].icon()))
         self.btn_view.setText(str(self.button_commande3[(0,0)].text()))
         self.button_commande3[(0,0)].setFocus()
         self.f1.show();self.id_commande.setValue(33)
         self.information_commande()
   def __pp2(self):
      if self.button_commande3[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(0,1)].icon()))
         self.btn_view.setText(str(self.button_commande3[(0,1)].text()))
         self.button_commande3[(0,1)].setFocus()
         self.f1.show();self.id_commande.setValue(34)
         self.information_commande()
   def __pp3(self):
      if self.button_commande3[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(0,2)].icon()))
         self.btn_view.setText(str(self.button_commande3[(0,2)].text()))
         self.button_commande3[(0,2)].setFocus()
         self.f1.show();self.id_commande.setValue(35)
         self.information_commande()
   def __pp4(self):
      if self.button_commande3[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(0,3)].icon()))
         self.btn_view.setText(str(self.button_commande3[(0,3)].text()))
         self.button_commande3[(0,3)].setFocus()
         self.f1.show();self.id_commande.setValue(36)
         self.information_commande()
   def __pp5(self):
      if self.button_commande3[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(1,0)].icon()))
         self.btn_view.setText(str(self.button_commande3[(1,0)].text()))
         self.button_commande3[(1,0)].setFocus()
         self.f1.show();self.id_commande.setValue(37)
         self.information_commande()
   def __pp6(self):
      if self.button_commande3[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(1,1)].icon()))
         self.btn_view.setText(str(self.button_commande3[(1,1)].text()))
         self.button_commande3[(1,1)].setFocus()
         self.f1.show();self.id_commande.setValue(38)
         self.information_commande()
   def __pp7(self):
      if self.button_commande3[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(1,2)].icon()))
         self.btn_view.setText(str(self.button_commande3[(1,2)].text()))
         self.button_commande3[(1,2)].setFocus()
         self.f1.show();self.id_commande.setValue(39)
         self.information_commande()
   def __pp8(self):
      if self.button_commande3[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(1,3)].icon()))
         self.btn_view.setText(str(self.button_commande3[(1,3)].text()))
         self.button_commande3[(1,3)].setFocus()
         self.f1.show();self.id_commande.setValue(40)
         self.information_commande()
   def __pp9(self):
      if self.button_commande3[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(2,0)].icon()))
         self.btn_view.setText(str(self.button_commande3[(2,0)].text()))
         self.button_commande3[(2,0)].setFocus()
         self.f1.show();self.id_commande.setValue(41)
         self.information_commande()
   def __pp10(self):
      if self.button_commande3[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(2,1)].icon()))
         self.btn_view.setText(str(self.button_commande3[(2,1)].text()))
         self.button_commande3[(2,1)].setFocus()
         self.f1.show();self.id_commande.setValue(42)
         self.information_commande()
   def __pp11(self):
      if self.button_commande3[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(2,2)].icon()))
         self.btn_view.setText(str(self.button_commande3[(2,2)].text()))
         self.button_commande3[(2,2)].setFocus()
         self.f1.show();self.id_commande.setValue(43)
         self.information_commande()
   def __pp12(self):
      if self.button_commande3[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(2,3)].icon()))
         self.btn_view.setText(str(self.button_commande3[(2,3)].text()))
         self.button_commande3[(2,3)].setFocus()
         self.f1.show();self.id_commande.setValue(44)
         self.information_commande()
   def __pp13(self):
      if self.button_commande3[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(3,0)].icon()))
         self.btn_view.setText(str(self.button_commande3[(3,0)].text()))
         self.button_commande3[(3,0)].setFocus()
         self.f1.show();self.id_commande.setValue(45)
         self.information_commande()
   def __pp14(self):
      if self.button_commande3[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(3,1)].icon()))
         self.btn_view.setText(str(self.button_commande3[(3,1)].text()))
         self.button_commande3[(3,1)].setFocus()
         self.f1.show();self.id_commande.setValue(46)
         self.information_commande()
   def __pp15(self):
      if self.button_commande3[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(3,2)].icon()))
         self.btn_view.setText(str(self.button_commande3[(3,2)].text()))
         self.button_commande3[(3,2)].setFocus()
         self.f1.show();self.id_commande.setValue(47)
         self.information_commande()
   def __pp16(self):
      if self.button_commande3[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande3[(3,3)].icon()))
         self.btn_view.setText(str(self.button_commande3[(3,3)].text()))
         self.button_commande3[(3,3)].setFocus()
         self.f1.show();self.id_commande.setValue(48)
         self.information_commande()
   def ___pp1(self):
      if self.button_commande4[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(0,0)].icon()))
         self.btn_view.setText(str(self.button_commande4[(0,0)].text()))
         self.button_commande4[(0,0)].setFocus()
         self.f1.show();self.id_commande.setValue(49)
         self.information_commande()
   def ___pp2(self):
      if self.button_commande4[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(0,1)].icon()))
         self.btn_view.setText(str(self.button_commande4[(0,1)].text()))
         self.button_commande4[(0,1)].setFocus()
         self.f1.show();self.id_commande.setValue(50)
         self.information_commande()
   def ___pp3(self):
      if self.button_commande4[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(0,2)].icon()))
         self.btn_view.setText(str(self.button_commande4[(0,2)].text()))
         self.button_commande4[(0,2)].setFocus()
         self.f1.show();self.id_commande.setValue(51)
         self.information_commande()
   def ___pp4(self):
      if self.button_commande4[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(0,3)].icon()))
         self.btn_view.setText(str(self.button_commande4[(0,3)].text()))
         self.button_commande4[(0,3)].setFocus()
         self.f1.show();self.id_commande.setValue(52)
         self.information_commande()
   def ___pp5(self):
      if self.button_commande4[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(1,0)].icon()))
         self.btn_view.setText(str(self.button_commande4[(1,0)].text()))
         self.button_commande4[(1,0)].setFocus()
         self.f1.show();self.id_commande.setValue(53)
         self.information_commande()
   def ___pp6(self):
      if self.button_commande4[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(1,1)].icon()))
         self.btn_view.setText(str(self.button_commande4[(1,1)].text()))
         self.button_commande4[(1,1)].setFocus()
         self.f1.show();self.id_commande.setValue(54)
         self.information_commande()
   def ___pp7(self):
      if self.button_commande4[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(1,2)].icon()))
         self.btn_view.setText(str(self.button_commande4[(1,2)].text()))
         self.button_commande4[(1,2)].setFocus()
         self.f1.show();self.id_commande.setValue(55)
         self.information_commande()
   def ___pp8(self):
      if self.button_commande4[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(1,3)].icon()))
         self.btn_view.setText(str(self.button_commande4[(1,3)].text()))
         self.button_commande4[(1,3)].setFocus()
         self.f1.show();self.id_commande.setValue(56)
         self.information_commande()
   def ___pp9(self):
      if self.button_commande4[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(2,0)].icon()))
         self.btn_view.setText(str(self.button_commande4[(2,0)].text()))
         self.button_commande4[(2,0)].setFocus()
         self.f1.show();self.id_commande.setValue(57)
         self.information_commande()
   def ___pp10(self):
      if self.button_commande4[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(2,1)].icon()))
         self.btn_view.setText(str(self.button_commande4[(2,1)].text()))
         self.button_commande4[(2,1)].setFocus()
         self.f1.show();self.id_commande.setValue(58)
         self.information_commande()
   def ___pp11(self):
      if self.button_commande4[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(2,2)].icon()))
         self.btn_view.setText(str(self.button_commande4[(2,2)].text()))
         self.button_commande4[(2,2)].setFocus()
         self.f1.show();self.id_commande.setValue(59)
         self.information_commande()
   def ___pp12(self):
      if self.button_commande4[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(2,3)].icon()))
         self.btn_view.setText(str(self.button_commande4[(2,3)].text()))
         self.button_commande4[(2,3)].setFocus()
         self.f1.show();self.id_commande.setValue(60)
         self.information_commande()
   def ___pp13(self):
      if self.button_commande4[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(3,0)].icon()))
         self.btn_view.setText(str(self.button_commande4[(3,0)].text()))
         self.button_commande4[(3,0)].setFocus()
         self.f1.show();self.id_commande.setValue(61)
         self.information_commande()
   def ___pp14(self):
      if self.button_commande4[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(3,1)].icon()))
         self.btn_view.setText(str(self.button_commande4[(3,1)].text()))
         self.button_commande4[(3,1)].setFocus()
         self.f1.show();self.id_commande.setValue(62)
         self.information_commande()
   def ___pp15(self):
      if self.button_commande4[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(3,2)].icon()))
         self.btn_view.setText(str(self.button_commande4[(3,2)].text()))
         self.button_commande4[(3,2)].setFocus()
         self.f1.show();self.id_commande.setValue(63)
         self.information_commande()
   def ___pp16(self):
      if self.button_commande4[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande4[(3,3)].icon()))
         self.btn_view.setText(str(self.button_commande4[(3,3)].text()))
         self.button_commande4[(3,3)].setFocus()
         self.f1.show();self.id_commande.setValue(64)
         self.information_commande()

   #++++++++++++++++++++++++++++++++++++++  PAGE PANIER 5 A 8

   def p1(self):
      if self.button_commande5[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(0,0)].icon()))
         self.btn_view.setText(str(self.button_commande5[(0,0)].text()))
         self.button_commande5[(0,0)].setFocus()
         self.f1.show();self.id_commande.setValue(65)
         self.information_commande()
   def p2(self):
      if self.button_commande5[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(0,1)].icon()))
         self.btn_view.setText(str(self.button_commande5[(0,1)].text()))
         self.button_commande5[(0,1)].setFocus()
         self.f1.show();self.id_commande.setValue(66)
         self.information_commande()
   def p3(self):
      if self.button_commande5[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(0,2)].icon()))
         self.btn_view.setText(str(self.button_commande5[(0,2)].text()))
         self.button_commande5[(0,2)].setFocus()
         self.f1.show();self.id_commande.setValue(67)
         self.information_commande()
   def p4(self):
      if self.button_commande5[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(0,3)].icon()))
         self.btn_view.setText(str(self.button_commande5[(0,3)].text()))
         self.button_commande5[(0,3)].setFocus()
         self.f1.show();self.id_commande.setValue(68)
         self.information_commande()
   def p5(self):
      if self.button_commande5[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(1,0)].icon()))
         self.btn_view.setText(str(self.button_commande5[(1,0)].text()))
         self.button_commande5[(1,0)].setFocus()
         self.f1.show();self.id_commande.setValue(69)
         self.information_commande()
   def p6(self):
      if self.button_commande5[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(1,1)].icon()))
         self.btn_view.setText(str(self.button_commande5[(1,1)].text()))
         self.button_commande5[(1,1)].setFocus()
         self.f1.show();self.id_commande.setValue(70)
         self.information_commande()
   def p7(self):
      if self.button_commande5[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(1,2)].icon()))
         self.btn_view.setText(str(self.button_commande5[(1,2)].text()))
         self.button_commande5[(1,2)].setFocus()
         self.f1.show();self.id_commande.setValue(71)
         self.information_commande()
   def p8(self):
      if self.button_commande5[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(1,3)].icon()))
         self.btn_view.setText(str(self.button_commande5[(1,3)].text()))
         self.button_commande5[(1,3)].setFocus()
         self.f1.show();self.id_commande.setValue(72)
         self.information_commande()
   def p9(self):
      if self.button_commande5[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(2,0)].icon()))
         self.btn_view.setText(str(self.button_commande5[(2,0)].text()))
         self.button_commande5[(2,0)].setFocus()
         self.f1.show();self.id_commande.setValue(73)
         self.information_commande()
   def p10(self):
      if self.button_commande5[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(2,1)].icon()))
         self.btn_view.setText(str(self.button_commande5[(2,1)].text()))
         self.button_commande5[(2,1)].setFocus()
         self.f1.show();self.id_commande.setValue(74)
         self.information_commande()
   def p11(self):
      if self.button_commande5[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(2,2)].icon()))
         self.btn_view.setText(str(self.button_commande5[(2,2)].text()))
         self.button_commande5[(2,2)].setFocus()
         self.f1.show();self.id_commande.setValue(75)
         self.information_commande()
   def p12(self):
      if self.button_commande5[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(2,3)].icon()))
         self.btn_view.setText(str(self.button_commande5[(2,3)].text()))
         self.button_commande5[(2,3)].setFocus()
         self.f1.show();self.id_commande.setValue(76)
         self.information_commande()
   def p13(self):
      if self.button_commande5[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(3,0)].icon()))
         self.btn_view.setText(str(self.button_commande5[(3,0)].text()))
         self.button_commande5[(3,0)].setFocus()
         self.f1.show();self.id_commande.setValue(77)
         self.information_commande()
   def p14(self):
      if self.button_commande5[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(3,1)].icon()))
         self.btn_view.setText(str(self.button_commande5[(3,1)].text()))
         self.button_commande5[(3,1)].setFocus()
         self.f1.show();self.id_commande.setValue(78)
         self.information_commande()
   def p15(self):
      if self.button_commande5[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(3,2)].icon()))
         self.btn_view.setText(str(self.button_commande5[(3,2)].text()))
         self.button_commande5[(3,2)].setFocus()
         self.f1.show();self.id_commande.setValue(79)
         self.information_commande()
   def p16(self):
      if self.button_commande5[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande5[(3,3)].icon()))
         self.btn_view.setText(str(self.button_commande5[(3,3)].text()))
         self.button_commande5[(3,3)].setFocus()
         self.f1.show();self.id_commande.setValue(80)
         self.information_commande()
   def _p1(self):
      if self.button_commande6[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(0,0)].icon()))
         self.btn_view.setText(str(self.button_commande6[(0,0)].text()))
         self.button_commande6[(0,0)].setFocus()
         self.f1.show();self.id_commande.setValue(81)
         self.information_commande()
   def _p2(self):
      if self.button_commande6[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(0,1)].icon()))
         self.btn_view.setText(str(self.button_commande6[(0,1)].text()))
         self.button_commande6[(0,1)].setFocus()
         self.f1.show();self.id_commande.setValue(82)
         self.information_commande()
   def _p3(self):
      if self.button_commande6[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(0,2)].icon()))
         self.btn_view.setText(str(self.button_commande6[(0,2)].text()))
         self.button_commande6[(0,2)].setFocus()
         self.f1.show();self.id_commande.setValue(83)
         self.information_commande()
   def _p4(self):
      if self.button_commande6[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(0,3)].icon()))
         self.btn_view.setText(str(self.button_commande6[(0,3)].text()))
         self.button_commande6[(0,3)].setFocus()
         self.f1.show();self.id_commande.setValue(84)
         self.information_commande()
   def _p5(self):
      if self.button_commande6[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(1,0)].icon()))
         self.btn_view.setText(str(self.button_commande6[(1,0)].text()))
         self.button_commande6[(1,0)].setFocus()
         self.f1.show();self.id_commande.setValue(85)
         self.information_commande()
   def _p6(self):
      if self.button_commande6[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(1,1)].icon()))
         self.btn_view.setText(str(self.button_commande6[(1,1)].text()))
         self.button_commande6[(1,1)].setFocus()
         self.f1.show();self.id_commande.setValue(86)
         self.information_commande()
   def _p7(self):
      if self.button_commande6[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(1,2)].icon()))
         self.btn_view.setText(str(self.button_commande6[(1,2)].text()))
         self.button_commande6[(1,2)].setFocus()
         self.f1.show();self.id_commande.setValue(87)
         self.information_commande()
   def _p8(self):
      if self.button_commande6[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(1,3)].icon()))
         self.btn_view.setText(str(self.button_commande6[(1,3)].text()))
         self.button_commande6[(1,3)].setFocus()
         self.f1.show();self.id_commande.setValue(88)
         self.information_commande()
   def _p9(self):
      if self.button_commande6[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(2,0)].icon()))
         self.btn_view.setText(str(self.button_commande6[(2,0)].text()))
         self.button_commande6[(2,0)].setFocus()
         self.f1.show();self.id_commande.setValue(89)
         self.information_commande()
   def _p10(self):
      if self.button_commande6[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(2,1)].icon()))
         self.btn_view.setText(str(self.button_commande6[(2,1)].text()))
         self.button_commande6[(2,1)].setFocus()
         self.f1.show();self.id_commande.setValue(90)
         self.information_commande()
   def _p11(self):
      if self.button_commande6[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(2,2)].icon()))
         self.btn_view.setText(str(self.button_commande6[(2,2)].text()))
         self.button_commande6[(2,2)].setFocus()
         self.f1.show();self.id_commande.setValue(91)
         self.information_commande()
   def _p12(self):
      if self.button_commande6[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(2,3)].icon()))
         self.btn_view.setText(str(self.button_commande6[(2,3)].text()))
         self.button_commande6[(2,3)].setFocus()
         self.f1.show();self.id_commande.setValue(92)
         self.information_commande()
   def _p13(self):
      if self.button_commande6[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(3,0)].icon()))
         self.btn_view.setText(str(self.button_commande6[(3,0)].text()))
         self.button_commande6[(3,0)].setFocus()
         self.f1.show();self.id_commande.setValue(93)
         self.information_commande()
   def _p14(self):
      if self.button_commande6[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(3,1)].icon()))
         self.btn_view.setText(str(self.button_commande6[(3,1)].text()))
         self.button_commande6[(3,1)].setFocus()
         self.f1.show();self.id_commande.setValue(94)
         self.information_commande()
   def _p15(self):
      if self.button_commande6[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(3,2)].icon()))
         self.btn_view.setText(str(self.button_commande6[(3,2)].text()))
         self.button_commande6[(3,2)].setFocus()
         self.f1.show();self.id_commande.setValue(95)
         self.information_commande()
   def _p16(self):
      if self.button_commande6[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande6[(3,3)].icon()))
         self.btn_view.setText(str(self.button_commande6[(3,3)].text()))
         self.button_commande6[(3,3)].setFocus()
         self.f1.show();self.id_commande.setValue(96)
         self.information_commande()

   def __p1(self):
      if self.button_commande7[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(0,0)].icon()))
         self.btn_view.setText(str(self.button_commande7[(0,0)].text()))
         self.button_commande7[(0,0)].setFocus()
         self.f1.show();self.id_commande.setValue(97)
         self.information_commande()
   def __p2(self):
      if self.button_commande7[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(0,1)].icon()))
         self.btn_view.setText(str(self.button_commande7[(0,1)].text()))
         self.button_commande7[(0,1)].setFocus()
         self.f1.show();self.id_commande.setValue(98)
         self.information_commande()
   def __p3(self):
      if self.button_commande7[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(0,2)].icon()))
         self.btn_view.setText(str(self.button_commande7[(0,2)].text()))
         self.button_commande7[(0,2)].setFocus()
         self.f1.show();self.id_commande.setValue(99)
         self.information_commande()
   def __p4(self):
      if self.button_commande7[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(0,3)].icon()))
         self.btn_view.setText(str(self.button_commande7[(0,3)].text()))
         self.button_commande7[(0,3)].setFocus()
         self.f1.show();self.id_commande.setValue(100)
         self.information_commande()
   def __p5(self):
      if self.button_commande7[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(1,0)].icon()))
         self.btn_view.setText(str(self.button_commande7[(1,0)].text()))
         self.button_commande7[(1,0)].setFocus()
         self.f1.show();self.id_commande.setValue(101)
         self.information_commande()
   def __p6(self):
      if self.button_commande7[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(1,1)].icon()))
         self.btn_view.setText(str(self.button_commande7[(1,1)].text()))
         self.button_commande7[(1,1)].setFocus()
         self.f1.show();self.id_commande.setValue(102)
         self.information_commande()
   def __p7(self):
      if self.button_commande7[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(1,2)].icon()))
         self.btn_view.setText(str(self.button_commande7[(1,2)].text()))
         self.button_commande7[(1,2)].setFocus()
         self.f1.show();self.id_commande.setValue(103)
         self.information_commande()
   def __p8(self):
      if self.button_commande7[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(1,3)].icon()))
         self.btn_view.setText(str(self.button_commande7[(1,3)].text()))
         self.button_commande7[(1,3)].setFocus()
         self.f1.show();self.id_commande.setValue(104)
         self.information_commande()
   def __p9(self):
      if self.button_commande7[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(2,0)].icon()))
         self.btn_view.setText(str(self.button_commande7[(2,0)].text()))
         self.button_commande7[(2,0)].setFocus()
         self.f1.show();self.id_commande.setValue(105)
         self.information_commande()
   def __p10(self):
      if self.button_commande7[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(2,1)].icon()))
         self.btn_view.setText(str(self.button_commande7[(2,1)].text()))
         self.button_commande7[(2,1)].setFocus()
         self.f1.show();self.id_commande.setValue(106)
         self.information_commande()
   def __p11(self):
      if self.button_commande7[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(2,2)].icon()))
         self.btn_view.setText(str(self.button_commande7[(2,2)].text()))
         self.button_commande7[(2,2)].setFocus()
         self.f1.show();self.id_commande.setValue(107)
         self.information_commande()
   def __p12(self):
      if self.button_commande7[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(2,3)].icon()))
         self.btn_view.setText(str(self.button_commande7[(2,3)].text()))
         self.button_commande7[(2,3)].setFocus()
         self.f1.show();self.id_commande.setValue(108)
         self.information_commande()
   def __p13(self):
      if self.button_commande7[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(3,0)].icon()))
         self.btn_view.setText(str(self.button_commande7[(3,0)].text()))
         self.button_commande7[(3,0)].setFocus()
         self.f1.show();self.id_commande.setValue(109)
         self.information_commande()
   def __p14(self):
      if self.button_commande7[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(3,1)].icon()))
         self.btn_view.setText(str(self.button_commande7[(3,1)].text()))
         self.button_commande7[(3,1)].setFocus()
         self.f1.show();self.id_commande.setValue(110)
         self.information_commande()
   def __p15(self):
      if self.button_commande7[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(3,2)].icon()))
         self.btn_view.setText(str(self.button_commande7[(3,2)].text()))
         self.button_commande7[(3,2)].setFocus()
         self.f1.show();self.id_commande.setValue(111)
         self.information_commande()
   def __p16(self):
      if self.button_commande7[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande7[(3,3)].icon()))
         self.btn_view.setText(str(self.button_commande7[(3,3)].text()))
         self.button_commande7[(3,3)].setFocus()
         self.f1.show();self.id_commande.setValue(112)
         self.information_commande()
   def ___p1(self):
      if self.button_commande8[(0,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(0,0)].icon()))
         self.btn_view.setText(str(self.button_commande8[(0,0)].text()))
         self.button_commande8[(0,0)].setFocus()
         self.f1.show();self.id_commande.setValue(113)
         self.information_commande()
   def ___p2(self):
      if self.button_commande8[(0,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(0,1)].icon()))
         self.btn_view.setText(str(self.button_commande8[(0,1)].text()))
         self.button_commande8[(0,1)].setFocus()
         self.f1.show();self.id_commande.setValue(114)
         self.information_commande()
   def ___p3(self):
      if self.button_commande8[(0,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(0,2)].icon()))
         self.btn_view.setText(str(self.button_commande8[(0,2)].text()))
         self.button_commande8[(0,2)].setFocus()
         self.f1.show();self.id_commande.setValue(115)
         self.information_commande()
   def ___p4(self):
      if self.button_commande8[(0,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(0,3)].icon()))
         self.btn_view.setText(str(self.button_commande8[(0,3)].text()))
         self.button_commande8[(0,3)].setFocus()
         self.f1.show();self.id_commande.setValue(116)
         self.information_commande()
   def ___p5(self):
      if self.button_commande8[(1,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(1,0)].icon()))
         self.btn_view.setText(str(self.button_commande8[(1,0)].text()))
         self.button_commande8[(1,0)].setFocus()
         self.f1.show();self.id_commande.setValue(117)
         self.information_commande()
   def ___p6(self):
      if self.button_commande8[(1,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(1,1)].icon()))
         self.btn_view.setText(str(self.button_commande8[(1,1)].text()))
         self.button_commande8[(1,1)].setFocus()
         self.f1.show();self.id_commande.setValue(118)
         self.information_commande()
   def ___p7(self):
      if self.button_commande8[(1,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(1,2)].icon()))
         self.btn_view.setText(str(self.button_commande8[(1,2)].text()))
         self.button_commande8[(1,2)].setFocus()
         self.f1.show();self.id_commande.setValue(119)
         self.information_commande()
   def ___p8(self):
      if self.button_commande8[(1,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(1,3)].icon()))
         self.btn_view.setText(str(self.button_commande8[(1,3)].text()))
         self.button_commande8[(1,3)].setFocus()
         self.f1.show();self.id_commande.setValue(120)
         self.information_commande()
   def ___p9(self):
      if self.button_commande8[(2,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(2,0)].icon()))
         self.btn_view.setText(str(self.button_commande8[(2,0)].text()))
         self.button_commande8[(2,0)].setFocus()
         self.f1.show();self.id_commande.setValue(121)
         self.information_commande()
   def ___p10(self):
      if self.button_commande8[(2,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(2,1)].icon()))
         self.btn_view.setText(str(self.button_commande8[(2,1)].text()))
         self.button_commande8[(2,1)].setFocus()
         self.f1.show();self.id_commande.setValue(122)
         self.information_commande()
   def ___p11(self):
      if self.button_commande8[(2,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(2,2)].icon()))
         self.btn_view.setText(str(self.button_commande8[(2,2)].text()))
         self.button_commande8[(2,2)].setFocus()
         self.f1.show();self.id_commande.setValue(123)
         self.information_commande()
   def ___p12(self):
      if self.button_commande8[(2,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(2,3)].icon()))
         self.btn_view.setText(str(self.button_commande8[(2,3)].text()))
         self.button_commande8[(2,3)].setFocus()
         self.f1.show();self.id_commande.setValue(124)
         self.information_commande()
   def ___p13(self):
      if self.button_commande8[(3,0)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(3,0)].icon()))
         self.btn_view.setText(str(self.button_commande8[(3,0)].text()))
         self.button_commande8[(3,0)].setFocus()
         self.f1.show();self.id_commande.setValue(125)
         self.information_commande()
   def ___p14(self):
      if self.button_commande8[(3,1)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(3,1)].icon()))
         self.btn_view.setText(str(self.button_commande8[(3,1)].text()))
         self.button_commande8[(3,1)].setFocus()
         self.f1.show();self.id_commande.setValue(126)
         self.information_commande()
   def ___p15(self):
      if self.button_commande8[(3,2)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(3,2)].icon()))
         self.btn_view.setText(str(self.button_commande8[(3,2)].text()))
         self.button_commande8[(3,2)].setFocus()
         self.f1.show();self.id_commande.setValue(127)
         self.information_commande()
   def ___p16(self):
      if self.button_commande8[(3,3)]:
         self.btn_view.setIcon(QIcon(self.button_commande8[(3,3)].icon()))
         self.btn_view.setText(str(self.button_commande8[(3,3)].text()))
         self.button_commande8[(3,3)].setFocus()
         self.f1.show();self.id_commande.setValue(128)
         self.information_commande()


   def ship_commande(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            try:
               self.cursor=self.bdd.cursor()
               self.cursor.execute(""" UPDATE commandes SET is_processed=1
               WHERE code_client=(SELECT code_client FROM clients WHERE code_commande="""+"'"+str(self.code_commande.text())+"'"+")")
               self.bdd.commit()
               self.refresh_commande()
               QMessageBox.information(self,str(self.app_name),'COMMANDE VALIDEE AVEC SUCCES')
               
            except:
               self.bdd.rollback()
               QMessageBox.information(self,str(self.app_name),"COMMANDE NON VALIDEE\nUNE ERREUR S'EST PRODUITE")               

      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass


   def return_commande(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  self.question=QMessageBox.question(self,str(self.app_name),'VOULEZ VOUS RENVOYEZ LES PRODUITS ?',QMessageBox.Yes,QMessageBox.No)
                  if self.question==QMessageBox.Yes:
                     self.cursor=self.bdd.cursor()
                     self.index_client=[]
                     self.index_commande=[]
                     
                     self.sq1=self.cursor.execute("""SELECT COUNT(*) FROM commandes WHERE is_processed='0' AND
                                                   code_commande="""+"'"+str(self.code_commande.text())+"'")
                     for i in self.sq1:
                        if int(i[0])>0:
                           self.cursor.execute("""SELECT code_produit,type,id_produit,code_client FROM commandes WHERE is_processed=0 AND
                                                   code_commande="""+"'"+str(self.code_commande.text())+"'")
                           self.rr=self.cursor.fetchall()
                           for i in self.rr:
                              if 'BOISSON' in i[1]:
                                 self.cursor.execute("""UPDATE boissons SET quantite = quantite + (SELECT quantite FROM commandes
                                 WHERE code_produit={0} AND type='BOISSON' AND code_client={1})
                                 WHERE code_produit={2} """.format("'"+str(i[0])+"'","'"+str(i[3])+"'","'"+str(i[0])+"'"))
                                 self.bdd.commit()
                              elif 'DESSERT' in i[1]:
                                 self.cursor.execute("""UPDATE desserts SET quantite = quantite + (SELECT quantite FROM commandes
                                 WHERE code_produit={0} AND type='DESSERT' AND code_client={1})
                                 WHERE code_produit={2} """.format("'"+str(i[0])+"'","'"+str(i[3])+"'","'"+str(i[0])+"'"))
                                 self.bdd.commit()
                              elif 'CAFE' in i[1]:
                                 self.cursor.execute("""UPDATE cafes SET quantite = quantite + (SELECT quantite FROM commandes
                                 WHERE code_produit={0} AND type='CAFE' AND code_client={1})
                                 WHERE code_produit={2} """.format("'"+str(i[0])+"'","'"+str(i[3])+"'","'"+str(i[0])+"'"))
                                 self.bdd.commit()
                              elif 'PLAT' in i[1]:
                                 self.cursor.execute("""UPDATE plats SET quantite = quantite + (SELECT quantite FROM commandes
                                 WHERE code_produit={0} AND type='PLAT' AND code_client={1})
                                 WHERE code_produit={2} """.format("'"+str(i[0])+"'","'"+str(i[3])+"'","'"+str(i[0])+"'"))
                                 self.bdd.commit()
                              else:
                                 self.bdd.roolback()
                                 QMessageBox.information(self,str(self.app_name),"RENVOI NON EFFECTUE")


                           self.cursor.execute("""DELETE FROM commandes WHERE is_processed='0' AND
                                                   code_commande="""+"'"+str(self.code_commande.text())+"'")
                           #==== MISE A JOUR ID COMMANDES
                           self.table_commande=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                           rownum,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,reduction,datetime,
                           code_commande,code_client,is_added,is_ordered,is_processed,is_shipped,is_paid FROM commandes""")
                           for i in self.table_commande:
                              self.index_commande.append(i)

                           self.cursor.execute("DELETE FROM commandes")
                           self.cursor.executemany("""INSERT INTO commandes
                           (id,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,reduction,datetime,
                           code_commande,code_client,is_added,is_ordered,is_processed,is_shipped,is_paid)
                                          VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index_commande)

                           
                           self.cursor.execute("""DELETE FROM clients WHERE code_commande="""+"'"+str(self.code_commande.text())+"'")
                           #==== MISE A JOUR ID CLIENTS
                           self.table_client=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                       rownum,code_commande,code_client,nom_client,numero_client,adresse_client,cnib_client,numero_table,datetime
                                                   FROM clients""")
                           for i in self.table_client:
                              self.index_client.append(i)

                           self.cursor.execute("DELETE FROM clients")
                           self.cursor.executemany("""INSERT INTO clients
                                          (id,code_commande,code_client,nom_client,numero_client,adresse_client,cnib_client,numero_table,datetime)
                                          VALUES (?,?,?,?,?,?,?,?,?)""",self.index_client)

                           self.cursor.execute("DELETE FROM preview_commandes")
                           self.reset()
                           QMessageBox.information(self,str(self.app_name),'PRODUITS RENVOYES AUX STOCKS\nAVEC SUCCES')
                        else:
                           QMessageBox.information(self,str(self.app_name),"PRODUITS NON RENVOYES AUX STOCKS")
                                 
                              
                     
                        
                        
                     self.bdd.commit()
                     self.refresh_commande()
               except:
                  self.bdd.roolback()
                  QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")


   def validate_commande(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            try:
               self.cursor=self.bdd.cursor()
               self.cursor.execute(""" UPDATE commandes SET is_processed=1
               WHERE code_client=(SELECT code_client FROM clients WHERE code_commande="""+"'"+str(self.code_commande.text())+"'"+")")
               self.bdd.commit()
               self.refresh_commande()
               QMessageBox.information(self,str(self.app_name),'COMMANDE VALIDEE AVEC SUCCES')
               
            except:
               self.bdd.rollback()
               QMessageBox.information(self,str(self.app_name),"COMMANDE NON VALIDEE\nUNE ERREUR S'EST PRODUITE")               

      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass

   def abort_commande(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            try:
               self.cursor=self.bdd.cursor()
               self.cursor.execute(""" UPDATE commandes SET is_processed=0
               WHERE code_client=(SELECT code_client FROM clients WHERE code_commande="""+"'"+str(self.code_commande.text())+"'"+")")
               self.bdd.commit()
               self.refresh_commande()
               QMessageBox.information(self,str(self.app_name),'COMMANDE ANNULEE AVEC SUCCES')
               
            except:
               self.bdd.rollback()
               QMessageBox.information(self,str(self.app_name),"COMMANDE NON ANNULEE\nUNE ERREUR S'EST PRODUITE")               

      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass

   def retirer_produit(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  self.question=QMessageBox.question(self,str(self.app_name),'VOULEZ VOUS RETIRER CE PRODUIT ?',QMessageBox.Yes,QMessageBox.No)
                  if self.question==QMessageBox.Yes:
                     self.cursor=self.bdd.cursor()
                     self.index_client=[]
                     self.index_commande=[]
                     self.sq1=self.cursor.execute("""SELECT COUNT(*) FROM commandes WHERE is_processed=0 AND code_commande="""+"'"+self.code_commande.text()+"'")
                     for i in self.sq1:
                        if int(i[0])>0:
                           self.cursor.execute("""SELECT * FROM commandes WHERE is_processed='0' AND code_commande="""+"'"+self.code_commande.text()+"'")
                           self.select=self.cursor.fetchall()
                           for i in self.select:
                              print(i)
                              if self.code_produit.text() in i[5] and +self.cat_commande.text()=='BOISSON':
                                 print("BOISSON")
                                 self.cursor.execute("""UPDATE boissons SET quantite = quantite + (SELECT quantite FROM commandes
                                 WHERE code_commande={0} AND code_produit={1})  WHERE code_produit={2}""".format(
                                    "'"+str(i[11])+"'","'"+str(i[5])+"'","'"+str(i[5])+"'"))
                                 self.bdd.commit()
                              elif self.code_produit.text() in i[5] and self.cat_commande.text()=='DESSERT':
                                 print("DESSERT")
                                 self.cursor.execute("""UPDATE desserts SET quantite = quantite + (SELECT quantite FROM commandes
                                 WHERE code_commande={0} AND code_produit={1})  WHERE code_produit={2}""".format(
                                    "'"+str(i[11])+"'","'"+str(i[5])+"'","'"+str(i[5])+"'"))
                                 self.bdd.commit()
                              elif self.code_produit.text() in i[5] and self.cat_commande.text()=='CAFE':
                                 print("CAFE")
                                 self.cursor.execute("""UPDATE cafes SET quantite = quantite + (SELECT quantite FROM commandes
                                 WHERE code_commande={0} AND code_produit={1})  WHERE code_produit={2}""".format(
                                    "'"+str(i[11])+"'","'"+str(i[5])+"'","'"+str(i[5])+"'"))
                                 self.bdd.commit()
                              elif self.code_produit.text() in i[5] and self.cat_commande.text()=='PLAT':
                                 print("PLAT")
                                 self.cursor.execute("""UPDATE plats SET quantite = quantite + (SELECT quantite FROM commandes
                                 WHERE code_commande={0} AND code_produit={1})  WHERE code_produit={2}""".format(
                                    "'"+str(i[11])+"'","'"+str(i[5])+"'","'"+str(i[5])+"'"))
                                 self.bdd.commit()
                              else:
                                 self.bdd.roolback()
                                 QMessageBox.information(self,str(self.app_name),"RENVOI NON EFFECTUE")

                           
                        else:
                           QMessageBox.information(self,str(self.app_name),"COMMANDE VALIDEE")

                     self.cursor.execute("""DELETE FROM commandes WHERE is_processed='0' AND code_commande="""+"'"+self.code_commande.text()+"'"+""" AND
                                        code_produit="""+"'"+self.code_produit.text()+"'")
                     
                     #==== MISE A JOUR ID COMMANDES
                     self.table_commande=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                     rownum,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,reduction,datetime,
                     code_commande,code_client,is_added,is_ordered,is_processed,is_shipped,is_paid FROM commandes""")
                     for a in self.table_commande:
                        self.index_commande.append(a)

                     self.cursor.execute("DELETE FROM commandes")
                     self.cursor.executemany("""INSERT INTO commandes
                     (id,nom,quantite,prix,id_produit,code_produit,type,categorie,photo,reduction,datetime,
                     code_commande,code_client,is_added,is_ordered,is_processed,is_shipped,is_paid)
                                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index_commande)
                     #==== MISE A JOUR ID CLIENTS
                     self.table_client=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                 rownum,code_commande,code_client,nom_client,numero_client,adresse_client,cnib_client,numero_table,datetime
                                             FROM clients""")
                     for b in self.table_client:
                        self.index_client.append(b)

                     self.cursor.execute("DELETE FROM clients")
                     self.cursor.executemany("""INSERT INTO clients
                                    (id,code_commande,code_client,nom_client,numero_client,adresse_client,cnib_client,numero_table,datetime)
                                    VALUES (?,?,?,?,?,?,?,?,?)""",self.index_client)
                     self.bdd.commit()
                     #self.cursor.execute("DELETE FROM preview_commandes")
                     #self.reset()
                     QMessageBox.information(self,str(self.app_name),'PRODUITS RENVOYES AUX STOCKS\nAVEC SUCCES')

                     self.refresh_commande()

                     
               except:
                  QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")

   def reset(self):
      #________PAGE 1
         self.button_commande1[(0,0)].setText("")
         self.lab_commande1[(0,0)].setText("")
         self.button_commande1[(0,0)].setIcon(QIcon(""))
         self.button_commande1[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(0,1)].setText("")
         self.lab_commande1[(0,1)].setText("")
         self.button_commande1[(0,1)].setIcon(QIcon(""))
         self.button_commande1[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(0,2)].setText("")
         self.lab_commande1[(0,2)].setText("")
         self.button_commande1[(0,2)].setIcon(QIcon(""))
         self.button_commande1[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(0,3)].setText("")
         self.lab_commande1[(0,3)].setText("")
         self.button_commande1[(0,3)].setIcon(QIcon(""))
         self.button_commande1[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(1,0)].setText("")
         self.lab_commande1[(1,0)].setText("")
         self.button_commande1[(1,0)].setIcon(QIcon(""))
         self.button_commande1[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(1,1)].setText("")
         self.lab_commande1[(1,1)].setText("")
         self.button_commande1[(1,1)].setIcon(QIcon(""))
         self.button_commande1[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(1,2)].setText("")
         self.lab_commande1[(1,2)].setText("")
         self.button_commande1[(1,2)].setIcon(QIcon(""))
         self.button_commande1[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(1,3)].setText("")
         self.lab_commande1[(1,3)].setText("")
         self.button_commande1[(1,3)].setIcon(QIcon(""))
         self.button_commande1[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(2,0)].setText("")
         self.lab_commande1[(2,0)].setText("")
         self.button_commande1[(2,0)].setIcon(QIcon(""))
         self.button_commande1[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(2,1)].setText("")
         self.lab_commande1[(2,1)].setText("")
         self.button_commande1[(2,1)].setIcon(QIcon(""))
         self.button_commande1[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(2,2)].setText("")
         self.lab_commande1[(2,2)].setText("")
         self.button_commande1[(2,2)].setIcon(QIcon(""))
         self.button_commande1[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(2,3)].setText("")
         self.lab_commande1[(2,3)].setText("")
         self.button_commande1[(2,3)].setIcon(QIcon(""))
         self.button_commande1[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(3,0)].setText("")
         self.lab_commande1[(3,0)].setText("")
         self.button_commande1[(3,0)].setIcon(QIcon(""))
         self.button_commande1[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(3,1)].setText("")
         self.lab_commande1[(3,1)].setText("")
         self.button_commande1[(3,1)].setIcon(QIcon(""))
         self.button_commande1[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(3,2)].setText("")
         self.lab_commande1[(3,2)].setText("")
         self.button_commande1[(3,2)].setIcon(QIcon(""))
         self.button_commande1[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))

         self.button_commande1[(3,3)].setText("")
         self.lab_commande1[(3,3)].setText("")
         self.button_commande1[(3,3)].setIcon(QIcon(""))
         self.button_commande1[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))


   def selection_item(self):
      try:
         self.panier1=[]
         self.index1=[]
         self.bdd=sqlite3.connect('restaurant.bd')
         self.cursor=self.bdd.cursor()
         
         #==== ID COMMANDE MISE A JOUR
         self.id_client=int(self.list_commande.currentRow())+1

         #==== SELECTION ARTICLE DANS COMMANDE
         self.s_sq=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id) rownum,code_commande,code_client,nom_client,cnib_client,
                                       numero_client,adresse_client,numero_table FROM clients""")
         for i in self.s_sq:
            self.panier1.append(i)
            if len(self.panier1)==int(self.list_commande.count()):
               self.code_commande.setText(str(self.panier1[int(self.list_commande.currentRow())][1]))
               self.nom_client.setText(str(self.panier1[int(self.list_commande.currentRow())][3]))
               self.cnib_client.setText(str(self.panier1[int(self.list_commande.currentRow())][4]))
               self.adresse_client.setText(str(self.panier1[int(self.list_commande.currentRow())][6]))
               self.num_table.setText(str(self.panier1[int(self.list_commande.currentRow())][7]))
               

         #==== PREVIEW TABLE
         self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                        rownum,nom,quantite,prix,id_produit,code_produit,type,
                        categorie,photo,datetime,reduction,code_client FROM commandes WHERE code_commande="""+"'"+str(self.code_commande.text())+"'")
         for i in self.s_ss:
            self.index1.append(i)

         self.cursor.execute("DELETE FROM preview_commandes")            
         self.cursor.executemany("""INSERT INTO preview_commandes
                                   (id,nom,quantite,prix,id_produit,code_produit,type,
                                   categorie,photo,datetime,reduction,code_client) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1)


         


         self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                         rownum,nom,quantite,photo,prix,type FROM commandes WHERE
                         code_commande="""+"'"+str(self.code_commande.text())+"'")
         self.group=self.cursor.fetchall()
         #print(self.group)

         #________PAGE 1
         if len(self.group)>=1:
            self.button_commande1[(0,0)].setText(str(self.group[0][1]))
            self.lab_commande1[(0,0)].setText(str(self.group[0][2]))
            self.button_commande1[(0,0)].setIcon(QIcon(str(self.group[0][3])))
            self.button_commande1[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(0,0)].setText("")
            self.lab_commande1[(0,0)].setText("")
            self.button_commande1[(0,0)].setIcon(QIcon(""))
            self.button_commande1[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=2:
            self.button_commande1[(0,1)].setText(str(self.group[1][1]))
            self.lab_commande1[(0,1)].setText(str(self.group[1][2]))
            self.button_commande1[(0,1)].setIcon(QIcon(str(self.group[1][3])))
            self.button_commande1[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(0,1)].setText("")
            self.lab_commande1[(0,1)].setText("")
            self.button_commande1[(0,1)].setIcon(QIcon(""))
            self.button_commande1[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=3:
            self.button_commande1[(0,2)].setText(str(self.group[2][1]))
            self.lab_commande1[(0,2)].setText(str(self.group[2][2]))
            self.button_commande1[(0,2)].setIcon(QIcon(str(self.group[2][3])))
            self.button_commande1[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(0,2)].setText("")
            self.lab_commande1[(0,2)].setText("")
            self.button_commande1[(0,2)].setIcon(QIcon(""))
            self.button_commande1[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=4:
            self.button_commande1[(0,3)].setText(str(self.group[3][1]))
            self.lab_commande1[(0,3)].setText(str(self.group[3][2]))
            self.button_commande1[(0,3)].setIcon(QIcon(str(self.group[3][3])))
            self.button_commande1[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(0,3)].setText("")
            self.lab_commande1[(0,3)].setText("")
            self.button_commande1[(0,3)].setIcon(QIcon(""))
            self.button_commande1[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=5:
            self.button_commande1[(1,0)].setText(str(self.group[4][1]))
            self.lab_commande1[(1,0)].setText(str(self.group[4][2]))
            self.button_commande1[(1,0)].setIcon(QIcon(str(self.group[4][3])))
            self.button_commande1[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(1,0)].setText("")
            self.lab_commande1[(1,0)].setText("")
            self.button_commande1[(1,0)].setIcon(QIcon(""))
            self.button_commande1[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=6:
            self.button_commande1[(1,1)].setText(str(self.group[5][1]))
            self.lab_commande1[(1,1)].setText(str(self.group[5][2]))
            self.button_commande1[(1,1)].setIcon(QIcon(str(self.group[5][3])))
            self.button_commande1[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(1,1)].setText("")
            self.lab_commande1[(1,1)].setText("")
            self.button_commande1[(1,1)].setIcon(QIcon(""))
            self.button_commande1[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=7:
            self.button_commande1[(1,2)].setText(str(self.group[6][1]))
            self.lab_commande1[(1,2)].setText(str(self.group[6][2]))
            self.button_commande1[(1,2)].setIcon(QIcon(str(self.group[6][3])))
            self.button_commande1[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(1,2)].setText("")
            self.lab_commande1[(1,2)].setText("")
            self.button_commande1[(1,2)].setIcon(QIcon(""))
            self.button_commande1[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=8:
            self.button_commande1[(1,3)].setText(str(self.group[7][1]))
            self.lab_commande1[(1,3)].setText(str(self.group[7][2]))
            self.button_commande1[(1,3)].setIcon(QIcon(str(self.group[7][3])))
            self.button_commande1[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(1,3)].setText("")
            self.lab_commande1[(1,3)].setText("")
            self.button_commande1[(1,3)].setIcon(QIcon(""))
            self.button_commande1[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=9:
            self.button_commande1[(2,0)].setText(str(self.group[8][1]))
            self.lab_commande1[(2,0)].setText(str(self.group[8][2]))
            self.button_commande1[(2,0)].setIcon(QIcon(str(self.group[8][3])))
            self.button_commande1[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(2,0)].setText("")
            self.lab_commande1[(2,0)].setText("")
            self.button_commande1[(2,0)].setIcon(QIcon(""))
            self.button_commande1[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=10:
            self.button_commande1[(2,1)].setText(str(self.group[9][1]))
            self.lab_commande1[(2,1)].setText(str(self.group[9][2]))
            self.button_commande1[(2,1)].setIcon(QIcon(str(self.group[9][3])))
            self.button_commande1[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(2,1)].setText("")
            self.lab_commande1[(2,1)].setText("")
            self.button_commande1[(2,1)].setIcon(QIcon(""))
            self.button_commande1[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=11:
            self.button_commande1[(2,2)].setText(str(self.group[10][1]))
            self.lab_commande1[(2,2)].setText(str(self.group[10][2]))
            self.button_commande1[(2,2)].setIcon(QIcon(str(self.group[10][3])))
            self.button_commande1[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(2,2)].setText("")
            self.lab_commande1[(2,2)].setText("")
            self.button_commande1[(2,2)].setIcon(QIcon(""))
            self.button_commande1[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=12:
            self.button_commande1[(2,3)].setText(str(self.group[11][1]))
            self.lab_commande1[(2,3)].setText(str(self.group[11][2]))
            self.button_commande1[(2,3)].setIcon(QIcon(str(self.group[11][3])))
            self.button_commande1[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(2,3)].setText("")
            self.lab_commande1[(2,3)].setText("")
            self.button_commande1[(2,3)].setIcon(QIcon(""))
            self.button_commande1[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=13:
            self.button_commande1[(3,0)].setText(str(self.group[12][1]))
            self.lab_commande1[(3,0)].setText(str(self.group[12][2]))
            self.button_commande1[(3,0)].setIcon(QIcon(str(self.group[12][3])))
            self.button_commande1[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(3,0)].setText("")
            self.lab_commande1[(3,0)].setText("")
            self.button_commande1[(3,0)].setIcon(QIcon(""))
            self.button_commande1[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=14:
            self.button_commande1[(3,1)].setText(str(self.group[13][1]))
            self.lab_commande1[(3,1)].setText(str(self.group[13][2]))
            self.button_commande1[(3,1)].setIcon(QIcon(str(self.group[13][3])))
            self.button_commande1[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(3,1)].setText("")
            self.lab_commande1[(3,1)].setText("")
            self.button_commande1[(3,1)].setIcon(QIcon(""))
            self.button_commande1[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=15:
            self.button_commande1[(3,2)].setText(str(self.group[14][1]))
            self.lab_commande1[(3,2)].setText(str(self.group[14][2]))
            self.button_commande1[(3,2)].setIcon(QIcon(str(self.group[14][3])))
            self.button_commande1[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(3,2)].setText("")
            self.lab_commande1[(3,2)].setText("")
            self.button_commande1[(3,2)].setIcon(QIcon(""))
            self.button_commande1[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
         if len(self.group)>=16:
            self.button_commande1[(3,3)].setText(str(self.group[15][1]))
            self.lab_commande1[(3,3)].setText(str(self.group[15][2]))
            self.button_commande1[(3,3)].setIcon(QIcon(str(self.group[15][3])))
            self.button_commande1[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
         else:
            self.button_commande1[(3,3)].setText("")
            self.lab_commande1[(3,3)].setText("")
            self.button_commande1[(3,3)].setIcon(QIcon(""))
            self.button_commande1[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))

         
                     
         self.bdd.commit()
         self.refresh_commande()
      
      except:
         self.bdd.rollback()
         QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")

   def refresh_commande(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()

               self.list_commande.clear()
               self.cursor.execute("SELECT * FROM clients")
               self.records=self.cursor.fetchall()
               for r in self.records:
                  self.list_produit=("ID CLIENT: ------ " + str(r[0]) + " \n " +
                                     "DATE: ------ " + str(r[8]) + " \n " +
                                     "NOM CLIENT: ------ " + str(r[3]) + " \n " +
                                     "CODE CLIENT: ------ " + str(r[2]) + " \n " +
                                     "NUMERO CLIENT: ------ " + str(r[4]))
                  
                  #====FRAME WIDGET
                  self.choose1=QFrame(self.list_commande)
                  self.choose1.setStyleSheet("""
                       background-color:#490063;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                       font-weight:bold;border-radius:25px
                       """)
                  self.label1 = QLabel(self.list_produit,self.choose1)
                                    
                  self.layout = QHBoxLayout(self.choose1)
                  self.layout.addWidget(self.label1)
                  self.setLayout(self.layout)
                  
                  self.item = QListWidgetItem(self.list_commande)         
                  self.item_widget = self.choose1        
                  self.item.setSizeHint(self.item_widget.sizeHint())
                  
                  self.list_commande.addItem(self.item)
                  self.list_commande.setItemWidget(self.item,self.item_widget)
               
               #==== MISE A JOUR QUANTITE ET PRIX DANS LA TABLE COMMANDES
               self.sql__=self.cursor.execute(""" SELECT SUM(preview_commandes.quantite),
                                   SUM((preview_commandes.quantite*preview_commandes.prix)-
                              ((preview_commandes.quantite*preview_commandes.prix)*preview_commandes.reduction/100))
                                                      FROM preview_commandes """)
               
               for c in self.sql__:
                  if c[0] != None and c[0] > 0 and c[0] < 2 and self.id_client != 0:
                     self.btn_total.setText("QUANTITE COMMANDEE : "+str(c[0])+" PRODUIT"+" --- TOTAL A PAYER: "+str(c[1])+" F CFA")
                  elif c[0] != None and c[0] >= 2 and self.id_client != 0:
                     self.btn_total.setText("QUANTITE COMMANDEE : "+str(c[0])+" PRODUITS"+" --- TOTAL A PAYER: "+str(c[1])+" F CFA")
                  else:
                     self.btn_total.setText("QUANTITE COMMANDEE : 0 --- TOTAL A PAYER: 0 F CFA")

               self.sql_client=self.cursor.execute("""SELECT COUNT(*) FROM clients""")
               for row in self.sql_client:
                  if row[0] is not None:
                     self.num_client.setText(str(row[0]))
                  else:
                     self.num_client.setText("0")

                     

               self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                               rownum,nom,quantite,photo,prix,type FROM commandes WHERE
                               is_processed=1 AND code_commande="""+"'"+str(self.code_commande.text())+"'")
               self.group_check=self.cursor.fetchall()

               #________PAGE 1
               if len(self.group_check)>=1:
                  self.lab_validate1[(0,0)].show()
               else:
                  self.lab_validate1[(0,0)].hide()
               if len(self.group_check)>=2:
                  self.lab_validate1[(0,1)].show()
               else:
                  self.lab_validate1[(0,1)].hide()
               if len(self.group_check)>=3:
                  self.lab_validate1[(0,2)].show()
               else:
                  self.lab_validate1[(0,2)].hide()
               if len(self.group_check)>=4:
                  self.lab_validate1[(0,3)].show()
               else:
                  self.lab_validate1[(0,3)].hide()
               if len(self.group_check)>=5:
                  self.lab_validate1[(1,0)].show()
               else:
                  self.lab_validate1[(1,0)].hide()
               if len(self.group_check)>=6:
                  self.lab_validate1[(1,1)].show()
               else:
                  self.lab_validate1[(1,1)].hide()
               if len(self.group_check)>=7:
                  self.lab_validate1[(1,2)].show()
               else:
                  self.lab_validate1[(1,2)].hide()
               if len(self.group_check)>=8:
                  self.lab_validate1[(1,3)].show()
               else:
                  self.lab_validate1[(1,3)].hide()
               if len(self.group_check)>=9:
                  self.lab_validate1[(2,0)].show()
               else:
                  self.lab_validate1[(2,0)].hide()
               if len(self.group_check)>=10:
                  self.lab_validate1[(2,1)].show()
               else:
                  self.lab_validate1[(2,1)].hide()
               if len(self.group_check)>=11:
                  self.lab_validate1[(2,2)].show()
               else:
                  self.lab_validate1[(2,2)].hide()
               if len(self.group_check)>=12:
                  self.lab_validate1[(2,3)].show()
               else:
                  self.lab_validate1[(2,3)].hide()
               if len(self.group_check)>=13:
                  self.lab_validate1[(3,0)].show()
               else:
                  self.lab_validate1[(3,0)].hide()
               if len(self.group_check)>=14:
                  self.lab_validate1[(3,1)].show()
               else:
                  self.lab_validate1[(3,1)].hide()
               if len(self.group_check)>=15:
                  self.lab_validate1[(3,2)].show()
               else:
                  self.lab_validate1[(3,2)].hide()
               if len(self.group_check)>=16:
                  self.lab_validate1[(3,3)].show()
               else:
                  self.lab_validate1[(3,3)].hide()


               """
               #________PAGE 1
               self.b1=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=1")               
               for row in self.b1:
                  self.button_commande1[(0,0)].setText(str(row[0]))
                  self.lab_commande1[(0,0)].setText(str(row[1]))
                  self.button_commande1[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b2=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=2")            
               for row in self.b2:
                  self.button_commande1[(0,1)].setText(str(row[0]))
                  self.lab_commande1[(0,1)].setText(str(row[1]))
                  self.button_commande1[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b3=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=3")              
               for row in self.b3:
                  self.button_commande1[(0,2)].setText(str(row[0]))
                  self.lab_commande1[(0,2)].setText(str(row[1]))
                  self.button_commande1[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b4=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=4")              
               for row in self.b4:
                  self.button_commande1[(0,3)].setText(str(row[0]))
                  self.lab_commande1[(0,3)].setText(str(row[1]))
                  self.button_commande1[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b5=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=5")               
               for row in self.b5:
                  self.button_commande1[(1,0)].setText(str(row[0]))
                  self.lab_commande1[(1,0)].setText(str(row[1]))
                  self.button_commande1[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b6=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=6")              
               for row in self.b6:
                  self.button_commande1[(1,1)].setText(str(row[0]))
                  self.lab_commande1[(1,1)].setText(str(row[1]))
                  self.button_commande1[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b7=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=7")               
               for row in self.b7:
                  self.button_commande1[(1,2)].setText(str(row[0]))
                  self.lab_commande1[(1,2)].setText(str(row[1]))
                  self.button_commande1[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b8=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=8")               
               for row in self.b8:
                  self.button_commande1[(1,3)].setText(str(row[0]))
                  self.lab_commande1[(1,3)].setText(str(row[1]))
                  self.button_commande1[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b9=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=9")               
               for row in self.b9:
                  self.button_commande1[(2,0)].setText(str(row[0]))
                  self.lab_commande1[(2,0)].setText(str(row[1]))
                  self.button_commande1[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b10=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=10")               
               for row in self.b10:
                  self.button_commande1[(2,1)].setText(str(row[0]))
                  self.lab_commande1[(2,1)].setText(str(row[1]))
                  self.button_commande1[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b11=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=11")               
               for row in self.b11:
                  self.button_commande1[(2,2)].setText(str(row[0]))
                  self.lab_commande1[(2,2)].setText(str(row[1]))
                  self.button_commande1[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b12=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=12")               
               for row in self.b12:
                  self.button_commande1[(2,3)].setText(str(row[0]))
                  self.lab_commande1[(2,3)].setText(str(row[1]))
                  self.button_commande1[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b13=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=13")               
               for row in self.b13:
                  self.button_commande1[(3,0)].setText(str(row[0]))
                  self.lab_commande1[(3,0)].setText(str(row[1]))
                  self.button_commande1[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b14=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=14")               
               for row in self.b14:
                  self.button_commande1[(3,1)].setText(str(row[0]))
                  self.lab_commande1[(3,1)].setText(str(row[1]))
                  self.button_commande1[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b15=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=15")               
               for row in self.b15:
                  self.button_commande1[(3,2)].setText(str(row[0]))
                  self.lab_commande1[(3,2)].setText(str(row[1]))
                  self.button_commande1[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b16=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=16")               
               for row in self.b16:
                  self.button_commande1[(3,3)].setText(str(row[0]))
                  self.lab_commande1[(3,3)].setText(str(row[1]))
                  self.button_commande1[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande1[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 2
               self.b17=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=17")               
               for row in self.b17:
                  self.button_commande2[(0,0)].setText(str(row[0]))
                  self.lab_commande2[(0,0)].setText(str(row[1]))
                  self.button_commande2[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b18=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=18")               
               for row in self.b18:
                  self.button_commande2[(0,1)].setText(str(row[0]))
                  self.lab_commande2[(0,1)].setText(str(row[1]))
                  self.button_commande2[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b19=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=19")               
               for row in self.b19:
                  self.button_commande2[(0,2)].setText(str(row[0]))
                  self.lab_commande2[(0,2)].setText(str(row[1]))
                  self.button_commande2[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b20=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=20")               
               for row in self.b20:
                  self.button_commande2[(0,3)].setText(str(row[0]))
                  self.lab_commande2[(0,3)].setText(str(row[1]))
                  self.button_commande2[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b21=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=21")               
               for row in self.b21:
                  self.button_commande2[(1,0)].setText(str(row[0]))
                  self.lab_commande2[(1,0)].setText(str(row[1]))
                  self.button_commande2[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b22=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=22")               
               for row in self.b22:
                  self.button_commande2[(1,1)].setText(str(row[0]))
                  self.lab_commande2[(1,1)].setText(str(row[1]))
                  self.button_commande2[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b23=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=23")               
               for row in self.b23:
                  self.button_commande2[(1,2)].setText(str(row[0]))
                  self.lab_commande2[(1,2)].setText(str(row[1]))
                  self.button_commande2[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b24=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=24")               
               for row in self.b24:
                  self.button_commande2[(1,3)].setText(str(row[0]))
                  self.lab_commande2[(1,3)].setText(str(row[1]))
                  self.button_commande2[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b25=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=25")               
               for row in self.b25:
                  self.button_commande2[(2,0)].setText(str(row[0]))
                  self.lab_commande2[(2,0)].setText(str(row[1]))
                  self.button_commande2[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b26=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=26")               
               for row in self.b26:
                  self.button_commande2[(2,1)].setText(str(row[0]))
                  self.lab_commande2[(2,1)].setText(str(row[1]))
                  self.button_commande2[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b27=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=27")               
               for row in self.b27:
                  self.button_commande2[(2,2)].setText(str(row[0]))
                  self.lab_commande2[(2,2)].setText(str(row[1]))
                  self.button_commande2[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b28=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=28")               
               for row in self.b28:
                  self.button_commande2[(2,3)].setText(str(row[0]))
                  self.lab_commande2[(2,3)].setText(str(row[1]))
                  self.button_commande2[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b29=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=29")               
               for row in self.b29:
                  self.button_commande2[(3,0)].setText(str(row[0]))
                  self.lab_commande2[(3,0)].setText(str(row[1]))
                  self.button_commande2[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b30=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=30")               
               for row in self.b30:
                  self.button_commande2[(3,1)].setText(str(row[0]))
                  self.lab_commande2[(3,1)].setText(str(row[1]))
                  self.button_commande2[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b31=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=31")               
               for row in self.b31:
                  self.button_commande2[(3,2)].setText(str(row[0]))
                  self.lab_commande2[(3,2)].setText(str(row[1]))
                  self.button_commande2[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b32=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=32")               
               for row in self.b32:
                  self.button_commande2[(3,3)].setText(str(row[0]))
                  self.lab_commande2[(3,3)].setText(str(row[1]))
                  self.button_commande2[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande2[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 3
               self.b33=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=33")               
               for row in self.b33:
                  self.button_commande3[(0,0)].setText(str(row[0]))
                  self.lab_commande3[(0,0)].setText(str(row[1]))
                  self.button_commande3[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b34=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=34")               
               for row in self.b34:
                  self.button_commande3[(0,1)].setText(str(row[0]))
                  self.lab_commande3[(0,1)].setText(str(row[1]))
                  self.button_commande3[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b35=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=35")               
               for row in self.b35:
                  self.button_commande3[(0,2)].setText(str(row[0]))
                  self.lab_commande3[(0,2)].setText(str(row[1]))
                  self.button_commande3[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b36=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=36")               
               for row in self.b36:
                  self.button_commande3[(0,3)].setText(str(row[0]))
                  self.lab_commande3[(0,3)].setText(str(row[1]))
                  self.button_commande3[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b37=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=37")               
               for row in self.b37:
                  self.button_commande3[(1,0)].setText(str(row[0]))
                  self.lab_commande3[(1,0)].setText(str(row[1]))
                  self.button_commande3[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b38=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=38")               
               for row in self.b38:
                  self.button_commande3[(1,1)].setText(str(row[0]))
                  self.lab_commande3[(1,1)].setText(str(row[1]))
                  self.button_commande3[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b39=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=39")               
               for row in self.b39:
                  self.button_commande3[(1,2)].setText(str(row[0]))
                  self.lab_commande3[(1,2)].setText(str(row[1]))
                  self.button_commande3[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b40=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=40")               
               for row in self.b40:
                  self.button_commande3[(1,3)].setText(str(row[0]))
                  self.lab_commande3[(1,3)].setText(str(row[1]))
                  self.button_commande3[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b41=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=41")               
               for row in self.b41:
                  self.button_commande3[(2,0)].setText(str(row[0]))
                  self.lab_commande3[(2,0)].setText(str(row[1]))
                  self.button_commande3[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b42=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=42")               
               for row in self.b42:
                  self.button_commande3[(2,1)].setText(str(row[0]))
                  self.lab_commande3[(2,1)].setText(str(row[1]))
                  self.button_commande3[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b43=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=43")               
               for row in self.b43:
                  self.button_commande3[(2,2)].setText(str(row[0]))
                  self.lab_commande3[(2,2)].setText(str(row[1]))
                  self.button_commande3[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b44=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=44")               
               for row in self.b44:
                  self.button_commande3[(2,3)].setText(str(row[0]))
                  self.lab_commande3[(2,3)].setText(str(row[1]))
                  self.button_commande3[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b45=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=45")               
               for row in self.b45:
                  self.button_commande3[(3,0)].setText(str(row[0]))
                  self.lab_commande3[(3,0)].setText(str(row[1]))
                  self.button_commande3[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b46=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=46")               
               for row in self.b46:
                  self.button_commande3[(3,1)].setText(str(row[0]))
                  self.lab_commande3[(3,1)].setText(str(row[1]))
                  self.button_commande3[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b47=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=47")               
               for row in self.b47:
                  self.button_commande3[(3,2)].setText(str(row[0]))
                  self.lab_commande3[(3,2)].setText(str(row[1]))
                  self.button_commande3[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b48=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=48")               
               for row in self.b48:
                  self.button_commande3[(3,3)].setText(str(row[0]))
                  self.lab_commande3[(3,3)].setText(str(row[1]))
                  self.button_commande3[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande3[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 4
               self.b49=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=49")               
               for row in self.b49:
                  self.button_commande4[(0,0)].setText(str(row[0]))
                  self.lab_commande4[(0,0)].setText(str(row[1]))
                  self.button_commande4[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b50=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=50")           
               for row in self.b50:
                  self.button_commande4[(0,1)].setText(str(row[0]))
                  self.lab_commande4[(0,1)].setText(str(row[1]))
                  self.button_commande4[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b51=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=51")               
               for row in self.b51:
                  self.button_commande4[(0,2)].setText(str(row[0]))
                  self.lab_commande4[(0,2)].setText(str(row[1]))
                  self.button_commande4[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b52=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=52")               
               for row in self.b52:
                  self.button_commande4[(0,3)].setText(str(row[0]))
                  self.lab_commande4[(0,3)].setText(str(row[1]))
                  self.button_commande4[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b53=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=53")               
               for row in self.b53:
                  self.button_commande4[(1,0)].setText(str(row[0]))
                  self.lab_commande4[(1,0)].setText(str(row[1]))
                  self.button_commande4[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b54=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=54")               
               for row in self.b54:
                  self.button_commande4[(1,1)].setText(str(row[0]))
                  self.lab_commande4[(1,1)].setText(str(row[1]))
                  self.button_commande4[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b55=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=55")               
               for row in self.b55:
                  self.button_commande4[(1,2)].setText(str(row[0]))
                  self.lab_commande4[(1,2)].setText(str(row[1]))
                  self.button_commande4[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b56=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=56")               
               for row in self.b56:
                  self.button_commande4[(1,3)].setText(str(row[0]))
                  self.lab_commande4[(1,3)].setText(str(row[1]))
                  self.button_commande4[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b57=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=57")               
               for row in self.b57:
                  self.button_commande4[(2,0)].setText(str(row[0]))
                  self.lab_commande4[(2,0)].setText(str(row[1]))
                  self.button_commande4[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b58=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=58")               
               for row in self.b58:
                  self.button_commande4[(2,1)].setText(str(row[0]))
                  self.lab_commande4[(2,1)].setText(str(row[1]))
                  self.button_commande4[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b59=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=59")               
               for row in self.b59:
                  self.button_commande4[(2,2)].setText(str(row[0]))
                  self.lab_commande4[(2,2)].setText(str(row[1]))
                  self.button_commande4[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b60=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=60")               
               for row in self.b60:
                  self.button_commande4[(2,3)].setText(str(row[0]))
                  self.lab_commande4[(2,3)].setText(str(row[1]))
                  self.button_commande4[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b61=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=61")               
               for row in self.b61:
                  self.button_commande4[(3,0)].setText(str(row[0]))
                  self.lab_commande4[(3,0)].setText(str(row[1]))
                  self.button_commande4[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b62=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=62")               
               for row in self.b62:
                  self.button_commande4[(3,1)].setText(str(row[0]))
                  self.lab_commande4[(3,1)].setText(str(row[1]))
                  self.button_commande4[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b63=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=63")               
               for row in self.b63:
                  self.button_commande4[(3,2)].setText(str(row[0]))
                  self.lab_commande4[(3,2)].setText(str(row[1]))
                  self.button_commande4[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b64=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=64")               
               for row in self.b64:
                  self.button_commande4[(3,3)].setText(str(row[0]))
                  self.lab_commande4[(3,3)].setText(str(row[1]))
                  self.button_commande4[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande4[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 5
               self.b65=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=65")               
               for row in self.b65:
                  self.button_commande5[(0,0)].setText(str(row[0]))
                  self.lab_commande5[(0,0)].setText(str(row[1]))
                  self.button_commande5[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b66=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=66")             
               for row in self.b66:
                  self.button_commande5[(0,1)].setText(str(row[0]))
                  self.lab_commande5[(0,1)].setText(str(row[1]))
                  self.button_commande5[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b67=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=67")               
               for row in self.b67:
                  self.button_commande5[(0,2)].setText(str(row[0]))
                  self.lab_commande5[(0,2)].setText(str(row[1]))
                  self.button_commande5[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b68=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=68")               
               for row in self.b68:
                  self.button_commande5[(0,3)].setText(str(row[0]))
                  self.lab_commande5[(0,3)].setText(str(row[1]))
                  self.button_commande5[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b69=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=69")               
               for row in self.b69:
                  self.button_commande5[(1,0)].setText(str(row[0]))
                  self.lab_commande5[(1,0)].setText(str(row[1]))
                  self.button_commande5[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b70=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=70")               
               for row in self.b70:
                  self.button_commande5[(1,1)].setText(str(row[0]))
                  self.lab_commande5[(1,1)].setText(str(row[1]))
                  self.button_commande5[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b71=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=71")               
               for row in self.b71:
                  self.button_commande5[(1,2)].setText(str(row[0]))
                  self.lab_commande5[(1,2)].setText(str(row[1]))
                  self.button_commande5[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b72=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=72")               
               for row in self.b72:
                  self.button_commande5[(1,3)].setText(str(row[0]))
                  self.lab_commande5[(1,3)].setText(str(row[1]))
                  self.button_commande5[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b73=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=73")               
               for row in self.b73:
                  self.button_commande5[(2,0)].setText(str(row[0]))
                  self.lab_commande5[(2,0)].setText(str(row[1]))
                  self.button_commande5[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b74=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=74")               
               for row in self.b74:
                  self.button_commande5[(2,1)].setText(str(row[0]))
                  self.lab_commande5[(2,1)].setText(str(row[1]))
                  self.button_commande5[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b75=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=75")               
               for row in self.b75:
                  self.button_commande5[(2,2)].setText(str(row[0]))
                  self.lab_commande5[(2,2)].setText(str(row[1]))
                  self.button_commande5[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b76=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=76")               
               for row in self.b76:
                  self.button_commande5[(2,3)].setText(str(row[0]))
                  self.lab_commande5[(2,3)].setText(str(row[1]))
                  self.button_commande5[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b77=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=77")               
               for row in self.b77:
                  self.button_commande5[(3,0)].setText(str(row[0]))
                  self.lab_commande5[(3,0)].setText(str(row[1]))
                  self.button_commande5[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b78=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=78")               
               for row in self.b78:
                  self.button_commande5[(3,1)].setText(str(row[0]))
                  self.lab_commande5[(3,1)].setText(str(row[1]))
                  self.button_commande5[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b79=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=79")               
               for row in self.b79:
                  self.button_commande5[(3,2)].setText(str(row[0]))
                  self.lab_commande5[(3,2)].setText(str(row[1]))
                  self.button_commande5[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b80=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=80")               
               for row in self.b80:
                  self.button_commande5[(3,3)].setText(str(row[0]))
                  self.lab_commande5[(3,3)].setText(str(row[1]))
                  self.button_commande5[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande5[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 6
               self.b81=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=81")               
               for row in self.b81:
                  self.button_commande6[(0,0)].setText(str(row[0]))
                  self.lab_commande6[(0,0)].setText(str(row[1]))
                  self.button_commande6[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b82=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=82")               
               for row in self.b82:
                  self.button_commande6[(0,1)].setText(str(row[0]))
                  self.lab_commande6[(0,1)].setText(str(row[1]))
                  self.button_commande6[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b83=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=83")               
               for row in self.b83:
                  self.button_commande6[(0,2)].setText(str(row[0]))
                  self.lab_commande6[(0,2)].setText(str(row[1]))
                  self.button_commande6[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b84=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=84")               
               for row in self.b84:
                  self.button_commande6[(0,3)].setText(str(row[0]))
                  self.lab_commande6[(0,3)].setText(str(row[1]))
                  self.button_commande6[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b85=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=85")               
               for row in self.b85:
                  self.button_commande6[(1,0)].setText(str(row[0]))
                  self.lab_commande6[(1,0)].setText(str(row[1]))
                  self.button_commande6[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b86=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=86")               
               for row in self.b86:
                  self.button_commande6[(1,1)].setText(str(row[0]))
                  self.lab_commande6[(1,1)].setText(str(row[1]))
                  self.button_commande6[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b87=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=87")               
               for row in self.b87:
                  self.button_commande6[(1,2)].setText(str(row[0]))
                  self.lab_commande6[(1,2)].setText(str(row[1]))
                  self.button_commande6[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b88=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=88")               
               for row in self.b88:
                  self.button_commande6[(1,3)].setText(str(row[0]))
                  self.lab_commande6[(1,3)].setText(str(row[1]))
                  self.button_commande6[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b89=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=89")               
               for row in self.b89:
                  self.button_commande6[(2,0)].setText(str(row[0]))
                  self.lab_commande6[(2,0)].setText(str(row[1]))
                  self.button_commande6[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b90=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=90")               
               for row in self.b90:
                  self.button_commande6[(2,1)].setText(str(row[0]))
                  self.lab_commande6[(2,1)].setText(str(row[1]))
                  self.button_commande6[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b91=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=91")               
               for row in self.b91:
                  self.button_commande6[(2,2)].setText(str(row[0]))
                  self.lab_commande6[(2,2)].setText(str(row[1]))
                  self.button_commande6[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b92=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=92")               
               for row in self.b92:
                  self.button_commande6[(2,3)].setText(str(row[0]))
                  self.lab_commande6[(2,3)].setText(str(row[1]))
                  self.button_commande6[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b93=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=93")               
               for row in self.b93:
                  self.button_commande6[(3,0)].setText(str(row[0]))
                  self.lab_commande6[(3,0)].setText(str(row[1]))
                  self.button_commande6[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b94=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=94")               
               for row in self.b94:
                  self.button_commande6[(3,1)].setText(str(row[0]))
                  self.lab_commande6[(3,1)].setText(str(row[1]))
                  self.button_commande6[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b95=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=95")               
               for row in self.b95:
                  self.button_commande6[(3,2)].setText(str(row[0]))
                  self.lab_commande6[(3,2)].setText(str(row[1]))
                  self.button_commande6[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b96=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=96")               
               for row in self.b96:
                  self.button_commande6[(3,3)].setText(str(row[0]))
                  self.lab_commande6[(3,3)].setText(str(row[1]))
                  self.button_commande6[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande6[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 7
               self.b97=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=97")               
               for row in self.b97:
                  self.button_commande7[(0,0)].setText(str(row[0]))
                  self.lab_commande7[(0,0)].setText(str(row[1]))
                  self.button_commande7[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b98=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=98")               
               for row in self.b98:
                  self.button_commande7[(0,1)].setText(str(row[0]))
                  self.lab_commande7[(0,1)].setText(str(row[1]))
                  self.button_commande7[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b99=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=99")               
               for row in self.b99:
                  self.button_commande7[(0,2)].setText(str(row[0]))
                  self.lab_commande7[(0,2)].setText(str(row[1]))
                  self.button_commande7[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b100=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=100")               
               for row in self.b100:
                  self.button_commande7[(0,3)].setText(str(row[0]))
                  self.lab_commande7[(0,3)].setText(str(row[1]))
                  self.button_commande7[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b101=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=101")               
               for row in self.b101:
                  self.button_commande7[(1,0)].setText(str(row[0]))
                  self.lab_commande7[(1,0)].setText(str(row[1]))
                  self.button_commande7[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b102=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=102")               
               for row in self.b101:
                  self.button_commande7[(1,1)].setText(str(row[0]))
                  self.lab_commande7[(1,1)].setText(str(row[1]))
                  self.button_commande7[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b103=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=103")               
               for row in self.b103:
                  self.button_commande7[(1,2)].setText(str(row[0]))
                  self.lab_commande7[(1,2)].setText(str(row[1]))
                  self.button_commande7[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b104=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=104")               
               for row in self.b104:
                  self.button_commande7[(1,3)].setText(str(row[0]))
                  self.lab_commande7[(1,3)].setText(str(row[1]))
                  self.button_commande7[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b105=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=105")               
               for row in self.b105:
                  self.button_commande7[(2,0)].setText(str(row[0]))
                  self.lab_commande7[(2,0)].setText(str(row[1]))
                  self.button_commande7[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b106=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=106")               
               for row in self.b106:
                  self.button_commande7[(2,1)].setText(str(row[0]))
                  self.lab_commande7[(2,1)].setText(str(row[1]))
                  self.button_commande7[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b107=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=107")               
               for row in self.b107:
                  self.button_commande7[(2,2)].setText(str(row[0]))
                  self.lab_commande7[(2,2)].setText(str(row[1]))
                  self.button_commande7[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b108=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=108")               
               for row in self.b108:
                  self.button_commande7[(2,3)].setText(str(row[0]))
                  self.lab_commande7[(2,3)].setText(str(row[1]))
                  self.button_commande7[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b109=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=109")               
               for row in self.b109:
                  self.button_commande7[(3,0)].setText(str(row[0]))
                  self.lab_commande7[(3,0)].setText(str(row[1]))
                  self.button_commande7[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b110=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=110")               
               for row in self.b110:
                  self.button_commande7[(3,1)].setText(str(row[0]))
                  self.lab_commande7[(3,1)].setText(str(row[1]))
                  self.button_commande7[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b111=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=111")               
               for row in self.b111:
                  self.button_commande7[(3,2)].setText(str(row[0]))
                  self.lab_commande7[(3,2)].setText(str(row[1]))
                  self.button_commande7[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b112=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=112")               
               for row in self.b112:
                  self.button_commande7[(3,3)].setText(str(row[0]))
                  self.lab_commande7[(3,3)].setText(str(row[1]))
                  self.button_commande7[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande7[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               #________PAGE 8
               self.b113=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=113")               
               for row in self.b113:
                  self.button_commande8[(0,0)].setText(str(row[0]))
                  self.lab_commande8[(0,0)].setText(str(row[1]))
                  self.button_commande8[(0,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(0,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b114=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=114")           
               for row in self.b114:
                  self.button_commande8[(0,1)].setText(str(row[0]))
                  self.lab_commande8[(0,1)].setText(str(row[1]))
                  self.button_commande8[(0,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(0,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b115=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=115")               
               for row in self.b115:
                  self.button_commande8[(0,2)].setText(str(row[0]))
                  self.lab_commande8[(0,2)].setText(str(row[1]))
                  self.button_commande8[(0,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(0,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b116=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=116")               
               for row in self.b116:
                  self.button_commande8[(0,3)].setText(str(row[0]))
                  self.lab_commande8[(0,3)].setText(str(row[1]))
                  self.button_commande8[(0,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(0,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b117=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=117")               
               for row in self.b117:
                  self.button_commande8[(1,0)].setText(str(row[0]))
                  self.lab_commande8[(1,0)].setText(str(row[1]))
                  self.button_commande8[(1,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(1,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b118=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=118")               
               for row in self.b118:
                  self.button_commande8[(1,1)].setText(str(row[0]))
                  self.lab_commande8[(1,1)].setText(str(row[1]))
                  self.button_commande8[(1,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(1,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b119=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=119")               
               for row in self.b119:
                  self.button_commande8[(1,2)].setText(str(row[0]))
                  self.lab_commande8[(1,2)].setText(str(row[1]))
                  self.button_commande8[(1,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(1,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b120=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=120")               
               for row in self.b120:
                  self.button_commande4[(1,3)].setText(str(row[0]))
                  self.lab_commande8[(1,3)].setText(str(row[1]))
                  self.button_commande8[(1,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(1,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b121=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=121")               
               for row in self.b121:
                  self.button_commande8[(2,0)].setText(str(row[0]))
                  self.lab_commande8[(2,0)].setText(str(row[1]))
                  self.button_commande8[(2,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(2,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b122=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=122")               
               for row in self.b122:
                  self.button_commande8[(2,1)].setText(str(row[0]))
                  self.lab_commande8[(2,1)].setText(str(row[1]))
                  self.button_commande8[(2,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(2,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b123=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=123")               
               for row in self.b123:
                  self.button_commande8[(2,2)].setText(str(row[0]))
                  self.lab_commande8[(2,2)].setText(str(row[1]))
                  self.button_commande8[(2,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(2,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b124=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=124")               
               for row in self.b124:
                  self.button_commande8[(2,3)].setText(str(row[0]))
                  self.lab_commande8[(2,3)].setText(str(row[1]))
                  self.button_commande8[(2,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(2,3)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b125=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=125")               
               for row in self.b125:
                  self.button_commande8[(3,0)].setText(str(row[0]))
                  self.lab_commande8[(3,0)].setText(str(row[1]))
                  self.button_commande8[(3,0)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(3,0)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b126=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=126")               
               for row in self.b126:
                  self.button_commande8[(3,1)].setText(str(row[0]))
                  self.lab_commande8[(3,1)].setText(str(row[1]))
                  self.button_commande8[(3,1)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(3,1)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b127=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=127")               
               for row in self.b127:
                  self.button_commande8[(3,2)].setText(str(row[0]))
                  self.lab_commande8[(3,2)].setText(str(row[1]))
                  self.button_commande8[(3,2)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(3,2)].setIconSize(QSize(self.icon_size,self.icon_size))
               self.b128=self.cursor.execute("SELECT nom,quantite,photo,prix,type FROM commandes  WHERE rowid=128")               
               for row in self.b128:
                  self.button_commande8[(3,3)].setText(str(row[0]))
                  self.lab_commande8[(3,3)].setText(str(row[1]))
                  self.button_commande8[(3,3)].setIcon(QIcon(str(row[2])))
                  self.button_commande8[(3,3)].setIconSize(QSize(self.icon_size,self.icon_size))"""
               self.bdd.commit()
               #====================== REFRESH LAB ==#
               #=====================================#
               for x in range(4):
                  for y in range(4):
                     #====================== PANIER
                     self.lab_commande1[(x,y)].adjustSize()
                     self.lab_commande2[(x,y)].adjustSize()
                     self.lab_commande3[(x,y)].adjustSize()
                     self.lab_commande4[(x,y)].adjustSize()
                     self.lab_commande5[(x,y)].adjustSize()
                     self.lab_commande6[(x,y)].adjustSize()
                     self.lab_commande7[(x,y)].adjustSize()
                     self.lab_commande8[(x,y)].adjustSize()
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass
   
   def information_commande(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.sql1=self.cursor.execute("""SELECT COUNT(*) FROM preview_commandes""")      
               for row in self.sql1:
                  if self.id_commande.value()> int(row[0]):
                     self.nom_commande.setText("")
                     self.qte_commande.setValue(0)
                     self.prix_commande.setValue(0)
                     self.photo=""
                     self.cat_commande.setText("")
                     self.id_produit.setValue(0)
                     self.code_produit.setText("")
                     #self.code_commande.setText("")
                     self.reduction.setText("")
                  else:
                     if self.id_client!=0:
                        self.sql2=self.cursor.execute("""SELECT nom,quantite,prix,photo,type,id_produit,code_produit,reduction
                                                         FROM preview_commandes WHERE id="""+"'"+str(self.id_commande.value())+"'")
                        for row in self.sql2:
                           self.nom_commande.setText(row[0])
                           self.qte_commande.setValue(int(row[1]))
                           self.prix_commande.setValue(float(row[2]))
                           self.photo=row[3]
                           self.cat_commande.setText(str(row[4]))
                           self.id_produit.setValue(int(row[5]))
                           self.code_produit.setText(str(row[6]))
                           self.reduction.setText(str(row[7]))
                        
                  
               #==== MISE A JOUR QUANTITE ET PRIX DANS LA TABLE COMMANDES
               self.sql__=self.cursor.execute(""" SELECT SUM(preview_commandes.quantite),
                                   SUM((preview_commandes.quantite*preview_commandes.prix)-
                              ((preview_commandes.quantite*preview_commandes.prix)*preview_commandes.reduction/100))
                                                      FROM preview_commandes """)
               
               for c in self.sql__:
                  if c[0] != None and c[0] > 0 and c[0] < 2 and self.id_client != 0:
                     self.btn_total.setText("QUANTITE COMMANDEE : "+str(c[0])+" PRODUIT"+" --- TOTAL A PAYER: "+str(c[1])+" F CFA")
                  elif c[0] != None and c[0] >= 2 and self.id_client != 0:
                     self.btn_total.setText("QUANTITE COMMANDEE : "+str(c[0])+" PRODUITS"+" --- TOTAL A PAYER: "+str(c[1])+" F CFA")
                  else:
                     self.btn_total.setText("QUANTITE COMMANDEE : 0 --- TOTAL A PAYER: 0 F CFA")
             
               self.bdd.commit()
               self.refresh_commande()
            else:
               pass

   def select_photo_commande(self):
      self.question=QMessageBox.question(self,str(self.app_name),'VOULEZ VOUS CHOISIR UNE IMAGE ?',QMessageBox.Yes,QMessageBox.No)
      if self.question==QMessageBox.Yes:
         filename = QFileDialog.getOpenFileName(self,"CHOISIR UNE IMAGE")
         self.photo=str(str(filename).split(",")[0].split("(")[1].split("'")[1])
         self.btn_view.setIcon(QIcon(self.photo))
         
         #QMessageBox.information(self,str(self.app_name),'--PHOTO SELECTIONNEE AVEC SUCCES--'+'\n\n\n ADRESSE DU FICHIER: '+self.photo+'\n')
      else:
         pass

   #______________________________________________DATA BASE PRODUITS END


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
   app.setStyle('plastique')
   screen=Commande()   
   screen.show()
   sys.exit(app.exec_())
      


