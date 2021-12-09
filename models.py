import json
from urllib import request
from datetime import datetime
import requests

# Fetch data dari API dan akan dikirimkan ke view

def provinsi() :
  url = "https://indonesia-covid-19.mathdro.id/api/provinsi"

  response = request.urlopen(url);
  data = json.loads(response.read())
  return data

def dunia() :
  url = "https://covid19.mathdro.id/api/confirmed"

  response = request.urlopen(url);
  data = json.loads(response.read())
  return data

def ambilTanggal() :
  today = datetime.now().strftime('%A, %d %B %Y')
  return today

def indonesia() : 
  url = "https://api.kawalcorona.com/indonesia/"

  response = requests.get(url).json()
  return response

def harian_indo() :
  url = "https://apicovid19indonesia-v2.vercel.app/api/indonesia/harian"
  response = requests.get(url).json()
  return response

def india() :
  url = "https://covid19.mathdro.id/api/countries/india/confirmed"
  response = requests.get(url).json()
  return response

def india_global() :
  url = "https://covid19.mathdro.id/api/countries/india"
  response = requests.get(url).json()
  return response

def turki() :
  url = "https://covid19.mathdro.id/api/countries/turkey/confirmed"
  response = requests.get(url).json()
  return response

def turki_global() :
  url = "https://covid19.mathdro.id/api/countries/turkey"
  response = requests.get(url).json()
  return response

def us() :
  url = "https://covid19.mathdro.id/api/countries/us/confirmed"
  response = requests.get(url).json()
  return response

def us_global() :
  url = "https://covid19.mathdro.id/api/countries/us"
  response = requests.get(url).json()
  return response

  # provinsi = data['data']['provinsi']
  # positif = data['data']['kasusPosi']
  # sembuh = data['data']['kasusSemb']
  # meninggal = data['data']['kasusMeni']

  # for covid in data['data'] :
  #   print('------------')
  #   print(f"Provinsi : {covid['provinsi']}")
  #   print(f"Kasus Positif : {covid['kasusPosi']}")
  #   print(f"Kasus Sembuh : {covid['kasusSemb']}")
  #   print(f"Kasus Meninggal : {covid['kasusMeni']}")

  # Kawal Covid : covid[iterator]['attributes']['Positif']