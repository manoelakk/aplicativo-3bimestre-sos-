from uuid import uuid4


class RedeApoio:
    def __init__(self, nome, telefone, endereco, tipo):
        self.endereco = endereco
        self.id = uuid4()
        self.latitude = 0.0
        self.longitude = 0.0
        self.nome = nome
        self.telefone = telefone
        self.tipo = tipo

    def localizarProximas(self, latitude, longitude):
        return f"Redes de apoio próximas à localização ({latitude}, {longitude})."
