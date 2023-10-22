import inflect
from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route("/numberToString", methods=['POST'])
def hello():
	input=request.form['digit']
	language=request.form['language']
	result= NumberToString(input)
	returnable=""
	
	url = "http://translatedigit-service:80/translate"
	form_data = {
    "digit": result,
    "language": language
	}
	
	response = requests.post(url, data=form_data)
	if response.status_code == 200:
		returnable=response.text
		print(response.text)
	else:
		returnable="error in talk"
	return Response(response.content, content_type="audio/mpeg")
	
def NumberToString(digit):
	p = inflect.engine()
	written_form = p.number_to_words(digit)
	return written_form