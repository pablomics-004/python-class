with open("data/secuencias_arn.txt","w") as outfile:

    # Ingreso de las secuencias del usuario
    dna_seq = input("Ingrese varias secuencias de ADN separadas por comas: ").split(",")

    # Conversión de DNA a RNA
    rna_seq = [seq.replace("T","U") for seq in dna_seq]

    # Generando el archivo de secuencias de RNA
    for seq in rna_seq:
        print(f"{seq}\n",file=outfile,end='')
    
    print("\nArchivo 'secuencias_arn.txt' generado con éxito.\n")