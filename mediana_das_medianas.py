def mediana_das_medianas(vetor, k):

    if len(vetor) <= 5:
        return sorted(vetor)[k]

    grupos = [
        vetor[i:i+5]
        for i in range(0, len(vetor), 5)
    ]

    medianas = []

    for grupo in grupos:
        grupo.sort()
        medianas.append(
            grupo[len(grupo)//2]
        )

    pivo = mediana_das_medianas(
        medianas,
        len(medianas)//2
    )

    menores = [x for x in vetor if x < pivo]
    iguais = [x for x in vetor if x == pivo]
    maiores = [x for x in vetor if x > pivo]

    if k < len(menores):
        return mediana_das_medianas(
            menores,
            k
        )

    elif k < len(menores) + len(iguais):
        return pivo

    else:
        return mediana_das_medianas(
            maiores,
            k - len(menores) - len(iguais)
        )