from os import system
system("cls")
import random

trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez",
                "Miguel Sanchez","Isabel Gomez","Francisco Diaz","Elena Fernandez"]

sueldos = []
sueldo_trabajadores = []




def sueldo_aleatorio():
    for i in range (10):
        sueldo=random.randint(300000,2500000)
        sueldos.append(sueldo)
        sueldo_trabajadores.append(trabajadores[i])
        sueldo_trabajadores.append(sueldo)
        #print(sueldos)
    print("Sueldos asignados correctamente.")
    return sueldo
def clasificar_sueldos(sueldos, sueldo_trabajadores):
    menor_800k=0
    entre_800k_2m=0
    mayor_2m=0

    for i in range(10):
        if sueldos[i] < 800000:
            menor_800k += 1
    print(menor_800k)

    for i in range(10):
        if sueldos[i] >= 800000 and sueldos[i] <=2000000:
            entre_800k_2m += 1
    print(entre_800k_2m)

    for i in range(10):
        if sueldos[i] > 2000000:
            mayor_2m += 1
    print(mayor_2m)
        

    #print(sueldo1)

    #print(sueldo_trabajadores)



    print(f"""SUELDOS MENORES A $800.000 TOTAL: {menor_800k}
SUELDOS ENTRE $800.000 Y $2.000.000: {entre_800k_2m}
SUELDOS SUPERIORES A $2.000.000: {mayor_2m}
NOMBRE EMPLEADO           SUELDO
{trabajadores[0]}               {sueldos[0]}
{trabajadores[1]}               {sueldos[1]}
{trabajadores[2]}               {sueldos[2]}
{trabajadores[3]}               {sueldos[3]}
{trabajadores[4]}               {sueldos[4]}
{trabajadores[5]}               {sueldos[5]}
{trabajadores[6]}               {sueldos[6]}
{trabajadores[7]}               {sueldos[7]}
{trabajadores[8]}               {sueldos[8]}
{trabajadores[9]}               {sueldos[9]}
""")

def reporte_sueldos(sueldos):
    
    print(F"""NOMBRE EMPLEADO        SUELDO BASE         DESC. SALUD         DESC AFP        SUELDO LIQUIDO
{trabajadores[0]}               {sueldos[0]}        {sueldos[0]*0.07}       {sueldos[0]*0.12}       {sueldos[0]-sueldos[0]*0.19}
{trabajadores[1]}               {sueldos[1]}        {sueldos[1]*0.07}       {sueldos[1]*0.12}       {sueldos[1]-sueldos[1]*0.19}
{trabajadores[2]}               {sueldos[2]}        {sueldos[2]*0.07}       {sueldos[2]*0.12}       {sueldos[2]-sueldos[2]*0.19}
{trabajadores[3]}               {sueldos[3]}        {sueldos[3]*0.07}       {sueldos[3]*0.12}       {sueldos[3]-sueldos[3]*0.19}
{trabajadores[4]}               {sueldos[4]}        {sueldos[4]*0.07}       {sueldos[4]*0.12}       {sueldos[4]-sueldos[4]*0.19}
{trabajadores[5]}               {sueldos[5]}        {sueldos[5]*0.07}       {sueldos[5]*0.12}       {sueldos[5]-sueldos[5]*0.19}
{trabajadores[6]}               {sueldos[6]}        {sueldos[6]*0.07}       {sueldos[6]*0.12}       {sueldos[6]-sueldos[6]*0.19}
{trabajadores[7]}               {sueldos[7]}        {sueldos[7]*0.07}       {sueldos[7]*0.12}       {sueldos[7]-sueldos[7]*0.19}
{trabajadores[8]}               {sueldos[8]}        {sueldos[8]*0.07}       {sueldos[8]*0.12}       {sueldos[8]-sueldos[8]*0.19}
{trabajadores[9]}               {sueldos[9]}        {sueldos[9]*0.07}       {sueldos[9]*0.12}       {sueldos[9]-sueldos[9]*0.19}
          """)

def ver_estadisticas(sueldos):
    for i in range(10):
        sueldos[i]
        sueldo_max = max(sueldos)
    print(f"El sueldo mas alto es: ", sueldo_max)

    for i in range(10):
        sueldos[i]
        sueldo_min = min(sueldos)
    print(f"El sueldo mas bajo es: ",sueldo_min)

    total_sueldos = sueldos[0]+sueldos[1]+sueldos[2]+sueldos[3]+sueldos[4]+sueldos[5]+sueldos[6]+sueldos[7]+sueldos[8]+sueldos[9]
    prom_sueldos = total_sueldos/10
    print(f"El promedio de los sueldos es: ",prom_sueldos)
        





while True:
    op = input("""
1.- Asignar sueldos aleatorios
2.- Clasificar sueldos
3.- Ver estadisticas
4.- Reporte de sueldos
5.- Salir 
Seleccione una opcion: """)
    
    match op:
        case "1":
            sueldo_aleatorio()
        case "2":
            clasificar_sueldos(sueldos, sueldo_trabajadores)
        case "3":
            ver_estadisticas(sueldos)
        case "4":
            reporte_sueldos(sueldos)
        case "5":
            print("""Saliendo del programa....
Desarrollado por Vicente Muñoz
RUT: 20.831.765-2
                  """)
            break
        case other:
            print("Seleccione una opcion dada...")