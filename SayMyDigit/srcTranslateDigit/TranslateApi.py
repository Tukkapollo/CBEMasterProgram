from flask import Flask, request, Response
from googletrans import Translator
import json
import requests

app = Flask(__name__)

@app.route("/translate", methods=['POST'])
def hello():
	digit=request.form['digit']
	language=request.form['language']
	result= Translate(digit,language)
	returnable=""
	url = "http://talk-service:80/talk"
	form_data = {
    "digit": result,
    "language": language
	}
	response = requests.post(url, data=form_data)
	
	
	return Response(response.content, content_type="audio/mpeg")
	
def Translate(digit,language):
	translator = Translator()
	return translator.translate(digit, src='en', dest=language).text