# Actividad 1: Red de Interacción de Proteínas
# Unidad 2: Estructuras de Datos

# Clase Nodo: representa cada elemento individual en la lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor          # Guardamos el nombre de la proteína
        self.siguiente = None       # Puntero al siguiente nodo

# Clase ListaEnlazada: gestiona la colección dinámica de interacciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None          # El inicio de la lista
        self.longitud = 0           # Contador de elementos

    # Método para verificar si la lista no tiene elementos
    def esta_vacia(self):
        return self.cabeza is None

    # Método para insertar una nueva interacción al principio de la lista
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        # El nuevo nodo apunta a la antigua cabeza
        nuevo_nodo.siguiente = self.cabeza
        # Actualizamos la cabeza para que sea el nuevo nodo
        self.cabeza = nuevo_nodo
        # Aumentamos el tamaño
        self.longitud += 1

    # Método para eliminar una interacción específica por su nombre
    def eliminar(self, dato):
        if self.cabeza is None:
            return # La lista está vacía, no hacemos nada

        # Caso especial: Si el nodo a eliminar es el primero (la cabeza)
        if self.cabeza.valor == dato:
            self.cabeza = self.cabeza.siguiente
            self.longitud -= 1
            return

        # Recorremos la lista buscando el nodo anterior al que queremos borrar
        actual = self.cabeza
        while actual.siguiente is not None:
            if actual.siguiente.valor == dato:
                # Saltamos el nodo que queremos eliminar
                actual.siguiente = actual.siguiente.siguiente
                self.longitud -= 1
                return
            actual = actual.siguiente

    # Método para comprobar si una proteína ya está en la lista de interacciones
    def existe(self, dato):
        actual = self.cabeza
        while actual is not None:
            if actual.valor == dato:
                return True
            actual = actual.siguiente
        return False

    # Método para mostrar el contenido de la lista visualmente
    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Clase Proteina: representa la entidad biológica
class Proteina:
    def __init__(self, nombre):
        self.nombre = nombre
        # Cada proteína tiene su propia lista enlazada de interacciones
        self.interacciones = ListaEnlazada()

# Clase RedProteinas: gestiona todo el sistema y el análisis
class RedProteinas:
    def __init__(self):
        self.lista_proteinas = []   # Lista para almacenar todas las proteínas creadas

    # Agrega una nueva proteína al sistema
    def agregar_proteina(self, nombre):
        nueva_prot = Proteina(nombre)
        self.lista_proteinas.append(nueva_prot)

    # Función auxiliar para buscar el objeto proteína por su nombre
    def buscar_proteina(self, nombre):
        for p in self.lista_proteinas:
            if p.nombre == nombre:
                return p
        return None

    # Crea una conexión (enlace) entre dos proteínas
    def agregar_conexion(self, nombre_prot1, nombre_prot2):
        # Primero buscamos las proteínas en nuestra lista
        p1 = self.buscar_proteina(nombre_prot1)
        p2 = self.buscar_proteina(nombre_prot2)

        # Si ambas existen, creamos la interacción bidireccional
        if p1 is not None and p2 is not None:
            # Añadimos la interacción solo si no existe ya
            if p1.interacciones.existe(nombre_prot2) == False:
                p1.interacciones.insertar(nombre_prot2)
            
            if p2.interacciones.existe(nombre_prot1) == False:
                p2.interacciones.insertar(nombre_prot1)

    # Elimina una conexión entre dos proteínas
    def eliminar_conexion(self, nombre_prot1, nombre_prot2):
        p1 = self.buscar_proteina(nombre_prot1)
        p2 = self.buscar_proteina(nombre_prot2)

        if p1 is not None and p2 is not None:
            p1.interacciones.eliminar(nombre_prot2)
            p2.interacciones.eliminar(nombre_prot1)
            print("Conexión eliminada entre", nombre_prot1, "y", nombre_prot2)

    # Analiza la estructura de la red e identifica la proteína HUB
    def analizar_red(self):
        print("\n--- INFORME DE LA RED ---")
        max_interacciones = -1
        nombre_hub = ""

        for p in self.lista_proteinas:
            # Mostramos las conexiones de cada proteína
            print("Proteína:", p.nombre, "| Interacciones:", end=" ")
            p.interacciones.mostrar()
            
            # Buscamos la proteína con más conexiones (HUB)
            numero_conexiones = p.interacciones.longitud
            if numero_conexiones > max_interacciones:
                max_interacciones = numero_conexiones
                nombre_hub = p.nombre
        
        print("\nRESULTADO DEL ANÁLISIS:")
        print("La proteína HUB (más conectada) es:", nombre_hub)
        print("Número de interacciones:", max_interacciones)

# --- EJECUCIÓN DE LA ACTIVIDAD ---

# 1. Crear la red vacía
mi_red = RedProteinas()

# 2. Agregar las proteínas (Nodos de la red)
nombres = ["P53", "MDM2", "ATM", "CHK2", "BRCA1", "CDK2"]
for n in nombres:
    mi_red.agregar_proteina(n)

# 3. Establecer conexiones simulando datos biológicos
# P53 interactúa con varias para el control del ciclo celular
mi_red.agregar_conexion("P53", "MDM2")
mi_red.agregar_conexion("P53", "ATM")
mi_red.agregar_conexion("P53", "CHK2")
mi_red.agregar_conexion("P53", "CDK2")

# Otras interacciones secundarias
mi_red.agregar_conexion("ATM", "CHK2")
mi_red.agregar_conexion("ATM", "BRCA1")
mi_red.agregar_conexion("MDM2", "CDK2")

# 4. Prueba de eliminación 
# Eliminamos una interacción para probar la lógica de borrado
mi_red.eliminar_conexion("MDM2", "CDK2")

# 5. Análisis final de la red
mi_red.analizar_red()
