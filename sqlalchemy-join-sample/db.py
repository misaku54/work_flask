import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base_dir = os.path.dirname(__file__)
database = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
# dbエンジン作成
db_engine = create_engine(database, echo=True) # 裏で実行するSQLをコンソールに表示する
Base = declarative_base()

class Item(Base):
  # テーブル名
  __tablename__ = 'items'

  # 商品ID
  item_id = Column(Integer, primary_key=True)
  item_name = Column(String(255), nullable=False, unique=True)
  price = Column(Integer, nullable=False)

class Shop(Base):
  __tablename__ = 'shops'

  shop_id = Column(Integer, primary_key=True)
  shop_name = Column(String(255), nullable=False, unique=True)

class Stock(Base):
  __tablename__ = 'stocks'

  shop_id = Column(Integer, primary_key=True)
  item_id = Column(Integer, primary_key=True)
  stock = Column(Integer)


# テーブル操作
print('(1)テーブルを削除してから作成')
Base.metadata.drop_all(db_engine)
Base.metadata.create_all(db_engine)

# セッション作成
session_maker = sessionmaker(bind=db_engine)
session = session_maker()

# 商品
print('(2)データ登録:実行')
item01 = Item(item_id=1, item_name='団子', price=100)
item02 = Item(item_id=2, item_name='肉まん', price=150)
item03 = Item(item_id=3, item_name='どら焼き', price=200)
item04 = Item(item_id=4, item_name='コンビーフ', price=500)
# addallはリストで渡す
session.add_all([item01,item02,item03,item04])
session.commit()

# 店舗
shop01 = Shop(shop_id=1, shop_name='東京店')
shop02 = Shop(shop_id=2, shop_name='大阪店')
session.add_all([shop01, shop02])
session.commit()

# 在庫
stock01 = Stock(shop_id=1, item_id=1, stock=10)
stock02 = Stock(shop_id=1, item_id=2, stock=20)
stock03 = Stock(shop_id=1, item_id=3, stock=30)
stock04 = Stock(shop_id=2, item_id=1, stock=100)
stock05 = Stock(shop_id=2, item_id=2, stock=200)
stock06 = Stock(shop_id=2, item_id=3, stock=300)
session.add_all([stock01, stock02, stock03, stock04, stock05, stock06])
session.commit()

print('(3)データ参照:実行')
print('内部結合')
join_3tables_all = session.query(Shop, Item.item_name, Stock.stock).join(Stock, Shop.shop_id==Stock.shop_id).join(Item, Item.item_id==Stock.item_id).all()

print("ここから",join_3tables_all,"ここまで")
shop_all = session.query(Shop.shop_id, Shop.shop_name).all()
print("shopここから",shop_all,"ここまで")
for row in shop_all:
  print(row.shop_id,"は")
# for row in join_3tables_all:
#   print(f'店：{row.Shop.shop_name} -> 商品名：{row.item_name} -> 在庫数：{row.stock}')