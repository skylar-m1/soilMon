import requests
import datetime
# I want to limit the api requests to the weather api provider (dos, limited requests)
'''
Possible Solutions
#1 Only query on specified hours
- 
'''
# create readmoisture, getweather, predict functions


def getweather():
    # query api
    # save weather data into WeatherData
    # set time variable

    pass



# parse will write to the file to save
class reader():
    def parse(self):
        self.time = datetime.now().strftime("%H")
        if (time - self.time) >= 2:
            run = True
        else:
            run = False
        if run:
            getweather()
        else:
            # Open the data file and use the saved variables
            pass
        '''self.moisture = 0.28 # self.moisture = self.read()
        self.current_weather = "Sunny"
        self.forecast = "Sunny"
        self.data = {"moisture":self.moisture, "currenlty":self.current_weather, "forecast":self.forecast}
        return self.data'''
