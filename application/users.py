from application import app, db
from flask import jsonify, request, render_template, redirect, url_for, flash
from application.models import Users, UserSchema, user_schema
from webargs.flaskparser import use_args
from application.utils import validate_json_content_type


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/v1/users', methods=['GET'])
def get_users_html():
    users = Users.query.all()
    user_schema = UserSchema(many=True)
    return render_template('get_users.html', users=users, number_of_records=len(users))


@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    user = Users.query.get_or_404(user_id, description=f'User with id {user_id} not found')
    return render_template('get_user.html', user=user)


@app.route('/create_user', methods=['GET'])
def show_create_user_form():
    return render_template('create_user.html')


@app.route('/api/v1/users', methods=['POST'])
def create_user():
    args = request.form
    user = Users(**args)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('get_users_html'))


@app.route('/edit_user/<int:user_id>', methods=['GET'])
def edit_user(user_id: int):
    user = Users.query.get_or_404(user_id, description=f'User with id {user_id} not found')
    return render_template('update_user.html', user=user)


@app.route('/api/v1/users/<int:user_id>', methods=['POST'])
def update_user(user_id: int):
    user = Users.query.get_or_404(user_id, description=f'User with id {user_id} not found')

    user.name = request.form['name']
    user.age = int(request.form['age'])
    user.email = request.form['email']

    db.session.commit()

    return redirect(url_for('get_users_html'))


@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def confirm_delete_user(user_id: int):
    user = Users.query.get_or_404(user_id, description=f'User with id {user_id} not found')
    if request.method == 'POST':
        db.session.delete(user)
        db.session.commit()
        flash(f'User with id {user_id} has been deleted', 'success')
        return redirect(url_for('get_all_users'))

    return render_template('delete_user.html', user=user)


@app.route('/api/v1/users_delete/<int:user_id>', methods=['POST'])
def delete_user(user_id: int):
    print("test")
    user = Users.query.get_or_404(user_id, description=f'User with id {user_id} not found')
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('get_users_html'))
