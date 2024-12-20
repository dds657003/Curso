# Lista inicial de jogadores da Sharkcoders
lista_jogadores = ["Alexandre", "Bernardo", "Diogo", "Daniel", "Eduardo"]

# Menu interativo
while True:
    print("\n ⚽ Gestão da Equipa Sharkcoders 🦈")
    print("1️⃣ Ver a equipa atual")
    print("2️⃣ Substituir um jogador")
    print("3️⃣ Adicionar um novo jogador")
    print("4️⃣ Remover um jogador")
    print("5️⃣ Reorganizar a equipa")
    print("6️⃣ Sair")

    escolha = int(input("Escolhe uma opção: "))

    if escolha == 1:
        print("\n 📄 Equipa atual:")
        for i, jogador in enumerate(lista_jogadores):
            print(f"{i} - {jogador}")

    elif escolha == 2:
        print("\n 📄 Equipa atual:")
        for i, jogador in enumerate(lista_jogadores):
            print(f"{i} - {jogador}")
        posicao = int(input("Insire o número do jogador a substituir: "))
        if 0 <= posicao < len(lista_jogadores):
            novo_jogador = input("Insere o nome do novo jogador: ")
            lista_jogadores[posicao] = novo_jogador
            print("Jogador substituído com sucesso!")
        else:
            print("Posição inválida.")

    elif escolha == 3:
        novo_jogador = input("Insere o nome do novo jogador: ")
        lista_jogadores.append(novo_jogador)
        print(f"{novo_jogador} foi adicionado à equipa!")

    elif escolha == 4:
        escolha_remover = input("Queres remover por nome ou por posição? (nome/posição): ")
        if escolha_remover == "nome":
            nome = input("Insere o nome do jogador a remover: ")
            if nome in lista_jogadores:
                lista_jogadores.remove(nome)
                print(f"{nome} foi removido da equipa.")
        elif escolha_remover == "posição":
            posicao = int(input("Insere o número do jogador a remover: "))
            if 0<= posicao < len(lista_jogadores):
                removido = lista_jogadores.pop(posicao)
                print(f"{removido} foi removido da equipa. ")
            else:
                print("Posição inválida.")

    elif escolha == 6:
        print(" A gestão da equipa foi encerrada. Até à próxima!")
        break

    else:
        print("Opção inválida. Tenta novamente.")

