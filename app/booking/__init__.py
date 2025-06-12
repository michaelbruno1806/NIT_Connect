from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.main.routes import main
    from app.booking.routes import booking

    app.register_blueprint(main)
    app.register_blueprint(booking)

    return app