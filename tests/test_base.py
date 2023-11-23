import pytest
from app import app
#db


@pytest.fixture
def app():
    """
    Fixture to set up the Flask app for testing.
    """
    app = create_app(testing=True)
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """
    Fixture to create a test client for the Flask app.
    """
    return app.test_client()


@pytest.fixture
def runner(app):
    """
    Fixture to create a test runner for the Flask app.
    """
    return app.test_cli_runner()
