from flask import Flask
from flask.templating import render_template
from models import ambilData

application = Flask(__name__)
@application.route('/')
def index() :
  models = ambilData()
  return render_template('light.html',models=models)

@application.route('/dark')
def dark():   
   models = ambilData()
   return render_template('dark.html',models=models)

if __name__ == '__main__' :
  application.run(debug=True)
