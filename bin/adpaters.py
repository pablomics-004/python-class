with open("data/4_input_adapters.txt") as infile, open("results/4_input_no_adapters.txt","w") as outfile:
    
    # Recorremos el archivo
    for line in infile:

        # Retiro de los adaptadores
        new_line = line.strip()[14:]

        # Impresión en el nuevo archivo
        print(new_line,file=outfile,end="\n")
    
    # Mensaje al usuario
    print("\nGeneración del archivo: exitosa.\n")