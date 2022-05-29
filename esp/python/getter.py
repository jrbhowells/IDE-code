import urequests

def ioPost(data, feed):
    headers = {'X-AIO-Key': "aio_GPGU28EyqJ99W1vnjBMRTz3sha85", 'Content-Type': 'application/json'}
    url = 'https://io.adafruit.com/api/v2/jrbhowells/feeds/' + feed + '/data'

    try:
        r = urequests.post(url, json={'value': data}, headers=headers)
        return(r.text)
    except Exception as e:
        print(e)
    
def ioPostWithCo(data, co, feed):
    headers = {'X-AIO-Key': "aio_GPGU28EyqJ99W1vnjBMRTz3sha85", 'Content-Type': 'application/json'}
    url = 'https://io.adafruit.com/api/v2/jrbhowells/feeds/' + feed + '/data'

    cont = {'value': data, 'lat': co[0], 'lon': co[1]}

    try:
        r = urequests.post(url, json=cont, headers=headers)
        return(r.text)
    except Exception as e:
        print(e)

def ioGet(feed):
    headers = {'X-AIO-Key': "aio_GPGU28EyqJ99W1vnjBMRTz3sha85", 'Content-Type': 'application/json'}
    url = 'https://io.adafruit.com/api/v2/jrbhowells/feeds/' + feed + '/data/last'

    try:
        r = urequests.get(url, headers=headers)
        data = r.json()
        return(data["value"])
    except Exception as e:
        print(e)

def ioGetWithID(feed):
    headers = {'X-AIO-Key': "aio_GPGU28EyqJ99W1vnjBMRTz3sha85", 'Content-Type': 'application/json'}
    url = 'https://io.adafruit.com/api/v2/jrbhowells/feeds/' + feed + '/data/last'

    try:
        r = urequests.get(url, headers=headers)
        data = r.json()
        return(data["id"])
    except Exception as e:
        print(e)
