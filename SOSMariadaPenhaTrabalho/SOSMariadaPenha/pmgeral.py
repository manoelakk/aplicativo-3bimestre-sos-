from uuid import uuid4


class PMGeral:
    def __init__(self, nome, telefone):
        self.contato = telefone
        self.id = uuid4()
        self.nome = nome
        self.telefone = telefone

    def receberLinkRastreamento(self, link):
        return f"Link de rastreamento recebido: {link}"
