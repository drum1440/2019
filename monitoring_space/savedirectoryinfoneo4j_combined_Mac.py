#! python
#/usr/bin/python
######################################################
from PIL import Image, ImageFile
######################################################
import time
ymdhms = time.strftime("%Y%m%d_%H%M%S")
import os, sys
import binascii
# https://github.com/python-pillow/Pillow/issues/1510
# from PIL import Image, ImageFile
# ImageFile.LOAD_TRUNCATED_IMAGES = True
# orginal_image = Image.open('test.jpg')
# bmpinfo = orginal_image.size
# test = orginal_image.crop((0,0,0,0))
#
# added 20190926-184119
ImageFile.LOAD_TRUNCATED_IMAGES = True
#
try:
    MAX_SIZE = (50, 50)

    which_set = sys.argv[1]
    good_set_found = "n"
    if which_set == '1':
        os.chdir('/Users/brad/Pictures')
        fi = open('mypicturesiMaclocal.txt','r')
        fo2 = open('pictures_iMaclocal.csv','w')
        fo3 = open('pictures_iMaclocal_myfilename_check_for_errors_' + ymdhms + '.txt','w')
        good_set_found = "y"
        drive_id = 1
    if which_set == '2':
        os.chdir('/Volumes/SEAEXFAT1T/Brad Samsung S4 phone Android File Transfer')
        fi = open('mypicturesMac1BradSamsungS4.txt','r')
        fo2 = open('picturesMac1_1T_BradSamsungS4.csv','w')
        fo3 = open('picturesMac1_1T_BradSamsungS4_myfilename_check_for_errors_' + ymdhms + '.txt','w')
        good_set_found = "y"
        drive_id = 2
    if which_set == '3':
        os.chdir('/Volumes/SEAEXFAT1T/BradBackupPhotos_before_2015_combined')
        fi = open('mypicturesMac1Bradphotosbefore2015.txt','r')
        fo2 = open('picturesMac1_1T_Bradphotosbefore2015.csv','w')
        fo3 = open('picturesMac1_1T_Bradphotosbefore2015_myfilename_check_for_errors_' + ymdhms + '.txt','w')
        good_set_found = "y"
        drive_id = 3
    if which_set == '4':
        os.chdir('/Volumes/SEAEXFAT2T')
        fi = open('mypicturesMac12T.txt','r')
        fo2 = open('picturesMac1_2T_Mac12T.csv','w')
        fo3 = open('picturesMac1_2T_myfilename_check_for_errors_' + ymdhms + '.txt','w')
        good_set_found = "y"
        drive_id = 4
    if which_set == '5':
        os.chdir('/Users/brad/Documents')
        fi = open('mydocumentsiMaclocal.txt','r')
        fo2 = open('documents_iMaclocal.csv','w')
        fo3 = open('documents_iMaclocal_myfilename_check_for_errors_' + ymdhms + '.txt','w')
        good_set_found = "y"
        drive_id = 5
    if which_set == '6':
        os.chdir('/Volumes/WDMyBook4Tb')
        fi = open('mypictures_Mac2WDMyBook4Tb.txt','r')
        fo2 = open('picturesMac2_Mac2WDMyBook4Tb.csv','w')
        fo3 = open('picturesMac2_Mac2WDMyBook4Tb_myfilename_check_for_errors_' + ymdhms + '.txt','w')
        good_set_found = "y"
        drive_id = 6
    if which_set == '7':
        os.chdir('/Volumes/WDMyBook4Tb/fromseaexfat1t_Mac1')
        fi = open('mypictures_Mac2WDMyBook4Tb_fromseaexfat1t_Mac1.txt','r')
        fo2 = open('picturesMac2_Mac2WDMyBook4Tb_fromseaexfat1t_Mac1.csv','w')
        fo3 = open('picturesMac2_Mac2WDMyBook4Tb_fromseaexfat1t_Mac1_myfilename_check_for_errors_' + ymdhms + '.txt','w')
        good_set_found = "y"
        drive_id = 7
    if which_set == '8':
        os.chdir('/Volumes/WDMyBook4Tb/fromWindows10laptop')
        fi = open('mypictures_Mac2WDMyBook4Tb_fromWindows10laptop.txt','r')
        fo2 = open('picturesMac2_Mac2WDMyBook4Tb_fromWindows10laptop.csv','w')
        fo3 = open('picturesMac2_Mac2WDMyBook4Tb_fromWindows10laptop_myfilename_check_for_errors_' + ymdhms + '.txt','w')
        good_set_found = "y"
        drive_id = 8

    if good_set_found == "n":
        os.chdir('/Users/brad/Pictures')
        fi = open('mypicturesiMaclocal.txt','r')
        fo2 = open('pictures_iMaclocal.csv','w')
        fo3 = open('pictures_iMaclocal_myfilename_check_for_errors_' + ymdhms + '.txt','w')

    print ('good_set_found value =',good_set_found)

    goodrecordcounter = 0
    for line in fi:
        myline = str(line)
        myfilenamestartsave = 0
        myfilenamestartsearch = 0
        keeplookingforfilename = "n"
        myignore = "n"
    #   ignore ./$RECYCLE.BIN/ and ./.Trashes
        myignoresearch = myline.find('./$RECYCLE.BIN',1)
        if (myignoresearch > 0):
            myignore = "y"
        myignoresearch = myline.find('./.Trashes',1)
        if (myignoresearch > 0):
            myignore = "y"
        myignoresearch = myline.find(',',1)
        if (myignoresearch > 0):
            myignore = "y"
        myignoresearch = myline.find('/Photos Library',1)
        if (myignoresearch > 0):
            myignore = "y"
        myignoresearch = myline.find('/iPhoto Library',1)
        if (myignoresearch > 0):
            myignore = "y"
        if (myignore == "n"):
        #  foldername is just after ./
            myfoldernamestartloc = myline.find('./')
            if (myfoldernamestartloc > 0):
                keeplookingforfilename = "y"
        #       start looking for filename after first foldername is found
                myfilenamestartsearch = myfoldernamestartloc+1
                myfilenamestartsave = myfoldernamestartloc
                while keeplookingforfilename == "y":
                    # the largest myfilenamestartloc value minus two marks the end of
                    # foldername and myfilenamestartloc value plus one marks the start of filename
                    myfilenamestartloc = myline.find('/',myfilenamestartsearch)
                    if (myfilenamestartloc > myfilenamestartsave):
                        myfilenamestartsave = myfilenamestartloc
                        myfilenamestartsearch = myfilenamestartloc+1
                    else:
                        keeplookingforfilename = "n"
                        # if we found the start of filename, now look for the end (.jpg)
                    if (keeplookingforfilename == "n"):
                        myfindjpglowercase = myline.find('.jpg',myfilenamestartsave)
                        if (myfindjpglowercase > 0):
                            myfindjpgsave = myfindjpglowercase
                        else:
                            myfindjpguppercase = myline.find('.JPG',myfilenamestartsave)
                            if (myfindjpguppercase > 0):
                                myfindjpgsave = myfindjpguppercase
                            else:
                                myfindjpgsave = 0
                        if (myfindjpgsave > 0):
                            myfindfilenameend = myfindjpgsave + 4
                            myline2 = myline.replace('  ',' ')
                            mylookforfilesize = myline2.split(' ')
                            myfilesize = mylookforfilesize[5]
    #                       check for numeric
                            if myfilesize.isdigit():
                                myfilesize = str(myfilesize)
                            else:
                                myfilesize = str(myfilesize) + "<-ERROR"
                            myfoldername = myline[myfoldernamestartloc+2:myfilenamestartsave]
                            myfilenametemp = myline[myfilenamestartsave+1:myfindfilenameend]
                            myfilename = myfilenametemp.rstrip(' ')
                            myfilenametemp3 = myline.find('._',myfilenamestartsave)
                            # do not add + '\n' to the end of the following myfilename= line
                            if (myfilenametemp3 > 0):
                                myfilename = myline[myfilenametemp3+2:myfindfilenameend]
                            myfilenametemp4 = myfilename + '\n'
                            fo3.write(myfilenametemp4)
                            goodrecordcounter = goodrecordcounter + 1
                            # create thumbnail of Image
                            # then get hexadecimal value of thumbnail, save as text
                            # this is a unique (smaller) representation of the picture
                            try:
                                image = Image.open(os.path.join(myfoldername, myfilename))
                                image.thumbnail(MAX_SIZE)
                                tempvar = '/Users/brad/Documents/'
                                image.save(tempvar + 'tempthumbnail_' + ymdhms + '.jpg')
                                filenametemp = tempvar + "tempthumbnail_" + ymdhms + ".jpg"
                                with open(filenametemp, 'rb') as f:
                                    content = f.read()
                                    hexoutput = binascii.hexlify(content)
                                    picture_id_str = str(hexoutput)
                                myoutputpictures = str(drive_id) + "," + str(myfoldername) + "," + picture_id_str + "," + myfilename + "," + str(myfilesize) + '\n'
                                fo2.write(myoutputpictures)
                            except OSError as err:
                                with open('OSError_file__local_' + ymdhms + '.txt', 'a') as appendfileout:
                                    appendfileout.write(myfoldername + ' ' + myfilename + '\n')
                                    appendfileout.write(format(err) + '\n')
#
    fi.close()
    fo2.close()
    fo3.close()
    print ('good record counter=',goodrecordcounter)
except ValueError:
    print('Non-numeric data found in the file.')
except ImportError:
    print ('NO module found')
