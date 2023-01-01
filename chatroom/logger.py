DEBUG = 1
INFO = 2
WARNING = 3
ERROR = 4

class Logger:
    def __init__(self,level=INFO):
        self._level = level

    def Log(self,message,level=INFO):
        if level >= self._level:
            print(message)

    def Debug(self,message):
        self.Log(message,DEBUG)

    def Info(self,message):
        self.Log(message,INFO)

    def Warning(self,message):
        self.Log(message,WARNING)

    def Error(self,message):
        self.Log(message,ERROR)