'''     
Segundo examen parcial de PROGRAMACION
Nombre: Jhonny Molina Rea
Dni: 44260390
Division: 212

'''
import json
import pygame
def acomodar_datos (lista: list) -> list :
    # Se recibe la lista de diccionarios a tratar y se retorna una lista mucho mas facil de manejar
    lista_final = []
    lista_respuestas =[]
    lista_anidada = []
    for datos in lista:
        lista_respuestas = [datos["a"], datos["b"], datos["c"]]
        
        lista_anidada = [datos["pregunta"], lista_respuestas, datos["correcta"]]   
        lista_final += [lista_anidada]
    return lista_final

def crear_dibujar_rect (ubicacion_tamanio: tuple, superficie: str ,color: tuple):
    # Se reciben paramteros y se utilizan para crear y dibujar un rect en la pantalla
    crear = pygame.Rect(ubicacion_tamanio)
    pygame.draw.rect(superficie, color, crear, border_radius=15)
    return crear
def crear_texto (texto : str, color : tuple, ubicacion: tuple, superficie : str):
    # Se reciben parametros y se utilizan para crear y escribir un texto
    font = pygame.font.SysFont("Arial Narrow", 30)
    text = font.render(texto, True, color)
    superficie.blit(text, ubicacion)
    return text
def guardar_json (lista : list, nombre_archivo: str): #recive una lista y un str retorna un archivo json

    with open(f"C:/Users/aofbf/Downloads/Python 1 curso/clase/mijuego/{nombre_archivo}.json", "w") as archivo:
        json.dump(lista,archivo,indent=4,ensure_ascii=False) #llena el archivo con los datos de la lista
def cargar_imagen(direccion : str, ubicacion : tuple, escala : tuple, superficie: str):
    # Se carga un archivo imagen que luego sera mostrado como fondo de pantalla
    imagen = pygame.image.load(direccion)
    imagen = pygame.transform.scale(imagen, (escala))
    superficie.blit(imagen,(ubicacion))
    return imagen
def ordenar_lista(diccionario : dict):
    # Se recive un diccionario que luego sera ordenada de mayor a menor.
    indices = len(diccionario)
    for i in range(indices):
        for j in range(indices-i-1):
            if diccionario[j]["puntaje"] < diccionario[j+1]["puntaje"]:
                # swap
                diccionario[j], diccionario[j+1] = diccionario[j+1], diccionario[j]
    print(diccionario)
    return diccionario
def presiono_error( tecla_ocultar: str):
    #Funcion que ocurre en el caso de que el usuario presiona una respuesto erronea
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.1)
    sonido_error = pygame.mixer.Sound("clase/mijuego/sonidos/error_sonido.mp3")
    sonido_error.set_volume(0.4)
    sonido_error.play()   
    return tecla_ocultar
    

def presiono_correcta(texto_correcta: str, posicion_correcta: str)-> list :
    # La funcion recive los datos de la respuesta correcta y los retorna en una lista
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.1)
    sonido_correcto = pygame.mixer.Sound("clase/mijuego/sonidos/correcto_sonido.mp3")
    sonido_correcto.set_volume(0.4)
    sonido_correcto.play()
    return [texto_correcta, posicion_correcta]
    