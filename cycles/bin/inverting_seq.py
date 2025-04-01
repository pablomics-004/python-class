usr_input = input("Ingrese varias secuencias de ADN separadas por comas: ").split(",")

invert_seq = [seq.strip(",")[::-1] for seq in usr_input]

print(f"\nLas secuencias invertidas son: {invert_seq}\n")