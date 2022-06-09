#from Response import request
import requests

url = 'https://io.adafruit.com/api/v2/jrbhowells/feeds/ide-1/data'

headers = {'X-AIO-Key': "aio_GPGU28EyqJ99W1vnjBMRTz3sha85", 'Content-Type': 'application/json'}

body = {'value': 20}


'''try:
    r = urequests.post(url, json=body, headers=headers)
    print(r.text)
except Exception as e:
    print(e)

try:
    r = urequests.get(url + "/last", headers=headers)
    data = r.json()
    print(data["value"])
except Exception as e:
    print(e)
'''

'''
try:
    r = requests.post(url, json=body, headers=headers)
    print(r.text)
except Exception as e:
    print(e)'''

'''
try:
    r = requests.get(url + "/last", headers=headers)
    data = r.json()
    print(data["value"])
except Exception as e:
    print(e)
'''

data = 0.1
co = [50, 0]
feed = 'ide-progress'

headers = {'X-AIO-Key': "aio_qroT33zlvhHthcQDt9sQhLEyft4I", 'Content-Type': 'application/json'}
url = 'https://io.adafruit.com/api/v2/jrbhowells/feeds/' + feed + '/data'

cont = {'value': data, 'lat': co[0], 'lon': co[1]}

try:
    r = requests.post(url, json=cont, headers=headers)
    print(r.text)
except Exception as e:
    print("Not posted to IDE-Progress: " + e)


'''
try:
    r = request(url=url,
        data=body,
        params=None,
        headers=headers,
        method="POST",
        data_as_json=True,
        error_count=0)
    print(r.body)
except Exception as e:
    print(e)


try:
    r = request(url=url + "/last",
        data=None,
        params=None,
        headers=headers,
        method="GET",
        data_as_json=True,
        error_count=0)
    data = r.json()
    print(data["value"])
except Exception as e:
    print(e)
'''

