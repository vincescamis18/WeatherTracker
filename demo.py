import requests
from flask import Flask, render_template, request

app = Flask(__name__)

api_key = '59aedbbeddd0180da7c7f603f0f06b49'
#api_key = 'y9YzAx4SmoWZF75Yhw1b1LG9XHLLsEDB'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = {}
    if request.method == 'POST':
        city = request.form.get('city')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
#        url = f'http://dataservice.accuweather.com/locations/v1/search?q={city}&apikey={api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temp_c = data['main']['temp']
            desc = data['weather'][0]['description']
            weather_data = {'temp_c': temp_c, 'desc': desc}
    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)