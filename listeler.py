
"""
ilklistem=["kalem","kağıt","usb"]
print(ilklistem)
print(type(ilklistem))
ilklistem.append("kalemtraş")
print(ilklistem)
"""
"""
liste1=["ağaç","çiçek","odun"]
liste2=["lale","yasemin","hanımeli"]

liste1=liste2
liste2[0]="a"

print(liste1)
print(liste2)

sayi1=10
sayi2=20
sayi1=sayi2
sayi2=60
print(sayi2)
"""

liste1=["ağaç","çiçek","odun"]
liste2=["lale","yasemin","hanımeli"]

liste1[0]="a"

liste1=liste2
#liste1[0]="a"

print(liste1)
print(liste2)

#referans tip: list
#değer tip: int

listem="arduino"
print(listem[0])