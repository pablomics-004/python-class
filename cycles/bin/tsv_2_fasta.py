with open("data/dna_sequences.txt") as dnaseq, open("results/dna_sequences.fa","w") as dnaseq_fa:

    for line in dnaseq:
        # Obtenemos ID y secuencias
        columns = line.strip("\t").split()
        id_seq = columns[0]
        seq = columns[1].upper().replace("-","")

        # Imprimimos en el nuevo archivo
        dnaseq_fa.write(f"> {id_seq}\n{seq}\n")

    print("\nArchivo FASTA generado.\n")