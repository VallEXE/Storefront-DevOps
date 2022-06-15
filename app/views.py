from app import app
from flask import render_template
import requests
from requests.auth import HTTPBasicAuth


@app.route('/')
def home():
    return "<b>There has been a change!!!! :0</b>"


@app.route('/template')
def template():
    response = requests.get("https://store.192.9.134.29.nip.io/sm/stocklevel", auth=HTTPBasicAuth('jack', 'password'),
                            verify=False)
    if response.status_code == 200:
        return render_template('index.html', request=response.json())
    else:
        return render_template('home.html', request=response.json())
