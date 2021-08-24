import pprint
import requests

class WeatherForecastAPI:

    @staticmethod
    def get(city_name, range):
        url = f"http://api.weatherapi.com/v1/forecast.json?key=38b04baba9b44109985190006212208&q={city_name}&days={range}"
        data = requests.get(url).json()
        forecast_data = data["forecast"]["forecastday"]
        forecast = []
        for data in forecast_data:
            forecast.append({
                "date": data["date"],
                "temp_avg": data["day"]["avgtemp_c"],
                "temp_max": data["day"]["maxtemp_c"],
                "temp_min": data["day"]["mintemp_c"],
                "f_daily_chance_of_rain": data["day"]["daily_chance_of_rain"]
            })
        return forecast

class CityInfo:

    def __init__(self, city, waether_forecast=None):
        self.city = city
        self._weather_forecast = waether_forecast or WeatherForecastAPI()

    def weather_forecast(self, range=1):
        return self._weather_forecast.get(self.city, range)

def _main():
    city_info = CityInfo("Moscow")
    print(city_info.city)
    forecast = city_info.weather_forecast(3)
    pprint.pprint(forecast)

if __name__ == "__main__":
    _main()