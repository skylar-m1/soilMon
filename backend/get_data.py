# soiled
# Created by Skylar McDermott
#############################

import requests

# I want to limit the api requests to the weather api provider (dos, limited requests)
'''Possible Solutions
#1 save last scan time to file
 
'''

# weather api variables
latitude = '35.962639'
longitude ='-83.916718'
exclude = ['minutely','daily']
with open('backend/key.txt', 'r') as f: # API key stored in file
    WEATHER_API_KEY = f.read()
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&exclude=%s,%s&appid=%s" % (latitude, longitude, exclude[0],exclude[1], WEATHER_API_KEY)


# create readmoisture, getweather, predict functions

class reader():
    def getweather(self):
        # query api
        # save relevant weather data into WeatherData
        # write file
        # return WeatherData
        try:
            req = requests.get(url, params={'units':'imperial'})
            res = req.json()
            # return only necessary stuff in json
            return res
        except Exception as e:
            print("error getting weather data", e)
    
    def readmoisture(self):
        pass

    def create_save(self, wea, soilmois):
        # this function will create the json save file
        js = {
            "soil_moisture":soilmois,
            "current_weather":wea, ### wea will be a dictionary
            "percipitation":wea,
            "hourly_forcast":[ # five hours 
                wea,
                wea, 
                wea, 
                wea,
                wea,
            ]
        }
        with open("data.txt", "w") as d:
            d.write(js.json)
            d.close()

    def parse(self, up=False):
        if up == True:
            weather = self.getweather()
            # run other functions
            # 
            return wth
        else:
            pass      
        ''' Example of setting vars
        self.moisture = 0.28 # self.moisture = self.read()
        self.current_weather = "Sunny"
        self.forecast = "Sunny"
        self.data = {"moisture":self.moisture, "currenlty":self.current_weather, "forecast":self.forecast}
        return self.data
        '''
#print(time.strftime("%I", time.localtime()))


