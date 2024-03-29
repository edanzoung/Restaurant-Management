#####################################
# IZI TOC V1.0 by Edan_Zoung
#####################################

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import sys
import sqlite3

#import warnings
#warnings.filterwarnings("ignore")
import multitimer
import random
import queue
import time
from numpy import convolve
import numpy as np
import copy

class Forget(QMainWindow):
   def __init__(self):
      super().__init__()
      self.width=520
      self.height=400
      self.set=0
      self.photo_membre=''
      self.app_name='GESTION RESTAURANT'
      # this will hide the title bar
      #self.setWindowFlag(Qt.FramelessWindowHint)
      self.__pseudo=None
      self.offset = None
      self.setGeometry(100,100,self.width,self.height)
      self.setWindowTitle('CHANGER MOT DE PASSE')
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
                                background-color:#c22000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:10px;border-bottom-left-radius:10px;
                                border-bottom-right-radius:10px;border-top-right-radius:10px
                                """)
      self.dash_membre.move(50,50)
      self.dash_membre.resize(400,300)


      #_________________________________________CHANGER MOT DE PASSE

      self.btn_change_pass=QPushButton('CHANGER MOT DE PASSE',self.dash_membre)
      self.btn_change_pass.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_change_pass.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_change_pass.clicked.connect(self.Change)
      self.btn_change_pass.move(45,100)
      self.btn_change_pass.resize(150,100)



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
      self.dash2_membre.resize(220,300)

      #_______PSEUDO MEMBRE
      self.lab_pseudo=QLabel('PSEUDO',self.dash2_membre)
      self.lab_pseudo.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.lab_pseudo.move(10,30)
      self.lab_pseudo.resize(200,30)

      self.pseudo_membre=QLineEdit(self.dash2_membre)
      self.pseudo_membre.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.pseudo_membre.setAlignment(Qt.AlignCenter)
      self.pseudo_membre.move(10,60)
      self.pseudo_membre.resize(200,30)


      #_______TELEPHONE
      self.lab_tel=QLabel('TELEPHONE',self.dash2_membre)
      self.lab_tel.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.lab_tel.move(10,90)
      self.lab_tel.resize(200,30)

      self.tel=QLineEdit(self.dash2_membre)
      self.tel.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.tel.move(10,120)
      self.tel.resize(200,30)
      self.tel.setEchoMode(QLineEdit.Password)

      #_______DOCUMENT ID
      self.cnib_lab_membre=QLabel('N° CNIB/PASSEPORT',self.dash2_membre)
      self.cnib_lab_membre.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.cnib_lab_membre.move(10,150)
      self.cnib_lab_membre.resize(200,30)

      self.cnib_membre=QLineEdit(self.dash2_membre)
      self.cnib_membre.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.cnib_membre.move(10,180)
      self.cnib_membre.resize(200,30)
      self.cnib_membre.setEchoMode(QLineEdit.Password)

      #_______NOUVEAU MOT DE PASSE
      self.lab_new_pass=QLabel('NOUVEAU MOT DE PASSE',self.dash2_membre)
      self.lab_new_pass.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.lab_new_pass.move(10,210)
      self.lab_new_pass.resize(250,30)

      self.new_pass=QLineEdit(self.dash2_membre)
      self.new_pass.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.new_pass.move(10,240)
      self.new_pass.resize(200,30)
      self.new_pass.setEchoMode(QLineEdit.Password)


      #______________________________________________INTERFACE  membreS END

      #self.dash2_membre.show()
      
      

   def Change(self):
      
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:                                 
               self.cursor=self.bdd.cursor()
               
               self.ssql=self.cursor.execute("SELECT code_user,nom,prenom FROM login WHERE pseudo={0}".format("'"+str(self.pseudo_membre.text())+"'"))
               for i in self.ssql:
                  if len(i)==3:
                     self.membre_code=i[0]
                     self.membre_nom=i[1]
                     self.membre_prenom=i[2]
                     QMessageBox.information(self,str(self.app_name),'COMPTE EXISTANT')
                  
                  else:
                     QMessageBox.information(self,str(self.app_name),'COMPTE NON EXISTANT')
                     
               self.sql2=self.cursor.execute("""SELECT telephone,cnib FROM membres
                                                WHERE code_user=(SELECT code_user FROM login
                                             WHERE pseudo={0})""".format("'"+str(self.pseudo_membre.text())+"'"))
               for c in self.sql2:
                  if str(c[0])==self.tel.text() and str(c[1])==self.cnib_membre.text():
                     QMessageBox.information(self,str(self.app_name),'Numéro telephone et cnib/passeport \n\n Validés')
                     self.modify_pass()
                  else:
                     QMessageBox.information(self,str(self.app_name),'Numéro telephone et cnib/passeport non Validés')

               
               self.bdd.commit()               

               
            else:
               pass
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         QMessageBox.information(self,str(self.app_name),'BASE DE DONNE NON EXISTANTE')

   def modify_pass(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  if self.new_pass.text()!="":
                     self.cursor=self.bdd.cursor()
                     self.cursor.execute(""" UPDATE login SET pass={0} WHERE pseudo={1} AND
                                                code_user=(SELECT code_user FROM membres
                                                WHERE pseudo={2})""".format("'"+str(self.new_pass.text())+"'",
                                                                            "'"+str(self.pseudo_membre.text())+"'",
                                                                            "'"+str(self.pseudo_membre.text())+"'"))

                     self.bdd.commit()               
                     QMessageBox.information(self,str(self.app_name),'MOT DE PASSE MODIFIE AVEC SUCCES')
                  else:
                     QMessageBox.information(self,str(self.app_name),'NOUVEAU MOT DE PASSE OBLIGATOIRE')
                     
                  
               except:
                  QMessageBox.information(self,str(self.app_name),"MOT DE PASSE NON MODIFIE \n UNE ERREUR S'EST PRODUITE")
               
            else:
               pass
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         QMessageBox.information(self,str(self.app_name),'BASE DE DONNE NON EXISTANTE')

     
      
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
   screen=Forget()   
   screen.show()
   sys.exit(app.exec_())
