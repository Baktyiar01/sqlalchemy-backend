import xlsxwriter
from flask import Blueprint, request

from core.settings import EXCEL_FILE_DIRECTORY
from core.utils import json_response
from models.general import User, db

users_bp = Blueprint(name='users_bp', import_name=__name__)


@users_bp.route('/', methods=['GET', 'POST'])
def users():

    if request.method == 'POST':
        user = User(
            pname=request.json.get('name'),
            email=request.json.get('email'),
            phone=request.json.get('phone'),
        )

        db.session.add(user)
        db.session.commit()

        return json_response(data=user, status_code=201)

    users_list = db.session.query(User).all()

    return json_response(data=users_list)


@users_bp.route('/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(user_id):
    user = db.session.query(User).get(user_id)

    if request.method == 'PUT':
        user.name = request.json.get('name')
        user.email = request.json.get('email')
        user.phone = request.json.get('phone')

        db.session.add(user)
        db.session.commit()

        return json_response(data=user)

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()

        return json_response(data={'message': 'deleted'})

    return json_response(data=user)


@users_bp.route('/excel-file', methods=['POST'])
def create_user_excel_file():
    users = db.session.query(User).all()

    workbook = xlsxwriter.Workbook(f'{EXCEL_FILE_DIRECTORY}/db_data.xlsx')
    worksheet_users = workbook.add_worksheet('Список людей')
    head_column_styles = workbook.add_format({'align': 'center', 'bold': True})

    worksheet_users.write(0, 0, 'ID', head_column_styles)
    worksheet_users.write(0, 1, 'Имя', head_column_styles)
    worksheet_users.write(0, 2, 'Почта', head_column_styles)
    worksheet_users.write(0, 3, 'Номер телефона', head_column_styles)
    last_row = 0

    for i, user in enumerate(users, start=1):
        worksheet_users.write(i, 0, user.id)
        worksheet_users.write(i, 1, user.name)
        worksheet_users.write(i, 2, user.email)
        worksheet_users.write(i, 3, user.phone)
        last_row = i

    worksheet_users.write(last_row+2, 0, len(users))

    workbook.close()

    data = {'code': 0, 'message': 'Файл создан!'}

    return json_response(data=data, status_code=201)