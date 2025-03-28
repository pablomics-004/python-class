# Evitamos que haya espacios en el input del usuario
usr_seq = [seq.strip() for seq in input("Ingrese varias secuencias de ADN separadas por comas: ").split(",")]
bases = ["A","T","C","G"]

# Obtenemos una lista de listas con tuplas
freq_per_seq = [
    [(base,seq.count(base)) for base in bases]
    for seq in usr_seq
]

print(f"\nLa fecuencia de cada nucleótido por secuencia dada es de: {freq_per_seq}\n")