# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 14:51:10 2025

@author: juanp
"""

def registro_usuario2(dic:dict, documento:str, nombre:str, apellido:str, placa:str):
    if isinstance(dic,dict):
        llaves = list(dic.keys())
        if documento in llaves:
            return False
        else:
            dic[documento] = {
                'Nombre':nombre, 
                'Apellido':apellido, 
                'Placa':placa,
                }
            return dic
    else:
        return False