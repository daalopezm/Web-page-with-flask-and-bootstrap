from flask import Blueprint, url_for, render_template

deeplearning_sign_detection = Blueprint('deeplearning_sign_detection', __name__)
@deeplearning_sign_detection.route('/')
def deeplearning_sign_detection_page():
    return render_template('/blog/deeplearning/deeplearning-sign-detection.html')