from datetime import date
from uuid import uuid4
from enums import StatusUsuario


class Usuaria:
    def __init__(self, nome, email, senha, endereco, telefone,
                 status=StatusUsuario.RECEBIDO):
        self.dataCadastro = date.today()
        self.email = email
        self.endereco = endereco
        self.id = uuid4()
        self.nome = nome
        self.senha = senha
        self.status = status
        self.telefone = telefone

        # Relacionamento: USUARIA 1 POSSUI 0..* MEDIDAPROTETIVA.
        self.medidas_protetivas = []
        # Relacionamento: USUARIA 1 POSSUI 1..* DISPOSITIVO.
        self.dispositivos = []
        # Relacionamento: USUARIA 1 REGISTRA 0..* OCORRENCIA.
        self.ocorrencias = []
        # Relacionamento: USUARIA 1 CADASTRA 0..* GUARDIAO.
        self.guardioes = []
        # Relacionamento: USUARIA 1 POSSUI 0..* ALERTAEMERGENCIA.
        self.alertas = []

    def acionarEmergencia(self):
        from alertaemergencia import AlertaEmergencia
        alerta = AlertaEmergencia(
            "Emergência acionada pela usuária.", self.nome
        )
        self.alertas.append(alerta)
        return alerta

    def atualizarPerfil(self):
        return f"Perfil de {self.nome} atualizado."

    def consultarOcorrencias(self):
        return self.ocorrencias

    def fazerLogin(self, email, senha):
        return self.email == email and self.senha == senha

    def registrarOcorrencia(self, ocorrencia):
        # Relacionamento: USUARIA 1 REGISTRA 0..* OCORRENCIA.
        self.ocorrencias.append(ocorrencia)
        return ocorrencia
