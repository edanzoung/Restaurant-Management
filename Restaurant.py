#####################################
# GOOD  STOCK  V1.0 by Edan_Zoung
#####################################

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import sys
import sqlite3
import uuid

from stock import Stock
from membre import Membre
from commandes import Commande
from dash import Dash
from register import Register
from pass_forget import Forget
from config_app import name_app,name_app_btn

#import multitimer
#import random
#import queue
import time
import datetime
#from numpy import convolve
#import numpy as np
#import copy

class Gui(QMainWindow):
   def __init__(self):
      super().__init__()
      self.width=1200
      self.height=600
      self.set=0
      # this will hide the title bar
      #self.setWindowFlag(Qt.FramelessWindowHint)
      self.offset = None
      self.setGeometry(100,100,self.width,self.height)
      self.app_name=name_app
      self._app_name=name_app
      self.setWindowTitle(name_app_btn)  
      self.setStyleSheet(""" QMainWindow{ background-color:#000;color:#fff;
                             background-image: url("assets/background1.png");
                             background-repeat: no-repeat; 
                             background-position: center;}
                          QMessageBox{ background-color:#fff}""")
      #self.setFixedSize(self.width,self.height)
      self.setWindowOpacity(1)
      self.photo=''      
      self.widgets()
      self.user_pseudo=""
      self.login_page_at_starting()
      self.database()
      self.showMaximized()

   
      

   def widgets(self):

      #______________________________________________BANNER FRAME BEGINNING
      self.frame_banner=QFrame(self)
      self.frame_banner.setStyleSheet("""
                                background-color:#fc7f03;font-family: Time;font-style:italic;font-size:8pt;font-weight:bold;
                                border-color:#000;border-slyle:solid;border-size:1px;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.frame_banner.move(0,20)
      self.frame_banner.resize(1500,10)
      #______________________________________________BANNER FRAME END

      #______________________________________________INTERFACE LOGIN BEGINNING
      self.sizx=400
      self.sizy=400

      self.login=QFrame(self)
      self.login.setStyleSheet("""
                                background-color:transparent;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:10px;border-bottom-left-radius:10px;
                                border-bottom-right-radius:10px;border-top-right-radius:10px
                                """)
      self.login.move(250,100)
      self.login.resize(800,400)
          
      self.frame_login1=QToolButton(self.login)
      self.frame_login1.setStyleSheet("""
                         QToolButton::pressed{background-color :transparent;color:#f00;border-style:solid;
                         border-width:2px;border-color:transparent;font-family: Time;font-style:italic;font-size:30pt;
                         font-weight:bold;border-radius:10px}
                         QToolButton::!pressed{border-style:solid;border-width:2px;border-color:transparent;
                         background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:30pt;
                         font-weight:bold;border-radius:10px}
                       """)
      self.frame_login1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
      self.frame_login1.setCursor(QCursor(Qt.PointingHandCursor))
      #self.frame_login1.clicked.connect(self.stock_page)
      self.frame_login1.setIcon(QIcon('png/fourchette2.png'))
      self.frame_login1.setIconSize(QSize(300,300))
      self.frame_login1.move(0,0)
      self.frame_login1.resize(self.sizx,self.sizy)
      self.frame_login1.setText(str(self._app_name))

      self.frame_login2=QFrame(self.login)
      self.frame_login2.setStyleSheet("""
                                background-color :transparent;color:#fff;border-style:solid;
                         border-width:2px;border-color:#fc7f03;font-family: Time;font-style:italic;font-size:15pt;
                         font-weight:bold;border-radius:10px
                                """)                    
      self.frame_login2.move(400,0)            
      self.frame_login2.resize(self.sizx,self.sizy)

      

      #_______UTILISATEUR
      self.user_lab=QLabel('PSEUDO',self.frame_login2)
      self.user_lab.setStyleSheet("""
                                background-color :transparent;color:#fff;border-style:solid;
                         border-width:2px;border-color:transparent;font-family: Time;font-style:italic;font-size:15pt;
                         font-weight:bold;border-radius:10px
                                """)
      self.user_lab.move(120,30)
      self.user_lab.resize(200,30)

      self.user=QLineEdit(self.frame_login2)
      self.user.setStyleSheet("""
                                background-color :#fff;color:#000;border-style:solid;
                         border-width:2px;border-color:#000;font-family: Time;font-style:italic;font-size:15pt;
                         font-weight:bold;border-radius:10px
                                """)
      self.user.setAlignment(Qt.AlignCenter)
      self.user.setEchoMode(QLineEdit.Password)
      self.user.move(80,60)
      self.user.resize(250,30)


      #_______MOT DE PASSE
      self.mdp_lab=QLabel('MOT DE PASSE',self.frame_login2)
      self.mdp_lab.setStyleSheet("""
                                background-color :transparent;color:#fff;border-style:solid;
                         border-width:2px;border-color:transparent;font-family: Time;font-style:italic;font-size:15pt;
                         font-weight:bold;border-radius:10px
                                """)
      self.mdp_lab.move(120,110)
      self.mdp_lab.resize(200,30)

      self.mdp=QLineEdit(self.frame_login2)
      self.mdp.setStyleSheet("""
                                background-color :#fff;color:#000;border-style:solid;
                         border-width:2px;border-color:#000;font-family: Time;font-style:italic;font-size:15pt;
                         font-weight:bold;border-radius:10px
                                """)
      self.mdp.setAlignment(Qt.AlignCenter)
      self.mdp.setEchoMode(QLineEdit.Password)
      self.mdp.move(80,140)
      self.mdp.resize(250,30)

      #_______LOGIN BUTTON
      self.btn_login=QToolButton(self.frame_login2)
      self.btn_login.setStyleSheet("""
                         QToolButton::pressed{background-color :#1b1b1c;color:#000;border-style:solid;
                         border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:15pt;
                         font-weight:bold;border-radius:10px}
                         QToolButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                         background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                         font-weight:bold;border-radius:10px}
                         QToolButton::hover{background-color :#1b1b1c;color:#fff;border-style:solid;
                         border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:8pt;
                         font-weight:bold;border-radius:10px}
                                  """)
      self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_login.clicked.connect(self.session_login)
      self.btn_login.setText('SE CONNECTER')
      self.btn_login.move(160,200)
      self.btn_login.resize(100,20)

      """
      #_______REGISTER BUTTON
      self.register_lab=QLabel('VOTRE PREMIERE FOIS ?',self.frame_login2)
      self.register_lab.setStyleSheet(\"""
                                background-color :#000;color:#fff;border-style:solid;
                         border-width:2px;border-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                         font-weight:bold;border-radius:10px
                                \""")
      self.register_lab.move(10,320)
      self.register_lab.resize(150,30)
      
      self.btn_register=QToolButton(self.frame_login2)
      self.btn_register.setStyleSheet(\"""
                         QToolButton::pressed{background-color :#1b1b1c;color:#000;border-style:solid;
                         border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:15pt;
                         font-weight:bold;border-radius:10px}
                         QToolButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                         background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                         font-weight:bold;border-radius:10px}
                         QToolButton::hover{background-color :#1b1b1c;color:#0f0;border-style:solid;
                         border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:8pt;
                         font-weight:bold;border-radius:10px}
                                  \""")
      self.btn_register.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_register.clicked.connect(self.Register_page)
      self.btn_register.setText('CREER UN COMPTE')
      self.btn_register.move(10,350)
      self.btn_register.resize(120,40)
      """

      #_______CHANGE BUTTON
      self.change_lab=QLabel('MOT DE PASSE OUBLIE ?',self.frame_login2)
      self.change_lab.setStyleSheet("""
                                background-color :transparent;color:#fff;border-style:solid;
                         border-width:2px;border-color:transparent;font-family: Time;font-style:italic;font-size:8pt;
                         font-weight:bold;border-radius:10px
                                """)
      self.change_lab.move(240,320)
      self.change_lab.resize(150,20)
      
      self.btn_change=QToolButton(self.frame_login2)
      self.btn_change.setStyleSheet("""
                         QToolButton::pressed{background-color :#1b1b1c;color:#000;border-style:solid;
                         border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:15pt;
                         font-weight:bold;border-radius:10px}
                         QToolButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                         background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                         font-weight:bold;border-radius:10px}
                         QToolButton::hover{background-color :#1b1b1c;color:#0f0;border-style:solid;
                         border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:8pt;
                         font-weight:bold;border-radius:10px}
                                  """)
      self.btn_change.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_change.clicked.connect(self.Pass_Forget_page)
      self.btn_change.setText('CHANGER MOT DE PASSE')
      self.btn_change.move(240,350)
      self.btn_change.resize(150,20)

      
      
      #______________________________________________INTERFACE LOGIN END

      #______________________________________________INTERFACE  HOME BEGINNING
      self.size_x_home=400
      self.size_y_home=200
      self.home=QFrame(self)
      self.home.setStyleSheet("""
                                background-color:transparent;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.home.move(250,100)
      self.home.resize(800,600)
      
      self.button_home={}
      for i in range(3):
          for j in range(2):            
              self.button_home[(i,j)]=QToolButton(self.home)
              self.button_home[(i,j)].setStyleSheet("""
                                  QToolButton::pressed{background-color :transparent;color:#000;border-style:solid;
                                  border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:15pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::!pressed{border-style:solid;border-width:1px;border-color:transparent;
                                  background-color:transparent;color:#fff;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::hover{background-color :transparent;color:#fc7f03;border-style:solid;
                                  border-width:3px;border-color:transparent;font-family: Time;font-style:italic;font-size:15pt;
                                  font-weight:bold;border-radius:10px}
                                """)
              self.button_home[(i,j)].setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
              self.button_home[(i,j)].setCursor(QCursor(Qt.PointingHandCursor))
              self.button_home[(i,j)].resize(self.size_x_home,self.size_y_home)
              

      self.button_home[(0,0)].move(0,0)
      self.button_home[(0,1)].move(400,0)
      self.button_home[(1,0)].move(0,200)
      self.button_home[(1,1)].move(400,200)
      self.button_home[(2,0)].move(0,400)
      self.button_home[(2,1)].move(400,400)

      self.button_home[(0,0)].setText('MES STOCKS')
      self.button_home[(0,1)].setText('UTILISATEURS')
      self.button_home[(1,0)].setText('MES COMMANDES')
      self.button_home[(1,1)].setText('RESTAURANT')
      self.button_home[(2,0)].setText('MES VENTES')
      self.button_home[(2,1)].setText('MES LIVRAISONS')

      self.button_home[(0,0)].setIcon(QIcon('png/box2.png'))
      self.button_home[(0,0)].setIconSize(QSize(100,100))
      self.button_home[(0,1)].setIcon(QIcon('png/user2.png'))
      self.button_home[(0,1)].setIconSize(QSize(100,100))
      self.button_home[(1,0)].setIcon(QIcon('png/commande3.png'))
      self.button_home[(1,0)].setIconSize(QSize(100,100))
      self.button_home[(1,1)].setIcon(QIcon('png/shop2.png'))
      self.button_home[(1,1)].setIconSize(QSize(100,100))
      self.button_home[(2,0)].setIcon(QIcon('png/panier2.png'))
      self.button_home[(2,0)].setIconSize(QSize(100,100))
      self.button_home[(2,1)].setIcon(QIcon('png/commande2.png'))
      self.button_home[(2,1)].setIconSize(QSize(100,100))

      self.button_home[(0,0)].clicked.connect(self.Stock_page)
      self.button_home[(0,1)].clicked.connect(self.Membres_page)
      self.button_home[(1,0)].clicked.connect(self.Commandes_page)
      self.button_home[(1,1)].clicked.connect(self.Dash_page)
      #self.button_home[(2,0)].clicked.connect(self.Commandes_page)
      #self.button_home[(2,1)].clicked.connect(self.Dash_page)

      
      #______________________________________________INTERFACE  HOME END

      
      #___________________________________________INTERFACE  STOCK BEGINNING
      self.size_x_stock=400
      self.size_y_stock=200
      self.stock=QFrame(self)
      self.stock.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:0px;border-bottom-left-radius:0px;
                                border-bottom-right-radius:0px;border-top-right-radius:0px
                                """)
      self.stock.move(200,100)
      self.stock.resize(800,400)      
      #______________________________________________INTERFACE  STOCK END

      #______________________________________________PRINCIPAL INTERFACE BEGINNING

      #_________________________________________Home Button BEGINNING

      self.btn_h=QPushButton('ACCUEIL',self)
      self.btn_h.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_h.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_h.clicked.connect(self.h_page)
      self.btn_h.move(350,15)
      self.btn_h.resize(100,20)
      #_________________________________________Home Button END


      #_________________________________________PREV Button to VENTE

      self.btn_p=QPushButton('PRECEDENT',self)
      self.btn_p.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_p.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_p.clicked.connect(self.h_page)
      self.btn_p.move(250,15)
      self.btn_p.resize(100,20)

      #_________________________________________PREV Button to HOME

      self.btn_p2=QPushButton('PRECEDENT',self)
      self.btn_p2.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_p2.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_p2.clicked.connect(self.Stocks_page)
      self.btn_p2.move(250,15)
      self.btn_p2.resize(100,20)

      #_________________________________________Deconnexion Button BEGINNING
      self.btn_deco=QPushButton('DECONNEXION',self)
      self.btn_deco.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_deco.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_deco.clicked.connect(self.session_logout)
      self.btn_deco.move(50,15)
      self.btn_deco.resize(100,20)
      #_________________________________________Deconnexion Button END

      #______________________________________________PRINCIPAL INTERFACE END

   def get_pseudo(self):
      return self.user_pseudo
   

   def database(self):
      self.ui1="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui2="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui3="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui4="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui5="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui6="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui7="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui8="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui9="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui10="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui11="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui12="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui13="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui14="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui15="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui16="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui17="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui18="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui19="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui20="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui21="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui22="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui23="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui24="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui25="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui26="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui27="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui28="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui29="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui30="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui31="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui32="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui33="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui34="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui35="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      self.ui36="""{0}""".format(str(uuid.uuid4()).split('-')[0])
      
      self.set_date= """{0}-{1}-{2}/{3}:{4}:{5}""".format(str(datetime.datetime.utcnow().day),
                                                              str(datetime.datetime.utcnow().month),
                                                              str(datetime.datetime.utcnow().year),
                                                              str(datetime.datetime.utcnow().hour),
                                                              str(datetime.datetime.utcnow().minute),
                                                              str(datetime.datetime.utcnow().second))
      records=[(1,'eau_pure'),
               (2,'sucree'),
               (3,'alcool'),
               (4,'biscuit'),
               (5,'gateau'),
               (6,'glace'),
               (7,'bonbon'),
               (8,'fruit'),
               (9,'nescafe'),
               (10,'lipton'),
               (11,'cappuccino'),
               (12,'espresso'),
               (13,'poulet'),
               (14,'poisson'),
               (15,'salade'),
               (16,'sandwich'),
               (17,'pizza'),
               (18,'riz'),
               (19,'spaguetti'),
               (20,'couscous'),
               (21,'tô'),
               (22,'haricot'),
               (23,'attieke'),
               (24,'garba'),
               (25,'soupe'),
               (26,'omelette'),
               (27,'brochette')]
      record_role=[(1,'ADMIN'),
                   (2,'CAISSE'),
                   (3,'COMPTABILITE'),
                   (4,'LIVRAISON'),
                   (5,'STOCK')]
      record_boisson=[(1,'FANTA-C','100','400','png/e_fanta4.png','sucree',self.ui1,self.set_date,'0','0','0','0','0','0'),
               (2,'COCA-C','100','400','png/e_coca4.png','sucree',self.ui2,self.set_date,'0','0','0','0','0','0'),
               (3,'SPRITE-C','100','400','png/e_sprite2.png','sucree',self.ui3,self.set_date,'0','0','0','0','0','0'),
               (4,'REDBULL-C','100','400','png/redbull.png','sucree',self.ui4,self.set_date,'0','0','0','0','0','0'),
               (5,'GUINNESS-B','100','800','png/biere-guinness.png','alcool',self.ui5,self.set_date,'0','0','0','0','0','0'),
               (6,'BEAUFORT-B','100','600','png/beaufort.png','alcool',self.ui6,self.set_date,'0','0','0','0','0','0'),
               (7,'CHILL-B','100','500','png/petite-chill.png','alcool',self.ui7,self.set_date,'0','0','0','0','0','0'),
               (8,'DOPPEL-B','100','600','png/biere-doppel.png','alcool',self.ui8,self.set_date,'0','0','0','0','0','0'),
               (9,'COCA-B','100','500','png/e_coca1.png','sucree',self.ui9,self.set_date,'0','0','0','0','0','0'),
               (10,'FANTA-B','100','500','png/e_fanta1.png','sucree',self.ui10,self.set_date,'0','0','0','0','0','0'),
               (11,'LAFI-B','100','500','png/eau-lafi.png','eau_pure',self.ui11,self.set_date,'0','0','0','0','0','0'),
               (12,'BRAVO-ORANGE','100','600','png/bravo_orange_rouge.png','sucree',self.ui12,self.set_date,'0','0','0','0','0','0'),
               (13,'BRAVO-RAISIN','100','600','png/bravo_raisin.png','sucree',self.ui13,self.set_date,'0','0','0','0','0','0'),
               (14,'HEINEKEN','100','600','png/e_heineken1.png','alcool',self.ui14,self.set_date,'0','0','0','0','0','0')]
      
      record_dessert=[(1,'GLACE','100','500','png/glace2.png','glace',self.ui15,self.set_date,'0','0','0','0','0','0'),
               (2,'GATEAU','100','500','png/dessert.png','gateau',self.ui16,self.set_date,'0','0','0','0','0','0'),
               (3,'BONBON','100','50','png/bonbon.png','bonbon',self.ui17,self.set_date,'0','0','0','0','0','0'),
               (4,'BONBON','100','50','png/bonbon3.png','bonbon',self.ui18,self.set_date,'0','0','0','0','0','0'),
               (5,'BONBON','100','50','png/bonbon2.png','bonbon',self.ui19,self.set_date,'0','0','0','0','0','0'),
               (6,'GLACE','100','500','png/glace.png','glace',self.ui20,self.set_date,'0','0','0','0','0','0'),
               (7,'SALADE','100','500','png/fruits.png','fruit',self.ui21,self.set_date,'0','0','0','0','0','0')]

      record_cafe=[(1,'NESCAFE','100','200','png/nescafe.png','nescafe',self.ui22,self.set_date,'0','0','0','0','0','0'),
               (2,'CAPPUCCINO','100','500','png/cappuccino.png','capuccino',self.ui23,self.set_date,'0','0','0','0','0','0'),
               (3,'LIPTON','100','200','png/lipton.png','lipton',self.ui24,self.set_date,'0','0','0','0','0','0'),
               (4,'ESPRESSO','100','500','png/espresso.png','espresso',self.ui25,self.set_date,'0','0','0','0','0','0')]

      record_plat=[(1,'RIZ','100','500','png/rice.png','riz',self.ui26,self.set_date,'0','0','0','0','0','0'),
               (2,'SPAGUETTI','100','500','png/spaguetti.png','spaguetti',self.ui27,self.set_date,'0','0','0','0','0','0'),
               (3,'PIZZA','100','500','png/pizza.png','pizza',self.ui28,self.set_date,'0','0','0','0','0','0'),
               (4,'POULET','100','1500','png/poulet.png','poulet',self.ui29,self.set_date,'0','0','0','0','0','0'),
               (5,'POISSON','100','1500','png/poisson.png','poisson',self.ui30,self.set_date,'0','0','0','0','0','0'),
               (6,'OMELETTE','100','600','png/omelette2.png','omelette',self.ui31,self.set_date,'0','0','0','0','0','0'),
               (7,'BROCHETTE','100','600','png/brochette.png','brochette',self.ui32,self.set_date,'0','0','0','0','0','0'),
               (8,'SALADE','100','600','png/salade.png','salade',self.ui33,self.set_date,'0','0','0','0','0','0')]

      record_login=[(1,'Guest','','','',self.ui34,self.set_date),
                    (2,'Zoungrana','Elkana Daniel','edanzoung','Zoungrana',self.ui35,self.set_date),
                    (3,'Damiba','Jean Claude','jeanclaude','Damiba',self.ui36,self.set_date)]
      
      record_membre=[(1,'Guest','','','','','','png/user.png','ADMIN',self.ui34,self.set_date),
                     (2,'Zoungrana','Elkana Daniel','edanzoung','B12345678','22670516127','Tanghin','png/user1.png','ADMIN',self.ui35,self.set_date),
                     (3,'Damiba','Jean Claude','jeanclaude','B12345678','22671838312','Tanghin','png/user2.png','ADMIN',self.ui36,self.set_date)]
      
      if not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         self.question=QMessageBox.question(self,str(self.app_name),'BASE DE DONNEE NON EXISTANTE\nVOULEZ-VOUS EN CREER ?',QMessageBox.Yes,QMessageBox.No)
         if self.question==QMessageBox.Yes:
            try:
               self.bdd=sqlite3.connect('restaurant.bd')
            except sqlite3.Error as e:
               QMessageBox.information(self,str(self.app_name),e,QMessageBox.Ok)
            finally:
               if self.bdd:
                  
                  self.cursor=self.bdd.cursor()
                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS boissons (
                                      id integer primary key,
                                      nom text,
                                      quantite text,
                                      prix text,
                                      photo text,
                                      categorie text,
                                      code_produit text,
                                      datetime text,
                                      reduction text,
                                      is_added text,
                                      is_ordered text,
                                      is_processed text,
                                      is_shipped text,
                                      is_paid text)""")

                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS desserts (
                                      id integer primary key,
                                      nom text,
                                      quantite text,
                                      prix text,
                                      photo text,
                                      categorie text,
                                      code_produit text,
                                      datetime text,
                                      reduction text,
                                      is_added text,
                                      is_ordered text,
                                      is_processed text,
                                      is_shipped text,
                                      is_paid text)""")

                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS cafes (
                                      id integer primary key,
                                      nom text,
                                      quantite text,
                                      prix text,
                                      photo text,
                                      categorie text,
                                      code_produit text,
                                      datetime text,
                                      reduction text,
                                      is_added text,
                                      is_ordered text,
                                      is_processed text,
                                      is_shipped text,
                                      is_paid text)""")

                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS plats (
                                      id integer primary key,
                                      nom text,
                                      quantite text,
                                      prix text,
                                      photo text,
                                      categorie text,
                                      code_produit text,
                                      datetime text,
                                      reduction text,
                                      is_added text,
                                      is_ordered text,
                                      is_processed text,
                                      is_shipped text,
                                      is_paid text)""")

                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS panier (
                                      id integer primary key,
                                      nom text,
                                      quantite text,
                                      prix text,
                                      id_produit text,
                                      code_produit text,
                                      type text,
                                      categorie text,
                                      photo text,
                                      datetime text,
                                      reduction text,
                                      is_added text,
                                      is_ordered text,
                                      is_processed text,
                                      is_shipped text,
                                      is_paid text)""")

                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS commandes (
                                      id integer primary key,
                                      nom text,
                                      quantite text,
                                      prix text,
                                      id_produit text,
                                      code_produit text,
                                      type text,
                                      categorie text,
                                      photo text,
                                      reduction text,
                                      datetime text,
                                      code_commande text,
                                      code_client text,
                                      is_added text,
                                      is_ordered text,
                                      is_processed text,
                                      is_shipped text,
                                      is_paid text)""")

                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS preview_commandes (
                                      id integer primary key,
                                      nom text,
                                      quantite text,
                                      prix text,
                                      id_produit text,
                                      code_produit text,
                                      type text,
                                      categorie text,
                                      photo text,
                                      datetime text,
                                      reduction text,
                                      code_client text)""")

                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS clients (
                                      id integer primary key,
                                      code_commande text,
                                      code_client text,
                                      nom_client text,
                                      numero_client text,
                                      adresse_client text,
                                      cnib_client text,
                                      numero_table text,
                                      datetime text)""")

                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS livraisons (
                                      id integer primary key,
                                      nom text,
                                      quantite text,
                                      prix text,
                                      id_produit text,
                                      code_produit text,
                                      type text,
                                      categorie text,
                                      photo text,
                                      reduction text,
                                      datetime text,
                                      code_commande text,
                                      code_livraison text,
                                      code_client text,
                                      nom_client text,
                                      numero_client text,
                                      adresse_client text,
                                      cnib_client text,
                                      numero_table text,
                                      is_added text,
                                      is_ordered text,
                                      is_processed text,
                                      is_shipped text,
                                      is_paid text)""")

                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS login (
                                      id integer primary key,
                                      nom text,
                                      prenom text,
                                      pseudo text,
                                      pass text,
                                      code_user text,
                                      datetime text)""")

                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS session (
                                      id integer primary key,
                                      nom text,
                                      prenom text,
                                      pseudo text,
                                      code_user text,
                                      datetime text)""")

                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS membres (
                                      id integer primary key,
                                      nom text,
                                      prenom text,
                                      pseudo text,
                                      cnib text,
                                      telephone text,
                                      adresse text,
                                      photo text,
                                      rôle text,
                                      code_user text,
                                      datetime text)""")
                  

                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS categories (
                                      id integer primary key,
                                      categorie text)""")
                  
                  self.cursor.execute("""
                                      CREATE TABLE IF NOT EXISTS roles (
                                      id integer primary key,
                                      role text)""")

                  
                  self.cursor.executemany("""INSERT INTO categories (id,categorie)
                                         VALUES (?,?)""",records)
                  self.cursor.executemany("""INSERT INTO roles (id,role)
                                         VALUES (?,?)""",record_role)
                  self.cursor.executemany("""INSERT INTO boissons (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,is_added,is_ordered,is_processed,is_shipped,is_paid)
                                         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",record_boisson)
                  self.cursor.executemany("""INSERT INTO desserts (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,is_added,is_ordered,is_processed,is_shipped,is_paid)
                                         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",record_dessert)
                  self.cursor.executemany("""INSERT INTO cafes (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,is_added,is_ordered,is_processed,is_shipped,is_paid)
                                         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",record_cafe)
                  self.cursor.executemany("""INSERT INTO plats (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,is_added,is_ordered,is_processed,is_shipped,is_paid)
                                         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",record_plat)

                  self.cursor.executemany("""INSERT INTO membres (id,nom,prenom,pseudo,cnib,telephone,adresse,photo,rôle,code_user,datetime)
                                                VALUES (?,?,?,?,?,?,?,?,?,?,?)""",record_membre)
                  self.cursor.executemany("""INSERT INTO login (id,nom,prenom,pseudo,pass,code_user,datetime)
                                                VALUES (?,?,?,?,?,?,?)""",record_login)
                  
                  self.bdd.commit()
                  self.bdd.close()
                  QMessageBox.information(self,str(self.app_name),'BASE DE DONNEE CREEE AVEC SUCCES',QMessageBox.Ok)

               else:
                  self.bdd.rollback()
                  QMessageBox.information(self,str(self.app_name),"BASE DE DONNEE NON CREEE \nUNE ERREUR S'EST PRODUITE ",QMessageBox.Ok)
         else:
            QMessageBox.information(self,str(self.app_name),"SANS BASE DE DONNEE LE PROGRAMME\nNE FONCTIONNERA PAS CORRECTEMENT ",QMessageBox.Ok)
      else:
         pass

   def Stock_page(self):
      self.win_stock=Stock()
      self.win_stock.show()
   def Membres_page(self):     
      self.win_membre=Membre()
      self.win_membre.show()
   def Commandes_page(self):     
      self.win_paye=Commande()
      self.win_paye.show()
   def Dash_page(self):  
      self.win_vente=Dash()
      self.win_vente.show()
   def Register_page(self):     
      self.win_register=Register()
      self.win_register.show()

   def Pass_Forget_page(self):     
      self.win_pass_forget=Forget()
      self.win_pass_forget.show()

   def session_login(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  self.index1=[]
                  self.set_date= """{0}-{1}-{2}/{3}:{4}:{5}""".format(str(datetime.datetime.utcnow().day),
                                                                          str(datetime.datetime.utcnow().month),
                                                                          str(datetime.datetime.utcnow().year),
                                                                          str(datetime.datetime.utcnow().hour),
                                                                          str(datetime.datetime.utcnow().minute),
                                                                          str(datetime.datetime.utcnow().second))
                  self.cursor=self.bdd.cursor()                     
                  #==== VERIFICATION IF PSEUDO AND PASSWORD MATCH
                  self.cursor.execute("""SELECT nom,prenom,pass FROM login
                                            WHERE code_user = (SELECT code_user FROM membres WHERE pseudo = {0})""".format("'"+str(self.user.text())+"'"))
                  self._result=self.cursor.fetchone()
                  self.bdd.commit()
                  
                  if self._result[2] == str(self.mdp.text()):                     
                     QMessageBox.information(self,str(self.app_name),'COMPTE EXISTANT',QMessageBox.Ok)
                     #==== VERIFICATION IF MEMBRE IN SESSION
                     self.cursor.execute("""SELECT id,nom,prenom,code_user FROM session WHERE pseudo = {0}""".format("'"+str(self.user.text())+"'"))
                     self._result_session=self.cursor.fetchone()
                     if self._result_session == None:                        
                        #=====================================================================================
                        #================ SELECT 
                        self.cursor.execute("""SELECT nom,prenom,pseudo,code_user FROM login
                                                  WHERE  pseudo = {0} """.format("'"+str(self.user.text())+"'"))
                        self._result_membre=self.cursor.fetchone()
                        
                        #==== SESSION LOGIN
                        self.cursor.execute("""INSERT INTO session (nom,prenom,pseudo,code_user,datetime)
                                               VALUES (?,?,?,?,?)""",(str(self._result_membre[0]),str(self._result_membre[1]),
                                                                    str(self._result_membre[2]),str(self._result_membre[3]),self.set_date))
                   

                        #==== MISE A JOUR ID SESSION
                        self.select=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                         rownum,nom,prenom,pseudo,code_user,datetime
                                                         FROM session""")
                        for i in self.select:
                           self.index1.append(i)

                        self.cursor.execute("DELETE FROM session")
                        
                        self.cursor.executemany("""INSERT INTO session (id,nom,prenom,pseudo,code_user,datetime)
                                                   VALUES (?,?,?,?,?,?)""",self.index1)
                        #=====================================================================================
                        
                        self.cursor.execute("""SELECT nom,prenom,datetime FROM login
                                            WHERE code_user=(SELECT code_user FROM membres
                                                WHERE pseudo={0})""".format("'"+str(self.user.text())+"'"))
                        self._result_=self.cursor.fetchone()
                     
                        self.bdd.commit()

                        QMessageBox.information(self,str(self.app_name),'   CONNECTE   ',QMessageBox.Ok)
                        self.user.pseudo=str(self.user.text())
                        print(self.user.pseudo)
                        self.home.show()
                        self.login.hide()
                        self.stock.hide()
                        self.btn_h.hide()
                        self.btn_deco.show()
                        self.btn_p.hide()
                        self.btn_p2.hide()                                             
                        QMessageBox.information(self,str(self.app_name),'BIENVENUE '+str(self._result_[1])+" "+str(self._result_[0]),QMessageBox.Ok)
                        
                     else:
                        self.cursor.execute("""SELECT nom,prenom,datetime FROM login
                                            WHERE code_user=(SELECT code_user FROM membres
                                                WHERE pseudo={0})""".format("'"+str(self.user.text())+"'"))
                        self.result_=self.cursor.fetchone()
                     
                        self.bdd.commit()
                        QMessageBox.information(self,str(self.app_name),"COMPTE NON DECONNECTE\nLORS DE LA DERNIERE SESSION\n\nDERNIERE SESSION: {0}".format(str(self.result_[2])),QMessageBox.Ok)
                        self.home.show()
                        self.login.hide()
                        self.stock.hide()
                        self.btn_h.hide()
                        self.btn_deco.show()
                        self.btn_p.hide()
                        self.btn_p2.hide()                                             
                        QMessageBox.information(self,str(self.app_name),'BIENVENUE '+str(self._result_session[2])+" "+str(self._result_session[1]),QMessageBox.Ok)
                  else:
                     QMessageBox.information(self,str(self.app_name),'MOT DE PASSE NON VALIDE',QMessageBox.Ok)
                     
               except:
                  QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE",QMessageBox.Ok)

   def session_logout(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  self.index1=[]
                  self.cursor=self.bdd.cursor()
                  #==== VERIFICATION IF MEMBRE IN SESSION
                  self.cursor.execute("""SELECT id,nom,prenom,code_user FROM session
                                         WHERE pseudo = {0} """.format("'"+str(self.user.text())+"'"))
                  self._result_session=self.cursor.fetchone()
                  self.bdd.commit()
                  if self._result_session is not None:
                     self.question=QMessageBox.question(self,str(self.app_name),'VOUS VOULEZ DECONNECTER ?',QMessageBox.Yes,QMessageBox.No)
                     if self.question==QMessageBox.Yes:
                        #==== SESSION LOGOUT
                        self.cursor.execute("""DELETE FROM session WHERE pseudo={0}""".format("'"+str(self.user.text())+"'"))
                        self.bdd.commit()
                        #==== MISE A JOUR ID SESSION
                        self.select=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                         rownum,nom,prenom,pseudo,code_user,datetime
                                                         FROM session""")
                        for i in self.select:
                           self.index1.append(i)

                        self.cursor.execute("DELETE FROM session")
                        
                        self.cursor.executemany("""INSERT INTO session (id,nom,prenom,pseudo,code_user,datetime)
                                                   VALUES (?,?,?,?,?,?)""",self.index1)
                        self.bdd.commit()
                        self.user.setText("")
                        self.mdp.setText("")
                        QMessageBox.information(self,str(self.app_name),'A BIENTÔT ',QMessageBox.Ok)
                        self.login_page()                        
                  else:
                     QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE",QMessageBox.Ok)                        
               except:
                  QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE",QMessageBox.Ok)

   

   def h_page(self):
      self.home.show()
      self.login.hide()
      self.stock.hide()
      self.btn_h.hide()
      self.btn_deco.show()
      self.btn_p.hide()
      self.btn_p2.hide()
                        
      

   def login_page(self):     
      self.login.show()
      self.home.hide()
      self.stock.hide()
      self.btn_h.hide()
      self.btn_deco.hide()
      self.btn_p.hide()
      self.btn_p2.hide()
      QMessageBox.information(self,str(self.app_name),'   COMPTE DECONNECTE   ',QMessageBox.Ok)

   def login_page_at_starting(self):     
      self.login.show()
      self.home.hide()
      self.stock.hide()
      self.btn_h.hide()
      self.btn_deco.hide()
      self.btn_p.hide()
      self.btn_p2.hide()
      
   def Stocks_page(self):
      self.login.hide()
      self.home.hide()
      self.stock.show()
      self.btn_p2.hide()
      self.btn_p.hide()
      self.btn_h.show()
      self.set=0

   #_________________________________________close APP BEGINNING
   def close(self):
      self.question=QMessageBox.question(self,str(self.app_name),'QUITTER ?',QMessageBox.Yes,QMessageBox.No)
      if self.question==QMessageBox.Yes:
         os._exit(0)
      elif self.question==QMessageBox.No:
         pass
   #_________________________________________close APP END

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
   app.setStyle('Vista')
   screen=Gui()   
   screen.show()
   sys.exit(app.exec_())
