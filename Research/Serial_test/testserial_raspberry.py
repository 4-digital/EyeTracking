import time
import serial
import datetime
from random import randint

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

print(ser.name)

while 1:
    message = f"Number:{randint(0, 99)}"
    print(f"Sent: {message}")
    ser.write((message + "\n").encode('utf-8'))

    received_message = ser.readline()
    time.sleep(1)

    if received_message:
        timestamp = datetime.datetime.now()
        try:
            print(f"Received: {received_message.decode('utf-8').strip()} at {timestamp}")
        except UnicodeDecodeError:
            print("Received an invalid UTF-8 sequence.")
