from tkinter import *
from tkinter import filedialog
from io import open

rota = ""

def novo():
    global rota
    texto_rodape.set("Novo arquivo...")
    rota = ""
    #desde o caracter um até o final do texto
    texto.delete(1.0, END)
    root.title(rota + " - Editor de texto")
def abrir():
    global rota
    texto_rodape.set("Abrir arquivo...")
    rota = filedialog.askopenfilename(
        initialdir='.', 
        filetypes=(("Arquivos de texto", "*.txt"),), 
        title="Abrir um arquivo de texto")
        
    if rota != "":
        arquivo = open(rota, "r")
        conteudo = arquivo.read()
        texto.delete(1.0,END)
        texto.insert('insert', conteudo)
        arquivo.close()
        root.title(rota + " - Editor de texto")
        
def guardar():
    texto_rodape.set("Guardar arquivo...")
    if rota != "":
        conteudo = texto.get(1.0, 'end-1c')
        arquivo = open(rota, "w+")
        arquivo.write(conteudo)
        arquivo.close()
        texto_rodape.set("Arquivo guardado corretamente...")
    else:
        guardar_como()

def guardar_como():
    global rota
    texto_rodape.set("Guardar arquivo como...")
    arquivo = filedialog.asksaveasfile(title="Guardar como", mode="w", defaultextension=".txt")
    if arquivo is not None:
        rota = arquivo.name
        conteudo = texto.get(1.0, 'end-1c')
        arquivo = open(rota, "w+")
        arquivo.write(conteudo)
        arquivo.close()
        texto_rodape.set("Arquivo guardado corretamente...")
    else:
        texto_rodape.set("Arquivo não guardado...")
        rota = ""

root = Tk()
root.title("Editor de texto")
fonte_global = ("Verdana", 10)
icon_editor = PhotoImage(file="img/note.png")
root.iconphoto(True, icon_editor)

#menu superior
menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Novo", command=novo, font=fonte_global)
file_menu.add_command(label="Abrir", command=abrir, font=fonte_global)
file_menu.add_separator()
file_menu.add_command(label="Guardar", command=guardar, font=fonte_global)
file_menu.add_command(label="Guardar como", command=guardar_como, font=fonte_global)
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.quit, font=fonte_global)
menubar.add_cascade(menu=file_menu, label="Arquivo", font=fonte_global)

#caixa de edicao de texto
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=10, pady=10,font=fonte_global)

#rodape
texto_rodape = StringVar()
texto_rodape.set("Bem-vindo ao editor de texto...")
monitor_rodape = Label(root, textvariable=texto_rodape, font=fonte_global)
monitor_rodape.pack(side="left")

root.config(menu=menubar)
root.mainloop()