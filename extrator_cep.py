import re # Regular Expression -- regEx

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeira, RJ, 23440-128"

# 5 digítos + hífen (opicional) + 3 dígitos

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)