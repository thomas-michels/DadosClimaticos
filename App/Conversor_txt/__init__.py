
from App.URL import Url
from App.Extract_Data import ExtratorDeDados


class ConversorTXT:

    def __init__(self, dados: dict):
        self._dados = dados
        self.converter()

    

    def converter(self):

        dados_list = self._dados['observations']

        for medicao in dados_list:
            print(medicao)

if __name__ == '__main__':

    u = Url("20200708")
    ext = ExtratorDeDados(u)
    ext.extrair()
    dados = ext.get_dados()
    c = ConversorTXT(dados)