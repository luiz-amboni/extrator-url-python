class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.validar_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validar_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!!!")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_paremetros = self.url[indice_interrogacao + 1:]
        return url_paremetros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

#extrator_url = ExtratorURL("https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real")
extrator_url = ExtratorURL(None)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)