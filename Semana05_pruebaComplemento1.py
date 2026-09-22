from eii_utils import limpiar_consola, leer_booleano, leer_entero 

clima_soleado: bool = True
fin_mes: bool = True
pelicula: bool = True
salida: bool = True
dinero_uno: int = 0
dinero_dos: int = 0
pendientes_maria: int = 0 
pendientes_carlos: int = 0
cupones_adquiridos: int = 0
entradas_adquiridas: int = 0

limpiar_consola()
clima_soleado = leer_booleano("¿El clima está soleado? ")
fin_mes = leer_booleano("¿Es fin de mes? ")
pelicula = leer_booleano("¿Están presentando en el cine El Coyote vrs Acme? ")
dinero_uno = leer_entero("¿Cuánto dinero tiene para la cabina? ")
dinero_dos = leer_entero("Cuánto dinero tiene para salir? ")
pendientes_maria = leer_entero("¿Cuántas tareas tiene Maria? ")
pendientes_carlos = leer_entero("¿Cuántas tareas tiene Carlos? ")
cupones_adquiridos = leer_entero("¿Cuántos cupones tiene? ")
entradas_adquiridas = leer_entero("¿Cuántas entradas tiene? ")

opcion_uno = (clima_soleado == True) and (fin_mes == True) and (dinero_uno >= 100000)

opcion_dos = (dinero_dos >= 10000) and (pendientes_carlos == 0) and (pendientes_maria == 0)

opcion_tres = (pelicula == True) and (cupones_adquiridos > 0 or entradas_adquiridas >0)

salida = (opcion_uno or opcion_dos or opcion_tres) == True

print("¿Puedo salir?" , salida)

