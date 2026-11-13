from datetime import date
from uuid import uuid4


class Dispositivo:
    def __init__(self, plataforma, tokenFCM, versaoApp):
        self.id = uuid4()
        self.plataforma = plataforma
        self.tokenFCM = tokenFCM
        self.ultimoAcesso = date.today()
        self.versaoApp = versaoApp

    def atualizarUltimoAcesso(self):
        self.ultimoAcesso = date.today()

    def registrarToken(self, token):
        self.tokenFCM = token
