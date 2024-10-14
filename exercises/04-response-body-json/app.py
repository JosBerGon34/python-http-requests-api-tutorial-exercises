import requests
import json
import datetime
response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
data = response.json()
hours = datetime["hours"]
minutes = datetime["minutes"]
seconds = datetime["seconds"]


datetime_str = data("date_time")
datetime_object = datetime.fromisoformat(datetime_str)

hours = datetime_object.hours
minutes = datetime_object.minutes
seconds = datetime_object.seconds
print(response.text)
print(f"Current time: {hours} horas {minutes} minutos y {seconds} segundos")



