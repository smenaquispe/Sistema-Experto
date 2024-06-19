import json

path_json = 'countries.json'

with open(path_json) as f:
    paises = json.load(f)


conocido = set()
conocido_false = set()

def consulta():
    for pais, caracteristicas in paises.items():
        if prueba_presencia_de(pais, caracteristicas):
            escribe_diagnostico(pais)
            ofrece_explicacion_diagnostico(pais, caracteristicas)
            clean_scratchpad()
            return
    
    print('No hay suficiente conocimiento para elaborar un diagnostico.')
    clean_scratchpad()

def prueba_presencia_de(pais, caracteristicas):
    for topico, lista_caracteristicas in caracteristicas.items():
        for caracteristica in lista_caracteristicas:
            if not prueba_verdad_de(pais, caracteristica):
                return False
    return True

def prueba_verdad_de(pais, caracteristica):
    if caracteristica in conocido:
        return True
    if caracteristica in conocido_false:
        return False
    return pregunta_sobre(pais, caracteristica)

def pregunta_sobre(pais, caracteristica):
    while True:
        respuesta = input(f'El lugar al que deseas viajar tiene {caracteristica}? (si/no/porque): ').strip().lower()
        if respuesta == 'si':
            conocido.add(caracteristica)
            return True
        elif respuesta == 'no':
            conocido_false.add(caracteristica)
            return False
        elif respuesta == 'porque':
            print(f'Estoy investigando el país {pais}.')
            print(f'Para esto necesito saber si tiene {caracteristica}.')
        else:
            print('Debes contestar si, no o porque.')

def escribe_diagnostico(pais):
    print(f'El diagnóstico es que el país es {pais}.')

def ofrece_explicacion_diagnostico(pais, caracteristicas):
    while True:
        respuesta = input('¿Quieres que justifique este diagnóstico? (si/no): ').strip().lower()
        if respuesta == 'si':
            print('Se determinó este diagnóstico porque se encontraron las siguientes características:')
            escribe_caracteristicas_con_topico(caracteristicas)
            break
        elif respuesta == 'no':
            break
        else:
            print('Debes contestar si o no.')

def escribe_caracteristicas_con_topico(caracteristicas):
    for topico, lista_caracteristicas in caracteristicas.items():
        for caracteristica in lista_caracteristicas:
            if caracteristica in conocido:
                print(f'{topico}: {caracteristica}')

def clean_scratchpad():
    conocido.clear()
    conocido_false.clear()

# Ejecutar la consulta para iniciar el sistema experto
consulta()
