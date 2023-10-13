from flask import Flask, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/talk", methods=['POST'])
def talk():
	digit=request.form['digit']
	language=request.form['language']
	myobj = gTTS(text=digit, lang=language, slow=False)
	myobj.save("C:\\temp\\talk.mp3")
	mp3_file="C:\\temp\\talk.mp3"
	return send_file(mp3_file,as_attachment=True)