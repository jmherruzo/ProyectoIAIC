from Tkinter import *

class GUI:
	def __init__(self, tk):
		self.ui = tk;
	def initGUI(self):
		cuantia = Label(self.ui, text="Cuantia: ");
		cuantia.pack();
		cuantiaIn = Entry(self.ui, text=cuantia);
		cuantiaIn.pack();
		edad = Label(self.ui, text="Edad: ");
		edad.pack();
		edadIn = Entry(self.ui);
		edadIn.pack();
		duracion = Label(self.ui, text="Duracion del prestamo: ");
		duracion.pack();
		duracionIn = Entry(self.ui);
		duracionIn.pack();
		ahorros = Label(self.ui, text="Dinero ahorrado: ");
		ahorros.pack();
		ahorrosIn = Entry(self.ui);
		ahorrosIn.pack();
		nomina = Label(self.ui, text="Nomina: ");
		nomina.pack();
		nominaIn = Entry(self.ui);
		nominaIn.pack();
		aval = Checkbutton(self.ui, text="Aval")
		aval.pack();
		aval = Checkbutton(self.ui, text="Trabajo estable")
		aval.pack();
		

def main():
	root = Tk()
	root.geometry("300x300+300+300")
	root.title("Concesion de prestamos");
	a = GUI(root);
	a.initGUI();
	root.mainloop()  

if __name__ == '__main__':
    main()  