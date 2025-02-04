from Configuration import Configuration
from Models import Repository

def test_configuration():
    print("#################### READING REPOSITORY - START")
    a = Configuration()
    repositorios = a.getRepositorios()

    while (len(repositorios) != 0):
        repo = repositorios[0]
        print(repo.name, " -> " ,repo.path)
        repositorios.remove(repo)
    assert repositorios == []
    print("#################### READING REPOSITORY - END")

    print("#################### WRITING REPOSITORY - START")
    a = Configuration()
    repo = Repository('Um repositorio', 'C://qualquerlugar')
    repo2 = Repository('Dois repositorios', 'C://qualquerlugar')
    repo3 = Repository('Tres repositorios', 'C://qualquerlugar')
    repo4 = Repository('Quatro repositorio', 'C://qualquerlugar')
    a.addRepositorio(repo)
    a.addRepositorio(repo2)
    a.addRepositorio(repo3)
    a.addRepositorio(repo4)
    print("#################### WRITING REPOSITORY - END")