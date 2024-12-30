def saudacao():
    print("Olá")
    print("Como vai você?")
    print("O tempo hoje está bom para um passeio!")

saudacao()

def saudacao_com_nome(nome):
    print(f"Olá {nome}")
    print("Como vai você?")
    print("O tempo hoje está bom para um passeio!")

saudacao_com_nome("Carlos Henrique")

# argumentos posicionais
def saudacao_com_local(nome, local):
    print(f"Olá {nome}")
    print("Como vai você?")
    print(f"O tempo hoje está bom para um passeio em {local}!")

saudacao_com_local("Carlos Henrique", "Manaus")


# argumentos nomeados
def saudacao_com_local(nome, local):
    print(f"Olá {nome}")
    print("Como vai você?")
    print(f"O tempo hoje está bom para um passeio em {local}!")

saudacao_com_local(nome="Carlos Henrique", local="Manaus")