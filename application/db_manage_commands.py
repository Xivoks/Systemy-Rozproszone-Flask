import json
from pathlib import Path
from application import app, db
from application.models import Users


@app.cli.group()
def db_manage():
    """ Database management commands """
    pass


@db_manage.command()
def add_data():
    """Add sample data to database """
    try:
        users_path = Path(__file__).parent / 'samples' / 'users.json'
        with open(users_path) as file:
            data_json = json.load(file)
        for item in data_json:
            user = Users(**item)
            db.session.add(user)
        db.session.commit()
        print("Data has been successfully added to database")
    except Exception as exc:
        print("Unexpected error: {}".format(exc))


@db_manage.command()
def remove_data():
    """Remove all data from database """
    try:
        db.session.execute('TRUNCATE TABLE users')
        db.session.commit()
        print("Data has been successfully removed from database")
    except Exception as exc:
        print("Unexpected error: {}".format(exc))
