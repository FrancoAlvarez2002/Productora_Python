import os.path
import pickle
import random



class Pelicula:
    # tipo (1, 5) , forma(0,2), id_pais(0, 19)
    # 1: acción, 2: comedia, 3: drama, 4: Thriller, 5: Romantico etc.)
    def __init__(self, id, titulo, importe, tipo, id_pais):
        self.id = id
        self.titulo = titulo
        self.importe = importe
        self.tipo = tipo
        self.id_pais = id_pais

    def __str__(self):
        # self.tipo = 0 1 2 3 4
        tipo_str = tipo_to_str(self.tipo)

        cad = "ID: " + str(self.id)
        cad += " | Titulo: " + self.titulo
        cad += " | Importe: " + str(self.importe)
        cad += " | Tipo: " + tipo_str
        cad += " | ID Pais: " + str(self.id_pais)
        return cad


def tipo_to_str(tipo):
    # tipo =         1-1           2       3           4           5-1
    #               0           1           2       3           4
    tipos_pelis = ["Acción", "Comedia", "Drama", "Thriller", "Romantico"]
    return tipos_pelis[tipo-1]


# ==================================================================================
#                       Opcion 1
# ==================================================================================
def validar_n():
    n = int(input("Ingresar cantidad de peliculas a cargar: "))
    while n <= 0:
        n = int(input("Ingresar cantidad de peliculas a cargar (debe ser un valor positivo): "))
    return n


def validar_titulo(v_peli, titulo):
    # Funcion para Validar que no se repitan los titulos.
    for i in v_peli:
        if i.titulo == titulo:
            return True
    return False


def cargar_arreglo(v_peli, n):
    titulos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):  # n = 3         0       1       2
        id = random.randint(1, 10)

        titulo = random.choice(titulos) + str(random.randint(0, 9))
        while validar_titulo(v_peli, titulo):
            titulo = random.choice(titulos) + str(random.randint(0, 9))

        importe = round(random.uniform(0.1, 10), 2)
        tipo = random.randint(1, 5)
        id_pais = random.randint(0, 19)

        peli = Pelicula(id, titulo, importe, tipo, id_pais)
        add_in_order(v_peli, peli)





def add_in_order(v_peli, peli):         
    izq, der = 0, len(v_peli) - 1       

    while izq <= der:
        c = (izq + der) // 2
        if v_peli[c].titulo == peli.titulo:
            pos = c
            break
        elif v_peli[c].titulo > peli.titulo:        
            der = c - 1                             
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    
    v_peli[pos:pos] = [peli]


# ==================================================================================
#                       Opcion 2
# ==================================================================================
def mostrar_datos(v_peli):
    for i in v_peli:
        print(i)


# ==================================================================================
#                       Opcion 3
# ==================================================================================
def busqueda_binaria(v_peli, nom):
    izq, der = 0, len(v_peli) - 1       
    while izq <= der:
        c = (izq + der) // 2
        if v_peli[c].titulo == nom:
            return c
        elif v_peli[c].titulo > nom:                
            der = c - 1                            
        else:
            izq = c + 1
    return -1


def cambiar_importe_op3(v_peli, pos):
    if pos >= 0:
        imp = float(input("Ingresar nuevo importe a cambiar: "))
        v_peli[pos].importe = imp
        print(v_peli[pos])
        if v_peli[pos].tipo == 1 or v_peli[pos].tipo == 2:
            print("Opcion Preferencial.")

    else:
        print("No se encontro la pelicula buscada.")


# ==================================================================================
#                       Opcion 4
# ==================================================================================
def generar_archivo(v_peli, fd, x):
    m = open(fd, "wb")

    cont = 0
    se_cargaron = False
    for i in v_peli:
        if i.importe < x and i.id_pais != 10:
            pickle.dump(i, m)
            m.flush()      
            cont += 1
            se_cargaron = True

    if cont > 0:
        print("Se cargaron un total de", cont, "Peliculas al arcivo:", fd)
    else:
        print("No se cargaron nuevas Peliculas en el archivo.")

    m.close()  


# ==================================================================================
#                       Opcion 5
# ==================================================================================

def mostrar_archivo(fd):
    if os.path.exists(fd):
        m = open(fd, "rb")
        tam = os.path.getsize(fd)       
        cont, acum = 0, 0
        while m.tell() < tam:
            peli = pickle.load(m)
            print(peli)
            cont += 1
            acum += peli.importe

        if cont > 0:
            prom = acum/cont
            print("El promedio de los importes acumulado es:", prom)

    else:
        print("El archivo no existe, debe pasar primero por la opcion 4.")


# ==================================================================================
#                       Opcion 6
# ==================================================================================
def busqueda_lineal(v_peli, num):
    se_encontro = False
    cont = 0
    for i in range(len(v_peli)):
        if v_peli[i].id == num:
            print(v_peli[i])
            se_encontro = True
            cont += 1

    if cont > 0:
        print("Se printearon", cont, "de Peliculas.")

    if not se_encontro:
        print("No se encontro una pelicula con ese ID.")


# ==================================================================================
#                       Opcion 7
# ==================================================================================
def generar_matriz(v_peli):

    filas = 5       
    columnas = 20
    
    matriz = [[0] * columnas for i in range(filas)]

    # completar la matriz/ rellenar la matriz
    for i in v_peli:
        matriz[i.tipo-1][i.id_pais] += 1

    # mostrar la matriz:
    for f in range(len(matriz)):    
        
        for c in range(len(matriz[0])):     
            if matriz[f][c] > 0 and 5 <= c <= 10:
                print("La cantidad de peliculas por tipo:", tipo_to_str(f+1), "y id_pais:", c)
                print("El total es:", matriz[f][c])
                print("=" * 50)


def menu():
    print("=" * 50,
          "\n 1 - Cargar arreglo."
          "\n 2 - Mostrar arreglo."
          "\n 3 - Buscar titulo."
          "\n 4 - Crear archivo."
          "\n 5 - Mostrar archivo."
          "\n 6 - Buscar por ID."
          "\n 7 - Cantidad de peliculas por tipo."
          "\n 0 - Salir.")
    
    return int(input("Ingresar opcion: "))


def main():
    # vector/arreglo/lista principal
    v_peli = []

    # bandera
    validar_op1 = False

    # file description
    fd = "peliculas.dat"

    op = -1
    while op != 0:

        op = menu()

        if not validar_op1:
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_peli, n)
                validar_op1 = True
            else:
                print("Debe ingresar primero por la opcion 1.")

        else:
            if op == 1:
                n = validar_n()
                cargar_arreglo(v_peli, n)

            elif op == 2:
                mostrar_datos(v_peli)

            elif op == 3:
                nom = input("Ingresar Titulo a buscar: ")
                pos = busqueda_binaria(v_peli, nom)
                cambiar_importe_op3(v_peli, pos)

            elif op == 4:
                x = float(input("Importe al que debe ser menor: "))
                generar_archivo(v_peli, fd, x)

            elif op == 5:
                mostrar_archivo(fd)

            elif op == 6:
                num = int(input("Numero de identificacion (1, 10): "))
                busqueda_lineal(v_peli, num)

            elif op == 7:
                generar_matriz(v_peli)
            
            elif op == 0:
                print('El programa se ha finalizado. :)')


if __name__ == '__main__':
    main()
