with open("4_input_adapters.txt") as input_file, open("4_no_input_adapters.txt","w") as no_adapt:
    for line in input_file:
        new_line = line.strip()[14:]
        print(new_line,file=no_adapt,end="\n")
    
    print("\nGeneración del archivo: exitosa.\n")