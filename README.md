# WeatherAPIWrapper

A WeatherAPIWrapper é uma API simples desenvolvida em Flask que integra dados de previsão do tempo com a OpenWeatherMap API. A API retorna informações como a temperatura atual, condições climáticas, e velocidade do vento para uma localização específica, usando coordenadas de latitude e longitude.

# Funcionalidades

Obter informações sobre o clima atual com base em latitude e longitude.
Dados retornados em formato JSON, incluindo:
Nome da cidade.
Temperatura atual.
Descrição das condições climáticas.
Velocidade do vento.
# Tecnologias

Flask: Framework utilizado para a criação da API.
OpenWeatherMap API: Serviço de previsão do tempo usado para obter dados climáticos.
Requests: Biblioteca Python para fazer requisições HTTP.

Clone o repositório:

```bash
git clone https://github.com/username/WeatherAPIWrapper.git
```


# Resposta JSON:

```bash

{
  "name": "Salvador",
  "main": {
    "temp": 26.5
  },
  "weather": [
    {
      "description": "nuvens dispersas"
    }
  ],
  "wind": {
    "speed": 3.1
  }
}
