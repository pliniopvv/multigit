import configparser
from Models import Repository

class Configuration():
    def __init__(self, path = 'basic.ini'):
        self.path = path
        self.service = configparser.ConfigParser()
        self.service.read(path) # if None open basic.ini

        if ('repositorios' in self.service.sections()):
            lista = []
            for name, path in self.service['repositorios'].items():
                lista.append(Repository(name, path))
            self.repo = lista

    def _clear(self):
        self.repo = []
        self._save()
        
    def _save(self):
        file = open(self.path, 'w')
        if not ('repositorios' in self.service.sections()):
            self.service.add_section('repositorios')
        for repo in self.repo:
            self.service['repositorios'][repo.name] = repo.path
        self.service.write(file)
        file.close()
        pass


    def getRepositorios(self):
        if ('repo' in dir(self)):
            return self.repo
        return []

    def setRepositorio(self, repository):
        if not isinstance(repository, Repository): raise TypeError("Tipo não é um Repository!")

        if ('repo' in dir(self)):
            self.repo.append(repository)
        else:
            lista = []
            lista.append(repository)
            self.repo = lista
        self._save()
