usr_seq = [seq.strip() for seq in input("Ingrese varias secuencias de ADN separadas por comas: ").split(",")]
stop_codons = {"TAA","TAG","TGA"}

seq_stop = {
    seq
    for seq in usr_seq
    for codon in stop_codons
    if codon in seq
}

print(f"\nLas secuencias con al menos un codón de paro son:\n")

for seq in seq_stop:
    print(seq,end='\n')