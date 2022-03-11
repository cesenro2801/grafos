from email.charset import SHORTEST
from importlib.resources import path
from readline import insert_text

graph = {
    'cenivam': {
        'N23': 1
    },
    'N23': {
        'cenivam': 1,
        'N22': 1
    },
    'N22': {
        'diamante de softbol': 1,
        'N21': 1,
        'porteria carrera 30': 1
    },
    'diamante de softbol': {
        'N22': 1,
        'N21': 1
    },
    'porteria carrera 30': {
        'N22': 1,
        'coliseo': 1,
        'N29': 1
    },
    'N21': {
        'diamante de softbol': 1,
        'N22': 1,
        'recidencias universitarias': 1,
        'coliseo': 1
    },
    'recidencias universitarias': {
        'N21': 1,
        'N20': 1
    },
    'kiosco residencias': {
        'N20': 1
    },
    'N20': {
        'recidencias universitarias': 1,
        'kiosco residencias': 1,
        'N28': 1,
        'N19': 1,
        'coliseo': 1
    },
    'coliseo': {
        'porteria carrera 30': 1,
        'N21': 1,
        'N20': 1,
        'cancha de futbol sur': 1,
        'N29': 1
    },
    'N28': {
        'N20': 1,
        'N19': 1,
        'N27': 1,
        'canchas multiples': 1
    },
    'canchas multiples': {
        'N28': 1,
        'N27': 1
    },
    'N27': {
        'canchas multiples': 1,
        'N26': 1
    },
    'N19': {
        'N20': 1,
        'N28': 1,
        'N18': 1,
        'cancha de futbol sur': 1
    },
    'cancha de futbol sur': {
        'coliseo': 1,
        'N19': 1,
        'N29': 1
    },
    'N29': {
        'porteria carrera 30': 1,
        'coliseo': 1,
        'cancha de futbol sur': 1,
        'N30': 1
    },
    'N26': {
        'N27': 1,
        'N25': 1
    },
    'N25': {
        'N26': 1,
        'N24': 1,
        'administracion 2': 1,
        'bienestar universitario': 1
    },
    'N24': {
        'cancha 1 marzo': 1,
        'N25': 1,
        'insed': 1,
        'N33': 1,
        'administracion': 1,
        'N17': 1
    },
    'cancha 1 marzo': {
        'N24': 1
    },
    'N18': {
        'N19': 1,
        'canchas de tenis': 1,
        'N17': 1
    },
    'canchas de tenis': {
        'N18': 1
    },
    'N17': {
        'N18': 1,
        'N24': 1,
        'N31': 1,
        'administracion': 1
    },
    'N31': {
        'N17': 1,
        'N30': 1
    },
    'N30': {
        'N31': 1,
        'N29': 1,
        'N32': 1
    },
    'N32': {
        'N30': 1,
        'auditorio luis a. calvo': 1,
        'porteria carrer 27': 1
    },
    'porteria carrer 27': {
        'N32': 1,
        'P4': 1
    },
    'auditorio luis a. calvo': {
        'N32': 1,
        'P4': 1,
        'N15': 1
    },
    'N15': {
        'auditorio luis a. calvo': 1,
        'mantenimiento y planta fisica': 1,
        'N14': 1
    },
    'N14': {
        'administracion': 1,
        'N34': 1,
        'P3': 1,
        'N15': 1
    },
    'administracion': {
        'N17': 1,
        'N24': 1,
        'N33': 1,
        'N14': 1
    },
    'N33': {
        'administracion': 1,
        'N24': 1,
        'insed': 1,
        'N34': 1,
    },
    'insed': {
        'N24': 1,
        'administracion 2': 1,
        'N34': 1,
        'N33': 1
    },
    'administracion 2': {
        'N25': 1,
        'bienestar universitario': 1,
        'N12': 1,
        'N34': 1,
        'insed': 1,
    },
    'bienestar universitario': {
        'N25': 1,
        'administracion 2': 1,
        'la perla': 1
    },
    'la perla': {
        'bienestar universitario': 1,
        'N12': 1
    },
    'N12': {
        'la perla': 1,
        'N34': 1,
        'ingenieria industrial': 1,
        'N11': 1,
        'administracion 2': 1
    },
    'N34': {
        'N33': 1,
        'insed': 1,
        'administracion 2': 1,
        'N12': 1,
        'instituto de lenguas': 1,
        'N35': 1,
        'N14': 1
    },
    'P4': {
        'porteria carrer 27': 1,
        'auditorio luis a. calvo': 1,
        'mantenimiento y planta fisica': 1,
        'N16': 1
    },
    'mantenimiento y planta fisica': {
        'P4': 1,
        'N15': 1,
        'ingenieria mecanica': 1,
        'N16': 1
    },
    'ingenieria mecanica': {
        'mantenimiento y planta fisica': 1,
        'P3': 1,
        'aula max. de mecanica': 1,
        'N10': 1
    },
    'P3': {
        'ingenieria mecanica': 1,
        'N14': 1,
        'N35': 1,
        'biblioteca': 1,
        'N9': 1,
        'aula max. de mecanica': 1
    },
    'N35': {
        'P3': 1,
        'N34': 1,
        'cafeteria': 1,
        'biblioteca': 1,
        'instituto de lenguas': 1
    },
    'instituto de lenguas': {
        'N35': 1,
        'N34': 1,
        'N11': 1,
        'cafeteria': 1,
    },
    'N11': {
        'instituto de lenguas': 1,
        'N12': 1,
        'ingenieria industrial': 1,
        'diseño industrial': 1
    },
    'ingenieria industrial': {
        'N12': 1,
        'N11': 1
    },
    'cafeteria': {
        'N35': 1,
        'instituto de lenguas': 1,
        'planta telefonica': 1
    },
    'biblioteca': {
        'N35': 1,
        'P3': 1,
        'N36': 1
    },
    'planta telefonica': {
        'cafeteria': 1,
        'N36': 1,
        'diseño industrial': 1
    },
    'aula max. de mecanica': {
        'ingenieria mecanica': 1,
        'P3': 1,
        'N9': 1,
        'N10': 1
    },
    'ciencias humanas': {
        'N16': 1
    },
    'N16': {
        'ciencias humanas': 1,
        'P4': 1,
        'mantenimiento y planta fisica': 1,
        'N10': 1,
        'N39': 1
    },
    'N10': {
        'N16': 1,
        'ingenieria mecanica': 1,
        'aula max. de mecanica': 1,
        'N9': 1,
        'camilo torres': 1,
        'laboratorios livianos': 1,
        'N39': 1
    },
    'N9': {
        'aula max. de mecanica': 1,
        'P3': 1,
        'N36': 1,
        'N8': 1,
        'camilo torres': 1,
        'N10': 1
    },
    'N36': {
        'N9': 1,
        'biblioteca': 1,
        'planta telefonica': 1,
        'capruis y favuis': 1,
        'N37': 1
    },
    'diseño industrial': {
        'planta telefonica': 1,
        'N11': 1,
        'ingenieria electrica': 1,
        'N7': 1,
        'capruis y favuis': 1
    },
    'N7': {
        'diseño industrial': 1,
        'ingenieria electrica': 1,
        'lab hidraulica': 1
    },
    'ingenieria electrica': {
        'N7': 1,
        'ingenieria electrica': 1,
        'P1': 1
    },
    'invernadero': {
        'P1': 1,
        'caracterizacion de mat.': 1
    },
    'P1': {
        'ingenieria electrica': 1,
        'invernadero': 1,
        'caracterizacion de mat.': 1,
        'torres diseño industrial': 1
    },
    'caracterizacion de mat.': {
        'invernadero': 1,
        'P1': 1,
        'torres diseño industrial': 1
    },
    'N39': {
        'N16': 1,
        'N10': 1,
        'N1': 1
    },
    'laboratorios livianos': {
        'N10': 1,
        'N38': 1
    },
    'camilo torres': {
        'N10': 1,
        'N9': 1,
        'N8': 1
    },
    'N8': {
        'N9': 1,
        'camilo torres': 1,
        'centic': 1,
        'N3': 1,
        'N38': 1
    },
    'centic': {
        'N8': 1,
        'N3': 1
    },
    'capruis y favuis': {
        'N37': 1,
        'N36': 1,
        'diseño industrial': 1,
        'aula maxima de fisica': 1
    },
    'lab hidraulica': {
        'N7': 1,
        'N6': 1,
        'aula maxima de fisica': 1
    },
    'N38': {
        'laboratorios livianos': 1,
        'N8': 1,
        'P2': 1,
        'lab. de posgrados': 1
    },
    'N3': {
        'N8': 1,
        'N37': 1,
        'ingenieria quimica': 1,
        'P2': 1
    },
    'N37': {
        'N36': 1,
        'aula maxima de fisica': 1,
        'N3': 1
    },
    'aula maxima de fisica': {
        'N37': 1,
        'capruis y favuis': 1,
        'lab hidraulica': 1,
        'ceiam': 1
    },
    'torres diseño industrial': {
        'P1': 1,
        'caracterizacion de mat.': 1,
        'laboratorio alta tension': 1,
        'N6': 1
    },
    'laboratorio alta tension': {
        'torres diseño industrial': 1,
        'N6': 1
    },
    'N6': {
        'N4': 1,
        'lab hidraulica': 1,
        'laboratorio alta tension': 1,
        'torres diseño industrial': 1,
        'N5': 1,
        'ceiam': 1
    },
    'ceiam': {
        'N6': 1,
        'N4': 1,
        'aula maxima de fisica': 1
    },
    'N4': {
        'ingenieria quimica': 1,
        'ceiam': 1,
        'facultad ing. fisicomecanicas': 1
    },
    'ingenieria quimica': {
        'N3': 1,
        'N4': 1
    },
    'P2': {
        'N3': 1,
        'N38': 1,
        'lab. de posgrados': 1,
        'N2': 1,
        'jorge bautizta v': 1
    },
    'lab. de posgrados': {
        'N38': 1,
        'P2': 1,
        'N1': 1
    },
    'N1': {
        'N39': 1,
        'lab. de posgrados': 1,
        'N2': 1,
        'planta de aceros': 1,
        'jardineria': 1
    },
    'N2': {
        'N1': 1,
        'P2': 1,
        'jorge bautizta v': 1,
        'planta de aceros': 1
    },
    'jorge bautizta v': {
        'P2': 1,
        'N2': 1,
        'porteria carrera 25': 1
    },
    'planta de aceros': {
        'N1': 1,
        'N2': 1,
        'porteria carrera 25': 1,
        'jardineria': 1
    },
    'jardineria': {
        'N1': 1,
        'planta de aceros': 1,
        'porteria carrera 25': 1
    },
    'porteria carrera 25': {
        'jardineria': 1,
        'planta de aceros': 1,
        'jorge bautizta v': 1,
        'facultad ing. fisicomecanicas': 1
    },
    'facultad ing. fisicomecanicas': {
        'porteria carrera 25': 1,
        'N4': 1,
        'daniel casas': 1
    },
    'daniel casas': {
        'jorge bautizta v': 1,
        'N5': 1
    },
    'N5': {
        'N6': 1,
        'daniel casas': 1
    }
}


def dijkstra(graph, start, goal):
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph.copy()
    infinity = 999999
    track_path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:

        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:

            if weight + shortest_distance[
                    min_distance_node] < shortest_distance[child_node]:
                shortest_distance[
                    child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]

        except KeyError:
            print("Path is not reachable")
            break

    track_path.insert(0, start)

    if shortest_distance[goal] != infinity:
        print("La distancia más corta es " + str(shortest_distance[goal]))
        print("Camino óptimo" + str(track_path))
        print('')


dijkstra(graph, 'porteria carrera 25', 'P1')
dijkstra(graph, 'porteria carrera 25', 'P2')
dijkstra(graph, 'porteria carrera 25', 'P3')
dijkstra(graph, 'porteria carrera 25', 'P4')
dijkstra(graph, 'porteria carrera 25', 'cancha 1 marzo')