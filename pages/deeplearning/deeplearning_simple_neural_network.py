from flask import Blueprint, url_for, render_template

deeplearning_simple_neural_network = Blueprint('deeplearning_simple_neural_network', __name__)
@deeplearning_simple_neural_network.route('/')
def deeplearning_simple_neural_network_page():
    videos_deeplearning = {'video_dl_simpleNN_0': url_for('static', filename='videos/deeplearning/neuralnetwork0.mp4'),
    'video_dl_simpleNN_1': url_for('static', filename='videos/deeplearning/neuralnetwork1.mp4')}
    return render_template('/blog/deeplearning/deeplearning-simple-neural-network.html',**videos_deeplearning)