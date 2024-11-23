import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "2f210ffc39109cb711df8034e6c9628d"

@app.route('/weather', methods=['GET'])
def weather():
    print("Rota acessada com sucesso!")  # Diagnóstico
    
    # Parâmetros de latitude e longitude
    lat = request.args.get('lat', '-12.9714')  # Latitude padrão
    lon = request.args.get('lon', '-38.5014')  # Longitude padrão
    
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }
    
    # Requisição à API
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        print("Dados obtidos com sucesso!")  # Diagnóstico
        return jsonify(response.json())
    else:
        print(f"Erro ao acessar API: {response.status_code}")  # Diagnóstico
        return jsonify({"error": f"Erro na API: {response.status_code}"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True, port=8080)
