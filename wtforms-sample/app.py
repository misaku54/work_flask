from flask import Flask, render_template, request

app = Flask(__name__)


from forms import UserInfoForm

@app.route('/', methods=['GET','POST'])
def show_enter():
  form = UserInfoForm(request.form)

  if request.method == "POST":
    pass
  return render_template('enter.html', form=form)

if __name__ == '__main__':
  app.run()