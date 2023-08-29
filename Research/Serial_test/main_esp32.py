from machine import UART
from time import sleep

# Inițializează UART cu pinii specificați pentru TX și RX
uart = UART(2, baudrate=115200, tx=1, rx=2)

while True:
    if uart.any():  # Dacă există date în buffer
        data = uart.readline()  # Citește linia primită
        uart.write(data)  # Trimite înapoi datele exact cum au fost primite
        sleep(0.1)  # Mică pauză pentru a preveni suprasolicitarea buclei
