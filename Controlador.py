'''
Created on 28/06/2013

@author: Fernando Cobo Aguilera
@author: Antonio Cubero Fernandez
@author: Jose Manuel Herruzo Ruiz
'''

class Controlador:
    def procesar(self, valores, gui):
        self.campos = valores;
        self.ui = gui;
        for campo in self.campos:
            print campo + " " + str(self.campos[campo])
    def getInteres(self):
        if self.campos["Interes variable"]==0:
            return 5;
        else:
            return 2;
    def concedido(self):
        return True;