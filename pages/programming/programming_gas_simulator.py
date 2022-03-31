from flask import Blueprint, url_for, render_template

programming_gas_simulator = Blueprint('programming_gas_simulator', __name__)
@programming_gas_simulator.route('/')
def programming_gas_simulator_page():
    videos_programming = {'video_programming_gases': url_for('static', filename='videos/programming/Gases.mp4')}
    images_programming = {'image_programming_gas_explanation_1': url_for('static', filename='videos/programming/gas_explanation/field.png')}
    return render_template('/blog/programming/programming-gas-simulator.html',**videos_programming, **images_programming)