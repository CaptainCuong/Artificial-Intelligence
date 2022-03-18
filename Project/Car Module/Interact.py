from curses import baudrate
import os 
import time
from datetime import datetime 
from serial import Serial 

import serial

s = serial.Serial(port = 'COM7', baudrate=19200, bytesize = 8, timeout = 1)

s.write(str.encode('1.'))

# 0: dừng
# 1: thẳng
# 2: lùi
# 3: rẽ trái
# 4: rẽ phải
# 5: đi ngang qua trái
# 6: đi ngang qua phải
# 7: lùi trái 
# 8: lùi phải