from datetime import datetime as dt

ESPACIADO = 64

def fecha_hora():
    fecha = dt.now()
    anio, mes, dia = fecha.year, fecha.month, fecha.day
    fecha_ymd = f'{anio}-{str(mes).zfill(2)}-{str(dia).zfill(2)}'
    hora, min = fecha.hour, fecha.minute
    estado = 'am'
    if hora >= 13: 
        hora -= 12
        estado = 'pm'
    fecha_hm = f'{str(hora).zfill(2)}:{str(min).zfill(2)} {estado}'
    return fecha_ymd, fecha_hm

def imprimir_menu(nombre):
    fecha, hora = fecha_hora()
    print('*'*ESPACIADO)
    print(nombre.center(ESPACIADO))
    print(fecha.center(ESPACIADO))
    print(hora.center(ESPACIADO))
    print('*'*ESPACIADO)
    print('**Menu**'.ljust(ESPACIADO))
    print('01-->Registrar Usuario')
    print('02-->Ingresar vehiculo')
    print('03-->Retirar vehiculo')
    print('04-->Acceso administrador')
    print('05-->Salir')
    print('*'*ESPACIADO)

