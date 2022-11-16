import tkinter as tk 
from tkinter import ttk

class miscApp():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('450x430+1700+20')
        self.root.title('Menu Principal')
        #Set Menu label
        self.tittle_r = ttk.Label(self.root,text='Menu Inicio',font=('Monocraft',20))
        self.tittle_r.pack(side='top')
        #Set mainframe
        self.mainframe = tk.Frame(self.root,background='grey')
        self.mainframe.pack(side='bottom',expand=True,fill='both')
        #Add Motor Menu
        self.motor_menu = tk.Button(self.mainframe,text='< Entrar a Motor >',font=('Monocraft',17),command=self.men_motor)
        self.motor_menu.grid(row=1,column=1,padx=5,pady=10,sticky='NWES')
        #Add Rueda Menu
        self.rueda_menu = tk.Button(self.mainframe,text='< Entrar a Rueda >',font=('Monocraft',17),command=self.men_rued)
        self.rueda_menu.grid(row=2,column=1,padx=5,pady=10,sticky='NWES')
        #Add Ventana Menu
        self.ventana_menu = tk.Button(self.mainframe,text='< Entrar a Ventana >',font=('Monocraft',17),command=self.men_ven)
        self.ventana_menu.grid(row=3,column=1,padx=5,pady=10,sticky='NWES')
        #Add Puerta Menu
        self.puerta_menu = tk.Button(self.mainframe,text='< Entrar a Puerta >',font=('Monocraft',17),command=self.men_puert)
        self.puerta_menu.grid(row=4,column=1,padx=5,pady=10,sticky='NWES')
        
    
        self.root.mainloop()
    def menu_principal (self):
        self.clear()
        self.root.geometry('450x430+1700+20')
        self.tittle_r.config(text='Menu Principal')
        #Add Motor Menu
        self.motor_menu = tk.Button(self.mainframe,text='< Entrar a Motor >',font=('Monocraft',17),command=self.men_motor)
        self.motor_menu.grid(row=1,column=1,padx=5,pady=10,sticky='NWES')
        #Add Rueda Menu
        self.rueda_menu = tk.Button(self.mainframe,text='< Entrar a Rueda >',font=('Monocraft',17),command=self.men_rued)
        self.rueda_menu.grid(row=2,column=1,padx=5,pady=10,sticky='NWES')
        #Add Ventana Menu
        self.ventana_menu = tk.Button(self.mainframe,text='< Entrar a Ventana >',font=('Monocraft',17),command=self.men_ven)
        self.ventana_menu.grid(row=3,column=1,padx=5,pady=10,sticky='NWES')
        #Add Puerta Menu
        self.puerta_menu = tk.Button(self.mainframe,text='< Entrar a Puerta >',font=('Monocraft',17),command=self.men_puert)
        self.puerta_menu.grid(row=4,column=1,padx=5,pady=10,sticky='NWES')
        
    def clear (self):
        x = self.mainframe.grid_slaves()
        for l in x:
            l.destroy()
    
    def men_motor (self):
        self.clear() 
        self.root.geometry('740x220+1700+20')
        self.tittle_r.config(text='Menu Motor')
        #Add On
        self.on = tk.Button(self.mainframe,text='< Encender Motor >',font=('Monocraft',15),command=self.on_m)
        self.on.grid(row=1,column=1,padx=10,pady=15,sticky='NWES')
        #Add Status
        self.status = ttk.Label(self.mainframe,text='<< ESTADO MOTOR >> APAGADO',font=('Monocraft',18))
        self.status.grid(row=4,column=1,padx=10,pady=15)
        #Add Back
        self.back = tk.Button(self.mainframe,text='Volver',font=('Monocraft',15),command=self.menu_principal)
        self.back.grid(row=5,column=1,padx=10,pady=15,sticky='NWES')
    def on_m (self):
        self.status.config(text='<< ESTADO MOTOR >> ENCENDIDO')
        self.off = tk.Button(self.mainframe,text='< Apagar Motor >',font=('Monocraft',15),command=self.off_m)
        self.off.grid(row=1,column=2,padx=10,pady=15,sticky='NWES')
    def off_m (self):
        self.status.config(text='<< ESTADO MOTOR >> APAGADO')

    def men_rued (self):
        self.clear() 
        self.root.geometry('740x220+1700+20')
        self.tittle_r.config(text='Menu Rueda')
        #Add On
        self.inf = tk.Button(self.mainframe,text='< INFLAR >',font=('Monocraft',15),command=self.inflar)
        self.inf.grid(row=1,column=1,padx=10,pady=15,sticky='NWES')
        #Add Status
        self.status = ttk.Label(self.mainframe,text='<< ESTADO RUEDA >> INFLADA',font=('Monocraft',18))
        self.status.grid(row=4,column=1,padx=10,pady=15)
        #Add Back
        self.back = tk.Button(self.mainframe,text='Volver',font=('Monocraft',15),command=self.menu_principal)
        self.back.grid(row=5,column=1,padx=10,pady=15,sticky='NWES')
    def inflar (self):
        self.status.config(text='<< ESTADO RUEDA >> INFLADA')
        self.off = tk.Button(self.mainframe,text='< DESINFLAR >',font=('Monocraft',15),command=self.desinf)
        self.off.grid(row=1,column=2,padx=10,pady=15,sticky='NWES')
    def desinf (self):
        self.status.config(text='<< ESTADO RUEDA >> DESINFLAR')
    
    def men_ven (self):
        self.clear()
        self.root.geometry('740x220+1700+20')
        self.tittle_r.config(text='Menu Ventana')
        #Add On
        self.inf = tk.Button(self.mainframe,text='< ABRIR >',font=('Monocraft',15),command=self.abrir)
        self.inf.grid(row=1,column=1,padx=10,pady=15,sticky='NWES')
        #Add Status
        self.status = ttk.Label(self.mainframe,text='<< ESTADO VENTANA >> CERRADA',font=('Monocraft',18))
        self.status.grid(row=4,column=1,padx=10,pady=15)
        #Add Back
        self.back = tk.Button(self.mainframe,text='Volver',font=('Monocraft',15),command=self.menu_principal)
        self.back.grid(row=5,column=1,padx=10,pady=15,sticky='NWES')
    def abrir (self):
        self.status.config(text='<< ESTADO VENTANA >> ABIERTA')
        self.off = tk.Button(self.mainframe,text='< CERRAR >',font=('Monocraft',15),command=self.cerrar)
        self.off.grid(row=1,column=2,padx=10,pady=15,sticky='NWES')
    def cerrar (self):
        self.status.config(text='<< ESTADO VENTANA >> CERRADA')

    def men_puert (self):
        self.clear()
        self.root.geometry('740x220+1700+20')
        self.tittle_r.config(text='Menu Puerta')
        #Add On
        self.inf = tk.Button(self.mainframe,text='< ABRIR >',font=('Monocraft',15),command=self.abrir_puerta)
        self.inf.grid(row=1,column=1,padx=10,pady=15,sticky='NWES')
        #Add Status
        self.status = ttk.Label(self.mainframe,text='<< ESTADO PUERTA >> CERRADA',font=('Monocraft',18))
        self.status.grid(row=4,column=1,padx=10,pady=15)
        #Add Back
        self.back = tk.Button(self.mainframe,text='Volver',font=('Monocraft',15),command=self.menu_principal)
        self.back.grid(row=5,column=1,padx=10,pady=15,sticky='NWES')
    def abrir_puerta (self):
        self.status.config(text='<< ESTADO PUERTA >> ABIERTA')
        self.off = tk.Button(self.mainframe,text='< CERRAR >',font=('Monocraft',15),command=self.cerrar_puerta)
        self.off.grid(row=1,column=2,padx=10,pady=15,sticky='NWES')
    def cerrar_puerta (self):
        self.status.config(text='<< ESTADO PUERTA >> CERRADA')

    
    
if __name__ == '__main__':
    miscApp()