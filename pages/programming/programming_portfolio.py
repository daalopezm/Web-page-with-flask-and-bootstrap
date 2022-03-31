from flask import Blueprint, url_for, render_template

programming_portfolio = Blueprint('programming_portfolio', __name__)
@programming_portfolio.route("/")
def programming_portfolio_page():
    images_programming = {'image_programming_website': url_for('static', filename='videos/programming/website.png')}
    return render_template('/blog/programming/programming-portfolio.html', **images_programming)