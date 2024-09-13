import configparser

class Configuration():
    def __init__(self, path = 'basic.ini'):
        self.path = path
        self.service = configparser.ConfigParser()
        
        self.service.read(path) # if None open basic.ini

    def getRepositorios(self):
        return self.service['repositorios']
    
    def setRepositorio(self, path):
        self.service['repositorios'].append(path)
        self.service.write(self.path)
