from fileinput import filename
from flask import Blueprint, render_template, url_for
import os

home = Blueprint('home', __name__)


@home.route("/home")
@home.route("/")
def home_page():
    videos = {'video0': url_for('static', filename='videos/write.mp4'),
              'video1': url_for('static', filename='videos/code.mp4'),
              'video2': url_for('static', filename='videos/blackhole.mp4'),
              'video3': url_for('static', filename='videos/physics.mp4')}
    videos_programming = {'video_programming_gases': url_for('static', filename='videos/programming/Gases.mp4')}
    images = {f'image{num}': url_for('static', filename='images/{}'.format(
        os.listdir('./static/images/')[num])) for num in range(9)}
    return render_template('index.html', **images, **videos, **videos_programming)
