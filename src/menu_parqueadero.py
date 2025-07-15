# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 20:09:35 2025

@author: juanp
"""

import time
import Facturas
import registro_usuario2
import menu
def fechaHora():
    now = datetime.now()
    fecha = now.strftime('%Y-%m-%d')        
    hora = now.strftime('%H:%M:%S')          
    return [fecha, hora]
from datetime import datetime
dicUsuarios = {}
dicRegistro = {}
vehiculos_historial = []
vehiculos_retirados = []
usuarios_admin = {
    "alfred": "Batman123",
    "duque": "1240",
    "anita": "0510",
    "sarita": "2903",
    "belen": "0615"
}
def admin_module():
    while True:
        print("\n--- SUBMENÚ DE ADMINISTRACIÓN ---")
        print("1. Total de vehículos registrados")
        print("2. Total de vehículos retirados")
        print("3. Total de vehículos sin retirar")
        print("4. Total pago de vehículos retirados")
        print("5. Tiempo promedio de estancia por vehículo")
        print("6. Lista de usuarios administradores")
        print("7. Vehículo con mayor y menor tiempo de parqueo")
        print("8. Volver al menú principal")

        opcion = input("Seleccione una opción del módulo: ")

        if opcion == "1":
            total_registrados = len(vehiculos_historial)
            print(f" Total de vehículos registrados en el parqueadero: {total_registrados}")

        elif opcion == "2":
            print(f"→ Total de vehículos retirados: {len(vehiculos_retirados)}")
        elif opcion == "3":
            sin_retirar = len(vehiculos_historial) - len(vehiculos_retirados)
            print("→ Vehículos sin retirar:", sin_retirar)

        elif opcion == "4":
            total_pagos = sum(v["cobro"] for v in vehiculos_retirados)
            print(f"→ Total recaudado por cobros: ${total_pagos}")

        elif opcion == "5":
            if len(vehiculos_retirados) == 0:
                print(" No hay vehículos retirados para calcular el tiempo promedio.")
            else:
                suma_tiempos = 0
                for v in vehiculos_retirados:
                    tiempo_estancia = v["salida"] - v["ingreso"]
                    suma_tiempos += tiempo_estancia
        
                promedio_segundos = suma_tiempos / len(vehiculos_retirados)
        
                horas = int(promedio_segundos // 3600)
                minutos = int((promedio_segundos % 3600) // 60)
                segundos = int(promedio_segundos % 60)
        
                print(f" Tiempo promedio de estancia: {horas} horas, {minutos} minutos y {segundos} segundos")

        elif opcion == "6":
            print("→ Lista de usuarios administradores:")
            for user in usuarios_admin:
                print(f"   - {user}")

        elif opcion == "7":
            if len(vehiculos_retirados) == 0:
                print(" No hay vehículos retirados para evaluar tiempos.")
            else:
                # Calcular el tiempo de estancia de cada vehículo
                vehiculo_mayor = max(vehiculos_retirados, key=lambda v: v["salida"] - v["ingreso"])
                vehiculo_menor = min(vehiculos_retirados, key=lambda v: v["salida"] - v["ingreso"])
                tiempo_mayor = vehiculo_mayor["salida"] - vehiculo_mayor["ingreso"]
                tiempo_menor = vehiculo_menor["salida"] - vehiculo_menor["ingreso"]
        
                def tiempo(segundos):
                    horas = int(segundos // 3600)
                    minutos = int((segundos % 3600) // 60)
                    segundos = int(segundos % 60)
                    return f"{horas}h {minutos}m {segundos}s"
        
                print("Vehículo con mayor tiempo:")
                print(f"--->Placa: {vehiculo_mayor['placa']}")
                print(f"--->Tiempo: {tiempo(tiempo_mayor)}")
                
                print("Vehículo con menor tiempo:")
                print(f"--->Placa: {vehiculo_menor['placa']}")
                print(f"--->Tiempo: {tiempo(tiempo_menor)}")

        elif opcion == "8":
            print("Saliendo del módulo de administración.")
            break

        else:
            print("Opción inválida, intenta nuevamente.")
def CalculoPago(tiempo_segundos: float, valor_hora=7000, valor_cuarto=1500):
   
    tiempo_horas = tiempo_segundos / 3600
    horas_completas = int(tiempo_horas)
    fraccion_hora = tiempo_horas - horas_completas
    cuartos_hora = int(fraccion_hora * 4)
    cobro = horas_completas * valor_hora + cuartos_hora * valor_cuarto
    if cobro < 7000:
        cobro = 7000
    return cobro, horas_completas, cuartos_hora

def validar_datos(documento:str, nombre:str, apellido:str, placa:str)->bool:
    validar = True
    global error
    # Validacion del documento
    if isinstance(documento, str):
        if documento.isdigit():
            if len(documento) <= 3 or len(documento) >= 15:
                validar = False
                print('ERROR, El documento debe tener entre 3 y 15 digitos|\n')
            else:
                pass
        else:
            validar = False
            print('ERROR, el documento debe ser numerico|\n' )
            print(error)
    else:
        validar = False
        print('ERROR, El documento no es correcto|\n')
        print(error)
    # Validacion del nombre
    if isinstance(nombre, str):
        if nombre.isalpha():
            if len(nombre) <= 3:
                validar = False
                print('ERROR, El nombre es muy corto|\n')
                print(error)
            else:
                pass
        else:
            validar = False
            print('ERROR, el nombre solo puede contener letras|\n')
        
    else:
        validar = False
        print('Error, El nombre no es correcto|\n')
    #validacion de apellido
    if isinstance(apellido, str):
        if apellido.isalpha():
            if len(apellido) <= 3:
                validar = False
                print('ERROR, El apellido es muy corto|\n')
            else:
                pass
        else:
            validar = False
            print('ERROR, el apellido solo puede contener letras|\n')
    else:
        validar = False
        print('ERROR, El apellido no es correcto|\n')
    #validación de placa 
    letras = placa[:3]
    numeros = placa[3:]
    if isinstance(placa, str):
        if len(placa) == 6:
            if letras.isalpha():
                if not numeros.isdigit():
                    validar = False
                    print('ERROR, los ultimos 3 digitos deben ser numeros')
            else:
                validar = False
                print('ERROR, los primeros 3 digitos deben ser letras')
        else:
            validar = False
            print('ERROR, la placa debe de tener 6 caracteres')
    else:
        validar = False
        print('ERROR, La placa no es correcta')
    return validar

while True:
    menu.imprimir_menu('Bienvenido a parqueadero la guarderia')
    opcion = input('Ingresar opción --> ')
    match opcion:
        case '1': # Registrar Usuario
            documento = input('Ingresar documento'.ljust(22)+'-->')
            nombre = input('Ingresar nombre'.ljust(22)+'-->').upper()
            apellido = input('Ingresar apellido'.ljust(22)+'-->').upper()
            placa = input('Ingresar placa'.ljust(22)+'-->').upper()
            if validar_datos(documento, nombre, apellido, placa):
                print('Validacion Correcta')

                temp = registro_usuario2.registro_usuario2(dicUsuarios, documento, nombre, apellido, placa)
                if temp:
                    dicUsuarios = temp
                    for i in range(3):
                        print('Guardando datos' + '.' * (i + 1), end='\r')
                        time.sleep(0.5)
                    print('Datos Guardados...   ')
                else:
                    print('ERROR, de almacenamiento, vuelve a intentarlo')
                    continue
            else:
                print('Favor corregir los datos, vuelve y registra los datos.')
                continue
        
        case '2':  # Ingresar vehículo
            print('Ingresar documento y placa del vehículo para ingresar:')
            documento = input('Ingresar documento'.ljust(22) + '--> ')
            placa = input('Ingresar placa'.ljust(22) + '--> ').upper()
        
            if documento in dicUsuarios:
                if placa in dicRegistro:
                    print(f"⚠ El vehículo {placa} ya está registrado dentro del parqueadero.")
                else:
                    tiempoinicial = round(time.time(), 0)
                    hora = datetime.now().strftime("%I:%M:%S %p")
                    fecha = datetime.now().strftime("%Y-%m-%d")
        
                    dicRegistro[placa] = {
                        'Placa': placa,
                        'Documento': documento,
                        'TiempoIngreso': tiempoinicial,
                        'FechaIngreso': fecha,
                        'TiempoSalida': 0
                    }
                    vehiculos_historial.append({
                        "placa": placa,
                        "ingreso": tiempoinicial,
                        "documento": documento
                    })
                    nombre = dicUsuarios[documento]['Nombre']
                    Facturas.ImprimirFacturaIngreso(nombre, documento, placa)
                    print(f" Vehículo de placas {placa} ingresado correctamente a las {hora} del día {fecha}.")
            else:
                print(f"ERROR, El documento {documento} no se encuentra registrado.")
                print("Registre primero al usuario y su vehículo usando la opción 1.")             
                    
        case '3':  # Retiro del vehículo
            placa = input('Ingrese la placa para retirar: ').upper()
        
            if placa in dicRegistro:
                dicRegistro[placa]['TiempoSalida'] = round(time.time(), 0)
        
                diferencia = dicRegistro[placa]['TiempoSalida'] - dicRegistro[placa]['TiempoIngreso']
                cobro, horas, cuartos = CalculoPago(diferencia)
                documento = dicRegistro[placa]['Documento']
        
                if documento in dicUsuarios:
                    nombre = dicUsuarios[documento]['Nombre']
                    apellido = dicUsuarios[documento]['Apellido']
                    vehiculos_retirados.append({
                      "placa": placa,
                      "documento": documento,
                      "nombre": nombre,
                      "apellido": apellido,
                      "ingreso": dicRegistro[placa]['TiempoIngreso'],
                      "salida": dicRegistro[placa]['TiempoSalida'],
                      "cobro": cobro,
                      "horas": horas,
                      "cuartos": cuartos
                  })
                    
                    Facturas.ImprimirFactura(nombre, apellido, documento, placa, cobro, horas, cuartos)
                    del dicRegistro[placa]
        
                    print(f"Vehículo {placa} retirado correctamente. Gracias por su visita.")
                else:
                    print(f"ERROR, No se encontró el documento {documento} asociado al vehículo {placa}.")
        
            else:
                print(f"ERROR, El vehículo {placa} no está registrado dentro del parqueadero.")
            
       
        case '4': # Acceso administrador
            print("\n== ACCESO AL MÓDULO DE ADMINISTRACIÓN ==")
            usuario = input("Usuario administrador: ")
            clave = input("Contraseña: ")
        
            if usuario in usuarios_admin and usuarios_admin[usuario] == clave:
                print("Acceso concedido.")
                admin_module()
            else:
                print(" Usuario o contraseña incorrectos. Acceso denegado.")
                
        case '5': # salir
            print('Gracias, por utilizar parqueadero "La Guarderia, vuelva pronto"')
            break
        case _:
            print('ERROR, Favor revisar, vuelve a intentarlo.')
            continue
