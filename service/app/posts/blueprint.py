from flask import Blueprint, render_template

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def index():
    try: 
        return render_template('posts/index.html')
    except TemplateNotFound:
        abort(404)