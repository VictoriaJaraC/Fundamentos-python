from eii_utils import limpiar_consola, leer_flotante

consumo_kwh: float = 0 
energia: float = 0
alumbrado: float = 0 
bomberos: float = 0
IVA: float = 0
total_pagar: float = 0 

limpiar_consola()

consumo_kwh = leer_flotante("Digite el consumo mensual")

if consumo_kwh <= 30:
    energia = 1744.80
elif consumo_kwh <= 200 :
    energia = 1744.80 + (consumo_kwh - 30) * 58.16
elif consumo_kwh <= 300 :
    energia = 1744.80 + (170 * 58.16) + (consumo_kwh - 200) * 89.24
else:
    energia = 1744.80 + (170 * 58.16) + (100 * 89.24) + (consumo_kwh - 200) * 97.27

alumbrado = consumo_kwh * 3.02 

if consumo_kwh > 100:
    bomberos = energia * 0.0175
else:
    bomberos = 0

if consumo_kwh >= 280:
    IVA = (energia + bomberos + alumbrado) * 0.013
else:
    IVA = 0

total_pagar = energia + alumbrado + bomberos + IVA

print("=" *50)
print("   DESGLOSE DE FACTURA ELÉCTRICA (CNFL)   ")
print("=" *50)
print(f"Consumo Mensual:          {consumo_kwh:10.2f} kwh")
print("=" *50)
print(f"Subtotal Energía:               ₡{energia:12.2f}")
print(f"Alumbrado Público:              ₡{alumbrado:12.2f}")
print(f"Tributo a Bomberos (1.75%):     ₡{bomberos:12.2f}")
print(f"Impuesto IVA (13%):             ₡{IVA:12.2f}")
print("=" *50)
print(f"TOTAL A PAGAR:                  ₡{total_pagar:12.2f}")       
print("=" *50)         