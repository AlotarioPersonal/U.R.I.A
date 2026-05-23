from gtts import gTTS
import datetime
from playsound import *
import os


month=0
day=0
year=0
hour=0
minute=0
ampm=0
speech=""
def timeCheck():
	global speech
	global month
	global day
	global year
	global hour
	global minute
	x = datetime.datetime.now()
	month=str(x.strftime("%B"))
	day=str(x.strftime("%d"))
	year=str(x.strftime("%Y"))
	minute=str(x.strftime("%M"))
	ampm=str(x.strftime("%p"))
	hour=str(x.strftime("%I"))
	speech=("Ooriah time check. Today's date is " + str(month) + " " + str(day) + ", " + str(year) + ". The time is " + str(hour) + ":" + str(minute) + str(ampm) + ". ")
	voice=gTTS(text=str(speech), lang="en", slow=False)
	voice.save("voicelines/voice.mp3")

def intDiagnostic():
	print("running voice cache, one sec, my throat is clogged")
	voice=gTTS(text="Pinging the internet DNS and running speed test client. You'll see some shit on screen.", lang="en", slow=False)
	voice.save("voicelines/voice2.mp3")
	voice=gTTS(text="That's working.", lang="en", slow=False)
	voice.save("voicelines/voice3.mp3")
	voice=gTTS(text="Didn't work. This program is kind of useless if you don't have internet, cunt.", lang="en", slow=False)
	voice.save("voicelines/voice4.mp3")
	print("alright i got it out")
	playsound("voicelines/voice2.mp3", block=True)
	response = os.system(f"ping -c 1 8.8.8.8")
	print(response)
	if response == 0:
		os.system("speedtest-cli --secure")
		print("pee")
		playsound("voicelines/voice3.mp3", block=False)
	else:
		playsound("voicelines/voice4.mp3")
