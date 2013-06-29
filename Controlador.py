'''
Created on 28/06/2013

@author: Fernando Cobo Aguilera
@author: Antonio Cubero Fernandez
@author: Jose Manuel Herruzo Ruiz
'''
import ModeloAplicacion

class Controlador:
    def procesar(self, valores, gui):
        self.campos = valores;
        self.ui = gui;
        self.datos = ModeloAplicacion.getData();
        self.resultados = []
        for nivel in self.datos:
            aux = True;
            if self.campos["Ahorros"] < self.campos["Cuantia"]*nivel["ahorros"]:
                aux = False
            elif self.campos["Edad"]+self.campos["Duracion"]>nivel["edad"]:
                aux = False
            elif self.campos["Duracion"]>nivel["duracion"]:
                aux=False;
            elif self.campos["Trabajo Estable"]<nivel["trabajo"]:
                aux=False;
            elif self.campos["Aval"] < nivel["aval"]:
                aux=False;
            elif self.campos["Edad"] < nivel["edad_min"]:
                aux=False;
            
            if aux==True:
                self.mensualidad = ModeloAplicacion.calcularMensualidad(self.campos["Cuantia"], nivel["interes_fijo"], self.campos["Duracion"]);
                if self.campos["Nomina"] < self.mensualidad*nivel["nomina"]:
                    aux = False;     
            
            self.resultados.append(aux);
            
        concesion = False;
        for result in self.resultados:
            if result:
                concesion = True;
                break;
                
        return concesion;
            
        
    def getInteres(self):
        for i in range(0, len(self.datos), 1):
            if self.resultados[i]:
                if self.campos["Interes variable"]==1:
                    return self.datos[i]["interes_variable"]+ModeloAplicacion.getEuribor();
                else:
                    return self.datos[i]["interes_fijo"];
    def getMensualidad(self):
        return self.mensualidad;