import json
from urllib import request

def ambilData() :
  url = "https://indonesia-covid-19.mathdro.id/api/provinsi"

  response = request.urlopen(url);
  data = json.loads(response.read())
  return data

  provinsi = data['data']['provinsi']
  positif = data['data']['kasusPosi']
  sembuh = data['data']['kasusSemb']
  meninggal = data['data']['kasusMeni']

  # for covid in data['data'] :
  #   print('------------')
  #   print(f"Provinsi : {covid['provinsi']}")
  #   print(f"Kasus Positif : {covid['kasusPosi']}")
  #   print(f"Kasus Sembuh : {covid['kasusSemb']}")
  #   print(f"Kasus Meninggal : {covid['kasusMeni']}")