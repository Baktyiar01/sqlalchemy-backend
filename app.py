from flask import request

from models.general import db, User, Position, UserPosition, Company
from core.utils import create_app, init_app, json_response
from api.users import users_bp
from api.positions import positions_bp
from api.companies import companies_bp

app = create_app()
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(positions_bp, url_prefix='/positions')
app.register_blueprint(companies_bp, url_prefix='/companies')
init_app(app)


if __name__ == '__main__':
    app.run(host='localhost', port=8000)