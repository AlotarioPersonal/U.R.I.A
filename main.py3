'''

   U.R.I.A (Unbelievably Retarded Intelligence Application)

   Version 0.1, 2026-5-22

   Clap-activated intelligence system designed to be fun to operate but ultimately unintuitive. Only a couple of basic functions.
   Moderate "plugin" system that enables for more scripts to be added to the double-clap by mounting them in PATH.py and running it.
   It will move to your default audio device and requires a pretty decent microphone to pick up the claps.
   (I am a diagnosed high-functioning autistic person and thus authorized to use the word "retarded." Please bear with me.)
   

   REQUIRED PACKAGES:
   -clapdetector
   -playsound (if on linux, also install portaudio19-dev using apt or whatever you use)
   -gtts

'''

import time
import os
import subprocess
import datetime
import random
from playsound import *
from clapDetector import ClapDetector, printDeviceInfo
from gtts import gTTS
import funcs


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
                                                             """)

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
            funcs.timeCheck()
            playsound("voicelines/voice.mp3", block=True)
        if resultLength == 5:
            z = random.randint(1,3) #usually the "music" folder has 3 mp3 files in it, but they're all copyrighted, so i can't share em
            megastr = ("music/" + str(z) + ".mp3")
            playsound(megastr, block=True)

except KeyboardInterrupt:
    print("Killing U.R.I.A")
finally:
    clapDetector.stop()
