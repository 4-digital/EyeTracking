# Modalitati de a urmari miscarea ochilor

Eye tracking (urmarirea privirii) este tehnica prin care se măsoară mișcările ochilor și punctele de focalizare ale unei persoane. Există mai multe metode și tehnologii pentru aceasta, variind de la simple la complexe.
Documentarea procesului de reaserch cu fotografii, link-uri si descriere

## Webcam-based Eye Tracking:

 Folosește software specializat care analizează imagini de la o cameră web standard pentru a estima unde privește utilizatorul. Exemple includ aplicații software precum "GazePointer".

## USB Camera cu OpenCV:
 Aceasta varianta ne-ar da posibilitatea de a monta camera video la un singur ochi, implicit mai putin hardware ce se monteaza pe sapca, ochelari.
 Am comandat doua tipuri de camera pentru inspectie. Nu stiu daca am sa le pot face sa functioneze cu raspberry, adica nu cred ca au drivere pentru linux.
 [Link]https://medium.com/@stepanfilonov/tracking-your-eyes-with-python-3952e66194a6

## Eye Tracking cu IR montate pe ochelari:
Posibil cea mai ieftina metoda dar inca nu stiu cat de eficiienta este.
Pentru aceasta varianta am comandat deja cateva piese si ma apuc de ea dupa ce probez OpenCV.
[Link]https://people.ece.cornell.edu/land/courses/ece4760/FinalProjects/s2010/yh428_aoo34/eyetracking/
[Link]https://people.ece.cornell.edu/land/courses/ece4760/FinalProjects/f2013/msw234_sf323/msw234_sf323_old/msw234_sf323/Eyetracker.htm

## Sisteme Standalone de Eye Tracking:
 Acestea sunt dispozitive specializate care sunt montate pe un monitor sau o pereche de ochelari. Ele folosesc surse de lumină infraroșie și camere pentru a urmări mișcarea ochilor. Exemple includ produse de la Tobii sau EyeTribe.
 [Link]https://www.tobii.com/products/eye-trackers
 [Link]https://theeyetribe.com/dev.theeyetribe.com/dev.theeyetribe.com/general/index.html
 [Link]https://pupil-labs.com/products/core/
 [Link]https://imotions.com/products/hardware/eye-tracking/eye-tracking-glasses/

## Eye Tracking în Realitate Virtuală (VR):
 Multe căști de realitate virtuală sunt echipate sau pot fi adaptate cu tehnologie de eye tracking, cum ar fi HTC Vive Pro Eye.

## Electrooculografie (EOG):
 O metodă care implică plasarea de electrozi în jurul ochilor pentru a măsura potențialele electrice care apar odată cu mișcarea globilor oculari.
[Link]https://en.wikipedia.org/wiki/Electrooculography


## Sisteme Invasive:
 Tehnici precum implanturile retiniene care pot fi utilizate pentru a urmări mișcarea ochilor de la interior.

## Eye Tracking Combinat cu Analiza EEG
 (Electroencefalografie): Unele sisteme avansate combină eye tracking-ul cu analiza EEG pentru a obține și mai multe informații despre atenția și răspunsul neurologic al utilizatorului.

 --- 
# Camere testate:
## Endoscop Cam

![Endoscop_cam](https://github.com/4-digital/EyeTracking/assets/26842625/4b4500fd-7835-4824-8349-bfdb72bd9042)
![endoscop_cam1](https://github.com/4-digital/EyeTracking/assets/26842625/721245ca-838a-4ecd-a724-dd156707cbf1)
![endoscop_cam2](https://github.com/4-digital/EyeTracking/assets/26842625/9054212c-8336-43f5-be65-14e867338e43)


## USB Cam




## Pi Zero Cam


![PiZero_CAM](https://github.com/4-digital/EyeTracking/assets/26842625/a1a7793a-04e4-4286-aaab-a6bcd622505d)


## USB Webcam

![USB_Webcam](https://github.com/4-digital/EyeTracking/assets/26842625/46b6be27-e90a-4ac6-b88c-0ac0652862b8)



# Front camera -primul test
 Am testat mai multe camere, ce am gasit in format mai mic. Din cele cu distanta focala mica, endoscope camera, incep sa focalizeze de la 3-4 cm. Chiar daca cei mai multi pozitioneaza camera in partea dreapta jos, pentru primele teste am sa o montez in fata ochiului drept pentru a se potrivi si cu tutorialele vazute pe net.
 ### avantaj cu camera montata in centru
  + Facand teste am vazut ca atunci cand este pozitionata frontal, chiar in fata irisului si aprinsa lumina pe camera, reflecta exact pe mijloc si cred ca este mai usor de scris un program care sa citeasca ca si punct de referinta.
  + lasa in portea de jos loc liber pentru alte sisteme de citire a ochilor, in cazul acesta Tobii. Oricum, si camera care se monteaza in partea de jos, poate fi pozitionata mai inspre deapta
  + sunt mai putine reflexii din lentila ochelarilor decat atunci cand camera e indreptata inspre ochi dintr-o parte
  + exemple cu OpenCV aveau majoritatea camera pozitionata central.
### dezavantaje
 - Este vizibila chiar si cu celalalt ochi.
 - Inestetic
 - Tot sunt reflexii in lentila ochelarilor. Chiar ledurile aflate pe camera sunt aproape neutilizabile(sunt necesare teste si afara)

|                                |                                 |                                      |
|--------------------------------|---------------------------------|--------------------------------------|
| ![Ochelari_focala](https://github.com/4-digital/EyeTracking/assets/26842625/7137b60b-2b14-4afe-a127-5fb728550e17) | ![ochelari_camera](https://github.com/4-digital/EyeTracking/assets/26842625/653c1a31-b25b-465c-af3f-d4083b428aa1) |  ![ochelari_camera1](https://github.com/4-digital/EyeTracking/assets/26842625/34e4d132-4c13-4fde-a350-082541243791) |



![suporti_electronica](https://github.com/4-digital/EyeTracking/assets/26842625/f7faa65c-f0a2-4579-9f84-919d05993fc9)
