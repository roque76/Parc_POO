import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as fgc

class lineaApp():
    def __init__(self):
        #Set root up
        self.root = tk.Tk()
        self.root.geometry('770x570+2200+20')
        self.root.title('LINEA RECTA')
        #Set Mainframe up
        self.mainframe = tk.Frame(self.root,background='grey')
        self.mainframe.pack(side='bottom',fill='both',expand=True)
        #Set title lable
        self.title_r = ttk.Label(self.root,text='Modelado Linea Recta',font=('Monocraft',20))
        self.title_r.pack(side='top',padx=5,pady=10)
        #Set label for x1
        self.x1_label = ttk.Label(self.mainframe,text='Valor de X en primera coordenada >>',font=('Monocraft',15),background='grey76')
        self.x1_label.grid(row=1,column=1,padx=5,pady=10,sticky='NWES')
        #Set x1 entry
        self.x1_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.x1_entry.grid(row=1,column=2,padx=5,pady=10,sticky='NWES')
        #Set Label for y1
        self.y1_label = ttk.Label(self.mainframe,text='Valor de Y en primera coordenada >>',font=('Monocraft',15),background='grey76')
        self.y1_label.grid(row=2,column=1,padx=5,pady=10,sticky='NWES')
        #Set y1 entry
        self.y1_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.y1_entry.grid(row=2,column=2,padx=5,pady=10,sticky='NWES')
        #Set x2 Label
        self.x2_label = ttk.Label(self.mainframe,text='Valor de X en segunda coordenada >>',font=('Monocraft',15),background='grey76')
        self.x2_label.grid(row=5,column=1,padx=5,pady=10,sticky='NWES')
        #Set x2 Entry
        self.x2_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.x2_entry.grid(row=5,column=2,padx=5,pady=10,sticky='NWES')
        #Set y2 Label
        self.y2_label = ttk.Label(self.mainframe,text='Valor de Y en segunda coordenada >>',font=('Monocraft',15),background='grey76')
        self.y2_label.grid(row=6,column=1,padx=5,pady=10,sticky='NWES')
        #Set y2 entry
        self.y2_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.y2_entry.grid(row=6,column=2,padx=5,pady=10,sticky='NWES')
#SET BUTTONS

        self.save_button = tk.Button(self.mainframe,text='Guardar Coordenadas')


        #MAINLOOP FOR APP
        self.root.mainloop()


if __name__ == '__main__':
    lineaApp()