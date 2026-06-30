import os
from dotenv import load_dotenv

load_dotenv()

MOSSORO_API = "https://transparencia.e-publica.net/epublica-portal/rest/mossoro/api/v1"
SICONFI_API = "https://apidatalake.tesouro.gov.br/ords/cdwhprd/siconfi/tt"
IBGE_API    = "https://servicodados.ibge.gov.br/api/v3"
DIARIO_OFICIAL_MOSSORO = "https://dom.mossoro.rn.gov.br/dom"
DATABASE_URL = os.getenv("DATABASE_URL")