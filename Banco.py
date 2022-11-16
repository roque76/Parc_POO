import tkinter as tk
from tkinter import ttk

class bancoApp():
    def __init__(self):
        #SET ROOT UP
        self.root = tk.Tk()
        self.root.geometry('770x570+1400+20')
        self.root.title('BANCO')
        #Set title from root
        self.title_r = ttk.Label(self.root,text='Cuenta Bancaria',font=('Monocraft',25))
        self.title_r.pack(side='top')
        #Set Mainframe
        self.mainframe = tk.Frame(self.root,background='grey')
        self.mainframe.pack(side='bottom',fill='both',expand=True)
        # Set # Account
        self.account = ttk.Label(self.mainframe,text='Ingresar # de cuenta >>',font=('Monocraft',17),background='grey70')
        self.account.grid(row=1,column=1,padx=5,pady=10,sticky='NWES')
        self.account_entry = ttk.Entry(self.mainframe,font=('Monocraft',17))
        self.account_entry.grid(row=1,column=2,padx=5,pady=10,sticky='NWES')
        #Set # DNI
        self.dni = ttk.Label(self.mainframe,text='Ingresar # de DNI >>',font=('Monocraft',17),background='grey70')
        self.dni.grid(row=2,column=1,padx=5,pady=10,sticky='NWES')
        self.dni_entry = ttk.Entry(self.mainframe,font=('Monocraft',17))
        self.dni_entry.grid(row=2,column=2,padx=5,pady=10,sticky='NWES')
        #Set Interes
        self.interes = ttk.Label(self.mainframe,text='Tasa de interes anual >>',font=('Monocraft',17),background='grey70')
        self.interes.grid(row=3,column=1,padx=5,pady=10,sticky='NWES')
        self.interes_entry = ttk.Entry(self.mainframe,font=('Monocraft',17))
        self.interes_entry.grid(row=3,column=2,padx=5,pady=10,sticky='NWES')
        #Set Saldo
        self.saldo = ttk.Label(self.mainframe,text='Saldo actual >>',font=('Monocraft',17),background='grey70')
        self.saldo.grid(row=4,column=1,padx=5,pady=10,sticky='NWES')
        self.saldo_entry = ttk.Entry(self.mainframe,font=('Monocraft',17))
        self.saldo_entry.grid(row=4,column=2,padx=5,pady=10,sticky='NWES')
        #Set Save Button
        self.save = tk.Button(self.mainframe,text='Guardar Datos.',font=('Monocraft',22),command=self.save)
        self.save.grid(row=5,column=1,padx=5,pady=10)
        self.root.mainloop()

    def save (self):
        global DNI,num_cuenta,interes,saldo_actual,int_diario

        num_cuenta = int(self.account_entry.get())
        DNI = int(self.dni_entry.get())
        interes = int(self.interes_entry.get())
        saldo_actual = float(self.saldo_entry.get())
        int_diario = 0
        self.menu()

    def clear(self):
        x = self.mainframe.grid_slaves()
        for i in x:
            i.destroy()

    def menu (self):
        self.clear()
        self.display_data = tk.Button(self.mainframe,text='Visualizar Datos',font=('Monocraft',18),command=self.display).grid(row=1,column=1,padx=7,pady=10)
        self.update_menu = tk.Button(self.mainframe,text='Actualizar Saldo',font=('Monocraft',17),command=self.update)
        self.update_menu.grid(row=1,column=2,padx=202,pady=10)


    def update (self):
        self.clear()
        #Suma Method
        self.agregar = tk.Button(self.mainframe,text='Ingresar  >>',font=('Monocraft',15),command=self.suma).grid(row=1,column=1,padx=5,pady=10,sticky='NWES')
        self.agregar_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.agregar_entry.grid(row=1,column=2,padx=5,pady=10,sticky='NWES')
        #Resta Method
        self.retirar = tk.Button(self.mainframe,text='Retirar dinero >>',font=('Monocraft',15),command=self.resta)
        self.retirar.grid(row=2,column=1,padx=5,pady=10,sticky='NWES')
        #Entry
        self.retirar_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.retirar_entry.grid(row=2,column=2,padx=5,pady=10,sticky='NWES')
        #Saldo crudo
        self.saldo_crudo = ttk.Label(self.mainframe,text=saldo_actual,font=('Monocraft',15)).grid(row=3,column=1,padx=5,pady=10,sticky='NWES')
        #Menu
        self.men_button = tk.Button(self.mainframe,text='Volver a Menu principal.',font=('Monocraft',17),command=self.menu)
        self.men_button.grid(row=5,column=1,padx=5,pady=10,sticky='NWES')

        
    def suma (self):
        global saldo_actual,int_diario
        sum = float(self.agregar_entry.get())
        saldo_actual = saldo_actual +sum   
        int_diario = (saldo_actual*interes)/365
        self.update()
    
    def resta(self):
        global saldo_actual, int_diario
        res = float(self.retirar_entry.get())
        saldo_actual = saldo_actual-res
        int_diario = (saldo_actual*interes)/365
        self.update()

    def display (self):
        self.clear()
        self.title_r.configure(text='Visualización de Datos')
        #SHOW DNI
        self.dni = ttk.Label(self.mainframe,text='Número de DNI >>',font=('Monocraft',20)).grid(row=1,column=1,padx=0,pady=15,sticky='NWES')
        self.dni_label = ttk.Label(self.mainframe,text=DNI,font=('Monocraft',20)).grid(row=1,column=2,padx=0,pady=15,sticky='NWES')
        #SHOW ACCOUNT NUMBER
        self.account = ttk.Label(self.mainframe,text='Número de cuenta bancaria >>',font=('Monocraft',20)).grid(row=2,column=1,padx=0,pady=15,sticky='NWES')
        self.account_label = ttk.Label(self.mainframe,text=num_cuenta,font=('Monocraft',20)).grid(row=2,column=2,padx=0,pady=15,sticky='NWES')
        #SHOW INTERES
        self.interes = ttk.Label(self.mainframe,text='Interes anual >>',font=('Monocraft',20)).grid(row=3,column=1,padx=0,pady=15,sticky='NWES')
        self.interes_label = ttk.Label(self.mainframe,text=interes,font=('Monocraft',20)).grid(row=3,column=2,sticky='NWES',padx=0,pady=15)
        #GO BACK BUTTON
        self.menu = tk.Button(self.mainframe,text='Volver a Menu principal.',font=('Monocraft',17),command=self.menu)
        self.menu.grid(row=5,column=1,padx=5,pady=10,sticky='NWES')
        #Set saldo 
        self.saldo = ttk.Label(self.mainframe,text='Saldo Actual >>',font=('Monocraft',20)).grid(row=4,column=1,padx=0,pady=15,sticky='NWES')
        self.saldo_label = ttk.Label(self.mainframe,text=saldo_actual+int_diario,font=('Monocraft',20)).grid(row=4,column=2,padx=0,pady=15,sticky='NWES')
        
if __name__ =='__main__':
    bancoApp()