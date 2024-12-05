import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# DBファイル作成
base_dir = os.path(__file__)
database = 'sqlite://' + os.path.join(base_dir, 'data.sqlite')

# データベースに接続するためのデータベースエンジンの作成(echo=Trueで実行するSQLをターミナルに表示
db_engine = create_engine(database, echo=True)
# データを表現するモデルクラスの作成
Base = declarative_base()

class Department(Base):
  # テーブル名
  __tablename__ = 'departments'

  # 部署ID
  id = Column(Integer, primary_key=True, autoincrement=True)
  # 部署名
  name = Column(String, nullable=False, unique=True)

  # リレーション（１対多）
  employees = relationship("Employee", back_populates = "department")

  def __str__(self):
    return f"部署ID:{self.id}, 部署名:{self.name}"
  
class Employee(Base):
  # テーブル名
  __tablename__ = 'employees'

  # 従業員ID
  id = Column(Integer, primary_key=True, autoincrement=True)
  # 従業員名
  name = Column(String, nullable=True)
  # 外部キー
  department_id = Column(Integer, ForeignKey('departments.id'))

  # リレーション(1:1)
  department = relationship('Department', back_populates='employee', uselist=False)

  def __str__(self):
    return f"従業員ID:{self.id}, 従業員:{self.name}"
  
print('テーブル作成')
Base.metadata.drop_all(db_engine)
Base.metadata.create_all(db_engine)

# セッション生成
session_maker = sessionmaker(bind=db_engine)
session = session_maker()
  
# データ作成
print('データ登録')
dept01 = Department(name='開発部')
dept02 = Department(name='営業部')

emp01 = Employee(name='せい')
emp02 = Employee(name='じろう')
emp03 = Employee(name='さぶろう')
emp04 = Employee(name='花子')

# 部署に従業員を紐づける
dept01.employees.append(emp01)
dept01.employees.append(emp02)
dept02.employees.append(emp03)
dept02.employees.append(emp04)

session.add_all([dept01,dept02])
session.commit()

print('データ参照')
print('Employeeの参照')
target_emp = session.query(Employee).filter_by(id=1).first()
print(target_emp)
print('Employeeに紐づいたDepartmentの参照')
print(target_emp.department)

print('データ参照')
print('Departmentの参照')
target_dept = session.query(Department).filter_by(id=1).first()
print(target_dept)
print('Departmentに紐づいたEmployeeの参照')

for emp in target_dept.employees:
  print(emp)