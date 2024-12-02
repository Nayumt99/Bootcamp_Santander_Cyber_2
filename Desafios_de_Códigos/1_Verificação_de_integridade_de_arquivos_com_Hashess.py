def verificar_hashes(lista_hashes):
    """
    Função que verifica se o hash calculado é igual ao hash esperado.
    :param lista_hashes: Lista de strings, onde cada string contém um par de hashes separados por vírgula.
    """
    for hash_comparacao in lista_hashes:
        # Dividir o par de hashes em hash_calculado e hash_esperado
        hash_calculado, hash_esperado = hash_comparacao.split(",")

        # Remover espaços em branco ao redor (caso haja)
        hash_calculado = hash_calculado.strip()
        hash_esperado = hash_esperado.strip()

        # Comparar os hashes e imprimir o resultado
        if hash_calculado == hash_esperado:
            print("Correto")
        else:
            print("Inválido")

# Ler a entrada do usuário
hashes_usuario = input()

# Dividir os pares de hashes em uma lista
lista_hashes = hashes_usuario.split(";")

# Chamar a função para verificar os hashes
verificar_hashes(lista_hashes)
