from flask import Flask, request

app = Flask(__name__)

# GET
@app.route('/get')
def do_get():
  name = request.args.get('name')
  return f'ハロー、{name}さん'

# POST
@app.route('/', methods=['GET','POST'])
def do_get_post():
  if request.method == 'POST':
    name = request.form.get('name')
    return f'こんにちは、{name}さん'
  return '''
    <h2>POSTで送信</h2>
    <form method="post">
      名前:<input type="text" name="name">
      <input type="submit" value="送信">
    </form>
  '''

if __name__ == '__main__':
  app.run()
