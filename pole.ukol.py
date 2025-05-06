cislo = [3, 7, 12, 5, 9, 15]
hodnota= int(input("Zadej číslo"))
for i in range(6):
    if hodnota== cislo[i]:
        print(f"cislo je v poli",i)
    else:
        print("cislo neni v poli")
        
