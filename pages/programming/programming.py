from flask import Blueprint, render_template

from .programming_gas_simulator import programming_gas_simulator
from .programming_portfolio import programming_portfolio

programming = Blueprint('programming',__name__,static_folder='../.././.././static',template_folder='../.././.././templates')
programming.register_blueprint(programming_gas_simulator, url_prefix='/gas_simulator')
programming.register_blueprint(programming_portfolio, url_prefix='/portfolio')

@programming.route("/")
def programming_page():
    return render_template('programming.html')

