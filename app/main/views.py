from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Blog
from .forms import UpdateProfile,BlogForm
from .. import db,photos




@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    blogs = Blog.get_all_blogs()
    title = 'Personal blog posts'

    return render_template('index.html', title = title, blogs = blogs)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>',methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort (404)

    form = UpdateProfile()

    if form.validate_on_submite():
        user.bio = form.bio.data 
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username))
    return render_template('profile/update.html',form = form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
@main.route('/blogs/new/',methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data
        user_id = current_user
        print(current_user._get_current_object().id)
        new_blog = Blog(user_id=current_user._get_current_object().id, title=title,blog=blog)
        db.session.add(new_blog)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('blogs.html',form=form,)

@main.route('/blog/comment/new/<int:blog_id>', method = ['GET','POST'])


    


