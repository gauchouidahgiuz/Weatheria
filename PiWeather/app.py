from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    api_key = 'apikey'
    location = 'location'
    
    url = f"https://api.weatherstack.com/current?access_key={api_key}&query={location}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()

        if 'current' in data:
            weather_data = {
                'temperature': data['current']['temperature'],
                'uv_index': data['current']['uv_index'],
                'icon': data['current']['weather_icons'][0],
                'humidity': data['current']['humidity'],
                'windspeed': data['current']['wind_speed'],
                'location': location
            }
            return render_template('weather.html', weather=weather_data)
        else:
            return render_template('weather.html', error="Weather data not found. Check API key and location.")

    except requests.exceptions.RequestException as e:
        return render_template('weather.html', error=f"Request error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
