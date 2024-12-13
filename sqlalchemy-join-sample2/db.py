import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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
  shops = relationship("Shop", secondary="stocks", back_populates="items")

class Shop(Base):
  __tablename__ = 'shops'

  shop_id = Column(Integer, primary_key=True)
  shop_name = Column(String(255), nullable=False, unique=True)
  items = relationship("Item", secondary="stocks", back_populates="shops")

class Stock(Base):
  __tablename__ = 'stocks'

  shop_id = Column(Integer, ForeignKey('shops.shop_id'),primary_key=True)
  item_id = Column(Integer, ForeignKey('items.item_id'),primary_key=True)
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
target_shop = session.query(Shop).filter_by(shop_id=1).first()
print(f'店舗名:{target_shop.shop_name}')

for item in target_shop.items:
  stock = session.query(Stock).filter_by(shop_id=target_shop.shop_id, item_id=item.item_id).first()
  print(f'商品名：{item.item_name} -> 在庫数: {stock.stock}')

# for row in join_3tables_all:
#   print(f'店：{row.Shop.shop_name} -> 商品名：{row.item_name} -> 在庫数：{row.stock}')