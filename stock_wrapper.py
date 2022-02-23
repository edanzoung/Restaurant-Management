#####################################
# IZI TOC V1.0 by Edan_Zoung
#####################################

import os
import sys
import sqlite3
import uuid


from config_app import name_app

import time
import datetime


class Stock:
   def __init__(self):
      self.app_name=name_app

      
   def get_all_data(self,table):
      # Category: boissons , desserts , cafes , plats
      self.data=dict()
      self.number=0
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error:
            print("Connection Error")
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.sql1=self.cursor.execute("""SELECT COUNT(*) FROM """+str(table) )             
               for row in self.sql1:
                  self.number=int(row[0])
                  if int(row[0]) <= 0:
                     print("Data not found")
                  else: 
                     self.cursor.execute("""SELECT nom,quantite,prix,photo,categorie,code_produit,reduction FROM """+str(table) )
                     self.sql2=self.cursor.fetchall()                     
                     self.data=self.sql2
                     for num in range(self.number):
                        for i in self.sql2:
                           self.data[num]={'produit':i[num],
                                           'quantite':i[num],
                                           'prix':i[num],
                                           'image':i[num],
                                           'categorie':i[num],
                                           'code':i[num],
                                           'reduction ':i[num]}

                        
      return self.data

   def get_single_data(self,table_name,line):
      # Category: boissons , desserts , cafes , plats
      self.data=dict()
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error:
            print("Connection Error")
         finally:
            if self.bdd:
               self.cursor=self.bdd.cursor()
               self.sql1=self.cursor.execute("""SELECT COUNT(*) FROM """+str(table_name) )             
               for row in self.sql1:
                  if int(row[0]) <= 0 or int(row[0]) <= int(line):
                     print("Data not found")
                  else: 
                     self.sql2=self.cursor.execute("""SELECT nom,quantite,prix,photo,categorie,code_produit,reduction
                                                     FROM """+str(table_name)+""" WHERE id = """+str(line) )             
                     for row in self.sql2:
                        self.data['produit']=row[0]
                        self.data['quantite']=row[1]
                        self.data['prix']=row[2]
                        self.data['image']=row[3]
                        self.data['categorie']=row[4]
                        self.data['code']=row[5]
                        self.data['reduction']=row[6]
      return self.data

   
   def add_data(self,table,line):
      if os.path.exists('restaurant.bd') and os.path.isfile('restaurant.bd'):
         try:
            self.bdd=sqlite3.connect('restaurant.bd')
         except sqlite3.Error as e:
            QMessageBox.information(self,str(self.app_name),e)
         finally:
            if self.bdd:
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

                  self.cursor.execute("""INSERT INTO """+str(table)+ """(nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                           is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                                    (input("Nom produit: "),
                                     input("Quantite produit: "),
                                     input("Nom produit: "),
                                     input("Photo produit: "),
                                     input("Category produit: "),
                                     self.ui,
                                     self.set_date,
                                     input("Reduction produit: "),
                                     "0","0","0","0","0"))

                  #==== MISE A JOUR ID PRODUIT
                  self.s_ss=self.cursor.execute("""SELECT row_number() OVER (ORDER BY id)
                                                   rownum,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                                   is_added,is_ordered,is_processed,is_shipped,is_paid FROM boissons""")
                  for i in self.s_ss:
                     self.index1.append(i)

                  self.cursor.execute("DELETE FROM "+str(table))
                  
                  self.cursor.executemany("""INSERT INTO """+str(table)+ """
                                            (id,nom,quantite,prix,photo,categorie,code_produit,datetime,reduction,
                                            is_added,is_ordered,is_processed,is_shipped,is_paid) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",self.index1)
               
                  self.bdd.commit()
                  self.refresh_data()
                  print(str(table)+" AJOUTE AVEC SUCCES")
                  
               except:
                  self.bdd.rollback()
                  print(str(table)+" NON AJOUTE\nUNE ERREUR S'EST PRODUITE")
                               
            else:
               pass
      elif not os.path.exists('restaurant.bd') and not os.path.isfile('restaurant.bd'):
         pass
