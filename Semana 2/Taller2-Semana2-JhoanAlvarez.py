#importamos la herramienta para fechas
import datetime

#obtenemos la fecha actual del equipo donde se ejecuta el agente
fecha_actual = datetime.datetime.now()
anio_actual = fecha_actual.year
mes_actual = fecha_actual.month
dia_actual = fecha_actual.day

#declaramos las siguientes variables para todo el flujo del agente
mx_intentos = 3
min_intentos = 0
rol = None
sistema_activo = True
mensaje = ""
historial_agente = []

#solicitamos el usuario que utilizara el sistema
print("-----Quien utilizara el sistema (Invitado - Administrador)------\n")
user = input("Tipo Usuario: ").lower()
#este while englobara toda la ejecucion dando un maximo de 3 intentos
while mx_intentos > min_intentos:
    #si selecciona como usuario Administrador
    if user == "administrador":
        admin = input("Ingrese su usuario Administrador: ").lower()
        if admin == "admin1":
            pasw_admin = input("Ingrese su contraseña: ").lower()
            if pasw_admin == "admin01":
                #Si ingresa usuario y contraseña correcta toma como rol administrador e indica la hora del sistema
                #tambien le solicitada actualizar la contraseña
                rol = "administrador"
                print("HOLA ADMINISTRADOR")
                print(f"-----Sistema Iniciado el {dia_actual}/{mes_actual}/{anio_actual}-----")
                print("-----Por seguridad debes cambiar tu contraseña...-----")
                new_pasw_admin = input("Ingrese nueva contraseña : ")
                #validamos que la nueva contraseña no sea la misma y tenga mas de 8 coracteres
                if new_pasw_admin == pasw_admin or len(new_pasw_admin) < 8:
                    while mx_intentos > 0:
                        print(f"Error: La contraseña no cumple los requisitos. Tiene {mx_intentos} intentos mas")
                        mx_intentos -= 1
                        new_pasw_admin = input("Ingrese nueva contraseña : ")
                    sistema_activo = False    
                else:
                    pasw_admin = new_pasw_admin
                    print("Contraseña actualizada correctamente.")
                #si cambia la contraseña correctamente rompe el bucle de login para ir al agente
                break
            else:
                print("Contraseña incorrecta")
                mx_intentos -= 1
        else:
            print("Usuario administrador incorrecto")
            mx_intentos -= 1
    #si selecciona usuario invitado
    elif user == "invitado":
        invt = input("Ingrese su usuario Invitado: ").lower()
        if invt == "invt1":
            pasw_invt = input("Ingrese su contraseña: ").lower()
            if pasw_invt == "invt01":
                rol = "invitado"
                print("HOLA INVITADO")
                print("[Fecha Sistema] Este comando requiere privilegios de administrador")
                break # Rompe el bucle de login para ir al agente
            else:
                print("Contraseña incorrecta")
                mx_intentos -= 1
        else:
            print("Usuario invitado incorrecto")
            mx_intentos -= 1
    else:
        print(f"------Ingrese un tipo de usuario permitido tiene {mx_intentos} intentos mas-------")
        mx_intentos -= 1
    if mx_intentos > 0:
        print("\n------Quien utilizara el sistema (Invitado - Administrador)------\n")
        user = input("Tipo Usuario: ").lower()
#si rol es administrador o invitado inicia el agente
if rol is not None and sistema_activo:
    while sistema_activo:
        cmd = input("Agente>: ").lower()
        #salir apaga el sistema con false
        if cmd == "salir":
            print("------Agente apagado. Vuelve pronto.------")
            mensaje = "Se ha solicitado terminar la sesión."
            registro = {
            "comando": cmd,
            "autor": rol, 
            "descripcion": mensaje}
            historial_agente.append(registro)
            sistema_activo = False
        #ping responde pong se guarda el mensaje
        elif cmd == "ping":
            print("pong!")
            mensaje = "Se ha enviado un ping y de respuesta se devolvió un pong."
            registro = {
            "comando": cmd,
            "autor": rol, 
            "descripcion": mensaje}
            historial_agente.append(registro)
        #solicita una palabra cuenta sus vocales y consonantes
        elif cmd == "contar":
            palabra = input("Ingrese una palabra: ").lower()
            tot_letras = len(palabra)
            tot_vocales = 0
            tot_cons = 0
            for p in palabra:
                if p in "aeiou":
                    tot_vocales += 1
                else:
                    tot_cons += 1
            print(f"Palabra: {palabra}\nVocales: {tot_vocales}\nConsonantes: {tot_cons}\nTotal: {tot_letras}")
            mensaje = f"Se solicitó el conteo de la palabra {palabra}, dando como resultados:"
            registro = {
            "comando": cmd,
            "autor": rol, 
            "descripcion": mensaje}
            historial_agente.append(registro)
        #calculadora, solicitamos 2 digitos y el operador se explica en los input, si falla guarda el mensaje
        elif cmd == "calculadora":
            num1 = int(input("Ingrese primer digito: "))
            oprd = input("Ingrese operador (+, -, *, /): ")
            num2 = int(input("Ingrese segundo digito: "))
            if oprd == "+": resultado = num1 + num2
            elif oprd == "-": resultado = num1 - num2
            elif oprd == "*": resultado = num1 * num2
            elif oprd == "/":
                resultado = num1 / num2 if num2 != 0 else "Error: Div por 0"
            else: 
                resultado = "Operador no válido"
                mensaje = "Operador no válido"
                registro = {
                "comando": cmd,
                "autor": rol, 
                "descripcion": mensaje}
                historial_agente.append(registro)
            print(f"El resultado es: {resultado}")
            mensaje = f"Se ejecuto el comando calculadora con el resultado: {resultado}"
            registro = {
            "comando": cmd,
            "autor": rol, 
            "descripcion": mensaje}
            historial_agente.append(registro)
        #en cada mensaje de respuesta el agente aplica un .append agregando a nuestro diccionario las respuestas
        elif cmd == "historial all":
            print("\n--- [HISTORIAL COMPLETO] ---")
            for m in historial_agente:
                print(f"- {m}")
        #la funcion .clar eliminara todo lo del historial
        elif cmd == "historial clear":
            historial_agente.clear()
            print("Historial eliminado.")
        #historial solicita que se ingrese la palabra clave, utilizaremos un for donde realizareme una consulta
        #segun la busqueda, de pende de la respuesta coincidencias sera + o - 1 y imprimira la respuesta
        elif cmd == "historial":
            busqueda = input("Ingresa la palabra clave a buscar:").lower()
            coincidencias = 0
            print("--- [Resultados de búsqueda] ---")
            for memoria in historial_agente:
                if busqueda in memoria["descripcion"].lower():
                    print(f"Autor: {memoria['autor']} | Mensaje: {memoria['descripcion']}")
                    coincidencias += 1
            if coincidencias == 0:
                print("[PseudoAgente] No encontré registros que coincidan con esa palabra.")
        else:
            print("Comando desconocido.")
# Si no se tiene rol al final de los intentos
if rol is None:
    print("------Usuario bloqueado - Cerrando sistema------")