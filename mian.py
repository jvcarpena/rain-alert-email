import os
from dotenv import load_dotenv
import requests
import smtplib

load_dotenv()

my_email = os.getenv("my_email")
my_password = os.getenv("mypassword")
api_key = os.getenv("api_key")
weather_url = os.getenv("weather_url")
parameters = {
    "lat": 14.204780,
    "lon": 121.154716,
    "appid": api_key,
    "cnt": 4
}
response = requests.get(url=weather_url, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for item in weather_data["list"]:  # inside "list", item is the index of the "list".
    condition_code = item["weather"][0]["id"]
    if condition_code < 600:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="jvcarpena11@gmail.com",
                            msg="Subject: It will rain\n\n"
                                "Bring an umbrella!")

# ENVIRONMENT VARIABLE:
# used to store a secret key in an environment instead in your codebase.
# EXAMPLE CODE OF THIS IS:
# export variable_name=key,        export API_KEY=83268916b9eecc77009b9fc36df72e62
# and then update your code like this:
# import os first and then
# key = os.environ.get("variable_name")   api_key = os.environ.get("API_KEY")

