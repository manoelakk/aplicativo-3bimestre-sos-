from datetime import datetime
from uuid import uuid4
from enums import StatusOcorrencia


class Ocorrencia:
    def __init__(self, descricao, status=StatusOcorrencia.ABERTA):
        self.dataHora = datetime.now()
        self.descricao = descricao
        self.id = uuid4()
        self.status = status

        # Relacionamento: OCORRENCIA 1 GERA 0..* EVIDENCIA.
        self.evidencias = []
        # Relacionamento: OCORRENCIA 1 POSSUI 1 LOCALIZACAO.
        self.localizacao = None
        # Relacionamento: OCORRENCIA 1 POSSUI 1 ALERTAEMERGENCIA.
        self.alerta_emergencia = None
        # Relacionamento: OCORRENCIA 1 E ATENDIDA POR 0..* EQUIPESeguranca.
        self.equipes_seguranca = []

    def adicionarEvidencia(self, evidencia):
        # Relacionamento: OCORRENCIA 1 GERA 0..* EVIDENCIA.
        self.evidencias.append(evidencia)

    def cancelar(self):
        self.status = StatusOcorrencia.CANCELADA

    def finalizar(self):
        self.status = StatusOcorrencia.FINALIZADA
