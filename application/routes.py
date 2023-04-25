from application import app

@app.route('/')
def index():
  return 'hello world'

@app.route('/att_todo')
def add_todo():
  return 'render_template("add_")'