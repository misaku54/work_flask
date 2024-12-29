import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# flaskの設定
app.config['SECRET_KEY'] = os.urandom(24)
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_DATEBASE_URI'] = database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SQLAlchemyを使用できるように設定
db = SQLAlchemy(app)
# flask_migrateを使用できるように設定
Migrate(app, db)

# モデル
class Task(db.Model):
  __tablename__ = 'tasks'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  content = db.Column(db.String(200), nullable=False)

  def __str__(self):
    return f'課題ID:{self.id} 内容:{self.content}'
