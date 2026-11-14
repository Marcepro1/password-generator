import os
import time
import random
import subprocess

#result = subprocess.getoutput("nmap")
#resultSplit = result.split()

def win():
    print()
    print(" Este Programa No Funciona En Windows ")
    print()
    enter()

def enter():
    enter = input(" pulse Enter ")

#################
nombre = ""
apellido = ""
edad = ""
mascotas = []
fechas = []
extras = []

#################
# configuracion #

cantidad = 100
contraseña_prueba = ""
system = "linux"
total = []
rnd = ["qwerty", "asdfgh", "zxcvbn", "qwerty123", "1q2w3e", "_", "@123", "2026", "contraseña", "Contraseña", "password", "Password", "321", "admin123", "Admin123", "admin"]
años = ["2026", "26", "_2026", "_26"]

#################

# 1. Lista original extendida (~600 elementos)
most_popular = [
    # Secuencias numéricas
    "123456", "123456789", "12345678", "12345", "1234567", "1234567890", "1234", "123123", "111111", 
    "000000", "000000000" "123321123", "666666666", "777777777", "555555555", "888888888", "12345678910", "654321", "987654321", 
    "112233", "121212", "12341234", "1234567890a", "123456a", "1234567a", "12345678a", "00000", "111111111", 
    "222222222", "333333333", "444444444", "999999999", "123456789b", "123456789c", "123456789d", "1234567891", 
    "1234567899", "12345678900", "123456789123", "102030", "123456789!", "123456!", "123456?", "123456.",
    "0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "12345678901",
    "13579", "24680", "11223344", "1122334455", "0123456789", "9876543210", "123123123", "11111111",
    
    # Sistema, Admin y Acceso
    "password", "admin", "admin123", "pass123", "administrator", "root", "user", "guest", "client", 
    "system", "service", "support", "test", "demo", "welcome", "login", "secret", "master", "access", 
    "default", "change", "changeme", "public", "private", "oracle", "cisco", "telecom", "admintelecom", 
    "admin1234", "admin1", "admin2023", "admin2024", "admin2025", "admin2026", "pass", "password1", 
    "Password123", "Pass123", "P@ssw0rd", "P@ssword", "Pass@123", "Admin@123", "Aa123456", "Aa@123456",
    "superuser", "supervisor", "operator", "manager", "webmaster", "host", "network", "firewall",
    "security", "root123", "roottoor", "toor", "adm", "adm123", "sysadmin", "itadmin", "helpdesk",
    
    # Teclado / Patrones físicos
    "qwerty", "qwertyuiop", "qwerty123", "qwerty1", "qazwsx", "1q2w3e4r", "1q2w3e4r5t", "1qaz2wsx", 
    "zxcvbnm", "asdfghjkl", "azerty", "zaq1zaq1", "123qwe", "qwe123", "asdf", "zxcvbn", "1q2w3e", 
    "q1w2e3r4", "1q2w3e4r5t6y", "w2e3r4t5", "1a2b3c", "a1b2c3", "abc123", "abcd123", "abcdef", "abcdefg",
    "qwertyuiopasdfghjklzxcvbnm", "asdfghjk", "zxcvbnmasdfghjkl", "qweasdzxc", "1q2w3e4r5t6y7u8i9o0p",
    "poiuytrewq", "mnbvcxz", "lkjhgfdsa", "ytrewq", "trewq", "asdfgh", "zxcvb", "1qazxsw2", "wsxedc",
    
    # Español / Nombres comunes
    "contrasena", "contraseña", "clave", "clave123", "hola", "holamundo", "bienvenido", "bienvenida", 
    "gracias", "tequiero", "familia", "amor", "teamo", "teamo123", "argentina", "mexico", "colombia", 
    "espana", "chile", "peru", "venezuela", "madrid", "barcelona", "guadalajara", "monterrey", "santiago", 
    "lima", "bogota", "buenosaires", "futbol", "realmadrid", "barca", "boca", "river", "america", 
    "chivas", "colo", "juan", "maria", "jose", "carlos", "ana", "luis", "pedro", "sofia", "mateo",
    "valeria", "lucia", "alejandro", "gabriel", "daniela", "carmen", "antonio", "francisco", "manuel",
    "jesus", "david", "daniel", "rafael", "jorge", "alberto", "miguel", "angel", "fernando", "pablo",
    "sara", "elena", "laura", "carmen", "claudia", "paula", "andrea", "marta", "patricia", "beatriz",
    "teamoamor", "amoroso", "micorazon", "miamor", "sol", "luna", "estrellita", "gatito", "perrito",
    
    # Inglés / Nombres globales
    "iloveyou", "monkey", "dragon", "baseball", "football", "trustno1", "mustang", "shadow", "sunshine", 
    "superman", "batman", "princess", "charlie", "michael", "jordan", "jessica", "ashley", "daniel", 
    "andrew", "david", "alexander", "starwars", "flower", "freedom", "hottie", "lovely", "whatever", 
    "donald", "ninja", "pokemon", "disney", "cookie", "matrix", "maggie", "harley", "chevy", "dodge",
    "basketball", "soccer", "hockey", "liverpool", "arsenal", "chelsea", "manchester", "barcelona",
    "titanic", "matrix", "pokemon", "naruto", "dragonball", "goku", "masterchief", "playstation", "xbox",
    "robert", "william", "richard", "thomas", "christopher", "charles", "matthew", "anthony", "mark",
    "elizabeth", "sarah", "karen", "nancy", "lisa", "betty", "margaret", "sandra", "ashley", "emily",
    
    # Variaciones con años y marcas
    "password123", "password01", "password2023", "password2024", "password2025", "password2026", 
    "google", "facebook", "youtube", "twitter", "instagram", "android", "iphone", "apple", "samsung", 
    "microsoft", "windows", "linux", "ubuntu", "myspace", "yahoo", "skype", "spotify", "netflix", 
    "amazon", "trustno", "internet", "online", "network", "server", "domain", "company", "office",
    "admin2020", "admin2021", "admin2022", "admin2023", "admin2024", "admin2025", "admin2026",
    "pass2020", "pass2021", "pass2022", "pass2023", "pass2024", "pass2025", "pass2026",
    "clave2020", "clave2021", "clave2022", "clave2023", "clave2024", "clave2025", "clave2026",
    "1234562024", "1234562025", "1234562026", "qwerty2024", "qwerty2025", "qwerty2026",
    "letmein", "letmein1", "letmein123", "open sesame", "masterkey", "keylogger", "hellothere",
    "matrix123", "shadow1", "sunshine1", "pepper1", "buster", "bailey", "lucky", "rocky", "teddy",
    "coco", "chloe", "daisy", "simba", "angel", "jack", "oliver", "lucy", "lily", "ruby", "gizmo",
    
    # Extensiones adicionales
    "abc12345", "qwerty12345", "asdfghjk", "zxcvbnmlkjhg", "112233445566", "0987654321",
    "qweasd", "asdzxc", "zxcqwe", "qazwsxedc", "wsxedcrfv", "edcrfvtgb", "rfvtgbyhn",
    "qwe123rty456", "asd789fgh", "zxc456vbn", "1q2w3e4r5t6y7u8i9o0p", "plokmijnuhbygvtfcrdxeswaq",
    "password!", "password@", "password#", "password$", "password%", "password&", "password*",
    "admin!", "admin@", "admin#", "admin$", "admin%", "admin123!", "admin123@", "admin123#",
    "system123", "system1", "system2024", "system2025", "system2026", "root1234", "root2024",
    "guest123", "guest1", "user123", "user1", "user2024", "user2025", "user2026", "test123",
    "test1234", "test2024", "test2025", "test2026", "demo123", "demo2024", "demo2025", "demo2026"
]

caracteres = ["-", "/", "&", "%", "$", "#", "@", "!", "=", "_"]
combinaciones = ["x_", "x", "X_", "X", "v", "V", "V_", "V" "123"]
separador = "_"

def generador():
    global nombre
    global apellido
    global edad
    global mascotas
    global fechas
    global extras
    global cantidad
    global contraseña_prueba
    global system
    global total

    pared = 0
    contador = 0
    todos = []
    contra = ""
    count = 0

    combinar = [
    random.choice(combinaciones) + contra, random.choice(caracteres) + contra, random.choice(rnd) + contra,
    random.choice(años) + contra, separador + contra
    ]

    while True:

        mostazar = random.randint(0, 20)

        azar1 = random.randint(1, 50)
        azar2 = random.randint(1, 50)
        azar3 = random.randint(1, 50)
        azar4 = random.randint(1, 50)

        azar5 = random.randint(0, 50)
        azar6 = random.randint(0, 50)
        azar7 = random.randint(0, 50)
        azar8 = random.randint(0, 50)

        azar9 = random.randint(0, 50)
        azar10 = random.randint(0, 50)

        if len(todos) > cantidad:
            break

        # ============ Generar Solo Primera Parte ============= #
        # ==== Ejemplo: Juan, Gimenez, 2010, Mascota, etc. ==== #
        # ===================================================== #
        if azar1 <= 15:
            if azar2 <= 5:
                if nombre != "":
                    contra = nombre
            if azar2 >= 6 and azar2 <= 10:
                if apellido != "":
                    contra = apellido
            if azar2 >= 11 and azar2 <= 16:
                if edad != "":
                    contra = edad
            if azar2 >= 17 and azar2 <= 22:
                if mascotas != []:
                    contra = random.choice(mascotas)
            if azar2 >= 23 and azar2 <= 29:
                if fechas != []:
                    contra = random.choice(fechas)
            if azar2 >= 30 and azar2 <= 39:
                if extras != []:
                    contra = random.choice(extras)
            if azar2 >= 40 and azar2 <= 43:
                contra = random.choice(caracteres)
            if azar2 >= 44 and azar2 <= 50:
                contra = random.choice(combinaciones)
            azarbreve = random.randint(1, 20)
            if contra == "":
                continue

            # ====================================================== #
            # ======================= FIN ========================== #
            # ====================================================== #



            # =============== GENERAR SEGUNDA PARTE ================ #
            # =========== EJEMPLOS ============ #
            # === 2010_jose = jose_2010 === #
            # === jose_pro = pro_jose  === # 
            # ========= ============= ========= #

            if azar4 >= 5 and azar4 <= 50:
                azarseparador = random.randint(0,20)
                if azarseparador <= 13:
                    contra = contra + separador
                if azar3 <= 5 and contra != nombre:
                    if nombre != "":
                        contra = contra + nombre
                if azar3 >= 6 and azar3 <= 10 and contra != apellido:
                    if apellido != "":
                        contra = contra + apellido
                if azar3 >= 11 and azar3 <= 16 and contra != edad:
                    if edad != "":
                        contra = contra + edad
                if azar3 >= 17 and azar3 <= 22:
                    if mascotas != []:
                        lisc = []
                        for i in mascotas:
                            lisc.append(i)
                        if contra not in lisc:
                            contra = contra + random.choice(lisc)
                        lisc = []
                if azar3 >= 23 and azar3 <= 29:
                    if fechas != []:
                        lis = []
                        for i in fechas:
                            lis.append(i)
                        if contra not in lis:
                            contra = contra + random.choice(lis)
                        lis = []
                if azar3 >= 30 and azar3 <= 39:
                    if extras != []:
                        li = []
                        for i in extras:
                            li.append(i)
                        if contra not in li:
                            contra = contra + random.choice(li)
                        li = []
                if azar3 >= 40 and azar3 <= 44:
                    contra = contra + random.choice(caracteres)
                if azar3 >= 45 and azar3 <= 49:
                    contra = contra = random.choice(combinaciones)
                azarbreve = random.randint(1, 20)
                if azarbreve <= 2:
                    continue

            # ====================================================== #
            # ======================== FIN ========================= #
            # ====================================================== #



            # =============== GENERAR TERCERA PARTE ================ #
            # ==================== EJEMPLOS ======================== #
            # @jose_villalba - 123_josevillalba - #_123jose - tom_jose123
            # jose_@_123 - @jose_321 - @JOSE_VILLALBA - tom@villalba
            # ====================================================== #

            if azar5 >= 25 and azar5 <= 50:
                tercero = random.randint(0,20)
                if tercero <= 5:
                    contra = random.choice(rnd) + contra
                if tercero >= 6 and tercero <= 11:
                    contra = random.choice(años) + contra
                if tercero >= 12 and tercero <= 16:
                    contra = random.choice(combinaciones) + contra
                if tercero >= 17:
                    contra = random.choice(caracteres) + contra

            # ==================================================== #
            # ==================== FIN =========================== #
            # ==================================================== #










            # =============== GENERADOR DIFERENTE ================ #
            # ================= EJEMPLOS ========================= #
            # marcelotom_2026 - marcepro_2026 - marceV_2026

            # ================== PRIMER BLOQUE =================== #
            # ========= SELECCIONAR DATO ALEATORIO =============== #
            if azar6 <= 35:
                contra = ""
                if azar7 <= 10:
                    if nombre != "":
                        contra = nombre
                if azar7 >= 11 and azar7 <= 16:
                    if apellido != "":
                        contra = apellido
                if azar7 >= 17 and azar7 <= 22:
                    if edad != "":
                        contra = edad
                if azar7 >= 23 and azar7 <= 29:
                    if mascotas != []:
                        contra = random.choice(mascotas)
                if azar7 >= 30 and azar7 <= 40:
                    if extras != []:
                        contra = random.choice(extras)
                if azar7 >= 41 and azar7 <= 47:
                    if fechas != []:
                        contra = random.choice(fechas)
                if azar7 >= 48:
                    contra = random.choice(años)

                # ============== SEGUNDO BLOQUE ============= #
                # EJ: marcetom - marcelotom - marcepro - marceloPRO
                azar_sep = random.randint(0, 10)
                if azar_sep <= 3:
                    contra = contra + separador

                if azar8 <= 7:
                    if nombre != "" and contra != nombre:
                        contra = contra + nombre
                if azar8 >= 8 and azar8 <= 14:
                    if apellido != "" and contra != apellido:
                        contra = contra + apellido
                if azar8 >= 15 and azar8 <= 21:
                    if edad != "" and contra != edad:
                        contra = contra + edad
                if azar8 >= 22 and azar8 <= 30 and mascotas != []:
                    #mascotas
                    mascotas_list = []
                    for i in mascotas:
                        if i == contra:
                            continue
                        mascotas_list.append(i)
                    if mascotas_list != []:
                        contra = contra + random.choice(mascotas_list)
                if azar8 >= 30 and azar8 <= 37 and fechas != []:
                    #fechas
                    fechas_list = []
                    for i in fechas:
                        if i == contra:
                            continue
                        fechas_list.append(i)
                    if fechas_list != []:
                        contra = contra + random.choice(fechas_list)
                if azar8 >= 38 and extras != []:
                    #extras
                    extras_list = []
                    for i in extras:
                        if i == contra:
                            continue
                        extras_list.append(i)
                    if extras_list != []:
                        contra = contra + random.choice(extras_list)

                # ============== BLOQUE FINAL ============= #
                if azar9 <= 24:
                    azar_separador = random.randint(0,10)
                    if azar_separador <= 5:
                        contra = contra + separador

                    if azar10 <= 10:
                        contra = contra + random.choice(rnd)
                    if azar10 >= 11 and azar10 <= 20 and extras != []:
                        contra = contra + random.choice(extras)
                    if azar10 >= 21 and azar10 <= 30 and fechas != []:
                        contra = contra + random.choice(fechas)
                    if azar10 >= 31 and azar10 <= 40 and mascotas != []:
                        contra = contra + random.choice(mascotas)
                # ================ FINAL ================ #







# =========================== ACTIVAR AL TERMINAR =========================== #
#        if len(contra) < 8:
#            while True:
#                azarz = random.randint(0,10)
#                if azarz <= 5:
#                    contra = contra + separador
#                azarcc = random.randint(0, 20)
#                if azarcc <= 3:
#                    contra = contra + random.choice(combinaciones)
#                if azarcc >= 4 and azarcc <= 7:
#                    contra = contra + random.choice(caracteres)
#                if azarcc >= 13 and azarcc <= 16:
#                    contra = contra + random.choice(rnd)
#                if azarcc >= 17:
#                    contra = contra + random.choice(años)
#                if len(contra) >= 8:
#                    break

        if contra in todos:
#            count += 1
#            if count >= 3:
            contra = ""
#                count = 0
            continue
        if contra == "":
            continue
        todos.append(contra)
        contra = ""
        continue



    nombb = "generados.txt"

    if os.path.exists(nombb):
        nombb = f"generados{random.randint(1,999)}.txt"

    with open(nombb, "w") as archivo:
        for i in todos:
            archivo.write(i + "\n")



    for i in todos:
        contador += 1
        print(" ",contador,i)
        if i == contraseña_prueba:
            print()
            print(" Contraseña Adivinada /",i,">",contraseña_prueba)
            print()
            enter()
            return
    print()
    enter()
    return


def menu():
    global nombre
    global apellido
    global edad
    global mascotas
    global fechas
    global extras
    global cantidad
    global contraseña_prueba
    global system
    global total
    while True:
        try:
            os.system("clear")
            print(" ==================")
            print(" Contraseña de Prueba:",contraseña_prueba)
            print(" Cantidad:",cantidad)
            print(" ==================")
            print(" [1] - Nombre ")
            print(" [2] - Apellido ")
            print(" [3] - Edad ")
            print(" [4] - Mascotas [lista]")
            print(" [5] - Fechas [lista]")
            print(" [6] - Extras [lista]")
            print(" ==================")
            for i in total:
                print(" ",i)
            print(" ==================")
            print(" [7] - Contraseña de prueba ")
            print(" [8] - Cantidad ")
            print(" [9] - Generar ")
            print(" [10] - borrar todo ")
            print(" [0] - Salir ")
            print(" ==================")
            print()

            trm = int(input(" >> "))
            if trm == 10:
                nombre = ""
                apellido = ""
                edad = ""
                mascotas = []
                fechas = []
                extras = []
                total = []
                continue
            if trm == 0:
                break
            if trm == 1:
                n = input(" Nombre: ")
                if n == "":
                    continue
                nombre = n
                total.append(n)

            if trm == 2:
                a = input(" Apellido: ")
                if a == "":
                    continue
                apellido = a
                total.append(a)

            if trm == 3:
                e = input(" Edad: ")
                if e == "":
                    continue
                edad = e
                total.append(e)

            if trm == 4:
                m = input(" Mascotas: ")
                if m == "":
                    continue
                mascotas.append(m)
                total.append(m)

            if trm == 5:
                f = input(" Fechas: ")
                if f == "":
                    continue
                fechas.append(f)
                total.append(f)

            if trm == 6:
                e = input(" Extras: ")
                if e == "":
                    continue
                extras.append(e)
                total.append(e)

            if trm == 7:
                p = input(" Contraseña de Prueba: ")
                if p == "":
                    continue
                contraseña_prueba = p

            if trm == 8:
                try:
                    c = int(input(" Cantidad: "))
                    if c < 1:
                        print()
                        print(" error ")
                        enter()
                        continue
                    cantidad = c
                except ValueError:
                    print()
                    print(" Utilize Numeros ")
                    print()
                    enter()

            if trm == 9:
                generador()

        except ValueError:
            print()
            print(" Seleccine con numeros ")
            print()
            enter()


def seleccion():
    while True:
        try:
            os.system("clear")
            print()
            print(" [0] - salir ")
            print(" [1] - Windows")
            print(" [2] - Linux")
            print()

            trm = int(input(" >> "))
            if trm == 0:
                break
            if trm == 1:
                win()
            if trm == 2:
                menu()
        except ValueError:
            print()
            print(" Utiliza Numeros ")
            print()
            enter()

seleccion()
