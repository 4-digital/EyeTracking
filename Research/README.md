# Modalitati de a urmari miscarea ochilor

Eye tracking (urmarirea privirii) este tehnica prin care se măsoară mișcările ochilor și punctele de focalizare ale unei persoane. Există mai multe metode și tehnologii pentru aceasta, variind de la simple la complexe.
Documentarea procesului de reaserch cu fotografii, link-uri si descriere

## Webcam-based Eye Tracking:

 Folosește software specializat care analizează imagini de la o cameră web standard pentru a estima unde privește utilizatorul. Exemple includ aplicații software precum "GazePointer".

## USB Camera cu OpenCV:
 Aceasta varianta ne-ar da posibilitatea de a monta camera video la un singur ochi, implicit mai putin hardware ce se monteaza pe sapca, ochelari.
 Am comandat doua tipuri de camera pentru inspectie. Nu stiu daca am sa le pot face sa functioneze cu raspberry, adica nu cred ca au drivere pentru linux.
 [Link]https://medium.com/@stepanfilonov/tracking-your-eyes-with-python-3952e66194a6

![inspektionCam](https://github.com/4-digital/EyeTracking/assets/26842625/9d09b487-d308-4033-af89-70942d66566a)

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



# Front camera -primul test
 Am testat mai multe camere, ce am gasit in format mai mic. Din cele cu distanta focala mica, endoscope camera, incep sa focalizeze de la 3-4 cm. Cei mai multi pozitioneaza camera in partea dreapta jos.
 ### avantaj cu camera montata in centru
  - Facand teste am vazut ca atunci cand este pozitionata frontal, chiar in fata irisului si aprinsa lumina pe camera, reflecta exact pe mijlo si cred ca este mai usor de scris un program care sa citeasca ca si punct de referinta.
  - lasa in portea de jos loc liber pentru alte sisteme de citire a ochilor, in cazul acesta Tobii. Oricum, si camera care se monteaza in partea de jos, poate fi pozitionata mai inspre deapta
  - parca sunt mai putine reflexii din lentila ochelarilor decat atunci cand camera e indreptata inspre ochi dintr-o parte
### dezavantaje
 - Este zizibila chiar si cu celalalt ochi.
 - Inestetic
 - Tot sunt reflexii in lentila ochelarilor. Chiar ledurile aflate pe camera sunt aproape neutilizabile(sunt necesare teste si afara)

![Ochelari_focala](https://github.com/4-digital/EyeTracking/assets/26842625/2c22d382-fcc0-4637-b153-a9a0663e0237)

![ochelari_camera](https://github.com/4-digital/EyeTracking/assets/26842625/8ae689d2-5cf1-44db-88f9-88e0d0753c09)
![ochelari_camera1](https://github.com/4-digital/EyeTracking/assets/26842625/638a98e8-02c1-4553-9387-b33bf7502826)
