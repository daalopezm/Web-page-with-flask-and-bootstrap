from fileinput import filename
from flask import Blueprint, render_template, url_for
from .programming.programming import programming

blog = Blueprint('blog',__name__)
blog.register_blueprint(programming, url_prefix='/programming')


@blog.route('/')
def blog_page():
    images = {'image1': url_for('static', filename='images/Blog/image1.jpg')}
    return render_template('blog.html', **images)

