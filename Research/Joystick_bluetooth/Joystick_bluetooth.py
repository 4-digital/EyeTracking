import serial
from evdev import InputDevice, categorize, ecodes
import time
import threading

ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

def send_serial(direction, value):
    # Verifică dacă valoarea este diferită de ultima trimisă pentru acea direcție
    if last_sent.get(direction) != value:
        cmd = f"{direction} {value}"
        print(cmd)
        ser.write(cmd.encode())
        last_sent[direction] = value  # Actualizăm ultima valoare trimisă

def check_timeout():
    global last_activity
    while True:
        time.sleep(0.5)
        current_time = time.time()

        if current_time - last_activity['LEFT/RIGHT'] > 1.0:
            send_serial('LEFT', 0)
            send_serial('RIGHT', 0)
            last_activity['LEFT/RIGHT'] = current_time

        if current_time - last_activity['FORWARD/BACKWARD'] > 1.0:
            send_serial('FORWARD', 0)
            send_serial('BACKWARD', 0)
            last_activity['FORWARD/BACKWARD'] = current_time

# Pornire thread în fundal
timeout_thread = threading.Thread(target=check_timeout)
timeout_thread.daemon = True
timeout_thread.start()

device_path = '/dev/input/event3'
dev = None

last_activity = {
    'LEFT/RIGHT': time.time(),
    'FORWARD/BACKWARD': time.time()
}

# Ținem evidența ultimei valori trimise pentru fiecare direcție
last_sent = {
    'LEFT': None,
    'RIGHT': None,
    'FORWARD': None,
    'BACKWARD': None
}

while True:
    try:
        if not dev:
            dev = InputDevice(device_path)
        for event in dev.read_loop():
            current_time = time.time()

            if event.type == ecodes.EV_REL:
                if event.code == ecodes.REL_X:
                    direction = 'RIGHT' if event.value > 0 else 'LEFT'
                    send_serial(direction, abs(event.value))
                    last_activity['LEFT/RIGHT'] = current_time
                elif event.code == ecodes.REL_Y:
                    direction = 'BACKWARD' if event.value > 0 else 'FORWARD'
                    send_serial(direction, abs(event.value))
                    last_activity['FORWARD/BACKWARD'] = current_time

    except OSError:
        print("Device deconectat. Încerc din nou în 5 secunde...")
        dev = None
        time.sleep(5)

