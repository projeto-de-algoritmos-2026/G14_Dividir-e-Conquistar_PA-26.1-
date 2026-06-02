from candidato import Candidato
from sistema_bolsa import SistemaBolsa
import random

sistema = SistemaBolsa()

while True:

    print("\n===== SISTEMA DE BOLSAS =====")
    print("1 - Adicionar candidato")
    print("2 - Listar candidatos")
    print("3 - Calcular nota de corte")
    print("4 - Mostrar Top 10%")
    print("5 - Buscar posição K")
    print("6 - Gerar relatório")
    print("7 - Gerar candidatos aleatórios")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        nome = input("Nome: ")
        nota = int(input("Nota: "))

        sistema.adicionar_candidato(
            Candidato(nome, nota)
        )

    elif opcao == "2":

        sistema.listar_candidatos()

    elif opcao == "3":

        print(
            f"Nota de corte: "
            f"{sistema.nota_de_corte()}"
        )

    elif opcao == "4":

        print("\nTOP 10%")

        for candidato in sistema.top_10_porcento():
            print(candidato)

    elif opcao == "5":

        k = int(
            input("Digite a posição: ")
        )

        print(
            sistema.candidato_posicao_k(k)
        )

    elif opcao == "6":

        sistema.gerar_relatorio()

    elif opcao == "7":

        quantidade = int(
            input(
                "Quantidade de candidatos: "
            )
        )

        for i in range(1, quantidade+1):

            sistema.adicionar_candidato(
                Candidato(
                    f"Aluno {i}",
                    random.randint(0, 1000)
                )
            )

        print(
            f"{quantidade} candidatos gerados!"
        )

    elif opcao == "0":

        print("Encerrando...")
        break

    else:

        print("Opção inválida.")