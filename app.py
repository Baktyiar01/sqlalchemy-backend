from flask import request


from models.general import db, User, Position, UserPosition, Company
from core.utils import create_app, init_app, json_response
from api.users import users_bp
from api.positions import positions_bp

app = create_app()
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(positions_bp, url_prefix='/positions')
init_app(app)


@app.route('/companies', methods=['GET', 'POST', 'DELETE', 'PUT'])
def companies():
    if request.method == 'POST':
        company = Company(
            title=request.json.get('title'),
            description=request.json.get('description')
        )

        db.session.add(company)
        db.session.commit()

        data = {'code': 0, 'message': 'Успешно создан!'}

        return json_response(data, status_code=201)

    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'GET':
        pass
    else:
        pass


if __name__ == '__main__':
    app.run(host='localhost', port=8000)