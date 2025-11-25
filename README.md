# Calculadora de IMC em Python (Tkinter)

Este repositório foi desenvolvido para auxiliar alunos iniciantes no aprendizado de **Python**, no uso da biblioteca **Tkinter**, e também para treinar como **subir o primeiro projeto no GitHub**.

## Objetivo do projeto
O programa permite que o usuário digite seu **peso** e **altura**, e o sistema calcula automaticamente o **IMC**, exibindo também a *classificação* correspondente (abaixo do peso, normal, sobrepeso ou obesidade).

O código também foi criado para que os alunos pratiquem:
- Estruturas básicas em Python  
- Manipulação de funções  
- Tratamento de erros  
- Criação de interfaces gráficas com Tkinter  
- Como subir um projeto no GitHub  

---

## Como executar o projeto

### 1. **Pré-requisitos**
Certifique-se de ter o **Python 3** instalado.  
Confira com:
python --version



### 2. **Baixar ou clonar o repositório**
Via Git:
git clone <link-do-repositorio>



Ou baixe o ZIP pelo GitHub e extraia os arquivos.

### 3. **Executar o programa**
No terminal, navegue até a pasta do projeto e execute:
python app.py


*(Substitua `app.py` pelo nome correto do arquivo, se for diferente.)*

---

## Como usar a calculadora

1. Abra o programa.  
2. Digite seu **peso em kg**.  
3. Digite sua **altura em metros**.  
4. Clique no botão **Calcular IMC**.  
5. Veja o resultado exibido na tela.

### ❗ Atenção ao digitar a altura:
Use **ponto** ao invés de vírgula.  
Exemplo correto:
1.76


Exemplo incorreto:
1,76


Python não reconhece vírgula como separador decimal.

![Calculadora](https://github.com/user-attachments/assets/1adc7d87-5d42-4e75-864f-5bf5a0badcb7)


---

## Estrutura do código

O arquivo principal contém:
- Interface gráfica com Tkinter  
- Entrada de dados com `Entry`  
- Botão para cálculo do IMC  
- Lógica de classificação  
- Tratamento de erros com `messagebox`  

---

## Praticando o uso do GitHub

Este exercício também serve para treinar como **subir um projeto no GitHub**.

### Passo a passo para enviar o projeto:

1. Crie um repositório no GitHub.  
2. No terminal, dentro da pasta do projeto, execute:

git init
git add .
git commit -m "Primeiro commit do projeto IMC"
git branch -M main
git remote add origin <url-do-repositorio>
git push -u origin main

shell
Copiar código

### Atualizar o repositório após mudanças:
git add .
git commit -m "Descrição do que foi atualizado"
git push



---

## Aprendizados envolvidos

Este projeto trabalha:
- Tkinter (Labels, Buttons, Entry, janela)  
- Funções e condicionais  
- F-strings  
- Try/except  
- Comandos básicos do Git e GitHub  

---

## Contribuições

Os alunos podem melhorar:
- Interface do programa  
- Validação dos campos  
- Novas funcionalidades (histórico, reset, tema escuro etc.)


---

## Contato

Em caso de dúvidas abra uma *Issue* aqui no repositório.

---

#### Deixe uma ⭐ e obrigado por utilizar este projeto para aprender Python e GitHub!
