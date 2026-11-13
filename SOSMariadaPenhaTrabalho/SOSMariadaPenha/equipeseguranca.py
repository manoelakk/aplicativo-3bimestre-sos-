from uuid import uuid4
from enums import StatusViatura


class EquipeSeguranca:
    def __init__(self, nome, telefone, endereco, tipo):
        self.endereco = endereco
        self.id = uuid4()
        self.latitude = 0.0
        self.longitude = 0.0
        self.nome = nome
        self.telefone = telefone
        self.tipo = tipo

        # Relacionamento: EQUIPESEGURANCA 1 ATENDE 0..* OCORRENCIA.
        self.ocorrencias = []
        # Relacionamento: EQUIPESEGURANCA 1 POSSUI 0..* VIATURA.
        self.viaturas = []
        # Relacionamento: EQUIPESEGURANCA 0..* RECEBE 1 CENTRALMONITORAMENTO.
        self.central = None

    def despacharViatura(self, viatura):
        # Relacionamento: EQUIPESEGURANCA 1 POSSUI 0..* VIATURA.
        if viatura not in self.viaturas:
            self.viaturas.append(viatura)
        viatura.equipe_seguranca = self
        viatura.atualizarStatus(StatusViatura.EM_DESLOCAMENTO)

    def visualizarAlerta(self, alerta):
        return alerta
