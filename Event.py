class Event:
    def __init__(self, command=""):
        self.set_command(command)
    
    def set_command(self, command):
        self.command = command
    
    def get_command(self):
        return self.command
