#url = "https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"
url = " "

# Sanitização da URL
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia!!!")

# Separa a base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
print(f'\nURL base: {url_base}')
url_paremetros = url[indice_interrogacao+1:]
print(f'URL parâmetros: {url_paremetros}')

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_paremetros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_paremetros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_paremetros[indice_valor:]
else:
    valor = url_paremetros[indice_valor:indice_e_comercial]

print(valor)
