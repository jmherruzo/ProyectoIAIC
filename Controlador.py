'''
Subsistema de Controlador, se encarga de controlar y procesar las peticiones de los usuarios

Created on 28/06/2013

@author: Fernando Cobo Aguilera
@author: Antonio Cubero Fernandez
@author: Jose Manuel Herruzo Ruiz
'''
import ModeloAplicacion

class Controlador:
    """Clase encargada de procesar una peticion y devolver su resultado"""
    def procesar(self, valores):
        """Procesa una peticion y devuelve un valor boolean
        @param valores - Valores introducidos por el cliente"""
        self.campos = valores;
        self.datos = ModeloAplicacion.getData();
        self.resultados = []
        for nivel in self.datos:
            aux = True;
            if self.campos["Ahorros"] < self.campos["Cuantia"]*nivel["ahorros"]:
                aux = False
                self.motivo = "Ahorros insuficientes"
            elif self.campos["Edad"]+self.campos["Duracion"]>nivel["edad"]:
                aux = False
                self.motivo = "La edad sumada a la duracion del prestamo supera el limite"
            elif self.campos["Duracion"]>nivel["duracion"]:
                aux=False;
                self.motivo = "La duracion supera el limite"
            elif self.campos["Trabajo Estable"]<nivel["trabajo"]:
                aux=False;
                self.motivo = "Es necesario un trabajo estable"
            elif self.campos["Aval"] < nivel["aval"]:
                aux=False;
                self.motivo = "Es necesario un aval"
            elif self.campos["Edad"] < nivel["edad_min"]:
                aux=False;
                self.motivo = "Son necesarios al menos 18 anyos para la concesion del prestamo"
            
            if aux==True:
                self.mensualidad = ModeloAplicacion.calcularMensualidad(self.campos["Cuantia"], nivel["interes_fijo"], self.campos["Duracion"]);
                if self.campos["Nomina"]*nivel["nomina"] < self.mensualidad:
                    aux = False;     
                    self.motivo = "Nomina insuficiente"
                
            self.resultados.append(aux);
            
        concesion = False;
        for result in self.resultados:
            if result:
                concesion = True;
                break;
            
                
        return concesion;
            
        
    def getInteres(self):
        """Devuelve el interes del ultimo prestamo procesado, en caso de concesion
        @return Interes del prestamo"""
        for i in range(0, len(self.datos), 1):
            if self.resultados[i]:
                if self.campos["Interes variable"]==1:
                    return self.datos[i]["interes_variable"]+ModeloAplicacion.getEuribor();
                else:
                    return self.datos[i]["interes_fijo"];
    def getMensualidad(self):
        """Devuelve la mensualidad que habria que pagar por el ultimo prestamo procesado
        @return Mensualidad del prestamo"""
        return self.mensualidad;
    
    def getMotivo(self):
        """Devuelve el motivo de la denegacion de un prestamo
        @return Motivo de la denegacion del prestamo"""
        return self.motivo;