import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

conexion = sqlite3.connect("estudiantes.db")
cursor = conexion.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT NOT NULL,
carrera TEXT NOT NULL,
nota REAL NOT NULL)
""")
conexion.commit()

COLOR_FONDO="#eef2f7"; COLOR_BARRA="#1f3b73"; FUENTE=("Segoe UI",11); FT=("Segoe UI",18,"bold")

def leer():
    for i in tabla.get_children(): tabla.delete(i)
    cursor.execute("SELECT * FROM estudiantes")
    for r in cursor.fetchall(): tabla.insert("",tk.END,values=r)

def limpiar():
    for e in (entry_nombre,entry_carrera,entry_nota):
        e.delete(0,tk.END)

def agregar():
    try:
        cursor.execute("INSERT INTO estudiantes(nombre,carrera,nota) VALUES(?,?,?)",
                       (entry_nombre.get(),entry_carrera.get(),float(entry_nota.get())))
        conexion.commit(); leer(); limpiar()
    except:
        messagebox.showerror("Error","Datos inválidos")

def editar():
    s=tabla.focus()
    if not s: return
    i=tabla.item(s)["values"][0]
    try:
        cursor.execute("UPDATE estudiantes SET nombre=?,carrera=?,nota=? WHERE id=?",
        (entry_nombre.get(),entry_carrera.get(),float(entry_nota.get()),i))
        conexion.commit(); leer(); limpiar()
    except: messagebox.showerror("Error","Datos inválidos")

def eliminar():
    s=tabla.focus()
    if not s:return
    i=tabla.item(s)["values"][0]
    cursor.execute("DELETE FROM estudiantes WHERE id=?",(i,))
    conexion.commit(); leer(); limpiar()

def sel(e):
    s=tabla.focus()
    if s:
        v=tabla.item(s)["values"]; limpiar()
        entry_nombre.insert(0,v[1]); entry_carrera.insert(0,v[2]); entry_nota.insert(0,v[3])

v=tk.Tk()
v.title("Sistema de Estudiantes")
v.geometry("700x520")
v.configure(bg=COLOR_FONDO)

style=ttk.Style(); style.theme_use("clam")
style.configure("Treeview",font=("Segoe UI",10),rowheight=28)
style.configure("Treeview.Heading",font=("Segoe UI",11,"bold"),background=COLOR_BARRA,foreground="white")

tk.Label(v,text="Sistema de Gestión de Estudiantes",font=FT,bg=COLOR_FONDO,fg=COLOR_BARRA).grid(row=0,column=0,columnspan=3,pady=15)

tk.Label(v,text="Nombre",bg=COLOR_FONDO,font=FUENTE).grid(row=1,column=0)
entry_nombre=tk.Entry(v,font=FUENTE); entry_nombre.grid(row=1,column=1)

tk.Label(v,text="Carrera",bg=COLOR_FONDO,font=FUENTE).grid(row=2,column=0)
entry_carrera=tk.Entry(v,font=FUENTE); entry_carrera.grid(row=2,column=1)

tk.Label(v,text="Nota",bg=COLOR_FONDO,font=FUENTE).grid(row=3,column=0)
entry_nota=tk.Entry(v,font=FUENTE); entry_nota.grid(row=3,column=1)

f=tk.Frame(v,bg=COLOR_FONDO); f.grid(row=4,column=0,columnspan=3,pady=10)
for t,c,cmd,col in [("Agregar","#2e8b57",agregar,0),("Editar","#1f77b4",editar,1),("Eliminar","#c0392b",eliminar,2),("Actualizar","#555",leer,3)]:
    tk.Button(f,text=t,bg=c,fg="white",font=FUENTE,relief="flat",width=12,command=cmd).grid(row=0,column=col,padx=5)

tabla=ttk.Treeview(v,columns=("ID","Nombre","Carrera","Nota"),show="headings",height=12)
for c,w in [("ID",50),("Nombre",180),("Carrera",220),("Nota",80)]:
    tabla.heading(c,text=c); tabla.column(c,width=w)
tabla.grid(row=5,column=0,columnspan=3,sticky="nsew",padx=10,pady=10)
tabla.bind("<<TreeviewSelect>>",sel)
leer()
v.mainloop()
