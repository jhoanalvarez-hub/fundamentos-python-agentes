import datetime  #Importamos la herramienta para fechas

#Obtenemos la fecha de HOY desde tu computadora
fecha_actual = datetime.datetime.now()
anio_actual = fecha_actual.year
mes_actual = fecha_actual.month
dia_actual = fecha_actual.day

#declaramos las siguientes variables
mx_intentos = 3
min_intentos = 0
#Declarar None es declarar un espacio pero sin ningun valor
rol = None
#De esta variable depende la ejecucion del agente
sistema_activo = True

#Iniciamos nuestros sistema solicitando el tipo usuario que lo utilizara
print("-----Quien utilizara el sistema (Invitado - Administrador)------\n")
user = input("Tipo Usuario: ").lower()

#Este while englobara toda la ejecucion dando un maximo de 3 intentos
#Aplica para tipo usuario, usuario ingresado y actualizar contraseña
while mx_intentos > min_intentos:
    #Si el tipo usuario es = administrador
    if user == "administrador":
        admin = input("Ingrese su usuario Administrador: ").lower()
        if admin == "admin1":
            pasw_admin = input("Ingrese su contraseña: ").lower()
            if pasw_admin == "admin01":
                #se declara rol como adminisrador
                rol = "administrador"
                #Si logra llegar a este punto imprime mensaje de bienvenida con hora del sistema, aplica unicamente para administrador
                print("HOLA ADMINISTRADOR")
                print(f"-----Sistema Iniciado el {dia_actual}/{mes_actual}/{anio_actual}-----")
                #solicita actualizar la contraseña
                print("-----Por seguridad debes cambiar tu contraseña, esta no puede ser igual a la anterior, debe tener como minimo 8 caracteres-----")
                new_pasw_admin = input("Ingrese nueva contraseña : ")
                #Aplica las 2 reglas "No puede ser igual a la anterior", "Mínimo 8 caracteres"
                if new_pasw_admin == pasw_admin or len(new_pasw_admin) < 8:
                    #Mientras tenga intento solicitara la contraseña
                    while mx_intentos > 0:
                        print("Error: La contraseña es igual a la anterior o tiene menos de 8 caracteres.")
                        mx_intentos -= 1
                        new_pasw_admin = input("Ingrese nueva contraseña : ")
                    #Si despues de 3 intentos la contraseña no cambia correctamente, bloquea usuario y cierra sistema
                    print("------Usuario bloqueado - Cerrando sistema------")
                    sistema_activo = False    
                else:
                    # Si pasa las validaciones, actualizamos la contraseña
                    pasw_admin = new_pasw_admin
                    print("Contraseña actualizada correctamente.")
                #Inicia el agente del administrador
                while sistema_activo:
                    #Inicia agente, espera el comando CMD - Administrador
                    cmd = input("Agente>: ").lower()
                    if cmd == "salir":
                        print("------Agente apagado. Vuelve pronto.------")
                        sistema_activo = False
                    elif cmd == "ping":
                        print("pong!")
                    elif cmd =="contar":
                        palabra = input("Ingrese una palabra: ").lower()
                        tot_letras = len(palabra)
                        tot_vocales = 0
                        tot_cons = 0
                        for p in palabra:
                            if p in "aeiou":
                                tot_vocales +=1
                            else:
                                tot_cons +=1
                        print(f"Palabra ingresada: {palabra}")
                        print(f"Total de vocales: {tot_vocales}")
                        print(f"Total de consonantes: {tot_cons}")
                        print(f"Total de letras: {tot_letras}")
                    #Inicia calculadora, solicita los 2 caracteres numericos y la operacion
                    elif cmd == "calculadora":
                        num1 = int(input("Ingrese primer digito numerico: "))
                        oprd = str(input("Ingrese operador (+, -, *, /): "))
                        num2 = int(input("Ingrese segundo digito numerico: "))
                        #Segun el operador ingresado realiza operacion
                        if oprd == "+":
                            resultado = num1 + num2
                        elif oprd == "-":
                            resultado = num1 - num2
                        elif oprd == "*":
                            resultado = num1 * num2
                        elif oprd == "/":
                                #No es posible dividir por 0
                                if num2 != 0:
                                    resultado = num1 / num2
                                else:
                                    resultado = "Error: No se puede dividir por cero"
                        else:
                                #Si el comando ingresado no es valido finaliza calculadora pero continua en consola
                                resultado = "Operador no válido"
                        #Imprime el resultado de la calculadora si logro realizar la operacion correctamente
                        print(f"El resultado es: {resultado}")
                    else:
                        print("------Comando desconocido. Intente de nuevo.-------")
                break
            else:
                print("Contraseña incorrecta")
                mx_intentos -= 1
        else:
            print("Usuario administrador incorrecto")
            mx_intentos -= 1
    #Si el tipo usuario es = Invitado
    elif user == "invitado":
        invt = input("Ingrese su usuario Invitado: ").lower()
        if invt == "invt1":
            pasw_invt = input("Ingrese su contraseña: ").lower()
            if pasw_invt == "invt01":
                #Se declara rol como invitado
                rol = "invitado"
                print("HOLA INVITADO")
                print("[Fecha Sistema] Este comando requiere privilegios de administrador")
                #inicia el sistema para inivitado es el mismo que administrador
                while sistema_activo:
                    #Inicia agente, espera el comando CMD - invitado
                    cmd = input("Agente>: ").lower()
                    if cmd == "salir":
                        print("------Agente apagado. Vuelve pronto.------")
                        sistema_activo = False
                        break
                    elif cmd == "ping":
                        print("pong!")
                    elif cmd =="contar":
                        palabra = input("Ingrese una palabra: ").lower()
                        tot_letras = len(palabra)
                        tot_vocales = 0
                        tot_cons = 0
                        for p in palabra:
                            if p in "aeiou":
                                tot_vocales +=1
                            else:
                                tot_cons +=1
                        print(f"Palabra ingresada: {palabra}")
                        print(f"Total de vocales: {tot_vocales}")
                        print(f"Total de consonantes: {tot_cons}")
                        print(f"Total de letras: {tot_letras}")
                    #Inicia calculadora, solicita los 2 caracteres numericos y la operacion
                    elif cmd == "calculadora":
                        num1 = int(input("Ingrese primer digito numerico: "))
                        oprd = str(input("Ingrese operador (+, -, *, /): "))
                        num2 = int(input("Ingrese segundo digito numerico: "))
                        #Segun el operador ingresado realiza operacion
                        if oprd == "+":
                            resultado = num1 + num2
                        elif oprd == "-":
                            resultado = num1 - num2
                        elif oprd == "*":
                            resultado = num1 * num2
                        elif oprd == "/":
                                #No es posible dividir por 0
                                if num2 != 0:
                                    resultado = num1 / num2
                                else:
                                    resultado = "Error: No se puede dividir por cero"
                        else:
                                #Si el comando ingresado no es valido finaliza calculadora pero continua en consola
                                resultado = "Operador no válido"
                        #Imprime el resultado de la calculadora si logro realizar la operacion correctamente
                        print(f"El resultado es: {resultado}")
                    else:
                        print("------Comando desconocido. Intente de nuevo.-------")
                break
            #Si intentos es >= continuara solicitando la contraseña admin e invitado
            else:
                print("Contraseña incorrecta")
                mx_intentos -= 1
        #Si intentos es >= 1 continuara solicitando el tipo usuario
        else:
            print("Usuario invitado incorrecto")
            mx_intentos -= 1
    else:
        #Tipo usuario muestra la cantidad de intentos que le quedan al usuario
        print(f"------Ingrese un tipo de usuario permitido tiene {mx_intentos} intentos mas-------")
        mx_intentos -= 1
    if mx_intentos > 0:
        print("\n------Quien utilizara el sistema (Invitado - Administrador)------\n")
        user = input("Tipo Usuario: ").lower()
#Si no se tiene rol, es decir si no se loguea como administrador o invitado se cerrara el sistema
if rol is None:
    print("------Usuario bloqueado - Cerrando sistema------")