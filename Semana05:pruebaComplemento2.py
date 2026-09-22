from eii_utils import limpiar_consola, leer_booleano, leer_entero

iphone: bool = True
promedio: int = 0
nota_uno: int = 0
nota_dos: int = 0
nota_tres: int = 0
nota_cuatro: int = 0
materias_aprobadas: int = 0
lav_carro_mama: int = 0
lav_carro_abuela: int = 0
Lav_conjuntas: int = 0

limpiar_consola()
nota_uno = leer_entero("Digite la nota ")
nota_dos = leer_entero("Digite la nota ")
nota_tres = leer_entero("Digite la nota ")
nota_cuatro = leer_entero("Digite la nota ")
materias_aprobadas = leer_entero("¿Cuántas materias aprobó? ")
lav_carro_mama = leer_entero("¿Cuántas veces lavó el carro de la mamá? ")
lav_carro_abuela = leer_entero("¿Cuántas veces lavó el carro de la abuela? ")
Lav_conjuntas = leer_entero("¿Cuantás veces lavó carros durante el mes? ")

promedio = (nota_uno + nota_dos + nota_tres + nota_cuatro) / 4
print ("el promedio es: " , promedio)

requisitos = (promedio >= 80) and (nota_uno >= 75) and (nota_dos >= 75) and (nota_tres >= 75) and (nota_cuatro>=75) and (materias_aprobadas == 4) and (lav_carro_mama >= 8 or lav_carro_abuela >= 8) or (Lav_conjuntas >= 12)

iphone = requisitos 
print("¿Hay iphone?" , iphone)