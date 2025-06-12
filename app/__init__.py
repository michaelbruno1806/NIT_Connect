from flask import Flask
import os

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'templates'),
        static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static')
    )

    from app.main.routes import main
    from app.booking.routes import booking

    app.register_blueprint(main)
    app.register_blueprint(booking)

    return app
