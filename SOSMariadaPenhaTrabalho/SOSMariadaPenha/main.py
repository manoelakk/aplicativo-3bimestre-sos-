# Projeto: SOS MARIA DA PENHA
# Curso: Tecnico em Informatica
# Ano: 2026
# Turma: 2º ano A Informatica
# Disciplina: Programacao Orientada a Objetos
# Integrantes: Bianca Cardoso de Andrade, Rute Danieli Moura da Silva, Manoela Belém Moraes, Ana Caroline Souza Soares, Sofhia Garcia da Costa.

from datetime import date, timedelta

from usuaria import Usuaria
from ocorrencia import Ocorrencia
from patrulhamariadapenha import PatrulhaMariaDaPenha
from viatura import Viatura
from evidencia import Evidencia
from localizacao import Localizacao
from pmgeral import PMGeral
from guardiao import Guardiao
from equipeseguranca import EquipeSeguranca
from redeapoio import RedeApoio
from medidaprotetiva import MedidaProtetiva
from dispositivo import Dispositivo
from alertaemergencia import AlertaEmergencia
from centralmonitoramento import CentralMonitoramento
from enums import StatusViatura, TipoEvidencia


def linha():
    print("-" * 60)


def executar_sistema():
    print("\n========== SOS MARIA DA PENHA ==========\n")

    usuaria = Usuaria("Maria", "maria@email.com", "1234",
                      "Rua Principal", "99999-9999")
    print("USUÁRIA")
    print("Nome:", usuaria.nome)
    print("Login válido:", usuaria.fazerLogin("maria@email.com", "1234"))

    dispositivo = Dispositivo("Android", "TOKEN-123", "1.0.0")
    # Relacionamento: USUARIA 1 POSSUI 1..* DISPOSITIVO.
    usuaria.dispositivos.append(dispositivo)

    medida = MedidaProtetiva("000123/2026", "Medida protetiva de urgência",
                             date.today(), date.today() + timedelta(days=30))
    # Relacionamento: USUARIA 1 POSSUI 0..* MEDIDAPROTETIVA.
    usuaria.medidas_protetivas.append(medida)
    medida.adicionarDocumento("documento_medida.pdf")

    ocorrencia = Ocorrencia("Ameaça recebida pela usuária.")
    # Relacionamento: USUARIA 1 REGISTRA 0..* OCORRENCIA.
    usuaria.registrarOcorrencia(ocorrencia)

    localizacao = Localizacao(-11.4269, -63.0338)
    # Relacionamento: OCORRENCIA 1 POSSUI 1 LOCALIZACAO.
    ocorrencia.localizacao = localizacao

    evidencia = Evidencia(TipoEvidencia.TEXTO, "evidencia.txt")
    ocorrencia.adicionarEvidencia(evidencia)

    alerta = AlertaEmergencia("Ajuda necessária.", usuaria.nome)
    # Relacionamento: OCORRENCIA 1 POSSUI 1 ALERTAEMERGENCIA.
    ocorrencia.alerta_emergencia = alerta
    # Relacionamento: USUARIA 1 POSSUI 0..* ALERTAEMERGENCIA.
    usuaria.alertas.append(alerta)
    alerta.enviar()

    central = CentralMonitoramento("Central SOS", "190")
    central.receberAlerta(alerta)

    equipe = EquipeSeguranca("Equipe Maria da Penha", "190",
                              "Base Central", "Segurança Pública")
    # Relacionamento: CENTRALMONITORAMENTO 1 RECEBE 1..* EQUIPESEGURANCA.
    central.equipes.append(equipe)
    equipe.central = central
    # Relacionamento: OCORRENCIA 1 É ATENDIDA POR 0..* EQUIPESEGURANCA.
    ocorrencia.equipes_seguranca.append(equipe)
    equipe.ocorrencias.append(ocorrencia)

    viatura = Viatura("VTR-01", "ABC1D23",
                      localizacao.latitude, localizacao.longitude)
    equipe.despacharViatura(viatura)

    patrulha = PatrulhaMariaDaPenha("Patrulha Maria da Penha")
    # Relacionamento: VIATURA 1 UTILIZA PATRULHAMARIADAPENHA 1.
    viatura.patrulha = patrulha
    patrulha.receberOcorrencia(ocorrencia)

    guardiao = Guardiao("João", "98888-8888", "Irmão", "joao@email.com")
    # Relacionamento: USUARIA 1 CADASTRA 0..* GUARDIAO.
    usuaria.guardioes.append(guardiao)
    guardiao.receberAlerta(alerta)

    pm = PMGeral("Policial Geral", "97777-7777")
    print(pm.receberLinkRastreamento("link de rastreamento"))

    rede = RedeApoio("Rede de Apoio Local", "96666-6666",
                     "Centro", "Apoio Social")
    print(rede.localizarProximas(localizacao.latitude, localizacao.longitude))

    ocorrencia.finalizar()
    alerta.encerrar()
    viatura.atualizarStatus(StatusViatura.NO_LOCAL)

    print("\nOCORRÊNCIA:", ocorrencia.status.value)
    print("ALERTA:", alerta.status.value)
    print("VIATURA:", viatura.status.value)
    linha()
    print("Sistema executado com sucesso!")


if __name__ == "__main__":
    executar_sistema()
