from application import app, db
from flask import jsonify, request
from application.models import Users, UserSchema, user_schema
from webargs.flaskparser import use_args
from application.utils import validate_json_content_type


@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = Users.query.all()
    user_schema = UserSchema(many=True)
    return jsonify({
        'success': True,
        'data': user_schema.dump(users),
        'number_of_records': len(users)
    })


@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    user = Users.query.get_or_404(user_id, description=f'User with id {user_id} not found')
    return jsonify({
        'success': True,
        'data': user_schema.dump(user)
    })


@app.route('/api/v1/users', methods=['POST'])
@use_args(user_schema)
@validate_json_content_type
def create_user(args: dict):
    user = Users(**args)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'success': True,
        'data': user_schema.dump(user)
    }), 201


@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
@validate_json_content_type
@use_args(user_schema, error_status_code=400)
def update_user(args: dict, user_id: int):
    user = Users.query.get_or_404(user_id, description=f'User with id {user_id} not found')
    user.name = args['name']
    user.age = args['age']
    user.email = args['email']
    db.session.commit()
    return jsonify({
        'success': True,
        'data': f'User with id {user_id} has been updated'
    })


@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    user = Users.query.get_or_404(user_id, description=f'User with id {user_id} not found')
    db.session.delete(user)
    db.session.commit()
    return jsonify({
        'success': True,
        'data': f'User with id {user_id} has been deleted'
    })
