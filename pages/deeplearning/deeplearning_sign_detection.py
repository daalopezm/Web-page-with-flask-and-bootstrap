from flask import Blueprint, url_for, render_template

deeplearning_sign_detection = Blueprint('deeplearning_sign_detection', __name__)
@deeplearning_sign_detection.route('/')
def deeplearning_sign_detection_page():
    pages = {'Simple Neural Network': 'blog.deeplearning.deeplearning_simple_neural_network.deeplearning_simple_neural_network_page',
            'Sign detection': 'blog.deeplearning.deeplearning_sign_detection.deeplearning_sign_detection_page'}
    return render_template('/blog/deeplearning/deeplearning-sign-detection.html', pages=pages)