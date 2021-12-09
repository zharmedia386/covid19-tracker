from flask import Flask
from flask.templating import render_template
from models import provinsi,ambilTanggal,dunia,indonesia,harian_indo,india,india_global,turki,turki_global,us,us_global

application = Flask(__name__)

# Route untuk halaman utama
@application.route('/')
def index() :
  return render_template('index.html')

# Route untuk halaman awal
@application.route('/post')
def post() :
  return render_template('post.html')

# Route untuk halaman Indonesia
@application.route('/post1')
def post1():   
   models = provinsi()
   date = ambilTanggal()
   indo = indonesia()
   # Mengambil Data dari Model untuk dikirim ke View (render)
   return render_template('post1.html',models=models,date=date,indo=indo)

# Route untuk halaman Global
@application.route('/post2')
def post2():   
   models = dunia()
   date = ambilTanggal()
   length = len(models)
   # Mengambil Data dari Model untuk dikirim ke View (render)
   return render_template('post2.html',models=models,date=date,length=length)

# Route untuk halaman Indonesia Harian
@application.route('/post3')
def post3():   
   models = harian_indo()
   date = ambilTanggal()
   length = len(models)
   # Mengambil Data dari Model untuk dikirim ke View (render)
   return render_template('post3.html',models=models,date=date,length=length)

# Route untuk halaman India
@application.route('/post4')
def post4():   
   models = india()
   india_ = india_global()
   date = ambilTanggal()
   length = len(models)
   # Mengambil Data dari Model untuk dikirim ke View (render)
   return render_template('post4.html',models=models,date=date,length=length,india=india_)

# Route untuk halaman Turki
@application.route('/post5')
def post5():   
   models = turki()
   turki_ = turki_global()
   date = ambilTanggal()
   length = len(models)
   # Mengambil Data dari Model untuk dikirim ke View (render)
   return render_template('post5.html',models=models,date=date,length=length,turki=turki_)

# Route untuk halaman United States
@application.route('/post6')
def post6():   
   models = us()
   us_ = us_global()
   date = ambilTanggal()
   length = len(models)
   # Mengambil Data dari Model untuk dikirim ke View (render)
   return render_template('post6.html',models=models,date=date,length=length,us=us_)

if __name__ == '__main__' :
  application.run(debug=True)
