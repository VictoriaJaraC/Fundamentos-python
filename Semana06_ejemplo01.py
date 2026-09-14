from eii_utils import limpiar_consola, leer_entero 

Nota:int = 0
Nota_Convertida:str = ""

limpiar_consola()
nota = leer_entero ("Digite su nota")

if nota >= 90:
    nota_convertida = "A"
elif nota >= 80:
    nota_convertida = "B"
elif nota >= 70:
    nota_vonvertida = "C"
elif nota >= 60:
    nota_convertida = "D"
else:
    nota_convertida = "F"

print (f"Su nota de {nota} equivale a {nota_convertida}")