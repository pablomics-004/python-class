with open("secuencias_arn.txt","w") as outfile:

    dna_seq = input("Ingrese varias secuencias de ADN separadas por comas: ").split(",")

    rna_seq = [seq.replace("T","U") for seq in dna_seq]

    for seq in rna_seq:
        print(f"{seq}\n",file=outfile,end='')
    
    print("\nArchivo 'secuencias_arn.txt' generado con éxito.\n")