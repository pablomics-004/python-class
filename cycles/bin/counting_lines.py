with open("data/dna_sequences.fa") as seqfa:
    
    # Conteo de secuencias en el archivo
    counts = len([
        line.strip() 
        for line in seqfa 
        if line.strip().startswith(">")
    ])
    
    # Resultado para el usuario
    print(f"\nEl archivo FASTA tiene {counts} secuencias.\n")