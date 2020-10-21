import time
import random
import requests
from threading import Thread
from secrets import TOKEN as tk
from playsound import playsound

class Crab():
    def __init__(self):
        self.colors = [
            "white",
            "red",
            "orange",
            "yellow",
            "cyan",
            "green",
            "blue",
            "purple",
            "pink"
        ]
        self.headers = {"Authorization": "Bearer %s" % tk,}
        self.period = 0.25
        self.cycles = 4
        self.delay = 0.08
        self.soundPath = "B:\Code\Automation\Lifx\sound.mp3"
        self._running = True
        
    """
    Setters and Getters
    """
    
    def getColors(self):
        return colors
    
    def setColors(self, x):
        self.colors == x
    
    def appendColors(self, x):
        self.colors.append(x)
        
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
        

    # Choose a random color from the to send to a data packet
    def randColor(self):
        return random.choice(self.colors)

    # Prep the data packet with the desired payload
    def setData(self):
        data = {
            "color": self.randColor(),
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
    c = Crab()
    t1 = Thread(target=c.createRespsonse).start()
    t2 = Thread(target=c.play).start()
    time.sleep(15)
    c.terminate()
    try:
        t1.join()
        t2.join()
    except AttributeError:
        pass