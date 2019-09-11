import os
from datetime import datetime
yyyymm = datetime.now().strftime('%Y%m')

num_of_days = 30
extrazero="0"

# example input file template_with_yyyymmdd.txt:
# select col1, col2 from mytable where datecolumn = 'yyyymmdd';

# set input directory for either Windows or Linux
os.chdir('C:\\Users\\<alias>\\Documents')
#os.chdir('/Users/<alias>/Documents')

# accumulated info is written to my_concat_output.txt in your Documents folder

try:
   with open('my_concat_output.txt','w') as fo:
        for day in range(num_of_days):
            day += 1
            if (day > 9):
                extrazero=""
            with open('template_with_yyyymmdd.txt','r') as fi:
                for line in fi:
                    myline = str(line)
                    mytempvar = str(yyyymm) + extrazero + str(day)
                    mytemp2 = myline.replace('yyyymmdd',mytempvar)
                    mytemp3 = mytemp2.strip() + "\n"
                    fo.write(mytemp3)
except:
    print ('except error')
