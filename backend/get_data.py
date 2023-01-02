# soiled
# Created by Skylar McDermott
#############################
# This script will be executed via a cron job every hour on the rpi
import requests
import json
import time

# weather api variables
latitude = '35.962639'
longitude ='-83.916718'
exclude = ['minutely','daily']
with open('key.txt', 'r') as f: # API key stored in file
    WEATHER_API_KEY = f.read()
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=%s,%s&appid=%s" % (latitude, longitude, exclude[0],exclude[1], WEATHER_API_KEY)


# Reader class holds functionality
class reader():

    def convert_time(self, timestamp):
        # Converts epoch time stamp into 24 hour time
        return time.strftime("%H", time.localtime(timestamp))

    def getweather(self):
        try:
            req = requests.get(url, params={'units':'imperial'})
            res = req.json()
            # will return the id of current weather 
            currently = res["current"]["weather"][0]["id"]
            hourly = {}
            percipitation = 0
            # Loop over for each hour
            for i in range(12):
                time = self.convert_time(res["hourly"][i]["dt"])
                hourly[time] = [res["hourly"][i]["weather"][0]["id"]]
            
            # IF there is rain forecasted add the percipitation value
            if res["hourly"][i]["weather"][0]["main"] == "Rain":
                hourly[time].append(res["hourly"][i]["rain"]["1h"])
                percipitation += res["hourly"][i]["rain"]["1h"]
            # No rain, percipitation 0.0
            else:
                hourly[time].append(0.0)
            if res["alerts"]:
                warn = {"name":res["alerts"][0]["event"], "desc":res["alerts"][0]["event"]}
            else:
                warn = ""
            percipitation = round(percipitation, 2)

            self.weather_data =  {"currently":currently,"hourly":[hourly],"total_percipitation":percipitation, "alerts":[warn]}
            return self.weather_data
        
        except Exception as e:
            print("error getting weather data", e)
    
    def readmoisture(self): # TO-DO
        pass

    def create_save(self, wea, soilmois):
        # this function will create the json save file
        # wea is dictionary passed from get weather
        js = {
            "soil_moisture":soilmois, 
            "current_weather":wea["currently"],
            "hourly_forcast":wea["hourly"], 
            "total_percipitation":wea["total_percipitation"],
            "alerts":wea["alerts"]
        }
        with open("../data.txt", "w") as d:
            d.write(json.dumps(js)) # REVIEW ME
            d.close()
        with open("../data.txt", "r") as f:
            saved = f.read()
            f.close()
        return json.loads(saved) # AND ME

    def main(self):
        # Runs all of the funcitons and creates save file
        weather = self.getweather()
        soil = 650 # hardcoded soil for now
        # create save
        resp = self.create_save(weather, soil)


