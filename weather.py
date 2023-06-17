from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError
from pyowm.commons.exceptions import APIRequestError
from pyowm.utils import config as cfg
from pyowm.utils import timestamps
import eel

owm = OWM("")

pyowmconfig = cfg.get_default_config()
pyowmconfig['language'] = 'ru'

eel.init("c:/dev/projects/weatherapp/ui")



@eel.expose
def get_weather(city):
    try:    # error handler by stepan
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        
        tg = weather.temperature("celsius")
        local_temp = tg['temp']
        f_like = tg['feels_like']
        max_temp = tg['temp_max']
        min_temp = tg['temp_min']
        e_temp = "🌡"
        e_status = " "

        hello = "Ты молодец!"

        wind = weather.wind()['speed']
        pressure = weather.pressure['press']
        moisture = weather.humidity
        status = weather.detailed_status 

        status_emoji = {
            "ясно": "☀️",
            "переменная облачность": "🌤",
            "облачно с прояснениями": "🌥",
            "небольшой дождь": "🌦",
            "пасмурно": "☁️",
            "небольшая облачность": "☁️",
            "дождь": "🌧",
            "мгла": "💨"
        }
        
        return (f"В городе {city} температура {int(local_temp)} °C {e_temp} \n\
                 Максимальная температура: {int(max_temp)} °C \n \
                 Минимальная температура: {int(min_temp)}°C \n \
                 Ощущается как: {int(f_like)} °C \n \
                 Скорость ветра: {int(wind)} м/c \n \
                 Давление: {int(pressure)} мм.рт.ст \n \
                 Влага: {int(moisture)} % \n \
                 По состоянию: {status} {status_emoji.get(status) or '🌍'}") 


    except (NotFoundError, APIRequestError):
        e_error = "🚫"
        error = f'Возможные ошибки: 1.Вы допустили ошибку в написании города "{city}" 2. \
        Вы отправили пустой запрос. 3. \
        Проблема с интернетом {e_error}'
        return error


eel.start("ui.html", size=(1089, 959), mode = 'chrome')

# trasher

# old return weather
'''

        return ("В городе " + str(city) + " температура " + str(local_temp) + " °C" + " \n " + ""
                "Максимальная температура: " + str(max_temp) + " °C" + "\n" +
                "Минимальная температура: " + str(min_temp) + " °C" + "\n" + 
                "Ощущается как: " + str(f_like) + " °C" + "\n" +
                "Скорость ветра: " + str(wind) + " м/с" + "\n"  +
                "Давление: " + str(pressure) + " мм.рт.ст" + "\n" +
                "Влажность: " + str(moisture) +" %")
'''


# old emoji weather 

"""

"""
