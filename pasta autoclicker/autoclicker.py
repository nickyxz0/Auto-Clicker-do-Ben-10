import customtkinter as ctk
from PIL import Image
import pyautogui
import keyboard
import threading
import time
import os



# Configurações

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

clicando = False



# Auto Click

def autoclick():
    global clicando

    while True:
        if clicando:
            try:
                cps = float(entry_cps.get())
                if cps <= 0:
                    cps = 10
            except:
                cps = 10

            pyautogui.click()
            time.sleep(1 / cps)

        else:
            time.sleep(0.01)



# Botões

def iniciar():
    global clicando
    clicando = True
    status.configure(
        text="Status: LIGADO",
        text_color="lime"
    )


def parar():
    global clicando
    clicando = False
    status.configure(
        text="Status: DESLIGADO",
        text_color="red"
    )



# Tecla F6

def tecla():
    while True:
        keyboard.wait("F6")

        if clicando:
            parar()
        else:
            iniciar()



# Janela

janela = ctk.CTk()

janela.title("Ben 10 Auto Clicker")
janela.geometry("400x300")
janela.resizable(False, False)



# Imagem de fundo

caminho = "ben10.jpg"

if os.path.exists(caminho):

    imagem = ctk.CTkImage(
        Image.open(caminho),
        size=(400, 300)
    )

    fundo = ctk.CTkLabel(
        janela,
        image=imagem,
        text=""
    )

    fundo.place(
        x=0,
        y=0,
        relwidth=1,
        relheight=1
    )



# Interface

titulo = ctk.CTkLabel(
    janela,
    text="BEN 10 AUTO CLICKER",
    font=("Arial", 15, "bold"),
    fg_color="transparent"
)

titulo.pack(pady=15)


entry_cps = ctk.CTkEntry(
    janela,
    width=200,
    placeholder_text="Cliques por segundo"
)

entry_cps.insert(0, "10")

entry_cps.pack(pady=10)



botao_iniciar = ctk.CTkButton(
    janela,
    text="INICIAR",
    width=200,
    fg_color="green",
    command=iniciar
)

botao_iniciar.pack(pady=5)



botao_parar = ctk.CTkButton(
    janela,
    text="PARAR",
    width=200,
    fg_color="red",
    command=parar
)

botao_parar.pack(pady=5)



status = ctk.CTkLabel(
    janela,
    text="Status: DESLIGADO",
    text_color="red",
    font=("Arial",14,"bold"),
    fg_color="transparent"
)

status.pack(pady=10)



info = ctk.CTkLabel(
    janela,
    text="Atalho: F6 liga/desliga",
    fg_color="transparent"
)

info.pack()




# Threads

threading.Thread(
    target=autoclick,
    daemon=True
).start()


threading.Thread(
    target=tecla,
    daemon=True
).start()



# Rodar

janela.mainloop()