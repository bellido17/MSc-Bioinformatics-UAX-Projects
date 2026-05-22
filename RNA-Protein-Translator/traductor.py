# Diccionario del código genético (RNA → aminoácido)
codigo_genetico = {
    "AUG": "M",  # Metionina (inicio)
    "UUU": "F", "UUC": "F",
    "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y",
    "UGU": "C", "UGC": "C",
    "UGG": "W",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "UAA": "*", "UAG": "*", "UGA": "*"  # codones STOP
}
def traducir_a_proteinas(secuencia_arn):
    """
    Traduce una secuencia de RNA a una secuencia de aminoácidos.
    Los codones desconocidos se traducen como 'X'.
    """

    proteina = ""

    # Recorremos la secuencia de 3 en 3
    for i in range(0, len(secuencia_arn), 3):
        codon = secuencia_arn[i:i+3]

        # Si el codón no tiene 3 letras, lo ignoramos
        if len(codon) != 3:
            continue

        # Buscamos el codón en el diccionario
        aminoacido = codigo_genetico.get(codon, "X")

        # Añadimos el aminoácido a la proteína
        proteina += aminoacido

    return proteina
