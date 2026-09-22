from eii_utils import limpiar_consola, leer_booleano, leer_entero, leer_flotante

temperatura: float = 0
presion_optima: bool = True
materia_prima: bool = True
reab_activo: bool = True
inspeccion_ap: bool= True
operarios_cap:int = 0
turno_nocturno: bool = False
mant_pendiente: bool = True


limpiar_consola ()

temperatura = leer_flotante("Digite la temperatura")
presion_optima = leer_booleano("¿La presión es óptima?")
materia_prima = leer_booleano("¿Hay materia prima?")
reab_activo = leer_booleano("¿Existe una orden de reabastecimiento activa?")
operarios_cap = leer_entero("¿Cuántos operarios capacitados hay?")
inspeccion_ap = leer_booleano("¿la inspección se aprobó?")
turno_nocturno = leer_booleano("¿Se encuentran en turno nocturno?")
mant_pendiente = leer_booleano("¿Hay algun mantenimiento pendiente?")

if temperatura >= 180 and presion_optima == True and materia_prima == True:
    if turno_nocturno == False and operarios_cap >= 3:
        print("El lote se programa en la Línea 1 (Alta Velocidad)")
    else:
     print("El lote se programa en la Línea 2 (Estándar/Supervisada)")
elif temperatura >= 180 and presion_optima == True and reab_activo == True:
    if turno_nocturno == False and operarios_cap >= 3:
           print("El lote se programa en la Línea 1 (Alta Velocidad)")
    else:
        print("El lote se programa en la Línea 2 (Estándar/Supervisada)")
else:
    if inspeccion_ap == False or mant_pendiente == True:
        print("Paro técnico obligatorio")
    else:
        print("Detenido en espera de materia prima")