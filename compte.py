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

class Compte(QMainWindow):
   def __init__(self):
      super().__init__()
      self.width=1200
      self.height=600
      self.set=0
      self.app_name='GESTION RESTAURANT'
      # this will hide the title bar
      #self.setWindowFlag(Qt.FramelessWindowHint)
      self.offset = None
      self.setGeometry(100,100,self.width,self.height)
      self.setWindowTitle('COMPTES UTILISATEURS')
      self.setStyleSheet(""" background-color:#000;color:#fff """)
      self.setFixedSize(self.width,self.height)
      self.setWindowOpacity(1)
      self.widgets()
      self.load_login()
   def widgets(self):
      #========= TABLE
      self.main_frame=QGroupBox('TABLEAU DES COMPTES UTILISATEURS',self)
      self.main_frame.setGeometry(10,10,955,500)
      self.main_frame.setStyleSheet("background-color:#4200a6;color:#fff;font-family: Time;font-style: italic;font-size: 10pt;font-weight: bold")
      self.tableWidget = QTableWidget(self.main_frame)
      self.tableWidget.setGeometry(10,20,940,475)

      #==== TABLE STYLE
      self.table_header=self.tableWidget.horizontalHeader()
      self.table_header.setSectionResizeMode(QHeaderView.ResizeToContents)
      self.tableWidget.setStyleSheet("""QTableWidget::item{background-color:#000;color:#f52707}
                                        QTableWidget::item::selected{background-color:#fff;color:#000}
                                        QHeaderView::section{background-color:#00a136;color:#000}""")
      
      #_________________________________________
      #_________________________________________
      #_________________________________________DASHBOARD


      self.dash2_paiement=QFrame(self)
      self.dash2_paiement.setStyleSheet("""
                                background-color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                font-weight:bold;
                                border-top-left-radius:10px;border-bottom-left-radius:10px;
                                border-bottom-right-radius:10px;border-top-right-radius:10px
                                """)

      self.dash2_paiement.move(980,50)
      self.dash2_paiement.resize(190,400)

      #_______CALCULATOR
      self.lab_cal=QLabel(self)
      self.lab_cal.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:15pt;
                                  font-weight:bold
                                  """)
      self.lab_cal.move(10,520)
      self.lab_cal.resize(900,20)
      self.lab_cal.setText('QUANTITE TOTALE: 25  --  RECETTE TOTALE: 35000 FCFA')

      #_______NOM
      self.nom_lab_paiement=QLabel('NOM',self.dash2_paiement)
      self.nom_lab_paiement.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.nom_lab_paiement.move(10,0)
      self.nom_lab_paiement.resize(100,20)

      self.nom_paiement=QLineEdit(self.dash2_paiement)
      self.nom_paiement.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.nom_paiement.setAlignment(Qt.AlignCenter)
      self.nom_paiement.setEnabled(False)
      self.nom_paiement.move(10,20)
      self.nom_paiement.resize(150,20)

      #_______QUANTITES
      self.qte_lab_paiement=QLabel('QUANTITE',self.dash2_paiement)
      self.qte_lab_paiement.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.qte_lab_paiement.move(10,40)
      self.qte_lab_paiement.resize(200,20)

      self.qte_paiement=QSpinBox(self.dash2_paiement)
      self.qte_paiement.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.qte_paiement.setAlignment(Qt.AlignCenter)
      self.qte_paiement.setEnabled(False)
      self.qte_paiement.setMinimum(0)
      self.qte_paiement.setMaximum(1000000)
      self.qte_paiement.move(10,60)
      self.qte_paiement.resize(150,20)

      #_______PRIX
      self.prix_lab_paiement=QLabel('PRIX ',self.dash2_paiement)
      self.prix_lab_paiement.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.prix_lab_paiement.move(10,80)
      self.prix_lab_paiement.resize(100,20)

      self.prix_paiement=QDoubleSpinBox(self.dash2_paiement)
      self.prix_paiement.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      #self.prix_paiement.setAlignment(Qt.AlignCenter)
      self.prix_paiement.setEnabled(False)
      self.prix_paiement.setMinimum(0)
      self.prix_paiement.setMaximum(1000000)
      self.prix_paiement.move(10,100)
      self.prix_paiement.resize(150,20)

      #_______TYPE
      self.cat_lab_paiement=QLabel('TYPE',self.dash2_paiement)
      self.cat_lab_paiement.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.cat_lab_paiement.move(10,120)
      self.cat_lab_paiement.resize(100,20)

      self.cat_paiement=QLineEdit(self.dash2_paiement)
      self.cat_paiement.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.cat_paiement.setAlignment(Qt.AlignCenter)
      self.cat_paiement.setEnabled(False)
      self.cat_paiement.move(10,140)
      self.cat_paiement.resize(150,20)
      #_______ID PAIEMENT
      self.id_lab_paiement=QLabel('ID PAIEMENT',self.dash2_paiement)
      self.id_lab_paiement.setStyleSheet("""
                                  background-color:#000;color:#fff;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold
                                  """)
      self.id_lab_paiement.move(10,160)
      self.id_lab_paiement.resize(100,20)

      self.id_paiement=QSpinBox(self.dash2_paiement)
      self.id_paiement.setStyleSheet("""
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:10pt;
                                  font-weight:bold;border-radius:5px
                                  """)
      self.id_paiement.setAlignment(Qt.AlignCenter)
      self.id_paiement.setValue(1)
      self.id_paiement.setEnabled(False)
      self.id_paiement.move(10,180)
      self.id_paiement.resize(150,20)

      """
      #_________________________________________REMOVE PRODUCT

      self.btn_remove=QPushButton('RETIRER',self.dash2_paiement)
      self.btn_remove.setStyleSheet(\"""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  \""")
      self.btn_remove.setCursor(QCursor(Qt.PointingHandCursor))
      #self.btn_remove.clicked.connect(self.remove_paiement)
      self.btn_remove.move(10,240)
      self.btn_remove.resize(150,20)
      """

      #_________________________________________COMPTES ROW
      self.btn_login=QPushButton('COMPTES',self.dash2_paiement)
      self.btn_login.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_login.clicked.connect(self.load_login)
      self.btn_login.move(10,260)
      self.btn_login.resize(150,20)
      #_________________________________________MEMBRES ROW
      self.btn_membre=QPushButton('MEMBRES',self.dash2_paiement)
      self.btn_membre.setStyleSheet("""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  """)
      self.btn_membre.setCursor(QCursor(Qt.PointingHandCursor))
      self.btn_membre.clicked.connect(self.load_membre)
      self.btn_membre.move(10,280)
      self.btn_membre.resize(150,20)

      """
      #_________________________________________DESSERTS ROW
      self.btn_dessert=QPushButton('DESSERTS',self.dash2_paiement)
      self.btn_dessert.setStyleSheet(\"""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  \""")
      self.btn_dessert.setCursor(QCursor(Qt.PointingHandCursor))
      #self.btn_dessert.clicked.connect(self.load_dessert)
      self.btn_dessert.move(10,300)
      self.btn_dessert.resize(150,20)
      #_________________________________________CAFES ROW
      self.btn_cafe=QPushButton('CAFES',self.dash2_paiement)
      self.btn_cafe.setStyleSheet(\"""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  \""")
      self.btn_cafe.setCursor(QCursor(Qt.PointingHandCursor))
      #self.btn_cafe.clicked.connect(self.load_cafe)
      self.btn_cafe.move(10,320)
      self.btn_cafe.resize(150,20)
      #_________________________________________PLATS ROW
      self.btn_plat=QPushButton('PLATS',self.dash2_paiement)
      self.btn_plat.setStyleSheet(\"""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  \""")
      self.btn_plat.setCursor(QCursor(Qt.PointingHandCursor))
      #self.btn_plat.clicked.connect(self.load_plat)
      self.btn_plat.move(10,340)
      self.btn_plat.resize(150,20)
      #_________________________________________EXPORTER
      self.btn_export=QPushButton('EXPORTER',self.dash2_paiement)
      self.btn_export.setStyleSheet(\"""
                                  QPushButton::pressed{background-color :#000;color:#fff;border-style:solid;
                                  border-width:2px;border-color:#f00;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  QPushButton::!pressed{border-style:solid;border-width:1px;border-color:#000;
                                  background-color:#fff;color:#000;font-family: Time;font-style:italic;font-size:8pt;
                                  font-weight:bold;border-radius:5px}
                                  \""")
      self.btn_export.setCursor(QCursor(Qt.PointingHandCursor))
      #self.btn_export.clicked.connect(self.load_all)
      self.btn_export.move(10,360)
      self.btn_export.resize(150,20)
      """
      
   def load_login(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  #self.question=QMessageBox.question(self,str(self.app_name),'CHARGER LES DONNEES ?',QMessageBox.Yes,QMessageBox.No)
                  #if self.question==QMessageBox.Yes:
                  self.cursor=self.bdd.cursor()

                  #==== HEADER LABELS
                  self.headers=['ID','NOM','PRENOM','PSEUDO','MOT DE PASSE','CODE USER','DATETIME']
                  
                  #==== COLUMN COUNT
                  self.tableWidget.setColumnCount(len(self.headers))
                  #==== ROW COUNT
                  self.tableWidget.setRowCount(0)

                  self.tableWidget.setHorizontalHeaderLabels(['ID','NOM','PRENOM','PSEUDO','MOT DE PASSE','CODE USER','DATETIME'])

                  self.line_count=self.cursor.execute(""" SELECT COUNT(*) FROM login """)                  

                  for i in self.line_count:
                     self.lab_cal.setText("""COMPTE TOTALE: {0} """.format(str(i[0])))
                  
                  
                  #==== TABLE paiements SELECTION
                  self.result=self.cursor.execute(""" SELECT  id,nom,prenom,pseudo,pass,code_user,datetime  FROM login """)
                  
                  for row_number,row_data in enumerate(self.result):                    
                     self.tableWidget.insertRow(row_number)
                     for column_number,data in enumerate(row_data):  
                        self.tableWidget.setItem(row_number,column_number, QTableWidgetItem(str(data)))
                        #self.tableWidget.setColumnWidth(column_number, 150)

                  self.bdd.commit()
                  self.bdd.close()
                  
                  
               except:
                  QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")

   def load_membre(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  #self.question=QMessageBox.question(self,str(self.app_name),'CHARGER LES DONNEES ?',QMessageBox.Yes,QMessageBox.No)
                  #if self.question==QMessageBox.Yes:
                  self.cursor=self.bdd.cursor()

                  #==== HEADER LABELS
                  self.headers=['ID','NOM','PRENOM','PSEUDO','CNIB','TELEPHONE','ADRESSE','RÔLE','CODE USER','DATETIME','PHOTO']
                  
                  #==== COLUMN COUNT
                  self.tableWidget.setColumnCount(len(self.headers))
                  #==== ROW COUNT
                  self.tableWidget.setRowCount(0)

                  self.tableWidget.setHorizontalHeaderLabels(['ID','NOM','PRENOM','PSEUDO','CNIB','TELEPHONE','ADRESSE',
                                                              'RÔLE','CODE USER','DATETIME','PHOTO'])

                  self.line_count=self.cursor.execute(""" SELECT COUNT(*) FROM membres """)                  

                  for i in self.line_count:
                     self.lab_cal.setText("""COMPTE TOTALE: {0} """.format(str(i[0])))
                  
                  
                  #==== TABLE paiements SELECTION
                  self.result=self.cursor.execute(""" SELECT  id,nom,prenom,pseudo,cnib,telephone,adresse,
                                                              rôle,code_user,datetime,photo  FROM membres """)
                  
                  for row_number,row_data in enumerate(self.result):                    
                     self.tableWidget.insertRow(row_number)
                     for column_number,data in enumerate(row_data):  
                        self.tableWidget.setItem(row_number,column_number, QTableWidgetItem(str(data)))
                        #self.tableWidget.setColumnWidth(column_number, 150)

                  self.bdd.commit()
                  self.bdd.close()
                  
                  
               except:
                  QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")
                  

   def load_boisson(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  #self.question=QMessageBox.question(self,str(self.app_name),'CHARGER LES DONNEES ?',QMessageBox.Yes,QMessageBox.No)
                  #if self.question==QMessageBox.Yes:
                  self.cursor=self.bdd.cursor()

                  #==== HEADER LABELS
                  self.headers=['ID_PAIEMENT','NOM','QUANTITE','PRIX','REDUCTION','DATETIME','CATEGORIE',
                                'NOM_CLIENT','CNIB_CLIENT','ADRESSE_CLIENT','ID_PRODUIT',
                                'CODE_PRODUIT','PHOTO']
                  
                  #==== COLUMN COUNT
                  self.tableWidget.setColumnCount(len(self.headers))
                  #==== ROW COUNT
                  self.tableWidget.setRowCount(0)

                  self.tableWidget.setHorizontalHeaderLabels(['ID_PAIEMENT','NOM','QUANTITE','PRIX','REDUCTION','DATETIME','CATEGORIE',
                                                              'NOM_CLIENT','CNIB_CLIENT','ADRESSE_CLIENT','ID_PRODUIT',
                                                              'CODE_PRODUIT','PHOTO'])

                  self.line_count=self.cursor.execute(""" SELECT SUM(paiements.quantite),
                                                          SUM(paiements.quantite*paiements.prix),
                                                          SUM((paiements.quantite*paiements.prix)-((paiements.quantite*paiements.prix)*paiements.reduction/100))
                                                          FROM paiements WHERE type='BOISSON' """)                  

                  for i in self.line_count:
                     self.lab_cal.setText("""QUANTITE TOTALE: {0}  --  COÛT TOTAL: {1} FCFA  --  VENDU: {2} FCFA""".format(str(i[0]),str(i[1]),str(i[2])))
                  
                  
                  #==== TABLE paiements SELECTION
                  self.result=self.cursor.execute(""" SELECT  id,nom,quantite,prix,reduction,datetime,categorie,
                                                                nom_client,cnib_client,adresse_client,
                                                                       id_produit,code_produit,
                                                                       photo  FROM paiements
                                                                       WHERE type='BOISSON' """)
                  
                  for row_number,row_data in enumerate(self.result):                    
                     self.tableWidget.insertRow(row_number)
                     for column_number,data in enumerate(row_data):  
                        self.tableWidget.setItem(row_number,column_number, QTableWidgetItem(str(data)))
                        #self.tableWidget.setColumnWidth(column_number, 150)

                  self.bdd.commit()
                  self.bdd.close()
                  
                  
               except:
                  QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")

   def load_dessert(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  #self.question=QMessageBox.question(self,str(self.app_name),'CHARGER LES DONNEES ?',QMessageBox.Yes,QMessageBox.No)
                  #if self.question==QMessageBox.Yes:
                  self.cursor=self.bdd.cursor()

                  #==== HEADER LABELS
                  self.headers=['ID_PAIEMENT','NOM','QUANTITE','PRIX','REDUCTION','DATETIME','CATEGORIE',
                                'NOM_CLIENT','CNIB_CLIENT','ADRESSE_CLIENT','ID_PRODUIT',
                                'CODE_PRODUIT','PHOTO']
                  
                  #==== COLUMN COUNT
                  self.tableWidget.setColumnCount(len(self.headers))
                  #==== ROW COUNT
                  self.tableWidget.setRowCount(0)

                  self.tableWidget.setHorizontalHeaderLabels(['ID_PAIEMENT','NOM','QUANTITE','PRIX','REDUCTION','DATETIME','CATEGORIE',
                                                              'NOM_CLIENT','CNIB_CLIENT','ADRESSE_CLIENT','ID_PRODUIT',
                                                              'CODE_PRODUIT','PHOTO'])

                  self.line_count=self.cursor.execute(""" SELECT SUM(paiements.quantite),
                                                          SUM(paiements.quantite*paiements.prix),
                                                          SUM((paiements.quantite*paiements.prix)-((paiements.quantite*paiements.prix)*paiements.reduction/100))
                                                          FROM paiements WHERE type='DESSERT' """)                  

                  for i in self.line_count:
                     self.lab_cal.setText("""QUANTITE TOTALE: {0}  --  COÛT TOTAL: {1} FCFA  --  VENDU: {2} FCFA""".format(str(i[0]),str(i[1]),str(i[2])))
                  
                  
                  #==== TABLE paiements SELECTION
                  self.result=self.cursor.execute(""" SELECT  id,nom,quantite,prix,reduction,datetime,categorie,
                                                                nom_client,cnib_client,adresse_client,
                                                                       id_produit,code_produit,
                                                                       photo  FROM paiements
                                                                       WHERE type='DESSERT' """)
                  
                  for row_number,row_data in enumerate(self.result):                    
                     self.tableWidget.insertRow(row_number)
                     for column_number,data in enumerate(row_data):  
                        self.tableWidget.setItem(row_number,column_number, QTableWidgetItem(str(data)))
                        #self.tableWidget.setColumnWidth(column_number, 150)

                  self.bdd.commit()
                  self.bdd.close()
                  
                  
               except:
                  QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")

   def load_cafe(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  #self.question=QMessageBox.question(self,str(self.app_name),'CHARGER LES DONNEES ?',QMessageBox.Yes,QMessageBox.No)
                  #if self.question==QMessageBox.Yes:
                  self.cursor=self.bdd.cursor()

                  #==== HEADER LABELS
                  self.headers=['ID_PAIEMENT','NOM','QUANTITE','PRIX','REDUCTION','DATETIME','CATEGORIE',
                                'NOM_CLIENT','CNIB_CLIENT','ADRESSE_CLIENT','ID_PRODUIT',
                                'CODE_PRODUIT','PHOTO']
                  
                  #==== COLUMN COUNT
                  self.tableWidget.setColumnCount(len(self.headers))
                  #==== ROW COUNT
                  self.tableWidget.setRowCount(0)

                  self.tableWidget.setHorizontalHeaderLabels(['ID_PAIEMENT','NOM','QUANTITE','PRIX','REDUCTION','DATETIME','CATEGORIE',
                                                              'NOM_CLIENT','CNIB_CLIENT','ADRESSE_CLIENT','ID_PRODUIT',
                                                              'CODE_PRODUIT','PHOTO'])

                  self.line_count=self.cursor.execute(""" SELECT SUM(paiements.quantite),
                                                          SUM(paiements.quantite*paiements.prix),
                                                          SUM((paiements.quantite*paiements.prix)-((paiements.quantite*paiements.prix)*paiements.reduction/100))
                                                          FROM paiements WHERE type='CAFE' """)                  

                  for i in self.line_count:
                     self.lab_cal.setText("""QUANTITE TOTALE: {0}  --  COÛT TOTAL: {1} FCFA  --  VENDU: {2} FCFA""".format(str(i[0]),str(i[1]),str(i[2])))
                  
                  
                  #==== TABLE paiements SELECTION
                  self.result=self.cursor.execute(""" SELECT  id,nom,quantite,prix,reduction,datetime,categorie,
                                                                nom_client,cnib_client,adresse_client,
                                                                       id_produit,code_produit,
                                                                       photo  FROM paiements
                                                                       WHERE type='CAFE' """)
                  
                  for row_number,row_data in enumerate(self.result):                    
                     self.tableWidget.insertRow(row_number)
                     for column_number,data in enumerate(row_data):  
                        self.tableWidget.setItem(row_number,column_number, QTableWidgetItem(str(data)))
                        #self.tableWidget.setColumnWidth(column_number, 150)

                  self.bdd.commit()
                  self.bdd.close()
                  
                  
               except:
                  QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")
   def load_plat(self):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
               try:
                  #self.question=QMessageBox.question(self,str(self.app_name),'CHARGER LES DONNEES ?',QMessageBox.Yes,QMessageBox.No)
                  #if self.question==QMessageBox.Yes:
                  self.cursor=self.bdd.cursor()

                  #==== HEADER LABELS
                  self.headers=['ID_PAIEMENT','NOM','QUANTITE','PRIX','REDUCTION','DATETIME','CATEGORIE',
                                'NOM_CLIENT','CNIB_CLIENT','ADRESSE_CLIENT','ID_PRODUIT',
                                'CODE_PRODUIT','PHOTO']
                  
                  #==== COLUMN COUNT
                  self.tableWidget.setColumnCount(len(self.headers))
                  #==== ROW COUNT
                  self.tableWidget.setRowCount(0)

                  self.tableWidget.setHorizontalHeaderLabels(['ID_PAIEMENT','NOM','QUANTITE','PRIX','REDUCTION','DATETIME','CATEGORIE',
                                                              'NOM_CLIENT','CNIB_CLIENT','ADRESSE_CLIENT','ID_PRODUIT',
                                                              'CODE_PRODUIT','PHOTO'])

                  self.line_count=self.cursor.execute(""" SELECT SUM(paiements.quantite),
                                                          SUM(paiements.quantite*paiements.prix),
                                                          SUM((paiements.quantite*paiements.prix)-((paiements.quantite*paiements.prix)*paiements.reduction/100))
                                                          FROM paiements WHERE type='PLAT' """)                  

                  for i in self.line_count:
                     self.lab_cal.setText("""QUANTITE TOTALE: {0}  --  COÛT TOTAL: {1} FCFA  --  VENDU: {2} FCFA""".format(str(i[0]),str(i[1]),str(i[2])))
                  
                  
                  #==== TABLE paiements SELECTION
                  self.result=self.cursor.execute(""" SELECT  id,nom,quantite,prix,reduction,datetime,categorie,
                                                                nom_client,cnib_client,adresse_client,
                                                                       id_produit,code_produit,
                                                                       photo  FROM paiements
                                                                       WHERE type='PLAT' """)
                  
                  
                  for row_number,row_data in enumerate(self.result):                    
                     self.tableWidget.insertRow(row_number)
                     for column_number,data in enumerate(row_data):  
                        self.tableWidget.setItem(row_number,column_number, QTableWidgetItem(str(data)))
                        #self.tableWidget.setColumnWidth(column_number, 150)

                  self.bdd.commit()
                  self.bdd.close()
                  
                  
               except:
                  QMessageBox.information(self,str(self.app_name),"UNE ERREUR S'EST PRODUITE")

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
   #_________________________________________DRAG MAIN WINDOW EVENTS END

if __name__=='__main__':
   app=QApplication(sys.argv)
   app.setStyle('Vista')
   screen=Compte()   
   screen.show()
   sys.exit(app.exec_())
