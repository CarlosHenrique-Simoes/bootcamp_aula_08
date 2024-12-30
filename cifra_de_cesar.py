alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def cifra_de_cesar(mensagem, codigo, direcao):
    mensagem_criptografada = ""

    if direcao == 2:
        codigo *= -1

    for letra in mensagem:
        if letra not in alfabeto:
            mensagem_criptografada += letra

        else:
            posicao_alternada = alfabeto.index(letra) + codigo
            posicao_alternada = posicao_alternada % len(alfabeto)
            mensagem_criptografada += alfabeto[posicao_alternada]

    if direcao == 1:
        print(f"Sua mensagem criptografada é:{mensagem_criptografada}")
    else:
        print(f"Sua mensagem descriptografada é:{mensagem_criptografada}")


rodar = True

while rodar == True:

    direcao = int(input("Digite 1 para criptografar ou 2 para descriptografar:\n"))
    mensagem = input("Digite sua mensagem:\n").lower()
    codigo = int(input("Digite o valor do codigo:\n"))

    cifra_de_cesar(mensagem=mensagem, codigo=codigo, direcao=direcao)

    reiniciar = input("Digite [S] para reiniciar ou [N] para sair:\n").lower()

    if reiniciar == "n":
        rodar = False
        print("Programa finalizado, Até mais.")

    elif reiniciar == "s":
        print("Reiniciando...")

    else:
        print("Seleção invalida...")
        print("Reiniciando...")