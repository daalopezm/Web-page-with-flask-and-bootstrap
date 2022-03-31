from flask import Blueprint, url_for, render_template

# class deeplearning_simple_neural_network:
#     def __init__(self, pages):
#         self.pages = pages

#     def 
deeplearning_simple_neural_network = Blueprint('deeplearning_simple_neural_network', __name__)
@deeplearning_simple_neural_network.route('/')
def deeplearning_simple_neural_network_page():
    videos_deeplearning = {'video_dl_simpleNN_0': url_for('static', filename='videos/deeplearning/neuralnetwork0.mp4'),
    'video_dl_simpleNN_1': url_for('static', filename='videos/deeplearning/neuralnetwork1.mp4')}
    pages = {'Simple Neural Network': 'blog.deeplearning.deeplearning_simple_neural_network.deeplearning_simple_neural_network_page',
            'Sign detection': 'blog.deeplearning.deeplearning_sign_detection.deeplearning_sign_detection_page'}
    return render_template('/blog/deeplearning/deeplearning-simple-neural-network.html',pages=pages,**videos_deeplearning)