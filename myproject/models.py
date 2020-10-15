from myproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    # authIP = db.Column(db.Text(),nullable=True)
    # authenticatedips = db.relationship('AuthenticatedIP', backref='User', lazy=True)
    #

    def __init__(self,username,password):
        self.username = username
        self.password_hash = password

    def check_password(self,password):
        print("aidoufhaisudhfiuasdhfiuhsd")
        print(self.password_hash)
        print(password)
        return self.password_hash == password

#
# class AuthenticatedIP(db.Model):
#     __tablename__ = 'authenticatedIPs'
#     id = db.Column(db.Integer, primary_key= True)
#     authenticatedip = db.Column(db.String,unique=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#
#     def __init__(self, authenticatedip, user_id):
#         self.authenticatedip = authenticatedip
#         self.user_id = user_id

