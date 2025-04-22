skola = ["lavice", "kniha", "učivo", "matematika", "učitelka", "židle"]
print(len(skola))
for i in skola:
    print(i)
dalsiSkola = input("Zadejte další věc co se týká školy")
skola.append(dalsiSkola)
skola.pop(3)
print(skola.sort())
print(skola.reverse())