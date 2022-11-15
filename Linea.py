import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as fgc

class lineaApp():
    def __init__(self):
        #Set root up
        self.root = tk.Tk()
        self.root.geometry('770x570+600+20')
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

        self.save_button = tk.Button(self.mainframe,text='Guardar',font=('Monocraft',15),command=self.save_coord)
        self.save_button.grid(row=7,column=1,padx=5,pady=10)
        
        # self.plot_button = tk.Button(self.mainframe,text='Graficar',font=('Monocraft',15),command=self.plot(x1,x2,y1,y2))
        # self.plot_button.grid(row=3,column=1,padx=5,pady=10,sticky='NWES')
        #MAINLOOP FOR APP
        self.root.mainloop()
#SET CLEAR FUNCTION TO CLEAR WINDOW
    def clear (self):
        x = self.mainframe.grid_slaves()
        for l in x:
            l.destroy()

    def save_coord (self):
        global x1,x2,y1,y2
        
        x1 = int(self.x1_entry.get())
        x2 = int(self.x2_entry.get())
        y1 = int(self.y1_entry.get())
        y2 = int(self.y2_entry.get())

        self.clear()
        #Set button for X values
        self.xvalues = tk.Button(self.mainframe,text='Mostrar valores en X',font=('Monocraft',15),command=lambda:self.xvalues_label.configure(text=f'[{x1},{x2}]'))
        self.xvalues.grid(row=1,column=1,padx=5,pady=10,sticky='NWES')
        #Set button for y values
        self.yvalues = tk.Button(self.mainframe,text='Mostrar valores en Y',font=('Monocraft',15),command=lambda:self.yvalues_label.configure(text=f'[{y1},{y2}]')).grid(row=2,column=1,padx=5,pady=10,sticky='NWES')
        #SETTING LABELS
        self.xvalues_label = ttk.Label(self.mainframe,text='',font=('Monocraft',15),background='grey')
        self.xvalues_label.grid(row=1,column=2,padx=5,pady=10,sticky='NWES')
        self.yvalues_label = ttk.Label(self.mainframe,text='',font=('Monocraft',15),background='grey')
        self.yvalues_label.grid(row=2,column=2,padx=5,pady=10,sticky='NWES')

        # Set ploting button
        self.plot_button = tk.Button(self.mainframe,text='Graficar',font=('Monocraft',15),command=self.plot)
        self.plot_button.grid(row=3,column=1,padx=5,pady=10,sticky='NWES')

    def plot (self):
        self.clear()
        xlist =[x1,x2]
        ylist =[y1,y2]
        #PLOTING
        fig = plt.figure(figsize=(4,4),dpi=100)
        fig.add_subplot(111).plot(xlist,ylist)
        plot = fgc(fig, self.mainframe)
        plt.grid()
        plt.axvline(0,color='black')
        plt.axhline(0,color='black')
        plot.get_tk_widget().grid(row=0,column=0,pady=10)
#UP BUTTON SET UP
        self.up = tk.Button(self.mainframe,text='Mover hacia arriba',font=('Monocraft',15),command=self.up)
        self.up.place(x=410,y=10)
        self.up_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.up_entry.place(x=410,y=50)
#DOWN BUTTON SET UP
        self.down = tk.Button(self.mainframe,text='Mover hacia abajo',font=('Monocraft',15),command=self.down)
        self.down.place(x=410,y=80)
        self.down_entry= ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.down_entry.place(x=410,y=120)
#LEFT BUTTON SET UP
        self.left = tk.Button(self.mainframe,text='Mover hacia la izquierda',font=('Monocraft',15),command=self.left)
        self.left.place(x=410,y=150)
        self.left_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.left_entry.place(x=410,y=190)
#RIGHT BUTTON SET UP
        self.right = tk.Button(self.mainframe,text='Mover hacia la derecha',font=('Monocraft',15),command=self.right)
        self.right.place(x=410,y=220)
        self.right_entry = ttk.Entry(self.mainframe,font=('Monocraft',15))
        self.right_entry.place(x=410,y=260)
    def up (self):
        up = float(self.up_entry.get())
        xlist=[x1,x2]
        ylist =[y1+up,y2+up]
        fig=plt.figure(figsize=(4,4),dpi=100)
        fig.add_subplot(111).plot(xlist,ylist)
        plot = fgc(fig,self.mainframe)
        plt.grid()
        plt.axvline(0,color='black')
        plt.axhline(0,color='black')
        plot.get_tk_widget().grid(row=0,column=0,pady=10)

    def down (self):
        down = float(self.down_entry.get())
        xlist=[x1,x2]
        ylist =[y1-down,y2-down]
        fig=plt.figure(figsize=(4,4),dpi=100)
        fig.add_subplot(111).plot(xlist,ylist)
        plot = fgc(fig,self.mainframe)
        plt.grid()
        plt.axvline(0,color='black')
        plt.axhline(0,color='black')
        plot.get_tk_widget().grid(row=0,column=0,pady=10)

    def left (self):
        left =float(self.left_entry.get())
        xlist=[x1-left,x2-left]
        ylist=[y1,y2]
        fig=plt.figure(figsize=(4,4),dpi=100)
        fig.add_subplot(111).plot(xlist,ylist)
        plot = fgc(fig,self.mainframe)
        plt.grid()
        plt.axvline(0,color='black')
        plt.axhline(0,color='black')
        plot.get_tk_widget().grid(row=0,column=0,pady=10)

    def right (self):
        right = float(self.right_entry.get())
        xlist=[x1+right,x2+right]
        ylist=[y1,y2]
        fig=plt.figure(figsize=(4,4),dpi=100)
        fig.add_subplot(111).plot(xlist,ylist)
        plot = fgc(fig,self.mainframe)
        plt.grid()
        plt.axvline(0,color='black')
        plt.axhline(0,color='black')
        plot.get_tk_widget().grid(row=0,column=0,pady=10)


    
if __name__ == '__main__':
        lineaApp()