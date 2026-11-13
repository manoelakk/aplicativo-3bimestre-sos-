from uuid import uuid4
from enums import StatusViatura


class Viatura:
    def __init__(self, identificacao, placa, latitudeAtual=0.0,
                 longitudeAtual=0.0, status=StatusViatura.DISPONIVEL):
        self.id = uuid4()
        self.identificacao = identificacao
        self.latitudeAtual = latitudeAtual
        self.longitudeAtual = longitudeAtual
        self.placa = placa
        self.status = status

        # Relacionamento: VIATURA 0..* POSSUI EQUIPESeguranca 1.
        self.equipe_seguranca = None
        # Relacionamento: VIATURA 1 UTILIZA PATRULHAMARIADAPENHA 1.
        self.patrulha = None

    def atualizarStatus(self, status):
        self.status = status
