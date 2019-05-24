# Nativas
import json
# Importadas
import requests
# Do projeto
from utils import Utilitario

class Classe_exemplo:
    def __init__(self):
        self.url = 'https://api.ipify.org'
    
    def consulta_com_nome(self):
        util = Utilitario()
        util.ser_util()
        try:
            response = requests.get(self.url)
            return json.loads(response.content), True
        except:
            return 'Não conseguimos nos conectar', False