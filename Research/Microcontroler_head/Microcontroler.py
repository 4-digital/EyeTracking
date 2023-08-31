from machine import UART, Pin
from neopixel import NeoPixel
from time import sleep

# Configurație NeoPixel
NUM_LED = 21
MAX_BRIGHTNESS = 38  # 15% din 255
pin = Pin(14, Pin.OUT)
np = NeoPixel(pin, NUM_LED)
status_led_index = 10
np[status_led_index] = (MAX_BRIGHTNESS, MAX_BRIGHTNESS, MAX_BRIGHTNESS)  # Led de status
np.write()

uart = UART(2, baudrate=115200, tx=1, rx=2)

def clear_movement_leds():
    for i in range(NUM_LED):
        if i != status_led_index:  # Excludem LED-ul de status
            np[i] = (0, 0, 0)
    np.write()

while True:
    if uart.any():
        data = uart.readline().decode('utf-8').strip()
        parts = data.split()
        if len(parts) != 2:
            continue  # Invalid data format

        direction, value_str = parts

        try:
            value = int(value_str)
        except ValueError:
            continue  # Invalid number format
        
        clear_movement_leds()  # La fiecare nouă comandă, ștergem luminile de mișcare
        
        if direction == "LEFT":
            for i in range(value):
                np[status_led_index - 1 - i] = (0, 0, MAX_BRIGHTNESS)
                
        elif direction == "RIGHT":
            for i in range(value):
                np[status_led_index + 1 + i] = (0, 0, MAX_BRIGHTNESS)
                
        elif direction == "FORWARD":
            if 1 <= value <= 4:
                intensity = int(MAX_BRIGHTNESS * value / 4)
                np[0] = (0, 0, intensity)
                np[NUM_LED - 1] = (0, 0, intensity)
            elif 4 < value <= 8:
                intensity = int(MAX_BRIGHTNESS * (value - 4) / 4)
                np[2] = (intensity, 0, 0)
                np[NUM_LED - 3] = (intensity, 0, 0)
            
        elif direction == "BACKWARD":
            if 1 <= value <= 4:
                intensity = int(MAX_BRIGHTNESS * value / 4)
                np[0] = (0, intensity, 0)
                np[NUM_LED - 1] = (0, intensity, 0)
            elif 4 < value <= 8:
                intensity = int(MAX_BRIGHTNESS * (value - 4) / 4)
                np[2] = (0, intensity, 0)
                np[NUM_LED - 3] = (0, intensity, 0)
            
        np.write()

    sleep(0.1)
