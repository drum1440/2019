# stack_clipboard_data_to_file
query clipboard data every 2 seconds, if the data changed, paste it at the end of a file

- Python program pasteappend.py
  - keeps reviewing your clipboard every 2 seconds
  - if it has changed append new clipboard data to file appendfileYYYYMMDDHHMMSS.txt
    - if your clipboard contains only the word stop then program execution will stop
    - To install pyperclip via pip first:
      - pip install pyperclip

