import os
import json
import urllib.request
from urllib.parse import quote
from flask import Flask, render_template, request

app = Flask(__name__)


SAMPLE_API_KEY = "14ed76f8584800044a17fc944b0454f5"
WEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY", SAMPLE_API_KEY)

def fetch_json(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))

@app.route("/getweather", methods=["POST", "GET"])
def weather():
    location = request.form.get("city", "").strip() if request.method == "POST" else "Chennai"
    if not location:
        return render_template("file.html", error="Please enter a city name.")

    try:

        weather_url = f"https://openweathermap.org{quote(location)}&appid={WEATHER_API_KEY}&units=metric"
        weather_data = fetch_json(weather_url)

        city_name = weather_data.get("name", location)
        country_code = weather_data.get("sys", {}).get("country", "").upper()
        temp_c = weather_data.get("main", {}).get("temp")

        data = {
            "country_code": country_code if country_code else "N/A",
            "temp": f"{temp_c} °C" if temp_c is not None else "N/A",
            "location": city_name,
        }

        return render_template("file.html", data=data)

    except Exception:
        return render_template("file.html", error="Something went wrong. Please try again.")

@app.route("/")
def index():
    return render_template("file.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
