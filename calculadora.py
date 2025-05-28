import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso /(altura **2)
        resultado = f"Seu IMC é:{imc:.2f}\n"

        if imc < 18.5:
            resultado += "Classificação: Abaixo do peso"
        elif 18.5 <= imc <25:
            resultado += "Classificação: Peso normal"
        elif 25 <= imc <30:
            resultado += "Classificação: Sobrepeso"
        else:
            resultado += "Clasiificação: Obesidade"

        label_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Error, Por favor, tente novamente")

janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x250")
janela.configure(bg="#f0f0f0")

tk.Label(janela, text="Peso (kg):"
         ,bg="#f0f0f0").pack(pady=5)
entry_peso = tk.Entry(janela)
entry_peso.pack()

tk.Label(janela, text="Altura (m):"
         ,bg="#f0f0f0").pack(pady=5)
entry_altura = tk.Entry(janela)
entry_altura.pack()

tk.Button(janela, text ="Calcular IMC",
          command=calcular_imc).pack(pady=10)

label_resultado = tk.Label(janela, text="",
                           bg="#f0f0f0", font=("Arial",10))
label_resultado.pack()

janela.mainloop()