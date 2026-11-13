from datetime import date
from uuid import uuid4
from enums import StatusMedida


class MedidaProtetiva:
    def __init__(self, numeroProcesso, descricao, dataInicio, dataFim,
                 status=StatusMedida.SUSPENSA):
        self.dataFim = dataFim
        self.dataInicio = dataInicio
        self.descricao = descricao
        self.id = uuid4()
        self.numeroProcesso = numeroProcesso
        self.status = status

        # Relacionamento: MEDIDAPROTETIVA POSSUI DOCUMENTOS.
        self.documentos = []

    def adicionarDocumento(self, url):
        self.documentos.append(url)

    def estaAtiva(self):
        hoje = date.today()
        return (
            self.dataInicio <= hoje <= self.dataFim
            and self.status not in (StatusMedida.EXPIRADA, StatusMedida.REVOGADA)
        )
