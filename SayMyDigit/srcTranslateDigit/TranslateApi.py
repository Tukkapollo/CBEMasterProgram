from flask import Flask, request
from googletrans import Translator
import json
import requests

app = Flask(__name__)

@app.route("/translate", methods=['POST'])
def hello():
	digit=request.form['digit']
	language=request.form['language']
	result= Translate(digit,language)
	
	url = "http://talk-service:8080/talk"
	form_data = {
    "digit": result,
    "language": language
	}
	
	response = requests.post(url, data=form_data)
	
	#return {"result": response}
	
def Translate(digit,language):
	translator = Translator()
	return translator.translate(digit, src='en', dest=language).text