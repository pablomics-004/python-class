usr_input = input("\nIngrese sus secuencias de DNA separadas por comas: ").split(",")

# Obtención de los primeros tres nucleótidos por secuencia
seq3 = [
    seq.strip()[:3] 
    for seq in usr_input
]

# Mensaje al usuario con el resultado
print(f"\nLos primeros tres nucleótidos de cada secuencia son: {seq3}\n")