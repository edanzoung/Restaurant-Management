import happiness
import love
import joy
import health
import wealth
import prosperity
from datetime import datetime

class Edan_zoung_wish(object):
   
   def __init__(self):
      self.life=[]
      self.time=None
      self.wish()

   def wish(self):
      self.time = "{0}/{1}/{2}".format(str(datetime.utcnow().day),
                                     str(datetime.utcnow().month),
                                     str(datetime.utcnow().year))
      
      self.begin_time = "01/01/2020"

      while self.time <= "31/12/2020":
         self.life.append(health)
         self.life.append(happiness)
         self.life.append(love)
         self.life.append(joy)
         self.life.append(wealth)            

         self.time++
         
      if bad_memories:
         self.life.remove(bad_memories)
      
      print("WISH YOU A VERY HAPPY AND PROSPEROUS NEW YEAR")
               


      
