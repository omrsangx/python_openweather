# Import models
from twilio.rest import Client
from decimal import Decimal
import requests

# Twilio API call
account_sid = "Your Twilio account SID goes here"
authentication_token = "Your Twilio authentication token goes here"

# Openweather API call
OpenWeatherMap_app_id = 'Your OpenWeatherMap app id goes here'
OpenWeatherMap_city_id = '5128581' # This city ID is for NYC

url = 'https://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s' % (OpenWeatherMap_city_id,OpenWeatherMap_app_id)

# Telephone number use for the From and To
send_from_number = 'Cell phone number goes here'
send_to_number = 'Cell phone number goes here'

# Openweather json data
json_data = requests.get(url).json()
json_to_python_data = json_data['main']['temp']
get_weather_description = json_data['weather'][0]['description']

# The temperature data that is imported from https://openweathermap.org/ is in Kelvin
# Convert from Kelvin to Fahrenheit and round the result to zero decimal value after the period
fahrenheit_temp = ((json_to_python_data - 273) * (9/5) + 32)
fah_temp = round(Decimal(fahrenheit_temp), 0)

# Twilio create messages
message_body = 'Temp: ' + str(fah_temp) + ' Fah, ' + get_weather_description
client = Client(account_sid, authentication_token)
text_message = client.messages.create(from_ = send_from_number, body = message_body, to = send_to_number)

# To print to the console / optional
print(message_body)
