"""
To deploy again, use:
        heroku git:remote infinite-thicket-70020
        git push heroku master

Author: Daniel Lopez
"""

from flask import Flask, render_template
from pages.home import home
from pages.about import about
from pages.blog import blog
from pages.programming.programming import programming
from pages.deeplearning.deeplearning import deeplearning
from os import path

DB_NAME = "database.db"

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(about, url_prefix='/about')
#app.register_blueprint(programming, url_prefix='/programming')
app.register_blueprint(deeplearning, url_prefix='/deeplearning')
app.register_blueprint(blog, url_prefix='/blog')

# app.config['SECRET_KEY'] = 'nani21'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

@app.errorhandler(404)
@app.errorhandler(405)
def not_found(error):
    return render_template('404.html', error=error)

# def create_database(app):
#     if not path.exists(DB_NAME):
#         db.create_all(app=app)
#         print("Created database!")

if __name__ == '__main__':
    app.run(debug=True)
    # create_database(app)
