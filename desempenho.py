import random
import time

from mediana_das_medianas import mediana_das_medianas


def teste_desempenho(tamanho):

    notas = [
        random.randint(0, 1000)
        for _ in range(tamanho)
    ]

    k = len(notas) // 2

    # Ordenação completa
    inicio = time.perf_counter()

    ordenado = sorted(notas)
    mediana_ordenacao = ordenado[k]

    fim = time.perf_counter()

    tempo_ordenacao = fim - inicio

    # Mediana das Medianas
    inicio = time.perf_counter()

    mediana_mdm = mediana_das_medianas(
        notas.copy(),
        k
    )

    fim = time.perf_counter()

    tempo_mdm = fim - inicio

    print(f"\n{tamanho} candidatos")
    print(f"Ordenação: {tempo_ordenacao:.6f}s")
    print(f"Mediana das Medianas: {tempo_mdm:.6f}s")


teste_desempenho(100)
teste_desempenho(1000)
teste_desempenho(10000)
teste_desempenho(100000)