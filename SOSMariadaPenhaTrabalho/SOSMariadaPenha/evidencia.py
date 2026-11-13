from datetime import datetime
from uuid import uuid4


class Evidencia:
    def __init__(self, tipo, url):
        self.dataHora = datetime.now()
        self.id = uuid4()
        self.tipo = tipo
        self.url = url

    def visualizar(self):
        return self.url
