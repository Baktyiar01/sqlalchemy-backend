from flask import Blueprint, request

from core.utils import json_response
from models.general import Position, db

positions_bp = Blueprint(name='positions_bp', import_name=__name__)


@positions_bp.route('/', methods=['GET', 'POST'])
def positions():

    if request.method == 'POST':
        position = Position(
            title=request.json.get('title'),
            description=request.json.get('description'),
        )

        db.session.add(position)
        db.session.commit()

        return json_response(position, status_code=201)

    positions_list = db.session.query(Position).all()

    return json_response(positions_list)


@positions_bp.route('/<int:position_id>', methods=['GET', 'PUT', 'DELETE'])
def position_detail(position_id):
    position = db.session.query(Position).get(position_id)

    if request.method == 'PUT':
        position.title = request.json.get('title')
        position.description = request.json.get('description')

        db.session.add(position)
        db.session.commit()

        return json_response(data=position)
    elif request.method == 'DELETE':
        db.session.delete(position)
        db.session.commit()

        return json_response(data={'message': 'deleted'})

    return json_response(data=position)