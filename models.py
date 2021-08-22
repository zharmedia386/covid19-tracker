import json
from urllib import request

url = "https://indonesia-covid-19.mathdro.id/api/provinsi"

response = request.urlopen(url);
data = json.loads(response.read())

for covid in data['data'] :
  print('------------')
  print(f"Provinsi : {covid['provinsi']}")
  print(f"Kasus Positif : {covid['kasusPosi']}")
  print(f"Kasus Sembuh : {covid['kasusSemb']}")
  print(f"Kasus Meninggal : {covid['kasusMeni']}")