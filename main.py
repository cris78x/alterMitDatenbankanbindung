import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mariadb

conn = mariadb.connect(
    user="projekt",
    password="admin123",
    host="localhost",
    port=3306,
    database="schlumpfshop3"
)

cur = conn.cursor()

def anrede_hinz():
    anrede = entry.get()
    if anrede:
        cur.execute("INSERT INTO Anrede (Anrede) VALUES (?)", (anrede,))
        conn.commit()
        messagebox.showinfo("Erfolg", f"Anrede '{anrede}' wurde erfolgreich hinzugefügt!")
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Bitte eine Anrede eingeben!")

def update_listbox():
    listbox.delete(0, tk.END)
    cur.execute("SELECT Anrede FROM Anrede")
    anreden = cur.fetchall()
    for anrede in anreden:
        listbox.insert(tk.END, anrede[0])

fenster = tk.Tk()
fenster.title("Verwalter")
fenster.geometry("800x600")

entry = ttk.Entry(fenster, width=40)
entry.pack(pady=10)

add_button = ttk.Button(fenster, text="Anrede Hinzufügen", width=20, command=anrede_hinz)
add_button.pack(pady=5)

listbox = tk.Listbox(fenster, width=40, height=10, bg="pink")
listbox.pack(pady=10)

update_listbox()
fenster.mainloop()

cur.close()
conn.close()
