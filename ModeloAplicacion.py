'''
Created on 29/06/2013

@author: Fernando Cobo Aguilera
@author: Antonio Cubero Fernandez
@author: Jose Manuel Herruzo Ruiz
'''
import Data

def getData():
    return Data.datos;

def getNivel(nivel):
    return Data.datos[nivel];

def getNumeroNiveles():
    return Data.datos.count;

def getEuribor():
    return Data.euribor;

def calcularMensualidad(cuantia, interes, duracion):
    cuantia += cuantia*(interes/100);
    return cuantia/(duracion*12);