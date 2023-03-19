from flask import Blueprint, request

from core.utils import json_response
from models.general import Company, db

companies_bp = Blueprint(name='companies_bp', import_name=__name__)

@companies_bp.route('/', methods=['GET', 'POST'])
def companies():
    if request.method == 'POST':
        company = Company(
            title=request.json.get('title'),
            description=request.json.get('description')
        )

        db.session.add(company)
        db.session.commit()

        return json_response(company, status_code=201)

    companies_list = db.session.query(Company).all()

    return json_response(companies_list)

@companies_bp.route('/<int:company_id>', methods=['GET', 'PUT', 'DELETE'])
def company_detail(company_id):
    company = db.session.query(Company).get(company_id)

    if request.method == 'PUT':
        company.title = request.json.get('title')
        company.description = request.json.get('description')

        db.session.add(company)
        db.session.commit()

        return json_response(data=company)

    elif request.method == 'DELETE':
        db.session.delete(company)
        db.session.commit()

        return json_response(data={'message': 'deleted'})

    return json_response(data=company)


