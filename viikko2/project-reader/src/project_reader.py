from urllib import request
from project import Project
import toml
class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        f = toml.loads(content)
        name = f["tool"]["poetry"]["name"]
        description = f["tool"]["poetry"]["description"]
        dependencies = f["tool"]["poetry"]["dependencies"]
        dev_dependencies = f["tool"]["poetry"]["group"]["dev"]["dependencies"]
        lisenssi = f["tool"]["poetry"]["license"] 
        authors = f["tool"]["poetry"]["authors"] 
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies,dev_dependencies,lisenssi, authors)
