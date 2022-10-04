# -*- coding: UTF-8 -*-

##differentes importattions
import serial  # bibliothèque permettant la communication série
import time    # pour le délai d'attente entre les messages

from numpy import sign
import RPi.GPIO as GPIO #pour les pins et le threading

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.flushInput()
#nom des pins des capteurs de butée
butG = 12
butD = 16
butH = 20
butB = 21
butG2 =18
butD2 =23
butH2 =24
butB2 =25
bounce = 100

##Set up du GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(13, GPIO.OUT, initial=GPIO.HIGH)

GPIO.setup(butG, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(butD, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(butH, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(butB, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(butG2, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(butD2, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(butH2, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(butB2, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)


def callbackCap(channel):
    if channel == butG :
        print("G")
        ser.write(b"G\n")
        #ser.write(str.encode("S9100090000E"))
#         ser.write(str.encode("S9100090000E"))    #horiz butée gauche
#         tabCommande[i][1]=100
    elif channel == butD :
        print("D")
        ser.write(b"D\n")
#         ser.write(str.encode("S9010090000E"))    #horiz butée droite
#         tabCommande[i][1]=0
    elif channel == butB :
        print("B")
        ser.write(b"B\n")
#         ser.write(str.encode("S9001090000E"))    #verti butée bas
#         tabCommande[i][2]=0
    elif channel == butH :
        print("H")
        ser.write(b"H\n")
#         ser.write(str.encode("S9000190000E"))   #verti butée haut
#         tabCommande[i][2]=100
    elif channel == butG2 :
        print("G2")
        ser.write(b"G2\n")
#         ser.write(str.encode("S9000091000E"))    #horiz butée gauche
#         tabCommande[i][3]=100
    elif channel == butD2 :
        print("D2")
        ser.write(b"D2\n")
#         ser.write(str.encode("S9000090100E"))    #horiz butée droite
#         tabCommande[i][3]=0
    elif channel == butB2 :
        print("B2")
        ser.write(b"B2\n")
#         ser.write(str.encode("S9000090010E"))    #verti butée bas
#         tabCommande[i][4]=0
    elif channel == butH2 :
        print("H2")
        ser.write(b"H2\n")
#         ser.write(str.encode("S9000090001E"))   #verti butée haut
#         tabCommande[i][4]=100
#


GPIO.add_event_detect(butG, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
GPIO.add_event_detect(butH, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
GPIO.add_event_detect(butB, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
GPIO.add_event_detect(butD, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
GPIO.add_event_detect(butG2, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
GPIO.add_event_detect(butH2, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
GPIO.add_event_detect(butB2, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
GPIO.add_event_detect(butD2, GPIO.RISING, callback=callbackCap, bouncetime=bounce)


##Activation des capteurs de butée, multi-threading
# 
# def callbackCap(channel):
#     global i, tabCommande
#     if channel == butG :
#         ser.write(str.encode("S9100090000E"))    #horiz butée gauche
#         tabCommande[i][1]=100
#     elif channel == butD :
#         ser.write(str.encode("S9010090000E"))    #horiz butée droite
#         tabCommande[i][1]=0
#     elif channel == butB :
#         ser.write(str.encode("S9001090000E"))    #verti butée bas
#         tabCommande[i][2]=0
#     elif channel == butH :
#         ser.write(str.encode("S9000190000E"))   #verti butée haut
#         tabCommande[i][2]=100
#     elif channel == butG2 :
#         ser.write(str.encode("S9000091000E"))    #horiz butée gauche
#         tabCommande[i][3]=100
#     elif channel == butD2 :
#         ser.write(str.encode("S9000090100E"))    #horiz butée droite
#         tabCommande[i][3]=0
#     elif channel == butB2 :
#         ser.write(str.encode("S9000090010E"))    #verti butée bas
#         tabCommande[i][4]=0
#     elif channel == butH2 :
#         ser.write(str.encode("S9000090001E"))   #verti butée haut
#         tabCommande[i][4]=100
#     else:
#         print("Butée detectée sur un pin sans lien avec les capteurs")
# 
# GPIO.add_event_detect(butG, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
# GPIO.add_event_detect(butH, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
# GPIO.add_event_detect(butB, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
# GPIO.add_event_detect(butD, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
# GPIO.add_event_detect(butG2, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
# GPIO.add_event_detect(butH2, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
# GPIO.add_event_detect(butB2, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
# GPIO.add_event_detect(butD2, GPIO.RISING, callback=callbackCap, bouncetime=bounce)
# 
# ##
# 
# #TODO fonction qui calcule la distance parcourue pour de vrai si jamais le chariot est trop lent afin de changer la case suivant
# 
# 
# 
# #formate la consigne en intensité à transmettre à l'arduino
# def intTOstr(a):
#     if a<10:
#         return str("0"+str(a)[0:1])
#     else:
#         return str(a)[0:2]
# 
# 
# #Création d'un tableau contenant toutes les commandes
# def getTab():
#     newTab = [[-0.1,1,1,1,1]]
#     with open('/home/pi/Documents/Commandes/' + nom_musique + '.csv', 'r') as file:
#         reader = csv.reader(file, delimiter=";")
#         for row in reader:
#             new_row = [float(row[0]), float(row[1]), float(row[2]),float(row[3]), float(row[4])]
#             newTab+=[new_row]
#     file.close()
#     return newTab
# 
# 
# #passage d'une consigne de position en consigne de vitesse, en vérifiant les limites du moteur
# #numb permet d'indiquer le rail, 0 pour le 1er, 2 pour le 2eme
# def distTOvit(dx,dy,ts,numb):
#     global tabCommande, i
#     dx = dx*Lx/(Vmax*ts)
#     dy = dy*Ly/(Vmax*ts)
#     if dx > 99:
#         tabCommande[i][1+numb] = tabCommande[i-1][1+numb] + (99/dx)*(tabCommande[i][1+numb]-tabCommande[i-1][1+numb])
#     if dy > 99:
#         tabCommande[i][2+numb] = tabCommande[i-1][2+numb] + (99/dy)*(tabCommande[i][2+numb]-tabCommande[i-1][2+numb])
#     return min(dx,99),min(dy,99)
# 
# 
# #passage des consignes en position en consignes pour l'arduino
# def asserv(tabNx , tabPv):
#     t = tabNx[0]-tabPv[0]
#     l = tabNx[1]-tabPv[1]
#     h = tabNx[2]-tabPv[2]
#     l2 = tabNx[3]-tabPv[3]
#     h2 = tabNx[4]-tabPv[4]
#     if l>0:
#         if h>0: sens = 2
#         else : sens = 3
#     else:
#         if h>0: sens = 0
#         else : sens = 1
#     if l2>0:
#         if h2>0: sens2 = 2
#         else : sens2 = 3
#     else:
#         if h2>0: sens2 = 0
#         else : sens2 = 1
#     l,h = distTOvit(abs(l),abs(h),t,0)
#     l2,h2 = distTOvit(abs(l2),abs(h2),t,2)
#     commande = str(sens)+intTOstr(l)+intTOstr(h)+str(sens2)+intTOstr(l2)+intTOstr(h2)
#     return commande
# 
# 
# #initialise la position sur gauche et bas pour le 1er rail (x=0;y=0)
# def initPosition():
#     global tabCommande
#     while (tabCommande[0][1]==1 or tabCommande[0][2] == 1):
#         if (tabCommande[0][1]==1 and tabCommande[0][2]==1):
#              ser.write(str.encode("S1251010000E"))
#         if tabCommande[0][1]==0 :
#             ser.write(str.encode("S1001010000E"))
#         if tabCommande[0][2]==0 :
#             ser.write(str.encode("S1250010000E"))
#         time.sleep(0.1)
#     ser.write(str.encode("S0000000000E"))
# 
# #initialise la position sur gauche et bas pour le 2eme rail (x=0;y=0)
# def initPosition2():
#     global tabCommande
#     while (tabCommande[0][3]==1 or tabCommande[0][4] == 1):
#         if (tabCommande[0][3]==1 and tabCommande[0][4]==1):
#              ser.write(str.encode("S1000012510E"))
#         if tabCommande[0][3]==0 :
#             ser.write(str.encode("S1000010010E"))
#         if tabCommande[0][4]==0 :
#             ser.write(str.encode("S1000012500E"))
#         time.sleep(0.1)
#     ser.write(str.encode("S0000000000E"))
# 
# #permet de passer le volume en commande selon la convention d'écriture d'omxplayer
# def volumeMusique(valCommande):
#     return (int(valCommande)-50)*19
# 
# 
# ##Fait tout
# 
# try:
#     tabCommande = getTab()
#     initPosition()
#     initPosition2()
#     temps = time.time()
#     subprocess.Popen(["omxplayer",'/home/pi/Documents/Musiques/' + nom_musique + '.wav'])
#     #TODO time.sleep(0.3)
#     for i in range(1,len(tabCommande)):
#         #check le fichier commande
#         commande = subprocess.check_output(['tail','-1','/home/pi/Documents/Talabox/commande.txt']).decode()
#         #si la commande est de faire pause, on arrete les moteurs et la musique en pause
#         if int(commande[0])==0:
#             ser.write(str.encode("S0000000000E"))
#             subprocess.Popen(["dbuscontrol.sh","pause"])
#             # quand on est en pause on ne fait rien d'autre que check si on est plus en pause
#             while int(commande[0])==0:
#                 time.sleep(0.1)
#                 commande = subprocess.check_output(['tail','-1','/home/pi/Documents/Talabox/commande.txt']).decode()
#             subprocess.Popen(["dbuscontrol.sh","pause"])
#             temps = time.time()
#         #on joue la musique et les déplacements
#         elif int(commande[0])==1:
#             vitesse = int(commande[2:4])
#             #si le volume est différent
#             if int(volume)!=volumeMusique(commande[6:9]):
#                 volume = str(volumeMusique(commande[6:9]))
#                 subprocess.Popen(["pkill","omxplayer"])
#                 tps = tabCommande[i][0]
#                 time_omx = str(int(tps/3600))+ ":" + str(int((tps%3600)/60)) + ":" + str(int(tps%60))
#                 subprocess.Popen(["omxplayer","--vol",volume,"-l",time_omx,'/home/pi/Documents/Musiques/' + nom_musique + '.wav'])
#             msg_ardui = asserv(tabCommande[i],tabCommande[i-1])
#             ser.write(str.encode("S"+msg_ardui+"E"))
#             temps = temps+(tabCommande[i][0]-tabCommande[i-1][0])
#             time.sleep(max(temps-time.time(),0))
#         else:
#             #pas un 0 ou un 1, erreur dans la commande, arrêt
#             subprocess.Popen(["pkill","omxplayer"])
#             ser.write(str.encode("S0000000000E"))
#             pid_file = open("pid.txt","w")
#             pid_file.write("0")
#             pid_file.close()
#             sys.exit()
# 
# except KeyboardInterrupt: #si un ctrl+c est entré, coupe proprement le programme
#     subprocess.Popen(["pkill","omxplayer"])
#     ser.write(str.encode("S0000000000E"))
#     pid_file = open("/home/pi/Documents/Talabox/pid.txt","w")
#     pid_file.write("0")
#     pid_file.close()
#     sys.exit()
# 
# #coupe proprement le programme
# subprocess.Popen(["pkill","omxplayer"])
# ser.write(str.encode("S0000000000E"))
# pid_file = open("/home/pi/Documents/Talabox/pid.txt","w")
# pid_file.write("0")
# pid_file.close()
# sys.exit()
