#!/usr/bin/env python3
#
# keeps reviewing your clipboard every 2 seconds
# if it has changed append new clipboard data to file appendfileYYYYMMDDHHMMSS.txt
# if your clipboard has 'stop' then program execution will stop
#
# To install pyperclip via pip first:
# pip install pyperclip
#
import time
from datetime import datetime
import pyperclip
ymdhms = datetime.today().strftime('%Y%m%d%H%M%S')
savedfromclipboard = str('empty_first_time')
activeclipboarddata = pyperclip.paste()
while (activeclipboarddata != 'stop'):
    activeclipboarddata = pyperclip.paste()
    if (savedfromclipboard != activeclipboarddata):
        if (activeclipboarddata != 'stop'):
            with open('appendfile' + str(ymdhms) + '.txt', 'a') as appendfileout:
                appendfileout.write(activeclipboarddata + '\n')
        savedfromclipboard = pyperclip.paste()
    time.sleep(2)
