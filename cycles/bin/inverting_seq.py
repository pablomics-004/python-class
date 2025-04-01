# Ingreso de las secuencias y retiro de caracteres de escape
usr_input = [
    seq.strip() 
    for seq in input("Ingrese varias secuencias de ADN separadas por comas: ").split(",")
]

# Invirtiendo las secuencias obtenidas por el usuario
invert_seq = [
    seq.split(",")[::-1] 
    for seq in usr_input
]

# Mensaje al usuario
print(f"\nLas secuencias invertidas son: {invert_seq}\n")