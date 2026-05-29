from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET', 'dev')

OWA_USER = os.environ.get('OWA_USERNAME')
OWA_PASS = os.environ.get('OWA_PASSWORD')

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/owa/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=os.environ.get('DEBUG') == 'true')
