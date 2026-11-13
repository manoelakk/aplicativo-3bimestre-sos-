from datetime import datetime
from uuid import uuid4
from enums import StatusAlerta


class AlertaEmergencia:
    def __init__(self, mensagem, origem, status=StatusAlerta.RECEBIDO):
        self.dataHora = datetime.now()
        self.id = uuid4()
        self.mensagem = mensagem
        self.origem = origem
        self.status = status

        # Relacionamento: ALERTAEMERGENCIA 0..* UTILIZA 1 CENTRALMONITORAMENTO.
        self.central = None
        # Relacionamento: ALERTAEMERGENCIA 1 PERTENCE A 1 OCORRENCIA.
        self.ocorrencia = None

    def encerrar(self):
        self.status = StatusAlerta.FINALIZADO

    def enviar(self):
        self.status = StatusAlerta.ENCAMINHADO

    def encaminharParaEquipe(self, ocorrencia):
        # Relacionamento: ALERTAEMERGENCIA ENCAMINHA A OCORRENCIA.
        self.ocorrencia = ocorrencia
        return ocorrencia

    def receberAlerta(self, alerta):
        return alerta

    def visualizarOcorrencia(self, ocorrencia):
        return ocorrencia
