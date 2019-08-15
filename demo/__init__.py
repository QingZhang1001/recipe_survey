from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from demo.config import Config
import psycopg2


bootstrap=Bootstrap()
db=SQLAlchemy()
migrate=Migrate(db)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from demo.start.routes import start
    from demo.question.routes import question
    from demo.token.routes import token
    app.register_blueprint(start)
    app.register_blueprint(question)
    app.register_blueprint(token)

    return app