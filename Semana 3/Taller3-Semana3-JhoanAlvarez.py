import datetime  # Traemos la herramienta para manejar el reloj del sistema

# SECCIÓN DE FUNCIONES

# Esta función es el "loguin" del sistema. Revisa si puede continuar al pseudoagente
def login(tipo_user: str, user: str, passwrd: str) -> dict:
    # Nuestra pequeña lista de usuarios permitidos
    credenciales = {
        "administrador": {"user": "admin1", "pass": "admin01", "desc": "Privilegios de Administrador activados."},
        "invitado": {"user": "invt1", "pass": "invt01", "desc": "Modo Invitado."}
    }
    
    # Primero vemos si el tipo de usuario (admin o invitado) existe en la lista
    if tipo_user in credenciales:
        datos = credenciales[tipo_user]
        # Luego comparamos si el nombre y la clave coinciden con lo guardado
        if user == datos["user"] and passwrd == datos["pass"]:
            # Si todo está bien, devolvemos un (un diccionario)
            return {"acceso": True, "rol": tipo_user, "descripcion": f"[Sistema] Acceso concedido. {datos['desc']}"}
    
    # Si algo falla, avisamos que no hay entrada
    return {"acceso": False, "rol": None, "descripcion": "[Error] Credenciales incorrectas."}

# Herramienta para que el Admin vea la hora (El invitado no tiene permiso)
def obtener_fecha(rol: str) -> str:
    if rol == "administrador":
        ahora = datetime.datetime.now()
        fecha_txt = ahora.strftime("%d/%m/%Y %H:%M:%S") # le damos formaro: Día/Mes/Año
        print(f"[INFO] Fecha y hora: {fecha_txt}")
        return f"Consulta de fecha exitosa: {fecha_txt}"
    
    print("[Acceso Denegado] Solo administradores pueden usar esto.")
    return "Intento fallido de consultar fecha (Sin permisos)."

# Herramienta para contar las palabras
def contar_letras() -> str:
    palabra = input("Ingrese una palabra: ").strip().lower()
    # Contamos vocales una por una
    vocales = sum(1 for p in palabra if p in "aeiouáéíóú")
    # Contamos consonantes
    consonantes = sum(1 for p in palabra if p.isalpha() and p not in "aeiouáéíóú")
    
    print(f"Resultados -> Vocales: {vocales} | Consonantes: {consonantes}")
    return f"Conteo en '{palabra}': {vocales} V, {consonantes} C."

# Calculadora básica
def ejecutar_calculadora() -> str:
    try:
        n1 = float(input("Primer número: "))
        op = input("Operador (+, -, *, /): ").strip()
        n2 = float(input("Segundo número: "))
        
        # Elegimos la operación según el símbolo
        if op == "+": res = n1 + n2
        elif op == "-": res = n1 - n2
        elif op == "*": res = n1 * n2
        elif op == "/": 
            # Evitamos que el programa se rompa si intentan dividir por cero
            res = n1 / n2 if n2 != 0 else "Error: No se puede dividir por 0"
        else: return "Operador no válido"
        
        print(f"Resultado: {res}")
        return f"Calculadora: {n1} {op} {n2} = {res}"
    except ValueError:
        # Si el usuario escribe letras en vez de números, capturamos el error aquí
        print("[Error] ¡Solo puedes ingresar números!")
        return "Error en calculadora: entrada no numérica."

# Función para ver qué hemos estado haciendo con un historial
def mostrar_historial(historial: list, busqueda: str = None):
    print(f"\n--- {'BÚSQUEDA' if busqueda else 'HISTORIAL COMPLETO'} ---")
    encontrados = False
    
    for i, m in enumerate(historial, 1):
        # Si no hay búsqueda, muestra todo. Si hay, filtra por el mensaje.
        if not busqueda or busqueda in m["descripcion"].lower():
            print(f"{i}. [{m['autor']}] {m['comando'].upper()}: {m['descripcion']}")
            encontrados = True
            
    if not encontrados:
        print("No hay registros que mostrar.")

# Variables de ejecucion
mx_intentos = 3          # Límite de errores permitidos
rol_usuario = None       # Aquí guardaremos quién entró (admin o invitado)
sistema_activo = False   # Esta variable controla si el programa sigue funcionando
historial_agente = []    # Nuestra "caja" donde guardaremos los logs de cada acción

#Inicio Loguin
print("----- Login de Sistema -----\n")
tipo_solicitado = input("Tipo Usuario: ").strip().lower()

# BUCLE DE LOGIN: Se repite mientras queden intentos y no hayamos entrado
while mx_intentos > 0 and not sistema_activo:
    usuario = input("Usuario: ").strip().lower()
    password = input("Contraseña: ").strip()
    
    # Le pedimos a la función 'login' que revise los datos
    resultado = login(tipo_solicitado, usuario, password)

    if resultado["acceso"]:
        print(resultado["descripcion"])
        sistema_activo = True       # ¡Entramos! El sistema se activa
        rol_usuario = resultado["rol"] # Guardamos el rol para saber qué permisos tiene
    else:
        mx_intentos -= 1
        print(f"{resultado['descripcion']} Intentos restantes: {mx_intentos}")

# BUCLE DEL AGENTE: Solo inicia si el login fue exitoso
if sistema_activo:
    while sistema_activo:
        cmd = input(f"\n{rol_usuario}@agente>: ").strip().lower()
        msg_log = "" # Aquí guardaremos lo que pasó para el historial

        if cmd == "salir":
            print("Cerrando sesión...")
            sistema_activo = False # Apagamos el bucle
            msg_log = "Sesión terminada por el usuario."
            
        elif cmd == "fecha":
            msg_log = obtener_fecha(rol_usuario)
            
        elif cmd == "ping":
            print("pong!")
            msg_log = "El usuario envió un ping exitoso."
            
        elif cmd == "contar":
            msg_log = contar_letras()
            
        elif cmd == "calculadora":
            msg_log = ejecutar_calculadora()
            
        elif cmd == "historial all":
            mostrar_historial(historial_agente)
            continue # 'continue' salta el resto del bucle para no guardar este comando en el historial
            
        elif cmd == "historial":
            q = input("Palabra clave a buscar: ").lower()
            mostrar_historial(historial_agente, q)
            continue
            
        elif cmd == "historial clear":
            historial_agente.clear()
            print("Historial borrado con éxito.")
            continue
            
        else:
            print("Comando no reconocido. Intenta de nuevo.")
            continue

        # Si el comando generó una acción, la guardamos en nuestra lista
        if msg_log:
            historial_agente.append({
                "comando": cmd,
                "autor": rol_usuario, 
                "descripcion": msg_log
            })