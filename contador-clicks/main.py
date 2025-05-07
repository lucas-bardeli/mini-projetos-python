
import tkinter as tk

root = tk.Tk()
root.geometry('300x300')
root.title('Contador de clicks')
root.configure(bg='#1d1d1d')

numero = 0


def mais():
    global numero
    numero = numero + 1
    contagem_clicks.configure(text=numero)


def menos():
    global numero
    numero = numero - 1
    contagem_clicks.configure(text=numero)
   

margem = tk.Canvas(root, height=80, background='#1d1d1d', bd=0, highlightthickness=0, relief='flat')
margem.pack()

botao_mais = tk.Button(root, bg='#fff', text='+', font=('Montserrat', 16, 'bold'), padx=10, command=mais)
botao_mais.pack()

contagem_clicks = tk.Label(root, text=numero, fg='#fff', bg='#1d1d1d', font=('Montserrat', 16, 'bold'))
contagem_clicks.pack()

botao_menos = tk.Button(root, bg='#fff', text='-', font=('Montserrat', 16, 'bold'), padx=10, command=menos)
botao_menos.pack()

root.mainloop()