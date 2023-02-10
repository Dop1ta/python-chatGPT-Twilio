import os

import flask
from flask import send_from_directory, request

import openai

# Define OpenAI API key 

app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"

from helperfunction.waSendMessage import sendMessage


@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp():
    print(request.get_data())
    message = request.form['Body']
    senderId = request.form['From'].split('+')[1]

    openai.api_key = "api_key"
    
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = message,
        temperature = 0.6,
        max_tokens = 150
    )

    twr = response.choices[0].text
   

    res = sendMessage(senderId,twr)
    print(f'This is the response --> {res}')
    return '200'

if __name__ == "__main__":
    app.run(port=5000, debug=True)
