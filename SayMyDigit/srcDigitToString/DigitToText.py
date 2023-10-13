import inflect
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/numberToString", methods=['POST'])
def hello():
	input=request.form['digit']
	language=request.form['language']
	result= NumberToString(input)
	
	url = "http://translatedigit-service:8080/translate"
	form_data = {
    "digit": result,
    "language": language
	}
	
	response = requests.post(url, data=form_data)
	
	#return {"result": response}
	
def NumberToString(digit):
	p = inflect.engine()
	written_form = p.number_to_words(digit)
	return written_form