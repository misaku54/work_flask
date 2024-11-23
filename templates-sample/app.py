from flask import Flask, render_template
from werkzeug.exceptions import NotFound
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('top.html')

# 一覧
@app.route('/list')
def item_list():
  return render_template('list.html')

# 詳細
@app.route('/detail/<int:id>')
def item_detail(id):
  return render_template('detail.html', show_id=id)

@app.route('/multple')
def show_jinja_multple():
  word1 = "テンプレートエンジン"
  word2 = "神社"
  return render_template('jinja/show1.html', temp=word1, jinja=word2)

@app.route('/dict')
def show_jinja_dict():
  words = {
    'temp': 'template',
    'jinja': 'jinja',  
  }
  return render_template('jinja/show2.html', key=words)

@app.route('/list2')
def show_jinja_list():
  e_list = ['aaa','bbb','ccc']
  return render_template('jinja/show3.html', users = e_list)

class Item:
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def __str__(self):
    return f'商品ID:{self.id} 商品名:{self.name}'
  
@app.route('/for_list')
def show_for_list():
  item_list = [Item(1, "aa"),Item(2, "bb"),Item(3, "cc"),]
  return render_template('for_list.html', items=item_list)

@app.route('/if/')
@app.route('/if/<target>')
def show_jinja_if(target="colorless"):
  print(target)
  return render_template('jinja/if_else.html', color=target)

@app.route('/filter')
def show_filter_block():
  word = 'pen'
  return render_template('filter/block.html', show_word=word)

@app.errorhandler(NotFound)
def show_404_page(error):
  msg = error.description
  print('エラー内容:', msg)
  return render_template('errors/404.html')

if __name__ == '__main__':
  app.run()