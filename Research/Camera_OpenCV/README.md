# Instalare si configurare
# Setari Camera
Camera folosita nu trimite un numar de serie ceea ce ingreuneaza detectia si pentru ca avem doua camere identice, cea care este detectata prima primeste identificatorul de camera0
Ele sunt conectate tot timpul in acelas port la USB Hub, de aceea folosim asta ca sa le numim in functie de unde sunt conectate:
    Obțineți calea de dispozitiv pentru fiecare cameră:


udevadm info -q path -n /dev/video0
udevadm info -q path -n /dev/video1
me@eyetrack:~ $ udevadm info -q path -n /dev/video0
udevadm info -q path -n /dev/video1
/devices/platform/soc/3f980000.usb/usb1/1-1/1-1.1/1-1.1.2/1-1.1.2.1/1-1.1.2.1:1.0/video4linux/video0
/devices/platform/soc/3f980000.usb/usb1/1-1/1-1.1/1-1.1.2/1-1.1.2.1/1-1.1.2.1:1.0/video4linux/video1

echo 'KERNEL=="video*", ATTRS{idVendor}=="1902", ATTRS{idProduct}=="8301", DEVPATH=="/devices/platform/soc/3f980000.usb/usb1/1-1/1-1.1/1-1.1.2/1-1.1.2.1/1-1.1.2.1:1.0/video4linux/video0", SYMLINK+="camera1"' | sudo tee /etc/udev/rules.d/99-camera1.rules


echo 'KERNEL=="video*", ATTRS{idVendor}=="1902", ATTRS{idProduct}=="8301", DEVPATH=="/devices/platform/soc/3f980000.usb/usb1/1-1/1-1.1/1-1.1.2/1-1.1.2.1/1-1.1.2.1:1.0/video4linux/video1", SYMLINK+="camera2"' | sudo tee /etc/udev/rules.d/99-camera2.rules

sudo udevadm control --reload-rules
sudo udevadm trigger

me@eyetrack:~ $ ls -l /dev/camera*
lrwxrwxrwx 1 root root 6 Aug 31 18:19 /dev/camera1 -> video0
lrwxrwxrwx 1 root root 6 Aug 31 18:19 /dev/camera2 -> video1

Asa se importa in OpenCV:
import cv2

# Pentru camera1
cap1 = cv2.VideoCapture('/dev/camera1')

# Pentru camera2
cap2 = cv2.VideoCapture('/dev/camera2')


Diferențierea prin udev: Redenumirea camerelor ca camera1 și camera2 folosind reguli udev vă oferă un control mai mare. Indiferent de ordinea în care sunt detectate sau de numărul de dispozitive conectate, camera1 va fi întotdeauna camera conectată la portul specificat în regula udev și la fel și pentru camera2. Acest lucru vă oferă o predictibilitate mai mare și vă asigură că software-ul sau scripturile dvs. se referă întotdeauna la camera corectă.