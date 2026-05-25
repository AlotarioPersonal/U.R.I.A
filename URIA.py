'''

   U.R.I.A (Unbelievably Retarded Intelligence Application)

   Version 0.1.1, 2026-5-24

   Clap-activated intelligence system designed to be fun to operate but ultimately unintuitive. Only a couple of basic functions.
   Moderate "plugin" system that enables for more scripts to be added to the double-clap by mounting them in PATH.py and running it.
   (I am a diagnosed high-functioning autistic person and thus authorized to use the word "retarded." Please bear with me.)
   

   REQUIRED PACKAGES:
   -clapdetector
   -playsound
   -gtts
   -random

   UPDATE 0.1.1: Structure refactor.

'''

import time
import os
import random
from playsound import *
from clapDetector import ClapDetector, printDeviceInfo
from extscripts import funcs
from extscripts import GENERATE_TTS

thresholdBias = 6000
lowcut = 200  #inc
highcut = 3300  #dec
clapDetector = ClapDetector(inputDevice=-1, logLevel=10)
clapDetector.initAudio()




os.system("clear")
print(""" ▄         ▄     ▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌       ▐░▌   ▐░░░░░░░░░░░▌   ▐░░░░░░░░░░░▌   ▐░░░░░░░░░░░▌
▐░▌       ▐░▌   ▐░█▀▀▀▀▀▀▀█░▌    ▀▀▀▀█░█▀▀▀▀    ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌   ▐░▌       ▐░▌        ▐░▌        ▐░▌       ▐░▌
▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄█░▌        ▐░▌        ▐░█▄▄▄▄▄▄▄█░▌
▐░▌       ▐░▌   ▐░░░░░░░░░░░▌        ▐░▌        ▐░░░░░░░░░░░▌
▐░▌       ▐░▌   ▐░█▀▀▀▀█░█▀▀         ▐░▌        ▐░█▀▀▀▀▀▀▀█░▌
▐░▌       ▐░▌   ▐░▌     ▐░▌          ▐░▌        ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄█░▌ ▄ ▐░▌      ▐░▌  ▄  ▄▄▄▄█░█▄▄▄▄  ▄ ▐░▌       ▐░▌
▐░░░░░░░░░░░▌▐░▌▐░▌       ▐░▌▐░▌▐░░░░░░░░░░░▌▐░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀  ▀         ▀  ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀  ▀         ▀ 
 Clap twice to activate bootloader                            """)

try:

    while True:
        audioData = clapDetector.getAudio()

        result = clapDetector.run(thresholdBias=thresholdBias, lowcut=lowcut, highcut=highcut, audioData=audioData)
        resultLength = len(result)
        if resultLength == 4:
            exit()
        if resultLength == 2:
            os.system("python PATH.py")
        if resultLength == 3:
            funcs.intDiagnostic()
        if resultLength == 1:
            #time.sleep(2)
            GENERATE_TTS.initialize()
            playsound("extscripts/voicelines/voice.mp3", block=True)

except KeyboardInterrupt:
    print("Killing U.R.I.A")
finally:
    clapDetector.stop()
