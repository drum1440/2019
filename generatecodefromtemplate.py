import os

# you can change these values from days to anything else to loop through 
days = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']

# example input file template_with_yyyymmdd.txt:
# select col1, col2 from mytable where datecolumn = 'yyyymmdd';

# set input directory for either Windows or Linux
#os.chdir('C:\\Users\<alias>\Documents')
os.chdir('/Users/<alias>/Documents')

# accumulated info is written to my_concat_output.txt in your Documents folder

fo = open('my_concat_output.txt','w')
try:
  for d in days: 
    fi = open('template_with_yyyymmdd.txt','r')
    for line in fi:
      myline = str(line)
      mytempvar = '201709'+d
      mytemp2 = myline.replace('yyyymmdd',mytempvar)
      fo.write(mytemp2)
except:
  print ('except error')
fi.close()
fo.close()
