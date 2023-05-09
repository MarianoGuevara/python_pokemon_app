from funciones import *


def crear_menu()->str:
    '''
    Brief: Crea un string que representa la parte visual del menu
    Parametros:
    Return: Devuelve ese menú string
    '''
    menu =\
    """
    MENU: POKEMONES
    1. Traer datos desde archivo
    2. Listar cantidad por tipo
    3. Listar pokemones por tipo
    4. Listar pokemones por habilidad
    5. Listar pokemones ordenados (por fuerza mayor a menor)
    6. Guardar Json
    7. Leer Json
    8. SALIR
    """
    return menu

def pedir_dato(mensaje_input:str)->int:
    '''
    Brief: Pide un dato input y lo devuelve
    Parametros: mensaje_input: Recibe un mensaje string que
    representa lo que irá dentro del input
    Return: Devuelve el input si está dentro del dato solicitado 
    '''
    while True:
        dato = input(mensaje_input)
        if dato.isdigit() == True:
            dato = int(dato)
            if dato > 0 and dato < 9:
                break
    return dato


def accionar_segun_opcion():
    '''
    Brief: Genera y pone en accion el menu principal, llamando 
    a las funciones de pedir dato e imprimir menu.
    Segun el input llama a la funcion adecuada y ejecuta las
    validaciones correspondientes
    Parametros:
    Return: 
    '''
    bandera = False
    lista_pokemones = []
    while True:
        print(crear_menu())
        dato_usuario = pedir_dato("Ingresa una opcion del menu: ")

        if dato_usuario == 8:
            break
        elif dato_usuario == 1:
            if bandera == True:
                print("Datos ya traidos y organizados con exito" 
                    " previamente")
            else:
                lista_pokemones = traer_datos_desde_archivos(ruta_csv)

                if lista_pokemones == False:
                    print("Archivo inexistente")
                elif lista_pokemones == -1:
                    print("Hubo un problema con la lista")
                elif lista_pokemones == -2:
                    print('El ataque o defensa no son numericos validos'/ 
                        'u ocurrio otro problema con el diccionario')
                else:
                    print("Datos traidos y organizados con exito!!")
                    bandera = True

        elif bandera == False:
            print("Llamar primero a 1")

        elif dato_usuario == 2:
            cantidad_tipos = listar_cantidad_por_tipo(lista_pokemones, 'tipo')
            if cantidad_tipos == False or cantidad_tipos == -2:
                print("Key inválida en este caso")
            elif cantidad_tipos == -3:
                print("Lista de parametro no valida")
            else:
                print(cantidad_tipos)

        elif dato_usuario == 3:
            listado_por_tipos = listar_nombres_por_tipo(lista_pokemones,
                                                        'tipo', 'nombre')
            if listado_por_tipos == False or listado_por_tipos == -2:
                print("Key no valida; revisar")
            elif listado_por_tipos == -3:
                print("La lista no es valida")
            else:
                print(listado_por_tipos)

        elif dato_usuario == 4:
            por_habilidades = listar_pokemones_por_habilidad(lista_pokemones,
                                            'habilidades', 'nombre')

            if por_habilidades == False or por_habilidades == -2:
                print("Key no valida")
            elif por_habilidades == -1:
                print("Habilidad ingresada"\
                    " no perteneciente a ningun pokemon")
            elif por_habilidades == -3:
                print("lista inválida")
            else:
                print(por_habilidades)

        elif dato_usuario == 5:
            ordenados = listar_pokemones_ordenados(lista_pokemones,
                                    "ataque", "nombre")
            if ordenados == False:
                print("Lista incorrecta")
            elif ordenados == -1:
                print("Parametros incorrectos")
            else:
                print(ordenados)
        elif dato_usuario == 6:
            msj_archivo = guardar_json(lista_pokemones, 'tipo', 
                                    "ataque", "defensa")
            if msj_archivo == False:
                print("Key inválida")
            elif msj_archivo == -1:
                print("El archivo de este tipo de pokemones ya existe")
            elif msj_archivo == -2:
                print("El dato ingresado no es ningun tipo de pokemon")
            elif msj_archivo == -3:
                print("Lista inválida")
            else:
                print("Archivo json generado y guardado exitosamente")
        else:
            lectura_json = leer_json("Ingrese un tipo de pokemon"\
                    " sobre el cual quiera abrir su archivo json: ")
            if lectura_json == False:
                print("No existe un archivo con ese tipo de pokemon"\
                ", por lo que leerlo es imposible."\
                " Primero pruebe generandolo (opcion 6)")
            elif lectura_json == -5:
                print("Problema en el contenido del json")
            else:
                print(lectura_json)
accionar_segun_opcion()