# Llamamos nuestro agente.py
from agente import PseudoAgente

def realizar_login():
    # Lista de usuarios permitidos (administrador - invitado)
    usuarios = {
        "administrador": {"user": "admin1", "pass": "admin01"},
        "invitado": {"user": "invt1", "pass": "invt01"}
    }
    
    intentos = 3
    print("----- INICIO DE SESION -----")
    tipo = input("Tipo (administrador/invitado): ").lower()

    # Bucle para pedir la clave 3 veces
    while intentos > 0:
        u = input("Usuario: ")
        p = input("Clave: ")

        # Revisamos si los datos estan en nuestra lista
        if tipo in usuarios and u == usuarios[tipo]["user"] and p == usuarios[tipo]["pass"]:
            print("Acceso concedido como " + tipo)
            return tipo # Devolvemos el rol para saber quien es
        
        intentos = intentos - 1
        print("Error. Te quedan " + str(intentos) + " intentos.")
    
    return None # Si llega aqui es porque fallo

def iniciar():
    # Primero corre el login
    rol_logueado = realizar_login()

    if rol_logueado != None:
        # Si el login funciono, creamos al agente
        mi_agente = PseudoAgente(rol_logueado)
        vivo = True

        # El menu principal
        while vivo == True and mi_agente.tokens > 0:
            print("\nAgente: " + mi_agente.nombre + " | Tokens: " + str(mi_agente.tokens))
            print("1. Fecha | 2. Contar | 3. Calculadora | 4. Dado | 5. Historial | 6. Ping | 7.Salir")
            
            op = input("Elige una opcion: ")

            if op == "1":
                res = mi_agente.fecha_hoy()
                print(res)
                mi_agente.gestionar_historial("Consulto fecha")

            elif op == "2":
                t = input("Escribe la palabra: ")
                res = mi_agente.contar_letras(t)
                print(res)
                mi_agente.gestionar_historial("Conto letras")

            elif op == "3":
                try:
                    n1 = float(input("Num 1: "))
                    signo = input("Signo: ")
                    n2 = float(input("Num 2: "))
                    res = mi_agente.ejecutar_calculadora(n1, signo, n2)
                    print("Resultado: " + res)
                    mi_agente.gestionar_historial("Uso calculadora")
                except:
                    print("Escribe solo numeros.")

            elif op == "4":
                res = mi_agente.lanzar_dado()
                print(res)
                mi_agente.gestionar_historial("Uso el dado")

            elif op == "5":
                # Muestra todo lo que se guardo en la lista del agente
                print("--- HISTORIAL ---")
                for h in mi_agente.historial_chat:
                    print(h["hora"] + " -> " + h["accion"])

            elif op == "6":
                res = mi_agente.hacer_ping()
                print(res)
                mi_agente.gestionar_historial("Hizo ping")

            elif op == "7":
                print("Cerrando...")
                vivo = False

            else:
                print("Opcion no valida.")

            # Si se acaba la energia, el while se detiene solo
            if mi_agente.tokens <= 0:
                print("\n!!! AGENTE AGOTADO. SISTEMA APAGADO !!!")

    else:
        print("No pudiste entrar al sistema.")

if __name__ == "__main__":
    iniciar()