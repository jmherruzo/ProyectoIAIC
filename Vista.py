'''
Created on 28/06/2013

@author: Fernando Cobo Aguilera
@author: Antonio Cubero Fernandez
@author: Jose Manuel Herruzo Ruiz
'''

from Tkinter import Label, Entry, Checkbutton, Tk, Button, IntVar
from Tkinter import *
from Controlador import Controlador
import tkMessageBox
import exceptions

campos = {"Cuantia":0, "Edad":1, "Duracion":2, "Ahorros":3, "Nomina":4};
checkBox = {"Trabajo Estable":0, "Aval":1, "Interes variable":2};
cbRefs = {"Trabajo Estable":0, "Aval":1, "Interes variable":2}
valores = {"Cuantia":0, "Edad":1, "Duracion":2, "Ahorros":3, "Nomina":4, "Trabajo Estable":5, "Aval":6, "Interes variable":7};

def mensaje(msg):
	tkMessageBox.showinfo(msg)

class GUI:
	def __init__(self, tk):
		self.ui = tk;
		self.ctrl = Controlador();
	def setBoton(self, but):
		self.b = but;
	def initGUI(self):
		for campo in campos:
			cad = campo + ":"
			l = Label(self.ui, text=cad);
			l.pack();
			campos[campo] = Entry(self.ui);
			campos[campo].pack();
		for cb in checkBox:
			cbRefs[cb] = IntVar();
			checkBox[cb] = Checkbutton(self.ui, text=cb, var=cbRefs[cb]);
			checkBox[cb].pack();
	def boton(self):
		try:
			for campo in campos:
				valores[campo] = int(campos[campo].get());
			for cb in checkBox:
				valores[cb] = cbRefs[cb].get();
			concedido = self.ctrl.procesar(valores, self.ui);
			if concedido:
				interes = str(self.ctrl.getInteres());
				tkMessageBox.showinfo("Enhorabuena", "Su prestamo ha sido concedido con un interes del "+ interes + "%" +"\n"
									+"Mensualidad: " + str(self.ctrl.getMensualidad()) + "Euros")
			else:
				tkMessageBox.showinfo("Lo sentimos", "Su prestamo ha sido denegado \n Motivo: " + self.ctrl.getMotivo())

		except exceptions.ValueError:
			tkMessageBox.showinfo("Error", "Algun campo esta vacio o es de un tipo erroneo")
		


def main():
	root = Tk();
	root.geometry("300x300+300+300")
	root.title("Concesion de prestamos");
	a = GUI(root);
	b = Button(root, text="OK", command=a.boton)
	a.setBoton(b);
	a.initGUI();
	b.pack()
	root.mainloop()  
if __name__ == '__main__':
	main()  