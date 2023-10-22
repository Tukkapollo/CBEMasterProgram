from flask import Flask, request
from gtts import gTTS
import os
import subprocess
#import vlc

app = Flask(__name__)

#@app.route("/talk", methods=['POST'])
#def talk():
digit="hello"
language="en"
myobj = gTTS(text=digit, lang=language, slow=False)
myobj.save("C:\\Users\\Tero\\talk.mp3")

comand = '"C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe" --play-and-exit --no-video-deco --no-embedded-video -f --one-instance --no-playlist-enqueue  C:\\Users\\Tero\\talk.mp3'
subprocess.run(comand, shell=True)
	#return {'return':'done here!'}