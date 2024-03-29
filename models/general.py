from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    description = db.Column(db.String(512))

    def __init__(self, title, description):
        self.title = title
        self.description = description


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    description = db.Column(db.String(512))
    company_id = db.Column(db.Integer, db.ForeignKey(Company.id))

    def __init__(self, title, description):
        self.title = title
        self.description = description


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True)
    department_id = db.Column(db.Integer, db.ForeignKey(Department.id))

    def __init__(self, pname, email, phone):
        self.name = pname
        self.email = email
        self.phone = phone

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.email}'


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(512))

    def __init__(self, title, description):
        self.title = title
        self.description = description


class UserPosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    position_id = db.Column(db.Integer, db.ForeignKey(Position.id))

    def __init__(self, user_id, position_id):
        self.user_id = user_id
        self.position_id = position_id