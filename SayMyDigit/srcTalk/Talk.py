from flask import Flask, request, send_file, Response
from gtts import gTTS
import os
import io

app = Flask(__name__)

@app.route("/talk", methods=['POST'])
def talk():
	digit=request.form['digit']
	language=request.form['language']
	myobj = gTTS(text=digit, lang=language, slow=False)
	myobj.save("/app/talk.mp3")
	#mp3_file="talk.mp3"
	mp3_buffer = io.BytesIO()
	myobj.write_to_fp(mp3_buffer)
	
	return Response(mp3_buffer.getvalue(), content_type="audio/mpeg")