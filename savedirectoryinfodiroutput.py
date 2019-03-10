#! python
#/usr/bin/python
# -------------------------------------------------------------------------------------------------------------------------------------


# change <alias> to your Windows alias



# 1. create directory output from desired lan drive
# from Windows command prompt:
# cd \
# dir *.* /s > "C:\Users\<alias>\Documents\directory_info_accum_ddl.txt"
# -------------------------------------------------------------------------------------------------------------------------------------
# 2. FYI
# the re.compile date search (below) searches for mm/dd
# -------------------------------------------------------------------------------------------------------------------------------------
# 3. You need to create a table to hold inserted data
# Postgres used in this example:
# database braddb_2, schema brad2, table mydirectoryinfo_P_accum_ddl
# 
# CREATE TABLE brad2.mydirectoryinfo_P_accum_ddl
# (
#   myvolume character varying (300),
#   myfolder character varying(1000),
#   mydate character varying(15),
#   myfilesize bigint,
#   myfilename character varying(1000),
#   insert_yyyymmdd character varying(8),
#   insert_hhmmss   character varying(6)
# )
# WITH (
#   OIDS=FALSE
# )
# TABLESPACE BRADTS3;
#
# ALTER TABLE brad2.mydirectoryinfo_P_accum_ddl
#   OWNER TO postgres;
# -------------------------------------------------------------------------------------------------------------------------------------
# 4. Run this program to generate insert statements with size info from your dir output;  
#
# py savedirectoryinfodiroutput.py
#
# -------------------------------------------------------------------------------------------------------------------------------------
# 5. run this after data was inserted into brad2.mydirectoryinfo_P_accum_ddl to review your folder/file sizes
# select a.myfolder, sum(a.myfilesize), 
# (case when sum(a.myfilesize) > (1024*1024) then sum(a.myfilesize)/(1024*1024) else -1 end) Mb
# from brad2.mydirectoryinfo_P_accum_ddl a
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
myyyyymmdd = time.strftime("%Y%m%d")
myhhmmss = time.strftime("%H%M%S")
os.chdir('C:\\Users\<alias>\Documents')
fi = open('directory_info_accum_ddl.txt','r')
fo = open('directory_info_accum_ddl.sql','w')
record_count = 0
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
         myoutput = "insert into brad2.mydirectoryinfo_P_accum_ddl values ('" + myvolume2 + "','" + myfolder2 + "','" + mydate2 + "','" + myfilesize2 + "','" + myfilename2 + "','" + myyyyymmdd + "','" + myhhmmss + "');" + "\n"
         fo.write(myoutput)
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
         myoutput = "insert into brad2.mydirectoryinfo_P_accum_ddl values ('" + myvolume2 + "','" + myfolder2 + "','" + mydate2 + "','" + myfilesize2 + "','" + myfilename2 + "','" + myyyyymmdd + "','" + myhhmmss  + "');" + "\n"
         fo.write(myoutput)
         record_count = record_count + 1
     else:
       tempnotused = None
except:
  print ('error on record after ', record_count)
myoutput = "commit;" + "\n"
fo.write(myoutput)
fi.close()
fo.close()
