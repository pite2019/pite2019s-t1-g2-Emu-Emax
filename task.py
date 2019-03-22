class Car:

    _speed = 0

    def __init__(self):
        self._speed = 0
  
    def act(self,event):
        if event == "speed":
            self._speed += 20
            print("Increased speed to " + str(self._speed) + " km/h !")

        if event == "slow" and self._speed != 0:
            self._speed -= 20
            print("Slowed to " + str(self._speed) + " km/h !")

        if event == "stop":
            while ( self._speed != 0):
                self._speed -= 10
                print ("slowing, now " + str(self._speed) + " km/h!")
            print("the car has stopped!")

print("type speed / slow / stop")
car1 = Car()

event = ""
while event != "stop":
    
    event= input('event: ')
    if event == "speed":
        car1.act(event)

car1.act("stop")
