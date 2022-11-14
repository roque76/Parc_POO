import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as fgc
from matplotlib.patches import Rectangle
import math as m


class appCont (tk.Tk):
    def __init__(self):
        #Set root up
        self.root = tk.Tk()
        self.root.geometry('770x570+1700+20')
        self.root.title('RECTANGULO')
        #Set Mainframe up
        self.mainframe = tk.Frame(self.root,background='grey')
        self.mainframe.pack(side='bottom',fill='both',expand=True)
        #Set title label
        self.title_r = ttk.Label(self.root,text='Moldeo rectangulo',font=('Monocraft',20),foreground='black')
        self.title_r.pack(side='top',padx=5,pady=10)
        #Set dropdown menu
        self.dropmenu = ttk.Combobox(self.mainframe,values=['Base y Altura','Puntos'],font=('Monocraft',15))
        self.dropmenu.grid(row=1,column=2,padx=5,pady=10,sticky='s')
        #Set button for dropdown menu
        self.options = tk.Button(self.mainframe,font=('Monocraft',15),text='Fijar opcion',command=self.option)
        self.options.grid(row=1,column=1,padx=5,pady=10,sticky='NWES')


        self.root.mainloop()
    #Set function for options on dropdown menu
    def option(self):
        option = self.dropmenu.get()
        if option == 'Puntos':
          self.puntos()
        elif option == 'Base y Altura':
            self.bh()
        else:
            self.error = tk.Button(self.mainframe,text='OPCION FUERA DE RANGO', font=('Monocraft',20),command=lambda: self.error.destroy())
            self.error.grid(row=2,column=2)
    # Set funciton to clear tkinter UI
    def clear (self):
        x = self.mainframe.grid_slaves()
        for l in x:
            l.destroy()
    
    def puntos(self):
        self.clear()
        self.title_r.configure(text='Moldeado por puntos')
#SETTING UP LABELS
        #Set x1 label
        self.x1_button = ttk.Label(self.mainframe,text='Ingresar valor de X en vertice inferior izquierdo >>',font=('Monocraft',10))
        self.x1_button.grid(row=1,column=1,padx=5,pady=10,sticky='NWES')
        #Set y1 label
        self.y1_button = ttk.Label(self.mainframe,text='Ingresar valor de Y en vertice inferior izqueirdo >>',font=('Monocraft',10))
        self.y1_button.grid(row=2,column=1,padx=5,pady=10,sticky='NWES')
        # Set x2 Label
        self.x2_button = ttk.Label(self.mainframe,text='Ingresar valor de X en vertice superior izquierdo >>',font=('Monocraft',10))
        self.x2_button.grid(row=3,column=1,padx=5,pady=10,sticky='NWES')
        #Set y2 Label
        self.y2_button = ttk.Label(self.mainframe,text='Ingresar valor de Y en vertice superior izqueirdo >>',font=('Monocraft',10))
        self.y2_button.grid(row=4,column=1,padx=5,pady=10,sticky='NWES')
        # Set x3 Label 
        self.x3_button = ttk.Label(self.mainframe,text='Ingresar valor de X en vertice superior derecho >>',font=('Monocraft',10))
        self.x3_button.grid(row=5,column=1,padx=5,pady=10,sticky='NWES')
        # Set y3 Label
        self.y3_button = ttk.Label(self.mainframe,text='Ingresar valor de Y en vertice superior derecho >>',font=('Monocraft',10))
        self.y3_button.grid(row=6,column=1,padx=5,pady=10,sticky='NWES')
        # Set x4 Label
        self.x4_button = ttk.Label(self.mainframe,text='Ingresar valor de X en vertice inferior derecho >>',font=('Monocraft',10))
        self.x4_button.grid(row=7,column=1,padx=5,pady=10,sticky='NWES')
        # Set y4 Label
        self.y4_button = ttk.Label(self.mainframe,text='Ingresar valor de Y en vertice inferior derecho >>',font=('Monocraft',10))
        self.y4_button.grid(row=8,column=1,padx=5,pady=10,sticky='NWES')

#SETTING UP ENTRYS
        #Set x1 entry
        self.x1_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.x1_entry.grid(row=1,column=2,padx=5,pady=10)
        #Set y1 entry
        self.y1_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.y1_entry.grid(row=2,column=2,padx=5,pady=10)
        # Set x2 entry
        self.x2_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.x2_entry.grid(row=3,column=2,padx=5,pady=10)
        #Set y2 entry
        self.y2_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.y2_entry.grid(row=4,column=2,padx=5,pady=10)
        #Set x3 entry
        self.x3_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.x3_entry.grid(row=5,column=2,padx=5,pady=10)
        #Set y3 entry
        self.y3_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.y3_entry.grid(row=6,column=2,padx=5,pady=10)
        #Set x4 entry
        self.x4_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.x4_entry.grid(row=7,column=2,padx=5,pady=10)
        #Set y4 entry
        self.y4_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.y4_entry.grid(row=8,column=2,padx=5,pady=10)
#SET UP COORDINATE BUTTON
        self.coordenada = tk.Button(self.mainframe,text='Graficar',font=('Monocraft',25),command=self.cord).grid(row=12,column=1,padx=5)

    def cord (self):
        x1 = int(self.x1_entry.get())
        y1 = int(self.y1_entry.get())
        x2 = int(self.x2_entry.get())
        y2 = int(self.y2_entry.get())
        x3 = int(self.x3_entry.get())
        y3 = int(self.y3_entry.get())
        x4 = int(self.x4_entry.get())
        y4 = int(self.y4_entry.get())
        
        self.clear()

        xlist=[x1,x2,x3,x4,x1]
        ylist=[y1,y2,y3,y4,y1]

        h = m.sqrt((x1-x2)**2)+((y1-y2)**2)
        b = m.sqrt((x1-x4)**2)+((y1-y4)**2)
        a = b*h

        fig = plt.figure(figsize=(5,5),dpi=(100))
        fig.add_subplot(111).plot(xlist,ylist)
        plot = fgc(fig,self.mainframe)
        plot.get_tk_widget().grid(row=1,column=1)
        plt.grid()
        plt.axhline(0,color='black')
        plt.axvline(0,color='black')

        self.res = ttk.Label(self.mainframe,text ='',font=('Monocraft',15),background='white')
        self.res.place(anchor='n',x=250,y=20)

        self.area = tk.Button(self.mainframe,text='Calcular Area',command=lambda: self.res.configure(text=a) ,font=('Monocraft',15))
        self.area.place(anchor='n',x=100,y=10)

    def bh (self):
        self.clear()
        #Change title
#SET LABELS UP
        self.title_r.configure(text='Modelado por base y altura')
        #Set label for base
        self.base_la = ttk.Label(self.mainframe,text='Ingresar base del rectangulo >>',font=('Monocraft',10)).grid(row=1,column=1,padx=5,pady=10,sticky='NWES')
        #Set label for height
        self.height_la = ttk.Label(self.mainframe,text='Ingresar valor de altura del rectangulo >>',font=('Monocraft',10)).grid(row=2,column=1,padx=5,pady=10,sticky='NWES')
#SET ENTRYS UP
        self.base_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.base_entry.grid(row=1,column=2,padx=5,pady=10,sticky='NWES')
        self.height_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.height_entry.grid(row=2,column=2,padx=5,pady=10,sticky='NWES')
#SET BUTTON UP
        self.graph = tk.Button(self.mainframe,font=('Monocraft',20),command=self.plot_bh,text='Graficar').grid(row=4,column=1,padx=5,pady=10)        

    def plot_bh (self):
        b = int(self.base_entry.get())
        h = int(self.height_entry.get())

        a = b*h
        self.clear()

        fig, ax = plt.subplots()
        ax.plot([0,5],[0,5],color='white')
        ax.add_patch(Rectangle((0,0),b,h,fill=False))
        plot = fgc(fig,self.mainframe)
        plot.get_tk_widget().grid(row=1,column=1,padx=5,pady=10)
#SET UP AREA LABEL AND BUTTON
        self.res_a = ttk.Label(self.mainframe,background='white',text='',font=('Monocraft',15))
        self.res_a.place(anchor='n',x=250,y=20)
        self.area = tk.Button(self.mainframe,text='Calcular area',font=('Monocraft',15),command=lambda: self.res_a.configure(text=a))
        self.area.place(anchor='n',x=100,y=10)
#SET MOVE ENTRY AND BUTTON
        #Setting labels
        self.ud = ttk.Label(self.mainframe,text='Val negativo Val positivo ^',font=('Monocraft',10))
        self.ud.grid(row=2,column=1,padx=5,sticky='NWES')
        self.lr = ttk.Label(self.mainframe,text='Val negativo < .Val positivo >',font=('Monocraft',10))
        self.lr.grid(row=3,column=1,padx=5,pady=10,sticky='NWES')
        #Placing Entry
        self.ud_entry =ttk.Entry(self.mainframe,font=('Monocraft',10))
        self.ud_entry.place(x=300,y=499)
        #Placing Entry
        self.lr =ttk.Entry(self.mainframe,font=('Monocraft',10))
        self.lr.place(x=300, y=527)
        #Setting base label
        self.base_la = ttk.Label(self.mainframe,text='Valor Base',font=('Monocraft',10))
        self.base_la.grid(sticky='NWES',padx=5,pady=10)
        self.base_la.place(x=640,y=10)
        #Setting base entry
        self.base_entry = ttk.Entry(self.mainframe,font=('Monocraft',10))
        self.base_entry.grid(sticky='NWES',padx=5,pady=10)
        self.base_entry.place(x=640,y=30)
        #Setting Height label
        self.height_la = ttk.Label(self.mainframe,text='Valor Altura',font=('Monocraft',10))
        self.height_la.grid(sticky='NWES',padx=5,pady=10)
        self.height_la.place(x=640,y=50)
        #Setting height entry
        self.height_entry = ttk.Entry(self.mainframe,font=('Monocraft',10))
        self.height_entry.grid(sticky='NWES',padx=5,pady=10)
        self.height_entry.place(x=640,y=70)
        #Setting ud button
        self.ud_button = tk.Button(self.mainframe,text='Mover!',font=('Monocraft',10),command=self.move_ud)
        self.ud_button.place(x=510,y=498)
        
        return b,h

    def move_ud (self):
        b = int(self.base_entry.get())
        h = int(self.height_entry.get())
        
        ud = int(self.ud_entry.get())

        self.clear( )
        fig, ax = plt.subplots()
        ax.plot([0,5],[0,5],color='white')
        ax.add_patch(Rectangle((0,0+ud),b,h,fill=False))
        plot = fgc(fig,self.mainframe)
        plot.get_tk_widget().grid(row=1,column=1,padx=5,pady=10)


if __name__== '__main__':
    appCont()