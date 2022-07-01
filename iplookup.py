# import urllib.request
# import json

# with urllib.request.urlopen("https://geolocation-db.com/json") as url:
#     data = json.loads(url.read().decode())
#     print(data)


# import requests


# def get_ip():
#     response = requests.get('https://api64.ipify.org?format=json').json()
#     return response["ip"]


# def get_location():
#     ip_address = get_ip()
#     response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
#     location_data = {
#         "ip": ip_address,
#         "city": response.get("city"),
#         "region": response.get("region"),
#         "country": response.get("country_name")
#     }
#     return location_data


# print(get_location())

import ipapi
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def Index():
    search = request.form.get('search')
    data = ipapi.location(ip=search, output='json')
    print(data)
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
