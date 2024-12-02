num_cellak = 400
cellak = [False] * num_cellak

for szolga in range(1, num_cellak + 1):  
    for cella in range(szolga - 1, num_cellak, szolga):  
        cellak[cella] = not cellak[cella]  

nyitva_cellak = [i + 1 for i, nyitva in enumerate(cellak) if nyitva]

print("Nyitva maradt cellák sorszámai:")
print(nyitva_cellak)
