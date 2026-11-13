from uuid import uuid4
from enums import StatusAlerta


class CentralMonitoramento:
    def __init__(self, nome, telefone):
        self.id = uuid4()
        self.nome = nome
        self.telefone = telefone

        # Relacionamento: CENTRALMONITORAMENTO 1 RECEBE 1..* EQUIPESEGURANCA.
        self.equipes = []
        # Relacionamento: CENTRALMONITORAMENTO 1 RECEBE 0..* ALERTAEMERGENCIA.
        self.alertas = []

    def receberAlerta(self, alerta):
        # Relacionamento: CENTRALMONITORAMENTO 1 RECEBE 0..* ALERTAEMERGENCIA.
        if alerta not in self.alertas:
            self.alertas.append(alerta)
        alerta.central = self
        alerta.status = StatusAlerta.RECEBIDO

    def visualizarOcorrencia(self, ocorrencia):
        return ocorrencia
