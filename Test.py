# Nhóm 30
# Ngô Duy Tân-N19DCCN165
# Trương Hoàng Sang- N19DCCN157
import numpy as np
import matplotlib.pyplot as plt
import math as mt
from scipy.spatial import distance_matrix

def calculo_distancia(m_distancia,camino,n_ciudades):
    c_dis = 0
    for c1 in range(0, n_ciudades):
        suma_actual = m_distancia[camino[c1], camino[c1 - 1]]
        c_dis = suma_actual + c_dis
    return c_dis

def enc_vecino(camino,p1,p2):
    vecino = np.array(camino)
    vecino[p1] = camino[p2]
    vecino[p2] = camino[p1]
    return vecino

ciudades = np.array([[1,7],[7,5],[7,1],[3,1],[4,3]])
n_ciudades = len(ciudades)
m_distancia = distance_matrix(ciudades,ciudades)
camino_0 = np.random.choice(np.arange(n_ciudades),n_ciudades,False)

# Inicializacion de Temperatura
lk = 10
tk = 0.1
rmin = 0.95
ra = 0
b = 1000

camino = np.array(camino_0)
camino_correcto = np.array(camino_0)
distancia_actual = calculo_distancia(m_distancia, camino, n_ciudades)
mut_anterior = np.random.choice(np.arange(n_ciudades), 1)
camino = np.array(camino_0)
while ra < rmin:
    # for c2 in range (0,3):
    int_aceptado = 0
    intento = 0
    for l in range(0, lk):
        # Selección de posición a mutar
        posicion_cambio = np.random.choice(np.arange(5), 1)
        # Evitar mutar el mísmo índice 2 veces seguidas
        if posicion_cambio == mut_anterior:
            l = l - 1
            continue
        else:
            mut_anterior = np.array(posicion_cambio)
            # Mutar
            if posicion_cambio == 5:
                nuevo_camino = np.array(enc_vecino(camino, int(posicion_cambio) - 2, int(posicion_cambio) - 1))
            else:
                nuevo_camino = np.array(enc_vecino(camino, posicion_cambio, int(posicion_cambio) - 1))
            # Cálculo nueva distancia
            nueva_distancia = calculo_distancia(m_distancia, nuevo_camino, n_ciudades)
            # Comparación distancias
            if nueva_distancia < distancia_actual:
                camino = np.array(nuevo_camino)
                distancia_actual = nueva_distancia
                int_aceptado = int_aceptado + 1
                camino_correcto = np.array(nuevo_camino)
            else:
                prob = mt.exp(-(nueva_distancia - distancia_actual) / tk)
                dss = np.random.random()
                if dss < prob:
                    camino = np.array(nuevo_camino)
                    distancia_actual = nueva_distancia
                    int_aceptado = int_aceptado + 1
            intento = intento + 1
        l = l + 1
    tk = b * tk
    ra = int_aceptado / intento

# Enfriamiento
cam_tom = []
cont = [0]
mut_anterior = np.random.choice(np.arange(5), 1)
distancia_actual = calculo_distancia(m_distancia,camino,n_ciudades)
#while tk > .00000000001:
for c2 in range (0,100):
    for l in range(0,lk):
        posicion_cambio = np.random.choice(np.arange(5), 1)
        if posicion_cambio == mut_anterior:
            l = l - 1
            continue
        else:
            mut_anterior = np.array(posicion_cambio)
            if posicion_cambio == 5:
                nuevo_camino = np.array(enc_vecino(camino, int(posicion_cambio) - 2, int(posicion_cambio) - 1))
            else:
                nuevo_camino = np.array(enc_vecino(camino, posicion_cambio, int(posicion_cambio) - 1))
                nueva_distancia = calculo_distancia(m_distancia, nuevo_camino, n_ciudades)
            if nueva_distancia < distancia_actual:
                camino = np.array(nuevo_camino)
                distancia_actual = nueva_distancia
                cam_tom.append(camino)
            else:
                if tk > .0000001:
                    prob = mt.exp(-(nueva_distancia - distancia_actual) / tk)
                    dss = np.random.random()
                    if dss < prob:
                        camino = np.array(nuevo_camino)
                        distancia_actual = nueva_distancia
                        tk = 1
        l = l + 1
    tk = tk * np.random.randint(.2, 1)

print('-------------------------------------')
print('Minimal distance found:')
print(distancia_actual)
print('-------------------------------------')
print('Order of the cities in the trajectory:')
print(camino)

# Cálculo promedio/desviación estandar
caminos_tomados = np.array(cam_tom)
c3 = 0
dd = []
for e1 in caminos_tomados:
    d = calculo_distancia(m_distancia, e1, n_ciudades)
    dd.append(d)

y = np.array(dd)
x = np.linspace(1, len(y), len(y))

vec_camino = []
for e2 in camino:
    vec_camino.append(ciudades[e2])
cc = np.array(vec_camino)
print('-------------------------------------')
print('Coordinates of the cities in the trajectory:')
print(cc)