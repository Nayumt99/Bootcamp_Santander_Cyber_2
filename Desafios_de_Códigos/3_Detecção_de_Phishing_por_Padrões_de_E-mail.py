# Função para verificar se o corpo do e-mail contém palavras suspeitas de phishing
def verificar_phishing(mensagem):
    # Lista de palavras que indicam possíveis e-mails de phishing
    palavras_suspeitas = ["ganhe", "prêmio", "urgente", "desconto", "click",  "promoção"]
    
    # Converte a mensagem para minúsculas para comparação insensível a maiúsculas/minúsculas
    mensagem = mensagem.lower()
    
    # Verifica se alguma palavra suspeita está presente no corpo do e-mail
    for palavra in palavras_suspeitas:
        if palavra in mensagem:
            return "Phishing"
    
    return "Seguro"

# Leitura do e-mail do usuário
email_usuario = input()

# Remover espaços extras do início e fim
email_usuario = email_usuario.strip()

# Chama a função para verificar o phishing
resultado = verificar_phishing(email_usuario)

# Exibe o resultado
print(f"Classificação: {resultado}")
