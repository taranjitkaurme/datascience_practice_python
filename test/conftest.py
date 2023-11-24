import pytest
from flask import Flask
from flask_restful import Api
from src.database.database import db as db_instance
from flask_sqlalchemy import SQLAlchemy

@pytest.fixture(scope='session')
def app():
    """
    Create and configure a new app instance for each test session.
    """
    # Create a new Flask app instance for testing
    app = Flask(__name__)
    api = Api(app)

    # Configure the in-memory database URI for testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the app
    db_instance.init_app(app)

    # Create the tables (this creates all tables defined in your models)
    with app.app_context():
        db_instance.create_all()

    return app

@pytest.fixture(scope='session')
def client(app):
    """
    Create a test client for the app.
    """
    with app.test_client() as client:
        yield client

@pytest.fixture(scope='session')
def db(app):
    """
    Create a new database for each test session.
    """
    with app.app_context():
        db_instance.create_all()
        yield db_instance
        db_instance.drop_all()

@pytest.fixture
def session(app, db):
    """
    Create a new database session for each test function.
    """
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()

        options = dict(bind=connection, binds={})
        session = db.create_scoped_session(options=options)

        db.session = session

        yield session

        transaction.rollback()
        connection.close()
        session.remove()
