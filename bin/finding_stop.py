# Ingreso de las secuencias y retiro de caracteres de escape
usr_seq = [
    seq.strip() 
    for seq in input("Ingrese varias secuencias de ADN separadas por comas: ").split(",")
]

# Set con los codones de paro
stop_codons = {"TAA","TAG","TGA"}

# Ubicando secuencias con codones de paro
seq_stop = {
    seq
    for seq in usr_seq
    for codon in stop_codons
    if codon in seq
}

print(f"\nLas secuencias con al menos un codón de paro son:\n")

# Impresión a pantalla de las secuencias obtenidas
for seq in seq_stop:
    print(seq,end='\n')