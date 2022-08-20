import requests

# I want to limit the api requests to the weather api provider (probably a good idea not to dos them)
'''
soiledapi creates object and calls parse
parse will run functions
getweather is called
getweather queries weather api
getweather writes to file, sets time
    if the current time is past the saved time by two hours
        requery the api
    else:
        reuse saved arguments
NOTES 

'''
class reader():
    # create read, getweather, predict functions
    def getweather(self):
        pass
    def parse(self):
        # parse will run all functions and set the variables
        self.moisture = 0.28 # self.moisture = self.read()
        self.current_weather = "Sunny"
        self.forecast = "Sunny"
        self.data = {"moisture":self.moisture, "currenlty":self.current_weather, "forecast":self.forecast}
        return self.data