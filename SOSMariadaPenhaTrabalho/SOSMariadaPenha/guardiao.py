from uuid import uuid4


class Guardiao:
    def __init__(self, nome, telefone, parentesco, email, ativo=True):
        self.ativo = ativo
        self.email = email
        self.id = uuid4()
        self.nome = nome
        self.parentesco = parentesco
        self.telefone = telefone

    def confirmarRecebimento(self, alerta):
        return self.receberAlerta(alerta)

    def receberAlerta(self, alerta):
        return alerta

    def visualizarLocalizacao(self, localizacao):
        return (localizacao.latitude, localizacao.longitude)

    def visualizarOcorrencia(self, ocorrencia):
        return ocorrencia
