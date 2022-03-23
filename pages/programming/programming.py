from flask import Blueprint, render_template
import os

programming = Blueprint('programming',__name__,static_folder='../.././.././static',template_folder='../.././.././templates')

@programming.route("/")
def programming_page():
    return render_template('programming.html')

