class Candidato:

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"{self.nome} - Nota: {self.nota}"