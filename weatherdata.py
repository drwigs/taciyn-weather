import requests
from prettytable import PrettyTable
from .visuals import get_terminal_size, center_text_in_terminal
from pysine import sine

from colorama import Fore, Back, Style

# Gracias ChatGPT

API_KEY = "7e48bed635e3ec17d58c152858f2f3b7"

print(Fore.WHITE)

def weather_data(key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': key,
        'units': 'metric' # Celsius
    }

    response = requests.get(base_url, params=params)


    data = response.json()
    
    if response.status_code == 200:
        main_data = data['main']
        wind_data = data['wind']
        weather_description = data['weather'][0]['description']

    else:
        print(Back.RED + "Error: ", data['message'] + Back.RESET)
        exit()

    data_table = PrettyTable(["Temperatura", "Humedad", "Viento"])

    sine(frequency=600.0, duration=0.1)
    print(Back.WHITE + Fore.BLACK)
    center_text_in_terminal(f"\nInformación sobre {city}")
    print(Back.BLUE + Fore.RESET + "\n")

    data_table.add_row(
    [f"{main_data['temp']}°C",
                        
    f"Humedad: {main_data['humidity']}%",

    f"{wind_data['speed']} m/s"])

    center_text_in_terminal(str(data_table))
    print(Back.RESET)
    #print(f"Descripción del clima: {weather_description}")

# Llave de la api
