from flask import Flask, jsonify, make_response, request
from app import flaskapp
from flask_cors import CORS
from phue import Bridge
import forecastio
import json
import random

#b = Bridge('192.168.2.2')
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

CORS(flaskapp)

@flaskapp.route('/')
def hello():
    return "Hello World!"

@flaskapp.route('/weather')
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

@flaskapp.route('/lightTypes')
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

@flaskapp.route('/locations')
def locations():
    response = {
        "Canada": [
            {
                "city": "Vancouver",
                "coords": [ -123.116226, 49.246292 ]
            },
            {
                "city": "Beamsville",
                "coords": [ -79.4760, 43.1571 ]
            },
            {
                "city": "Montreal",
                "coords": [ -73.5673, 45.5017 ]
            },
            {
                "city": "Quebec City",
                "coords": [ -71.2080, 46.8139 ]
            },
            {
                "city": "Halifax",
                "coords": [ -63.5752, 44.6488 ]
            }
        ],
        "United States": [
            {
                "city": "Detroit",
                "coords": [ -83.045753, 42.331429 ]
            },
            {
                "city": "Cleveland",
                "coords": [ -81.681290, 41.505493 ]
            },
            {
                "city": "Pittsburgh",
                "coords": [ -79.995888, 40.440624 ]
            },
            {
                "city": "Orlando",
                "coords": [ -81.379234, 28.538336]
            },
            {
                "city": "Miami",
                "coords": [ -80.191788, 25.761681 ]
            },
            {
                "city": "San Juan, Puerto Rico",
                "coords": [ -66.105721, 18.466333 ]
            },
        ]
    }
    return json.dumps(response)
# @app.route('/lights', methods= ['PUT'])
# def lights():
#     #reset all
#     b.set_light(lightsDict["overhead1"], "on", False)
#     b.set_light(lightsDict["overhead2"], "on", False)
#     b.set_light(lightsDict["lamp"], "on", False)

#     mode = request.headers.get('type')
#     if (mode == "studyMode"):
#         command = {
#             "on": True,
#             "bri": 254,
#             "sat": 0
#         }
#         b.set_light(lightsDict["overhead1"], command)
#         b.set_light(lightsDict["overhead2"], command)
#         b.set_light(lightsDict["lamp"], command)

#     elif (mode == "siren"):
#         leftCommand = {
#             "on": True, 
#             "hue": 0,
#             "sat": 200,
#             "alert": "lselect"
#         }
#         rightCommand = {
#             "on": True, 
#             "hue": 48000,
#             "sat": 254,
#             "alert": "lselect"
#         }
#         b.set_light(lightsDict["overhead1"], leftCommand)
#         b.set_light(lightsDict["overhead2"], rightCommand)
#         b.set_light(lightsDict["lamp"], "on", False)
    
#     elif (mode == "disco"):
#         overhead1 = {
#             "on": True, 
#             "hue": 0,
#             "sat": 254,
#             "effect": "colorloop"
#         }
#         overhead2 = {
#             "on": True, 
#             "hue": 21845,
#             "sat": 254,
#             "effect": "colorloop"
#         }
#         lamp = {
#             "on": True, 
#             "hue": 43690,
#             "sat": 254,
#             "effect": "colorloop"
#         }
#         b.set_light(lightsDict["overhead1"], overhead1)
#         b.set_light(lightsDict["overhead2"], overhead2)
#         b.set_light(lightsDict["lamp"], lamp)

#     elif(mode == "reading"):
#         overhead = {
#             "on": True, 
#             "bri": 10,
#             "hue": 0,
#             "sat": 50
#         }
#         lamp = {
#             "on": True, 
#             "bri": 100,
#             "hue": 0,
#             "sat": 50
#         }
#         b.set_light(lightsDict["overhead1"], overhead)
#         b.set_light(lightsDict["overhead2"], overhead)
#         b.set_light(lightsDict["lamp"], lamp)

#     elif(mode == "sexyTime"):
#         command = {
#             "on": True,
#             "bri": 75,
#             "hue": 0,
#             "sat": 225
#         }
#         b.set_light(lightsDict["overhead1"], command)
#         b.set_light(lightsDict["overhead2"], command)
#         b.set_light(lightsDict["lamp"], command)

# if __name__ == '__main__':
#     app.run()