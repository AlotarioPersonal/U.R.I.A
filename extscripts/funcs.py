from gtts import gTTS
from playsound import *
import os

def intDiagnostic():
	print("running voice cache, one sec, my throat is clogged")
	
	print("alright i got it out")
	playsound("extscripts/voicelines/voice2.mp3", block=True)
	response = os.system(f"ping -c 1 8.8.8.8")
	print(response)
	if response == 0:
		os.system("speedtest-cli --secure")
		print("pee")
		playsound("voicelines/voice3.mp3", block=False)
	else:
		playsound("voicelines/voice4.mp3")
