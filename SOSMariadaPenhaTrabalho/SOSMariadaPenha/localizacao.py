from datetime import datetime
from uuid import uuid4


class Localizacao:
    def __init__(self, latitude, longitude):
        self.dataHora = datetime.now()
        self.id = uuid4()
        self.latitude = latitude
        self.longitude = longitude
