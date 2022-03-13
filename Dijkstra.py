from email.charset import SHORTEST
from importlib.resources import path
from readline import insert_text

graph = {
    'cenivam': {
        'N23': 83
    },
    'N23': {
        'cenivam': 83,
        'N22': 78
    },
    'N22': {
        'diamante de softbol': 95,
        'N21': 30,
        'porteria carrera 30': 43
    },
    'diamante de softbol': {
        'N22': 95,
        'N21': 82
    },
    'porteria carrera 30': {
        'N22': 43,
        'coliseo': 69,
        'N29': 120
    },
    'N21': {
        'diamante de softbol': 82,
        'N22': 95,
        'recidencias universitarias': 61,
        'coliseo': 44
    },
    'recidencias universitarias': {
        'N21': 61,
        'N20': 25
    },
    'kiosco residencias': {
        'N20': 32
    },
    'N20': {
        'recidencias universitarias': 25,
        'kiosco residencias': 25,
        'N28': 120,
        'N19': 42,
        'coliseo': 53
    },
    'coliseo': {
        'porteria carrera 30': 69,
        'N21': 44,
        'N20': 53,
        'cancha de futbol sur': 60,
        'N29': 89
    },
    'N28': {
        'N20': 120,
        'N19': 150,
        'N27': 63,
        'canchas multiples': 52
    },
    'canchas multiples': {
        'N28': 52,
        'N27': 35
    },
    'N27': {
        'canchas multiples': 35,
        'N28': 63,
        'N26': 81
    },
    'N19': {
        'N20': 42,
        'N28': 150,
        'N18': 74,
        'cancha de futbol sur': 38
    },
    'cancha de futbol sur': {
        'coliseo': 60,
        'N19': 38,
        'N29': 35
    },
    'N29': {
        'porteria carrera 30': 120,
        'coliseo': 89,
        'cancha de futbol sur': 35,
        'N30': 135
    },
    'N26': {
        'N27': 81,
        'N25': 73
    },
    'N25': {
        'N26': 73,
        'N24': 68,
        'administracion 2': 30,
        'bienestar universitario': 54
    },
    'N24': {
        'cancha 1 marzo': 74,
        'N25': 68,
        'insed': 43,
        'N33': 54,
        'administracion': 46,
        'N17': 79
    },
    'cancha 1 marzo': {
        'N24': 74
    },
    'N18': {
        'N19': 74,
        'canchas de tenis': 45,
        'N17': 55
    },
    'canchas de tenis': {
        'N18': 45
    },
    'N17': {
        'N18': 55,
        'N24': 79,
        'N31': 50,
        'administracion': 68
    },
    'N31': {
        'N17': 50,
        'N30': 70
    },
    'N30': {
        'N31': 70,
        'N29': 135,
        'N32': 58
    },
    'N32': {
        'N30': 58,
        'auditorio luis a. calvo': 43,
        'porteria carrer 27': 39
    },
    'porteria carrer 27': {
        'N32': 39,
        'P4': 20
    },
    'auditorio luis a. calvo': {
        'N32': 43,
        'P4': 85,
        'N15': 20
    },
    'N15': {
        'auditorio luis a. calvo': 20,
        'mantenimiento y planta fisica': 62,
        'N14': 79
    },
    'N14': {
        'administracion': 61,
        'N34': 73,
        'P3': 64,
        'N15': 79
    },
    'administracion': {
        'N17': 68,
        'N24': 46,
        'N33': 25,
        'N14': 61
    },
    'N33': {
        'administracion': 25,
        'N24': 54,
        'insed': 20,
        'N34': 48
    },
    'insed': {
        'N24': 43,
        'administracion 2': 35,
        'N34': 59,
        'N33': 20
    },
    'administracion 2': {
        'N25': 30,
        'bienestar universitario': 63,
        'N12': 110,
        'N34': 130,
        'insed': 35,
    },
    'bienestar universitario': {
        'N25': 54,
        'administracion 2': 63,
        'la perla': 59
    },
    'la perla': {
        'bienestar universitario': 59,
        'N12': 41
    },
    'N12': {
        'la perla': 41,
        'N34': 76,
        'ingenieria industrial': 37,
        'N11': 29,
        'administracion 2': 110
    },
    'N34': {
        'N33': 48,
        'insed': 59,
        'administracion 2': 130,
        'N12': 76,
        'instituto de lenguas': 82,
        'N35': 78,
        'N14': 73
    },
    'P4': {
        'porteria carrer 27': 20,
        'auditorio luis a. calvo': 85,
        'mantenimiento y planta fisica': 51,
        'N16': 64
    },
    'mantenimiento y planta fisica': {
        'P4': 51,
        'N15': 62,
        'ingenieria mecanica': 31,
        'N16': 39
    },
    'ingenieria mecanica': {
        'mantenimiento y planta fisica': 31,
        'P3': 62,
        'aula max. de mecanica': 39,
        'N10': 49
    },
    'P3': {
        'ingenieria mecanica': 62,
        'N14': 64,
        'N35': 80,
        'biblioteca': 60,
        'N9': 38,
        'aula max. de mecanica': 26
    },
    'N35': {
        'P3': 80,
        'N34': 78,
        'cafeteria': 30,
        'biblioteca': 20,
        'instituto de lenguas': 38
    },
    'instituto de lenguas': {
        'N35': 38,
        'N34': 82,
        'N11': 21,
        'cafeteria': 23
    },
    'N11': {
        'instituto de lenguas': 21,
        'N12': 37,
        'ingenieria industrial': 27,
        'diseño industrial': 60
    },
    'ingenieria industrial': {
        'N12': 37,
        'N11': 27
    },
    'cafeteria': {
        'N35': 30,
        'instituto de lenguas': 23,
        'planta telefonica': 8
    },
    'biblioteca': {
        'N35': 20,
        'P3': 60,
        'N36': 18
    },
    'planta telefonica': {
        'cafeteria': 8,
        'N36': 22,
        'diseño industrial': 26
    },
    'aula max. de mecanica': {
        'ingenieria mecanica': 39,
        'P3': 26,
        'N9': 15,
        'N10': 37
    },
    'ciencias humanas': {
        'N16': 28
    },
    'N16': {
        'ciencias humanas': 28,
        'P4': 64,
        'mantenimiento y planta fisica': 39,
        'N10': 72,
        'N39': 94
    },
    'N10': {
        'N16': 72,
        'ingenieria mecanica': 49,
        'aula max. de mecanica': 37,
        'N9': 56,
        'camilo torres': 44,
        'laboratorios livianos': 55,
        'N39': 87
    },
    'N9': {
        'aula max. de mecanica': 15,
        'P3': 38,
        'N36': 53,
        'N8': 40,
        'camilo torres': 19,
        'N10': 56
    },
    'N36': {
        'N9': 53,
        'biblioteca': 12,
        'planta telefonica': 22,
        'capruis y favuis': 40,
        'N37': 65
    },
    'diseño industrial': {
        'planta telefonica': 26,
        'N11': 60,
        'ingenieria electrica': 42,
        'N7': 16,
        'capruis y favuis': 27
    },
    'N7': {
        'diseño industrial': 16,
        'ingenieria electrica': 129,
        'lab hidraulica': 21
    },
    'ingenieria electrica': {
        'N7': 29,
        'diseño industrial': 42,
        'P1': 30
    },
    'invernadero': {
        'P1': 56,
        'caracterizacion de mat.': 67
    },
    'P1': {
        'ingenieria electrica': 30,
        'invernadero': 56,
        'caracterizacion de mat.': 42,
        'torres diseño industrial': 43
    },
    'caracterizacion de mat.': {
        'invernadero': 67,
        'P1': 42,
        'torres diseño industrial': 52
    },
    'N39': {
        'N16': 94,
        'N10': 87,
        'N1': 98
    },
    'laboratorios livianos': {
        'N10': 55,
        'N38': 38
    },
    'camilo torres': {
        'N10': 44,
        'N9': 19,
        'N8': 15
    },
    'N8': {
        'N9': 40,
        'camilo torres': 15,
        'centic': 35,
        'N3': 40,
        'N38': 32
    },
    'centic': {
        'N8': 35,
        'N3': 52
    },
    'capruis y favuis': {
        'N37': 15,
        'N36': 40,
        'diseño industrial': 27,
        'aula maxima de fisica': 17
    },
    'lab hidraulica': {
        'N7': 21,
        'N6': 28,
        'aula maxima de fisica': 51
    },
    'N38': {
        'laboratorios livianos': 38,
        'N8': 32,
        'P2': 32,
        'lab. de posgrados': 40
    },
    'N3': {
        'N8': 35,
        'N37': 19,
        'ingenieria quimica': 15,
        'P2': 37,
        'centic': 52,
    },
    'N37': {
        'N36': 65,
        'aula maxima de fisica': 21,
        'N3': 19
    },
    'aula maxima de fisica': {
        'N37': 21,
        'capruis y favuis': 17,
        'lab hidraulica': 51,
        'ceiam': 23
    },
    'torres diseño industrial': {
        'P1': 43,
        'caracterizacion de mat.': 52,
        'laboratorio alta tension': 27,
        'N6': 22
    },
    'laboratorio alta tension': {
        'torres diseño industrial': 12,
        'N6': 9
    },
    'N6': {
        'lab hidraulica': 28,
        'laboratorio alta tension': 9,
        'torres diseño industrial': 22,
        'N5': 27,
        'ceiam': 38
    },
    'ceiam': {
        'N6': 38,
        'N4': 12,
        'aula maxima de fisica': 23
    },
    'N4': {
        'ingenieria quimica': 30,
        'ceiam': 12,
        'facultad ing. fisicomecanicas': 21
    },
    'ingenieria quimica': {
        'N3': 15,
        'N4': 30
    },
    'P2': {
        'N3': 37,
        'N38': 32,
        'lab. de posgrados': 25,
        'N2': 32,
        'jorge bautizta v': 42
    },
    'lab. de posgrados': {
        'N38': 40,
        'P2': 25,
        'N1': 69
    },
    'N1': {
        'N39': 98,
        'lab. de posgrados': 69,
        'N2': 67,
        'planta de aceros': 32,
        'jardineria': 38
    },
    'N2': {
        'N1': 67,
        'P2': 32,
        'jorge bautizta v': 35,
        'planta de aceros': 33
    },
    'jorge bautizta v': {
        'P2': 42,
        'N2': 35,
        'porteria carrera 25': 62
    },
    'planta de aceros': {
        'N1': 32,
        'N2': 33,
        'porteria carrera 25': 41,
        'jardineria': 38
    },
    'jardineria': {
        'N1': 37,
        'planta de aceros': 38,
        'porteria carrera 25': 45
    },
    'porteria carrera 25': {
        'jardineria': 45,
        'planta de aceros': 41,
        'jorge bautizta v': 62,
        'facultad ing. fisicomecanicas': 114
    },
    'facultad ing. fisicomecanicas': {
        'porteria carrera 25': 114,
        'N4': 21,
        'daniel casas': 23
    },
    'daniel casas': {
        'jorge bautizta v': 23,
        'N5': 14
    },
    'N5': {
        'N6': 27,
        'daniel casas': 14
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


dijkstra(graph, 'canchas de tenis', 'P1')
dijkstra(graph, 'porteria carrera 25', 'P2')
dijkstra(graph, 'porteria carrera 25', 'P3')
dijkstra(graph, 'porteria carrera 25', 'P4')
dijkstra(graph, 'porteria carrera 25', 'cancha 1 marzo')