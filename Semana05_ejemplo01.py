from eii_utils import leer_entero, leer_texto, limpiar_consola 

# declaracion
paciente: str = ""
edad: int = 0
encargado: str = ""

#entradas
limpiar_consola ()
paciente = leer_texto("Digite el nombre del paciente")
edad = leer_entero("Digite la edad")

if edad < 18: 
    encargado = leer_texto("Digite el nombre de la persona encaragada")

print(f"La persona paciente se llama {paciente} y tiene {edad} años")
print(f"la persona encargada es {encargado}")