class Car:

    def __init__(self, event):
        self.speed = 0
        self.wheelAngle = 0
        self.event = event
  
    def act(self, event):
        command = event.get_command()

        if command == "speed":
            self.speed += 20
            self.print_log("Increased speed to ", self.speed, " km/h")

        if command == "slow":
            if self.speed != 0:
                self.speed -= 20
                self.print_log("Slowed speed to ", self.speed, " km/h")
            else:
                self.print_log("Cannot slow, already stopped! ")
            
        if command == "stop":
            while( self.speed != 0 ):
                self.speed -= 10
                self.print_log("Slowing, now ", self.speed, " km/h")
                self.print_log("The car has stopped")
        
        if command == "turn_right":
            self.wheelAngle += 30
            self.print_log("Turned wheels to ", self.wheelAngle, " angle")
        
        if command == "turn_left":
            self.wheelAngle -= 30
            self.print_log("Turned wheels to ", self.wheelAngle, " angle")

    def print_log(self, message, value="", unit=""):
        print('{} {} {}'.format(message, value, unit))


