from flask import Flask, render_template, redirect, url_for
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://store.192.9.134.29.nip.io/sm/stocklevel", auth=HTTPBasicAuth('jack', 'password'),
                            verify=False)
    if response.status_code == 200:
        #Success
        return render_template('home.html', products=response.json())
    else:
        #Problem connecting with API
        return render_template('home.html', products=None)

@app.route('/shop')
def shop():
    response = requests.get("https://store.192.9.134.29.nip.io/sm/stocklevel", auth=HTTPBasicAuth('jack', 'password'),
                            verify=False)
    if response.status_code == 200:
        #Success
        return render_template('shop.html', products=response.json())
    else:
        #Problem connecting with API
        return render_template('shop.html', products=None)

@app.route('/shop/<name>')
def product_details(name):
    response = requests.get("https://store.192.9.134.29.nip.io/sm/stocklevel/" + name, auth=HTTPBasicAuth('jack', 'password'),
                            verify=False)
    if response.status_code == 200:
        #Success
        return render_template('detail.html', product=response.json())
    else:
        #Problem connecting with API
        return render_template('detail.html', product=None)

@app.route('/buy/<name>')
def buy_product(name):
    myobj = {"requestedItem": name,"requestedCount":2}
    response = requests.post("https://store.192.9.134.29.nip.io/sf/store/reserveStock/", json = myobj, auth=HTTPBasicAuth('jack', 'password'),
                            verify=False)
    if response.status_code == 200:
        #Success
        return redirect(url_for('product_details', name=name))
    else:
        #Problem connecting with API
        return redirect(url_for('product_details', name=name))

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)