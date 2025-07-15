# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 20:04:24 2025

@author: juanp
"""

from datetime import datetime

def ImprimirFacturaIngreso(nombre: str, documento: str, placa: str):
    ahora = datetime.now()
    fecha_ingreso = ahora.strftime('%Y-%m-%d')
    hora_ingreso = ahora.strftime('%I:%M:%S %p')

    factura_ingreso = (
        f"\n{'*'*60}\n"
        f"{'PARQUEADERO \"LA GUARDERÍA\"'.center(60)}\n"
        f"{'RECIBO DE INGRESO'.center(60)}\n"
        f"{'*'*60}\n"
        f"{'Fecha de ingreso:':<25} {fecha_ingreso}\n"
        f"{'Hora de ingreso:':<25} {hora_ingreso}\n"
        f"{'-'*60}\n"
        f"{'Cliente:':<25} {nombre}\n"
        f"{'Documento:':<25} {documento}\n"
        f"{'Placa del vehículo:':<25} {placa}\n"
        f"{'*'*60}\n"
        f"{'¡Gracias por preferirnos!'.center(60)}\n"
        f"{'*'*60}\n"
    )

    print(factura_ingreso)

def ImprimirFactura(nombre: str, apellido: str, documento: str, placa: str, cobro: float, horas: int, cuartos: int):
    ahora = datetime.now()
    fecha_emision = ahora.strftime('%Y-%m-%d')
    hora_emision = ahora.strftime('%I:%M:%S %p')

    factura = (
        f"\n{'*'*60}\n"
        f"{'PARQUEADERO "LA GUARDERÍA"'.center(60)}\n"
        f"{'FACTURA PARQUEADERO'.center(60)}\n"
        f"{'*'*60}\n"
        f"{'Fecha de emisión:':<25} {fecha_emision}\n"
        f"{'Hora de emisión:':<25} {hora_emision}\n"
        f"{'-'*60}\n"
        f"{'Cliente:':<25} {nombre} {apellido}\n"
        f"{'Documento:':<25} {documento}\n"
        f"{'Placa del vehículo:':<25} {placa}\n"
        f"{'-'*60}\n"
        f"{'Horas completas:':<25} {horas}\n"
        f"{'Cuartos de hora:':<25} {cuartos}\n"
        f"{'Valor horas:':<25} ${horas * 7000}\n"
        f"{'Valor cuartos:':<25} ${cuartos * 1500}\n"
        f"{'-'*60}\n"
        f"{'TOTAL A PAGAR:':<25} ${cobro}\n"
        f"{'*'*60}\n"
        f"{'¡Gracias por su visita!'.center(60)}\n"
        f"{'*'*60}\n"
    )
    print(factura)

