from flask import Flask
from flask.templating import render_template
from models import provinsi,ambilTanggal,dunia,indonesia,harian_indo,india,india_global,turki,turki_global

application = Flask(__name__)
@application.route('/')
def index() :
  return render_template('index.html')

@application.route('/post')
def post() :
  return render_template('post.html')

@application.route('/post1')
def post1():   
   models = provinsi()
   date = ambilTanggal()
   indo = indonesia()
   return render_template('post1.html',models=models,date=date,indo=indo)

@application.route('/post2')
def post2():   
   models = dunia()
   date = ambilTanggal()
   length = len(models)
   return render_template('post2.html',models=models,date=date,length=length)

@application.route('/post3')
def post3():   
   models = harian_indo()
   date = ambilTanggal()
   length = len(models)
   return render_template('post3.html',models=models,date=date,length=length)

@application.route('/post4')
def post4():   
   models = india()
   india_ = india_global()
   date = ambilTanggal()
   length = len(models)
   return render_template('post4.html',models=models,date=date,length=length,india=india_)

@application.route('/post5')
def post5():   
   models = turki()
   turki_ = turki_global()
   date = ambilTanggal()
   length = len(models)
   return render_template('post5.html',models=models,date=date,length=length,turki=turki_)

if __name__ == '__main__' :
  application.run(debug=True)
