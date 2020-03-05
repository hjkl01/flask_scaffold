import hashlib
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash

from app import db


class User(db.Model):
    __tablename__ = 'project_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    _password = db.Column("password", db.String, nullable=False)
    code = db.Column(db.String, nullable=True)
    superuser = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return self.username

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        """Store the password as a hash for security."""
        self._password = generate_password_hash(value)

    def check_password(self, value):
        return self.password == value

    def check_code(self, value):
        return self.code == value

    # md5
    def save(self, _dict):
        u = User(username=_dict.get('username'),
                 _password=hashlib.md5(
                     _dict.get('password').encode()).hexdigest(),
                 superuser=_dict.get('superuser', False))
        db.session.add(u)
        db.session.commit()
        print('user save success %s' % _dict.get('username'))
