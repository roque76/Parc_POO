import tkinter as tk 
from tkinter import ttk

class cafeteraApp():
    def __init__(self):
        global c_max
        c_max = 1000
        #Set up Root
        self.root = tk.Tk()
        self.root.geometry('770x430+1700+20')
        self.title_r = ttk.Label(self.root,text='Cafetera',font=('Monocraft',20))
        self.title_r.pack(side='top')
        #Mainframe
        self.mainframe = tk.Frame(self.root,background='grey')
        self.mainframe.pack(side='bottom',expand=True,fill='both')
        # Cap
        self.actual_label = ttk.Label(self.mainframe,text='',font=('Monocraft',17),background='grey')
        self.actual_label.grid(row=2,column=1,padx=5,pady=10,sticky='NWES')
        self.actual = tk.Label(self.mainframe,text=0,font=('Monocraft',17),background='grey')
        self.actual.grid(row=2,column=2,padx=5,pady=10,sticky='NWES')
        #Capacidad maxima
        self.c_max = ttk.Label(self.mainframe,text='Capacidad maxima >>',font=('Monocraft',17))
        self.c_max.grid(row=1,column=1,padx=0,pady=10,sticky='NWES')
        self.c_max_value = ttk.Label(self.mainframe,text=c_max,font=('Monocraft',17)).grid(row=1,column=2,padx=0,pady=10,sticky='NWES')
        #Set empyt button
        # self.empty = tk.Button(self.mainframe,text='Vaciar Cafetera',command=self.empty_c,font=('Monocraft',15)).grid(row=3,column=1,padx=5,pady=10,sticky='NWES')
        #Set Add Button
        self.add = tk.Button(self.mainframe,text='< Agregar café >>',font=('Monocraft',17),command=self.add_c).grid(row=4,column=1,padx=5,pady=10,sticky='NWES')
        self.add_entry = ttk.Entry(self.mainframe,font=('Monocraft',17))
        self.add_entry.grid(row=4,column=2,padx=5,pady=10,sticky='NWES')
        #Set Llenado
        self.full = tk.Button(self.mainframe,text='< LLenar Cafetera >',font=('Monocraft',17),command=self.full_c).grid(row=3,column=1,padx=5,pady=10,sticky='NWES')
       
        self.root.mainloop()
    
    def clear(self):
        x = self.mainframe.grid_slaves()
        for i in x:
            i.destroy()

    def full_c (self):
            global cap_actual
            cap_actual = c_max
            self.actual_label.config(text='< Capacidad Actual >>',background='white')
            self.actual.config(text=cap_actual,background='white')
            self.vaciar = tk.Button(self.mainframe,text='< Vaciar Cafetera >',font=('Monocraft',17),command=self.empty).grid(row=3,column=2,padx=5,pady=10,sticky='NWES')
            self.servir = tk.Button(self.mainframe,text='< Servir Café >>',font=('Monocraft',17),command=self.serve).grid(row=5,column=1,padx=5,pady=10,sticky='NWES')
            self.servir_entry = ttk.Entry(self.mainframe,font=('Monocraft',17))
            self.servir_entry.grid(row=5,column=2,padx=5,pady=10)
    def empty (self):
            self.actual.config(text=0)
        
    def add_c (self):
        global cap_actual
        cap_actual_val = int(self.actual.cget('text'))
        if cap_actual_val <c_max:
            cap_actual = float(self.add_entry.get())
            if cap_actual <= c_max:
                self.actual_label.config(text='< Capacidad Actual>>', background='white') 
                self.actual.config(text=cap_actual)
                #Set serve
                self.servir = tk.Button(self.mainframe,text='< Servir Café >>',font=('Monocraft',17),command=self.serve).grid(row=5,column=1,padx=5,pady=10,sticky='NWES')
                self.servir_entry = ttk.Entry(self.mainframe,font=('Monocraft',17))
                self.servir_entry.grid(row=5,column=2,padx=5,pady=10)
                #Set empty
                self.vaciar = tk.Button(self.mainframe,text='< Vaciar Cafetera >',font=('Monocraft',17),command=self.empty).grid(row=3,column=2,padx=5,pady=10,sticky='NWES')
        else:
            self.error = tk.Button(self.mainframe,text='Error, Cantidad Maxima superada',font=('Monocraft',15),command=lambda: self.error.destroy())
            self.error.grid(row=8,column=1,padx=10,pady=15)
    def serve (self):
        global cap_actual
        res = float(self.servir_entry.get())
        cap_actual = cap_actual-res
        self.actual.config(text=cap_actual)
if __name__ == '__main__':
    cafeteraApp()