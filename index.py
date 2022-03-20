from email.mime import image
from fileinput import filename
from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    images = {f'image{num}': url_for('static',filename='images/{}'.format(os.listdir('./static/images/')[num])) for num in range(9)}
    return render_template('index.html', **images)

@app.route('/about')
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)