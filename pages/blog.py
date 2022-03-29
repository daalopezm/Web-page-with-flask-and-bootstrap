from fileinput import filename
from flask import Blueprint, render_template, url_for


blog = Blueprint('blog',__name__)


@blog.route('/')
def blog_page():
    images = {'image1': url_for('static', filename='images/Blog/image1.jpg')}
    return render_template('blog.html', **images)