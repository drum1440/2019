# keep reviewing your clipboard every 2 seconds
# if it has changed append new clipboard data to file appendfile.txt
# if your clipboard has 'stop' then program execution will stop

# you may need to install pyperclip via pip first:
# pip install pyperclip

import pyperclip
import time
savedfromclipboard = str('empty_first_time')
activeclipboarddata = pyperclip.paste()
while (activeclipboarddata != 'stop'):
    activeclipboarddata = pyperclip.paste()
    if (savedfromclipboard != activeclipboarddata):
        if (activeclipboarddata != 'stop'):
            with open('appendfile.txt', 'a') as appendfileout:
                appendfileout.write(activeclipboarddata + '\n')
        savedfromclipboard = pyperclip.paste()
    time.sleep(2)
