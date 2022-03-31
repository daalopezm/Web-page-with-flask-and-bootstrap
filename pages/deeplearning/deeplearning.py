from flask import Blueprint, render_template, url_for

from .deeplearning_simple_neural_network import deeplearning_simple_neural_network
from .deeplearning_sign_detection import deeplearning_sign_detection

deeplearning = Blueprint('deeplearning',__name__,static_folder='../.././.././static',template_folder='../.././.././templates')
deeplearning.register_blueprint(deeplearning_simple_neural_network, url_prefix='/simple_neural_network')
deeplearning.register_blueprint(deeplearning_sign_detection, url_prefix='/sign_detection')

@deeplearning.route('/')
def deeplearning_page():
    return render_template('deeplearning.html')