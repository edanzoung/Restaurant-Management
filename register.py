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
import datetime

#import warnings
#warnings.filterwarnings("ignore")
import multitimer
import random
import queue
import time
from numpy import convolve
import numpy as np
import copy

class Register(QMainWindow):
   def __init__(self):
      super().__init__()
      self.width=520
      self.height=500
      self.set=0
      self.photo_membre=''
      self.app_name='GESTION RESTAURANT'
      # this will hide the title bar
      #self.setWindowFlag(Qt.FramelessWindowHint)
      self.offset = None
      self.setGeometry(100,100,self.width,self.height)
      self.setWindowTitle('CREATION COMPTE ')  
      self.setStyleSheet("""
                         background-color:#383838;color:#fff
                         """)
      self.setFixedSize(self.width,self.height)
      self.setWindowOpacity(1)
      self.widgets()
   def widgets(self):
      

      #_________________________________________
      #_________________________________________
      #_________________________________________DASH 1
      self.dash_membre=QFrame(self)
      self.dash_membre.setStyleSheet("""
                                background-color:#03dffc;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:10px;border-bottom-left-radius:10px;
                                border-bottom-right-radius:10px;border-top-right-radius:10px
                                """)
      self.dash_membre.move(50,50)
      self.dash_membre.resize(400,400)

      #____________________________________FRAME BTN VIEW

      self.btn_view_frame=QFrame(self.dash_membre)            
      self.btn_view_frame.setStyleSheet("""border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:10px
                            """)
      self.btn_view_frame.move(5,5)
      self.btn_view_frame.resize(200,200)
      
      self.btn_view=QToolButton(self.btn_view_frame)
      self.btn_view.setStyleSheet("""
                                  QToolButton::pressed{background-color :#1b1b1c;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#05b7f7;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#1b1b1c;color:#fff;font-family: Time;font-style:italic;font-size:30pt;
                                  font-weight:bold;border-radius:10px}
                                  QToolButton::hover{background-color :#1b1b1c;color:#fff;border-style:solid;
                                  border-width:3px;border-color:#e3128c;font-family: Time;font-style:italic;font-size:30pt;
                                  font-weight:bold;border-radius:10px}
                                """)
      
      self.btn_view.setIconSize(QSize(350,350))
      self.btn_view.move(0,0)
      self.btn_view.resize(200,200)
      self.btn_view.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
      self.btn_view.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_view.clicked.connect(self.select_photo_membre)

      #_______MOT DE PASSE
      self.pass_lab_membre=QLabel('MOT DE PASSE',self.dash_membre)
      self.pass_lab_membre.setStyleSheet("""
                                  background-color:#03dffc;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.pass_lab_membre.move(30,210)
      self.pass_lab_membre.resize(150,30)

      self.pass_membre=QLineEdit(self.dash_membre)
      self.pass_membre.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.adresse_membre.setAlignment(Qt.AlignCenter)
      self.pass_membre.move(30,240)
      self.pass_membre.resize(150,30)
      self.pass_membre.setEchoMode(QLineEdit.Password)


      #_________________________________________ADD

      self.btn_add_membre=QPushButton('CREER COMPTE',self.dash_membre)
      self.btn_add_membre.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_add_membre.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_add_membre.clicked.connect(self.add_membre)
      self.btn_add_membre.move(30,300)
      self.btn_add_membre.resize(150,35)



      #_________________________________________
      #_________________________________________DASH 2
      self.dash2_membre=QFrame(self)
      self.dash2_membre.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:10px;border-bottom-left-radius:10px;
                                border-bottom-right-radius:10px;border-top-right-radius:10px
                                """)
      self.dash2_membre.move(280,50)
      self.dash2_membre.resize(190,400)

      #_______NOM
      self.nom_lab_membre=QLabel('NOM',self.dash2_membre)
      self.nom_lab_membre.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.nom_lab_membre.move(10,0)
      self.nom_lab_membre.resize(100,30)

      self.nom_membre=QLineEdit(self.dash2_membre)
      self.nom_membre.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.nom_membre.setAlignment(Qt.AlignCenter)
      self.nom_membre.move(10,30)
      self.nom_membre.resize(150,30)

      #_______PRENOM
      self.prenom_lab_membre=QLabel('PRENOM',self.dash2_membre)
      self.prenom_lab_membre.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.prenom_lab_membre.move(10,60)
      self.prenom_lab_membre.resize(200,30)

      self.prenom_membre=QLineEdit(self.dash2_membre)
      self.prenom_membre.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.prenom_membre.move(10,90)
      self.prenom_membre.resize(150,30)

      #_______PSEUDO
      self.pseudo_lab_membre=QLabel('PSEUDO',self.dash2_membre)
      self.pseudo_lab_membre.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.pseudo_lab_membre.move(10,120)
      self.pseudo_lab_membre.resize(200,30)

      self.pseudo_membre=QLineEdit(self.dash2_membre)
      self.pseudo_membre.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.pseudo_membre.move(10,150)
      self.pseudo_membre.resize(150,30)

      #_______DOCUMENT ID
      self.cnib_lab_membre=QLabel('N° CNIB/PASSEPORT',self.dash2_membre)
      self.cnib_lab_membre.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.cnib_lab_membre.move(10,180)
      self.cnib_lab_membre.resize(200,30)

      self.cnib_membre=QLineEdit(self.dash2_membre)
      self.cnib_membre.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.cnib_membre.move(10,210)
      self.cnib_membre.resize(150,30)
      #self.cnib_membre.setEchoMode(QLineEdit.Password)

      #_______NUM TEL
      self.tel_lab_membre=QLabel('N° TELEPHONE',self.dash2_membre)
      self.tel_lab_membre.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.tel_lab_membre.move(10,240)
      self.tel_lab_membre.resize(200,30)

      self.tel_membre=QLineEdit(self.dash2_membre)
      self.tel_membre.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.tel_membre.move(10,270)
      self.tel_membre.resize(150,30)
      
      #_______ADRESSE
      self.adresse_lab_membre=QLabel('ADRESSE',self.dash2_membre)
      self.adresse_lab_membre.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.adresse_lab_membre.move(10,300)
      self.adresse_lab_membre.resize(200,30)

      self.adresse_membre=QLineEdit(self.dash2_membre)
      self.adresse_membre.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.adresse_membre.setAlignment(Qt.AlignCenter)
      self.adresse_membre.move(10,330)
      self.adresse_membre.resize(150,30)


      #______________________________________________INTERFACE  membreS END


      self.btn_view_frame.show()
      self.dash2_membre.show()
      
      

   def add_membre(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  self.index1=[]
                  self.index2=[]
                  
                  self.ui="""{0}""".format(str(uuid.uuid4()).split('-')[0])
                  self.set_date= """{0}-{1}-{2}/{3}:{4}:{5}""".format(str(datetime.datetime.utcnow().day),
                                                                          str(datetime.datetime.utcnow().month),
                                                                          str(datetime.datetime.utcnow().year),
                                                                          str(datetime.datetime.utcnow().hour),
                                                                          str(datetime.datetime.utcnow().minute),
                                                                          str(datetime.datetime.utcnow().second))
                  
                  self.cursor=self.bdd.cursor()

                  #==== VERIFICATION MEMBRE EXISTANT AND AJOUT
                  self.cursor.execute("""SELECT id,nom,prenom,code_user FROM login
                                         WHERE pseudo={0}""".format("'"+str(self.pseudo_membre.text())+"'"))
                  self._result=self.cursor.fetchone()
                  if self._result == None:
                     self.cursor.execute("INSERT INTO login (nom,prenom,pseudo,pass,code_user,datetime)VALUES (?,?,?,?,?,?)",
                                      (self.nom_membre.text(),
                                       self.prenom_membre.text(),
                                       self.pseudo_membre.text(),
                                       self.pass_membre.text(),
                                       self.ui,
                                       self.set_date))

                     self.cursor.execute("INSERT INTO membres (nom,prenom,pseudo,cnib,telephone,adresse,photo,rôle,code_user,datetime)VALUES (?,?,?,?,?,?,?,?,?,?)",
                                      (self.nom_membre.text(),
                                       self.prenom_membre.text(),
                                       self.pseudo_membre.text(),
                                       self.cnib_membre.text(),
                                       self.tel_membre.text(),
                                       self.adresse_membre.text(),
                                       self.photo_membre,
                                       "NON VERIFIER",
                                       self.ui,
                                       self.set_date))

                     #==== MISE A JOUR ID 
                     self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                      rownum,nom,prenom,pseudo,cnib,telephone,adresse,photo,rôle,code_user,datetime
                                                      FROM membres""")
                     for i in self.s_ss:
                        self.index1.append(i)

                     self.cursor.execute("DELETE FROM membres")
                     
                     self.cursor.executemany("""INSERT INTO membres (id,nom,prenom,pseudo,cnib,telephone,adresse,photo,rôle,code_user,datetime)
                                                VALUES (?,?,?,?,?,?,?,?,?,?,?)""",self.index1)

                     #==== MISE A JOUR ID 
                     self._s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                      rownum,nom,prenom,pseudo,pass,code_user,datetime
                                                      FROM login""")
                     for i in self._s_ss:
                        self.index2.append(i)

                     self.cursor.execute("DELETE FROM login")
                     
                     self.cursor.executemany("""INSERT INTO login (id,nom,prenom,pseudo,pass,code_user,datetime)
                                                VALUES (?,?,?,?,?,?,?)""",self.index2)
                     self.bdd.commit()
                     QMessageBox.information(self,str(self.app_name),'COMPTE CREE AVEC SUCCES')
                  else:
                     QMessageBox.information(self,str(self.app_name),'PSEUDO DEJA UTILISE')
                  
                  self.bdd.commit()               
                  
               except:
                  QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")
               
            else:
               pass
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         QMessageBox.information(self,str(self.app_name),'BASE DE DONNE NON EXISTANTE')

   def select_photo_membre(self):
      self.question=QMessageBox.question(self,str(self.app_name),'VOULEZ VOUS CHOISIR UNE IMAGE ?',QMessageBox.Yes,QMessageBox.No)
      if self.question==QMessageBox.Yes:
         filename = QFileDialog.getOpenFileName(self,"CHOISIR UNE IMAGE")
         self.photo_membre="png"+str(str(filename).split(",")[0].split("(")[1].split("'")[1].split("/png")[-1])
         self.btn_view.setIcon(QIcon(self.photo_membre))
         
         #QMessageBox.information(self,str(self.app_name),'--PHOTO SELECTIONNEE AVEC SUCCES--'+'\n\n\n ADRESSE DU FICHIER: '+self.photo_membre+'\n')
      else:
         pass
     
      
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
   #_________________________________________DRAP MAIN WINDOW EVENTS END

if __name__=='__main__':
   app=QApplication(sys.argv)
   app.setStyle('plastique')
   screen=Register()   
   screen.show()
   sys.exit(app.exec_())
