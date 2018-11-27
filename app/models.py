from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime 


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    blogs = db.relationship('Blog',backref = 'user',lazy = "dynamic")
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    comments = db.relationship('Comment',backref = 'user',lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'



class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    blog = db.Column(db.String)
    comments = db.relationship('Comment',backref = 'blog',lazy = 'dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_of_blog = db.Column(db.DateTime,default=datetime.utcnow)

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_blogs(cls):
        '''
        Function that queries the database and returns all the blogs
        '''

        return Blog.query.all()

    @classmethod
    def get_blogs(cls,id):
        blogs = Blog.query.order_by(blog_id = id).desc.all()
        return blogs
        

    


    def __repr__(self):
        return f'Blog {self.blog}'

class Comment(db.Model):
    all_comments = []
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comments(self):
        db.session.add(self)
        db.session.commit()
    def __repe__(self):
        return f"Comment : id {self.id} comment : {self.description}"



