from flask import Flask, jsonify, make_response, request
from app import app
from phue import Bridge
import forecastio
import json
import random

b = Bridge('192.168.2.2')
#b.connect() #first connect only
lightsDict = {
    "overhead1": 1,
    "lamp": 2,
    "overhead2": 3
}

api_key = "961d00284ae951c12d1d465857950732"
#Waterloo Ontario
lat = 43.477
lng = -80.537

#chrome.exe --user-data-dir="C:/Chrome dev session" --disable-web-security

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/weather')
def weather():
    forecast = forecastio.load_forecast(api_key, lat, lng)
    response = {
        "current": {
            "name":'Current',
            "temp": forecast.currently().temperature,
            "state": forecast.currently().summary,
            "pop": forecast.currently().precipProbability
        },
        "tomorrow": {
            "name": 'Tomorrow',
            "temp": forecast.daily().data[1].temperatureHigh,
            "state": forecast.daily().data[1].summary,
            "pop": forecast.daily().data[1].precipProbability
        }
    }
            
    return json.dumps(response)

@app.route('/lightTypes')
def lightTypes():
    response = {
        "studyMode": {
            "type": 'studyMode',
            "displayName": 'Study'
        },
        "siren": {
            "type": 'siren',
            "displayName": 'Siren'
        },
        "disco": {
            "type": 'disco',
            "displayName": 'Disco'
        },
        "reading": {
            "type": 'reading',
            "displayName": 'Reading'
        },
        "sexyTime": {
            "type": 'sexyTime',
            "displayName": 'Romantic'
        },
        "off": {
            "type": 'off',
            "displayName": 'Off'
        }
    }

    return json.dumps(response)

@app.route('/lights', methods= ['PUT'])
def lights():
    #reset all
    b.set_light(lightsDict["overhead1"], "on", False)
    b.set_light(lightsDict["overhead2"], "on", False)
    b.set_light(lightsDict["lamp"], "on", False)

    mode = request.headers.get('type')
    if (mode == "studyMode"):
        command = {
            "on": True,
            "bri": 254,
            "sat": 0
        }
        b.set_light(lightsDict["overhead1"], command)
        b.set_light(lightsDict["overhead2"], command)
        b.set_light(lightsDict["lamp"], command)

    elif (mode == "siren"):
        leftCommand = {
            "on": True, 
            "hue": 0,
            "sat": 200,
            "alert": "lselect"
        }
        rightCommand = {
            "on": True, 
            "hue": 48000,
            "sat": 254,
            "alert": "lselect"
        }
        b.set_light(lightsDict["overhead1"], leftCommand)
        b.set_light(lightsDict["overhead2"], rightCommand)
        b.set_light(lightsDict["lamp"], "on", False)
    
    elif (mode == "disco"):
        overhead1 = {
            "on": True, 
            "hue": 0,
            "sat": 254,
            "effect": "colorloop"
        }
        overhead2 = {
            "on": True, 
            "hue": 21845,
            "sat": 254,
            "effect": "colorloop"
        }
        lamp = {
            "on": True, 
            "hue": 43690,
            "sat": 254,
            "effect": "colorloop"
        }
        b.set_light(lightsDict["overhead1"], overhead1)
        b.set_light(lightsDict["overhead2"], overhead2)
        b.set_light(lightsDict["lamp"], lamp)

    elif(mode == "reading"):
        overhead = {
            "on": True, 
            "bri": 10,
            "hue": 0,
            "sat": 50
        }
        lamp = {
            "on": True, 
            "bri": 100,
            "hue": 0,
            "sat": 50
        }
        b.set_light(lightsDict["overhead1"], overhead)
        b.set_light(lightsDict["overhead2"], overhead)
        b.set_light(lightsDict["lamp"], lamp)

    elif(mode == "sexyTime"):
        command = {
            "on": True,
            "bri": 75,
            "hue": 0,
            "sat": 225
        }
        b.set_light(lightsDict["overhead1"], command)
        b.set_light(lightsDict["overhead2"], command)
        b.set_light(lightsDict["lamp"], command)

if __name__ == '__main__':
    app.run()