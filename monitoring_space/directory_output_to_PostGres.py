#! python
#/usr/bin/python
# -------------------------------------------------------------------------------------------------------------------------------------
# 1. create directory output from desired lan drive
# from Windows command prompt:
# P:
# cd \
# dir *.* /s > "C:\Users\<alias>\Documents\directory_info_input.txt"
# -------------------------------------------------------------------------------------------------------------------------------------
# 2. FYI
# this searches regex for valid date in line
# yyyy-mm-dd example from web: prog = re.compile("^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$")
# the date search (below) has been modified to search for mm/dd
# -------------------------------------------------------------------------------------------------------------------------------------
# 3. you need to first create a PostGres table to hold inserted data
#    change each of the following values in < >
# database <mydb>, schema <myschema>, table <mytable>, tablespace <mytablespace>, PostGres local password <mypwd>, your user alias <alias>
# 
# CREATE TABLE <myschema>.<mytable>
# (
#   myvolume character varying (300),
#   myfolder character varying(1000),
#   mydate character varying(15),
#   myfilesize bigint,
#   myfilename character varying(1000)
# )
# WITH (
#   OIDS=FALSE
# )
# TABLESPACE <mytablespace>;
#
# ALTER TABLE <myschema>.<mytable>
#   OWNER TO postgres;
# -------------------------------------------------------------------------------------------------------------------------------------
# 4. Call this program to insert existing dir *.* /s output file data into your PostGres db  
# 
# python directory_output_to_PostGres.py
#
# -------------------------------------------------------------------------------------------------------------------------------------
# 5. run this after data was inserted into <myschema>.<mytable> to find your largest folders
# select a.myfolder, sum(a.myfilesize), 
# (case when sum(a.myfilesize) > (1024*1024) then sum(a.myfilesize)/(1024*1024) else -1 end) Mb
# from <myschema>.<mytable> a
# group by a.myfolder
# having sum(a.myfilesize) > 0
# order by 2 desc;
# 
# -------------------------------------------------------------------------------------------------------------------------------------

import psycopg2
import os
import re
import time
print (time.strftime("%Y-%m-%d %H:%M:%S"))
os.chdir('C:\\Users\<alias>\Documents')
fi = open('directory_info_input.txt','r')
record_count = 0
conn = psycopg2.connect(host='localhost',database='<mydb>',user='postgres',password='<mypwd>')
cur = conn.cursor()
cur.execute("DELETE FROM <myschema>.<mytable>")
cur.execute('COMMIT')
try:
  for line in fi:
     myline = str(line)
     my13char = myline[1:13]
     if my13char == 'Directory of':
       mytemp = myline[14:15]
       myvolume2 = mytemp.strip()
       mytemp = myline[16:590]
       myfoldertemp = mytemp.strip()
       myfolder2 = myfoldertemp.replace("'","''")
     result = re.compile('^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.]')
     result2 = result.search(myline)
     if result2:
       mydate2 = myline[0:10]
       mytime = myline[12:20]
       mytemp = myline[21:38]
       myfilesize2 = mytemp.strip()
       myfilesizecheck = myfilesize2[0:5]
       if myfilesizecheck == '<DIR>':
         myfilesize2 = str(0)
       myfilesizecheck = myfilesize2[0:10]
       if myfilesizecheck == '<JUNCTION>':
         mytemp2 = myline[37:45]
         mytemp3 = mytemp2.strip()
         myfilesize2 = mytemp3.replace("'","''")
         if myfilesize2.isdigit() is True:
           tempnotused = None
         else:
           myfilesize2 = str(-1)
         mytemp = myline[45:590]
         mytemp2 = mytemp.strip()
         myfilename2 = mytemp2.replace("'","''")
         mysql = "insert into <myschema>.<mytable> values ('" + myvolume2 + "','" + myfolder2 + "','" + mydate2 + "','" + myfilesize2 + "','" + myfilename2 + "');"
         cur.execute(mysql)
         record_count = record_count + 1
       else:
         mytemp = myfilesize2.strip()
         myfilesize2 = mytemp.replace(',','')
         if myfilesize2.isdigit() is True:
           tempnotused = None
         else:
           myfilesize = str(-1)
         mytemp = myline[39:549]
         myfilename2 = mytemp.strip()
         mytemp = myfilename2.strip()
         myfilename2 = mytemp.replace("'","''")
         mysql = "insert into <myschema>.<mytable> values ('" + myvolume2 + "','" + myfolder2 + "','" + mydate2 + "','" + myfilesize2 + "','" + myfilename2 + "');"
         cur.execute(mysql)
         record_count = record_count + 1
     else:
       tempnotused = None
except:
  print ('error on record after ', record_count)
cur.execute('COMMIT')
cur.close()
fi.close()
import time
print (time.strftime("%Y-%m-%d %H:%M:%S"))
