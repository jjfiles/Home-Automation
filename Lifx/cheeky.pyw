import time
import random
import requests
from threading import Thread
from secrets import TOKEN as tk
from playsound import playsound

class Cheeky():
    def __init__(self):
        self.color = "red"
        self.headers = {"Authorization": "Bearer %s" % tk,}
        self.period = 2
        self.cycles = 10
        self.delay = self.period * self.cycles
        self.soundPath = "B:\\Code\\Automation\\Lifx\\ussr.mp3"
        self._running = True
        
    """
    Setters and Getters
    """
    
    def getColors(self):
        return color
    
    def setColors(self, x):
        self.color == x
        
    def getPeriod(self):
        return self.period
    
    def setPeriod(self, x):
        self.period = x
        
    def getCycles(self):
        return self.cycles
    
    def setCycles(self, x):
        self.cycles = x
    
    def getDelay(self):
        return self.delay
        
    def setDelay(self, x):
        self.delay = x
        
    def getSoundPath(self):
        return self.soundPath
    
    def setSoundPath(self, x):
        self.soundPath = x
        
    # Prep the data packet with the desired payload
    def setData(self):
        data = {
            "color": self.color,
            "period": self.period,
            "cycles": self.cycles,
            "persist": "false",
            "power_on": "true"
        }
        print("data: ", data)
        return data

    # Setup a https response for the lifx api
    def createRespsonse(self):
        while(self._running):
            response = requests.post(
                'https://api.lifx.com/v1/lights/location:Office/effects/pulse',
                data=self.setData(),
                headers=self.headers
            )
            print("Response: ", response)
            time.sleep(self.delay)
    # Play a specified sound file
    def play(self):
        if(self._running):
            print("Playing sound: ", self.soundPath)
            playsound(self.soundPath, False)
        
    def terminate(self):
        self._running = False
    
    
if __name__ == "__main__":
    c = Cheeky()
    t1 = Thread(target=c.createRespsonse).start()
    t2 = Thread(target=c.play).start()
    time.sleep(30)
    c.terminate()
    try:
        t1.join()
        t2.join()
    except AttributeError:
        pass