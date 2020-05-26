<h3> My Web Service </h3>

export FLASK_DEBUG=1
export FLASK_ENV=development

<!-- Requirements -->
pip install flask-sqlalchemy
pip install flask-sqlalchemy mysql-connector
pip install flask-admin
pip install flask-security
py -m pip install flask_migrate

<!-- DB Migration -->
py -m flask db init
py -m flask db migrate
py -m flask db upgrade

<!--  Test DB fof incert Post -->
>>> from app import db
>>> from app.models import Post, Tag
>>> p = Post(id= 3, title='Post 3', body='My post number 3')
>>> db.session.add(u)
>>> db.session.commit()

py -m flask run
