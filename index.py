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

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(about, url_prefix='/about')
app.register_blueprint(programming, url_prefix='/programming')
app.register_blueprint(blog, url_prefix='/blog')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
