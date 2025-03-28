with open("dna_sequences.txt") as dnaseq, open("dna_sequences.fa","w") as dnaseq_fa:

    for line in dnaseq:
        # Obtenemos ID y secuencias
        columns = line.strip("\t").split()
        id_seq = columns[0]
        seq = columns[1].upper()

        # Imprimimos en el nuevo archivo
        dnaseq_fa.write(f"> {id_seq}\n{seq}\n")

    print("\nArchivo FASTA generado.\n")