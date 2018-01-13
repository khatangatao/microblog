from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
# создаем объект db для предствления БД
db = SQLAlchemy(app)
# создаем объект migrate для представления механизма миграции БД
migrate = Migrate(app, db)

from app import routes, models
