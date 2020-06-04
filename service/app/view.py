from datetime import datetime, timedelta

from app import app
from app import db, user_datastore, security, maps

from flask import render_template, request, redirect, url_for, flash
from flask_security import login_required, current_user, SQLAlchemySessionUserDatastore, utils, url_for_security

from flask_googlemaps import Map

from app.email import send_password_reset_email, send_register_email
from app.models import Post, Tag, User, Service, Order, db_commit, order_service
from .forms import NewsForm, TagForm, RegistrationForm, OrderForm, ResetPasswordRequestForm, ResetPasswordForm


@app.route('/') # індексна сторінка
@app.route('/index')
def index():
    return render_template('index.html')

# http://localhost/register
# сторінка генерації реєстрації користувача
@app.route('/register', methods=['GET', 'POST'])  
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        username = request.form['username']
        password = utils.encrypt_password(request.form['password'])
        active = True
        user_datastore.create_user(name=name, email=email, phone=phone, username=username, password=password, active=active)
        db.session.commit()
        flash('Вітаємо! Ви зареєстровані!')
                
        return redirect(url_for('security.login'))
    
    name_form = 'user'
    title = 'Реєстрація користувача'
    form = RegistrationForm()    

    return render_template('create_form.html', form=form, form_type=name_form, title=title)

# http://localhost/create/order
# сторінка запису на СТО
@app.route('/create_order', methods=['GET', 'POST'])  
def create_order():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            if User.query.filter_by(email=request.form['email']).first():
                flash('Ви реєструвались у нас раніше!!!')
            else:
                name = request.form['name']
                email = request.form['email']
                phone = request.form['phone']
                username = request.form['email']
                password = utils.encrypt_password('123456')
                active = True
                user_datastore.create_user(name=name, email=email, phone=phone, username=username, password=password, active=active)
                db.session.commit()
                flash('Вітаємо! Ви зареєстровані! Ваш пароль 123456')

            user = User.query.filter_by(email=request.form['email']).first()
            user_id = user.id

            send_register_email(user)
        else:
            user_id = current_user.get_id()
        
        print(user_id)

        name_auto = request.form['name_auto']
        vin = request.form['vin']
        timefrom = datetime.strptime(request.form['timefrom'], '%d/%m/%Y')
        timeto = datetime.strptime(request.form['timefrom'], '%d/%m/%Y') + timedelta(days=1)
        comment = request.form['comment']

        order = Order(user_id=user_id, name_auto=name_auto, vin=vin, timefrom=timefrom, timeto=timeto, comment=comment)
        
        service = Service.query.filter_by(id=request.form['service']).first()
        
        order.services.append(service)
        db_commit(data=order)

        return redirect(url_for_security('login'))
    
    date_ordered = []
    orders = Order.query.all()
    for item in orders:
        date_ordered.append(item.timefrom.strftime('%d/%m/%Y'))
        date_ordered.append(item.timeto.strftime('%d/%m/%Y'))
        # print(item.timefrom.strftime("%d"))
    
    print(date_ordered)

    service_list = Service.query.order_by(Service.id)

    form = OrderForm(current_user, service_list)
    title = 'Записатись на СТО'

    return render_template('create_form.html', form=form, form_type='order', 
                            title=title, date_ordered=date_ordered)

# http://localhost/create/<form-name> 
# сторінка генерації форм відповідно моделей у forms.py
@app.route('/create/<name_form>', methods=['GET', 'POST'])  
@login_required
def create_form(name_form):
    if request.method == 'POST':
        if name_form == 'post':
            title = request.form['title']
            body = request.form['body']

            post = Post(title=title, body=body)
            db_commit(data=post)

        elif name_form == 'tag':
            name = request.form['name']
            
            tag = Tag(name=name)
            db_commit(data=tag)
        
        return redirect(url_for('news'))

    if name_form == 'news':
        form = NewsForm()
        title = 'Створити новину'
    elif name_form == 'tag':
        form = TagForm()
        title = 'Створити tag'
    else:
        return redirect(url_for('news'))

    return render_template('create_form.html', form=form, form_type=name_form, title=title)

# http://localhost/post/<Post slug>
@app.route('/post/<slug>') # сторінка поста
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    tags = post.tags
    return render_template('post_detail.html', post=post, tags=tags)

# http://localhost/tag/<Tag slug>
@app.route('/tag/<slug>') # Сторінка новин за тагом
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    for i in tag.posts:
        print(i)
    posts = tag.posts
    return render_template('tag_detail.html', posts=posts, tag=tag)

@app.route('/news') # сторінка новин
def news():
    # фільтруємо новини за пошуком
    search = request.args.get('search')

    if search:
        posts = Post.query.filter(Post.title.contains(search) | Post.body.contains(search))

    else:
        posts = Post.query.order_by(Post.created.desc())

    # пагінація сторінок новин
    page = request.args.get('page')
    
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    pages = posts.paginate(page=page, per_page=6)

    return render_template('news.html', posts=posts, pages=pages, search=search)

@app.route('/price') # сторінка новин
def price():
    
    price = Service.query.order_by(Service.id)
    print(price)

    # пагінація сторінок новин
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    pages = price.paginate(page=page, per_page=10)
    
    return render_template('price.html', price=price, pages=pages)

@app.route("/contacts")
def contacts():
    # задаємо координати для карти
    mymap = Map(
        identifier="iService",
        lat=49.4090433,
        lng=27.0124982,
        markers=[(49.4090433, 27.0124982)]
    )

    return render_template('contacts.html', mymap=mymap)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user:
            send_password_reset_email(user)
        flash('Перевірте Ваш email з інструкціями як змінити пароль')
        return redirect(url_for_security('login'))

    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if request.method == 'POST':
        user.set_password(request.form['email'])
        db.session.commit()
        flash('Ваш пароль змінено.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', 
                            title='Enter New Password', form=form)

