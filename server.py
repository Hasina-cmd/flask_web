from flask import Flask, render_template

web_app = Flask(__name__)

@web_app.route('/')
def index():
    return render_template('home.html')

@web_app.route('/home')
def home():
    return render_template('home.html')

web_app.run(host="0.0.0.0", port=5000, debug=True)