WeatherAPIWrapper
A WeatherAPIWrapper é uma API simples desenvolvida em Flask que integra dados de previsão do tempo com a OpenWeatherMap API. A API retorna informações como a temperatura atual, condições climáticas, e velocidade do vento para uma localização específica, usando coordenadas de latitude e longitude.

Funcionalidades
Obter informações sobre o clima atual com base em latitude e longitude.
Dados retornados em formato JSON, incluindo:
Nome da cidade.
Temperatura atual.
Descrição das condições climáticas.
Velocidade do vento.
Tecnologias
Flask: Framework utilizado para a criação da API.
OpenWeatherMap API: Serviço de previsão do tempo usado para obter dados climáticos.
Requests: Biblioteca Python para fazer requisições HTTP.
Como usar
Pré-requisitos
Certifique-se de que você tenha o Python 3.x e o pip instalados.

Clone o repositório:

bash
Copiar código
git clone https://github.com/username/WeatherAPIWrapper.git
Navegue até o diretório do projeto:

bash
Copiar código
cd WeatherAPIWrapper
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copiar código
python3 -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Crie um arquivo .env para armazenar sua chave de API da OpenWeatherMap. O arquivo deve conter a variável:

plaintext
Copiar código
API_KEY=SUA_CHAVE_AQUI
Execute a API:

bash
Copiar código
python app.py
Acesse a API através do navegador ou ferramenta de requisições como Postman, ou cURL:

Endpoint:
GET http://127.0.0.1:8080/weather?lat=<latitude>&lon=<longitude>

Exemplo:
GET http://127.0.0.1:8080/weather?lat=-12.9714&lon=-38.5014

Resposta JSON:

json
Copiar código
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
