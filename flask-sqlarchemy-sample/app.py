import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 乱数を設定
app.config['SECRET_KEY'] = os.urandom(24)
base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLARCHEMY_DATABASE_URI'] = database
app.config['SQLARCHEMY_TRACK_MODIFICATIONS'] = False

# 変数dbを通してSQLAlchemyを操作
db = SQLAlchemy(app)

class Task(db.Model):
  __tablename__ = 'tasks'

  id = db.Column(db.Integer, primary_key=True, autoincement=True)
  content = db.Column(db.String(200), nullable=False)

  # 表示用
  def __str__(self):
    return f'課題ID:{self.id} 内容:{self.content}'
  
# DB作成
def init_db():
  with app.app_context():
    print('テーブル作成')
    db.drop_all()
    db.create_all()

    # データ作成
    print('データ作成')
    task01 = Task(content='風呂掃除')
    task02 = Task(content='選択')
    task03 = Task(content='買い物')
    db.session.add_all([task01, task02, task03])
    db.session.commit()

# CRUD操作
def insert():
  with app.app_context():
    print('１件登録')
    task04 = Task(content='請求書作成')
    db.session.add(task04)
    db.session.commit()
    print('登録 =>', task04)

# 参照（全体）
def select_all():
  print('全権取得')
  with app.app_context():
    tasks = Task.quersy.all()
    for task in tasks:
      print(task)

  