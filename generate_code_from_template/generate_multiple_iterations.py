#! python

# this program generates code for multiple iterations, based on a generic input statement
# For example, if input file create_tablennn.txt includes nnn:

# CREATE TABLE <username>.<table_name>nnn (
# .
# .

# this program will generate:

# CREATE TABLE <username>.<table_name>001 (
# .
# .

# CREATE TABLE <username>.<table_name>040 (
# .
# .


import psycopg2
import os
import re
import time
iteration = ['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020','021','022','023','024','025','026','027','028','029','030','031','032','033','034','035','036','037','038','039','040']
os.chdir('C:\\Users\<username>\Documents')
fo = open('my_create_table_<table_name>.txt','w')
try:
   for d in iteration:  
     fi = open('create_table_<table_name>nnn.txt','r')
     for line in fi:
         myline = str(line)
         mytemp2 = myline.replace('nnn',d)
         fo.write(mytemp2)
except:
  print ('except error')
fi.close()
fo.close()

