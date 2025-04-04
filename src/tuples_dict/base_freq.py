seq = tuple("ATGCTTCGA")
bases = "ATGC"

freq = [
    (base,seq.count(base))
    for base in bases
]

print(f"\nFrecuencia de nucleótidos: {freq}\n.")