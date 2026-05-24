import sys
from gtts import gTTS
import datetime 

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
	speech=("Today's date is " + str(month) + " " + str(day) + ", " + str(year) + ". The time is " + str(hour) + ":" + str(minute) + str(ampm) + ". ")


def initialize():
	timeCheck()
	voice=gTTS(text=str(speech), lang="en", slow=False)
	voice.save("extscripts/voicelines/voice.mp3")
	voice=gTTS(text="Pinging the internet DNS and running speed test client. You'll see some shit on screen.", lang="en", slow=False)
	voice.save("extscripts/voicelines/voice2.mp3")
	voice=gTTS(text="Internet On.", lang="en", slow=False)
	voice.save("extscripts/voicelines/voice3.mp3")
	voice=gTTS(text="Internet Off.", lang="en", slow=False)
	voice.save("extscripts/voicelines/voice4.mp3")
