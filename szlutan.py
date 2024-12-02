num_cellak = 400
cellak = [False] * num_cellak

for szolga in range(1, num_cellak + 1):  
    for cella in range(szolga - 1, num_cellak, szolga):  
        cellak[cella] = not cellak[cella]  

open_cellak = [i + 1 for i, is_open in enumerate(cellak) if is_open]

print("Nyitva maradt cellák sorszámai:")
print(open_cellak)
