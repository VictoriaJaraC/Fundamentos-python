from eii_utils import limpiar_consola, leer_entero, imprimir_mensaje, imprimir_error

monto_total:int=0
cantidad_estudiantes:int=0

limpiar_consola()
cantidad_estudiantes = leer_entero("¿Cuantos estduiantes son?")
monto_total=leer_entero("Monto recolectado")

if monto_total >= (cantidad_estudiantes * 500):
    imprimir_mensaje("Nos fuimos de fiesta (de la alegria)")
else:
    imprimir_error("Se devuelve el dinero")