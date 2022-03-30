import Actionneur

class Serializer(Actionneur):
    
    def __init__(self,pin,baude_rate):
        super().__init__(pin,baude_rate)

    def actionner(self):
        if self.__serial:
            pass

    def sendCommand(self,command):
        while True:
            self.__serial.write(command) 