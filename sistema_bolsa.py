from mediana_das_medianas import mediana_das_medianas

class SistemaBolsa:

    def __init__(self):
        self.candidatos = []

    def adicionar_candidato(self, candidato):
        self.candidatos.append(candidato)

    def listar_candidatos(self):

        if not self.candidatos:
            print("Nenhum candidato cadastrado.")
            return

        for candidato in self.candidatos:
            print(candidato)

    def nota_de_corte(self):

        notas = [c.nota for c in self.candidatos]

        return mediana_das_medianas(
            notas,
            len(notas)//2
        )

    def candidato_posicao_k(self, k):

        ordenados = sorted(
            self.candidatos,
            key=lambda c: c.nota,
            reverse=True
        )

        return ordenados[k-1]

    def top_10_porcento(self):

        ordenados = sorted(
            self.candidatos,
            key=lambda c: c.nota,
            reverse=True
        )

        quantidade = max(
            1,
            int(len(ordenados) * 0.10)
        )

        return ordenados[:quantidade]

    def gerar_relatorio(self):


        if not self.candidatos:
            print("Nenhum candidato cadastrado.")
            return

        melhor = max(
            self.candidatos,
            key=lambda c: c.nota
        )

        pior = min(
            self.candidatos,
            key=lambda c: c.nota
        )

        print("\n===== RELATÓRIO =====")

        print(
            f"\nTotal de candidatos: "
            f"{len(self.candidatos)}"
        )

        print(
            f"\nNota de corte: "
            f"{self.nota_de_corte()}"
        )

        print("\nMelhor nota:")
        print(melhor)

        print("\nPior nota:")
        print(pior)