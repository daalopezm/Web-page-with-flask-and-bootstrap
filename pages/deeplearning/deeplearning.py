from flask import Blueprint, render_template, url_for

deeplearning = Blueprint('deeplearning',__name__,static_folder='../.././.././static',template_folder='../.././.././templates')

@deeplearning.route('/')
def deeplearning_page():
    videos_deeplearning = {'video_dl_simpleNN': url_for('static', filename='videos/deeplearning/neuralnetwork.mp4')}
    return render_template('deeplearning.html', **videos_deeplearning)