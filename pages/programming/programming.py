from fileinput import filename
from flask import Blueprint, render_template,url_for
import os

programming = Blueprint('programming',__name__,static_folder='../.././.././static',template_folder='../.././.././templates')

@programming.route("/")
def programming_page():
    videos_programming = {'video_programming_gases': url_for('static', filename='videos/programming/Gases.mp4')}
    images_programming = {'image_programming_website': url_for('static', filename='videos/programming/website.png'),
    'image_programming_gas_explanation_1': url_for('static', filename='videos/programming/gas_explanation/field.png')}
    return render_template('programming.html',**videos_programming, **images_programming)

