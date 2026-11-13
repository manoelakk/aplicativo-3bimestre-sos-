from uuid import uuid4


class PatrulhaMariaDaPenha:
    def __init__(self, nomeEquipe):
        self.id = uuid4()
        self.nomeEquipe = nomeEquipe

    def atualizarRota(self, ocorrencia):
        return f"Rota atualizada para a ocorrência {ocorrencia.id}."

    def confirmarRecebimento(self, ocorrencia):
        return True

    def receberOcorrencia(self, ocorrencia):
        return True
