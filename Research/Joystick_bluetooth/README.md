# Joystick/Gamepad Control
<img src="/photos/joystick.jpg">

Pentru a putea prelua comanda de la distanta se foloseste un joystick bluetooth versiunea3 care se conecteaza direct la raspberry
Acest cod este un test care citeste valoarea de la un joystick , actualizeaza valoarea de 0 care nu este trimisa pe bluetooth, afiseaza valoarea si o trimite pe serial.

sudo apt-get update
sudo apt-get install bluetooth bluez blueman

Pentru a instala evtest, folosește:


sudo apt-get install evtest
sudo apt-get install python3-evdev

Apoi, testează fiecare dispozitiv:


sudo evtest /dev/input/eventX



Înlocuiește eventX cu numerele corespunzătoare pentru fiecare dispozitiv de intrare pe care dorești să îl testezi. In cazul meu au fost afisate proprietatile joystick-ului la event3
```
^Cme@eyetrack:~ $ sudo evtest /dev/input/event3
Input driver version is 1.0.1
Input device ID: bus 0x5 vendor 0x5ac product 0x3232 version 0x1
Input device name: "VR BOX Mouse"
Supported events:
  Event type 0 (EV_SYN)
  Event type 1 (EV_KEY)
    Event code 272 (BTN_LEFT)
    Event code 273 (BTN_RIGHT)
    Event code 274 (BTN_MIDDLE)
    Event code 275 (BTN_SIDE)
    Event code 276 (BTN_EXTRA)
  Event type 2 (EV_REL)
    Event code 0 (REL_X)
    Event code 1 (REL_Y)
    Event code 8 (REL_WHEEL)
    Event code 11 (?)
  Event type 4 (EV_MSC)
    Event code 4 (MSC_SCAN)
Properties:
Testing ... (interrupt to exit)
Event: time 1693422351.471483, type 2 (EV_REL), code 1 (REL_Y), value -2
Event: time 1693422351.471483, -------------- SYN_REPORT ------------
Event: time 1693422351.479013, type 2 (EV_REL), code 1 (REL_Y), value -6
Event: time 1693422351.479013, -------------- SYN_REPORT ------------
Event: time 1693422351.486514, type 2 (EV_REL), code 1 (REL_Y), value -8
Event: time 1693422351.486514, -------------- SYN_REPORT ------------
Event: time 1693422351.494005, type 2 (EV_REL), code 1 (REL_Y), value -8
Event: time 1693422351.494005, -------------- SYN_REPORT ------------
Event: time 1693422351.501528, type 2 (EV_REL), code 1 (REL_Y), value -8
Event: time 1693422351.501528, -------------- SYN_REPORT ------------
Event: time 1693422351.509020, type 2 (EV_REL), code 1 (REL_Y), value -8
```
In partea de jos se vede cum am actionat maneta pe axa Y. Valoarea maxima, cand maneta este la stanga sau dreapta este de la 8 la -8

Atentie, Valoarea nu este actualizata daca se da drumul la maneta si aceasta revine la pozitia din mijloc.
Am incercat sa rezolv asta in cod, adica la fiecare 1 secunda daca valoarea nu este actualizata sau modificata, se presupune ca are valoarea 0
Cand gamepad-ul se afla la o distanta mai mare de raspberry se deconecteaza. Scriptul incearca sa scaneze la fiecare 5 secunde daca a fost reconectat. Daca timpul in care este deconectat nu este mai mare de cateva minute, pe gamepad clipeste un LED albastru se reconecteaza automat. Daca nu a fost folosit ceva timp gamepad-ul se opreste automat si trebuie repornit. Tine butonul de power apasat mai mult de 3 secunde.
