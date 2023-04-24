from application import app
from flask import jsonify


@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify({
        'success': True,
        'data': 'Get all users'
    })


@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    return jsonify({
        'success': True,
        'data': f'Get single user with id {user_id}'
    })


@app.route('/api/v1/users', methods=['POST'])
def create_user():
    return jsonify({
        'success': True,
        'data': 'New user has beed created'
    }), 201


@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    return jsonify({
        'success': True,
        'data': f'User with id {user_id} has been updated'
    })


@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    return jsonify({
        'success': True,
        'data': f'User with id {user_id} has been deleted'
    })
