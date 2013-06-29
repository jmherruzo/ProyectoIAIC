'''
Modulo Python correspondiente al subistema  de Modelo de la Aplicacion 
Su labor principal es la obtencion de informacion del archivo de datos

Created on 29/06/2013

@author: Fernando Cobo Aguilera
@author: Antonio Cubero Fernandez
@author: Jose Manuel Herruzo Ruiz
'''
import Data

def getData():
    """Devuelve los datos incluidos con la aplicacion"""
    return Data.datos;

def getNivel(nivel):
    """Devuelve los datos referentes a un escalon de concesion de prestamos
    @param nivel - Nivel que se devolvera
    @return Datos del nivel indicado"""
    return Data.datos[nivel];

def getNumeroNiveles():
    """Devuelve el numero de niveles incluidos en los datos
    @return Numero de niveles"""
    return Data.datos.count;

def getEuribor():
    """Devuelve el euribor actual
    @return Valor del euribor"""
    return Data.euribor;

def calcularMensualidad(cuantia, interes, duracion):
    """Calcula las mensualidades que se deberian de pagar
    @return Mensualidad del prestamo"""
    cuantia += cuantia*(interes/100);
    return cuantia/(duracion*12);