from candidato import Candidato
from mediana_das_medianas import mediana_das_medianas

class SistemaBolsa:

    def __init__(self):
        self.candidatos = []

    def adicionar_candidato(self, candidato):
        self.candidatos.append(candidato)

    def nota_de_corte(self):

        notas = [
            candidato.nota
            for candidato in self.candidatos
        ]

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