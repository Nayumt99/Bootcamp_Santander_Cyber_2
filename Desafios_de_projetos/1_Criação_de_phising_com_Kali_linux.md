# Simulação de Phishing Educacional no Kali Linux

**Aviso Importante:** Este guia é **estritamente para fins educacionais e de conscientização** em segurança cibernética. Ele deve ser utilizado apenas em ambientes controlados e autorizados, como laboratórios de treinamento ou aulas práticas. Qualquer uso fora desse contexto é ilegal e contrário às práticas éticas.

---

## Requisitos

- **Sistema Operacional**: Kali Linux
- **Ferramentas**: Social Engineering Toolkit (SET)
- **Permissões**: Acesso root

---

## Passo a Passo

### 1. **Obtenha Permissões de Administrador**
Abra o terminal e inicie como superusuário:
```bash
sudo su
```bash

### 2. Inicie o Social Engineering Toolkit (SET)
Execute o comando abaixo para iniciar o SET Toolkit:
```bash
setoolkit
```bash

### 3. **Selecione o Tipo de Ataque**
No menu principal, escolha a opção de ataques de engenharia social:
```bash
1) Social-Engineering Attacks
```bash

### 4. **Escolha o Vetor de Ataque**
Selecione o vetor de ataque baseado em sites:
```bash
2) Website Attack Vectors
```bash

### 5. **Escolha o Método de Ataque**
Opte pelo método de captura de credenciais:
```bash
3) Credential Harvester Attack Method
```bash

### 6. **Clone o Site Alvo**
Escolha a opção de clonar um site existente:
```bash
2) Site Cloner
```bash

Quando solicitado, insira o URL do site que será clonado para a simulação:
```bash
http://www.facebook.com
```bash

### 7. **Obtenha o Endereço da Máquina**
Identifique o IP do servidor local utilizando o comando:
```bash
ifconfig
```bash

## Considerações Importantes

###  **Ambiente Controlado:**

Realize a simulação em um ambiente seguro, como uma rede isolada.
Nunca utilize redes públicas ou sistemas sem permissão.

###  **Conscientização:**

Utilize este projeto para ensinar como identificar ataques de phishing.
Apresente técnicas de mitigação e melhores práticas.

###  **Práticas Éticas:**

Garanta que todos os envolvidos no treinamento entendam o propósito educacional da simulação.
Documente os aprendizados para avaliação posterior.


## **Resultados Esperados**

Aumento da Conscientização: Ensinar como identificar tentativas de phishing.
Fortalecimento de Defesas: Demonstrar vulnerabilidades em um ambiente seguro.
Aprendizado Ético: Aplicar técnicas reais de ataque para treinamentos autorizados.
