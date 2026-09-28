import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class GerenciadorBancoDados:
    def __init__(self):
        # Coleta de forma oculta e segura a URL que está salva no arquivo .env
        uri = os.getenv("MONGODB_URI")
        self.client = MongoClient(uri)
        self.db = self.client["oficina_db"]
        self.colecao_orcamentos = self.db["orcamentos"]

    def salvar_orcamento(self, dados_json: dict):
        """Grava as informações diretamente no banco NoSQL em nuvem"""
        return self.colecao_orcamentos.insert_one(dados_json)
