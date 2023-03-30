#!/usr/bin/env python
import cgi
import cgitb
import os
import datetime

# Define o local do arquivo de mensagens
MESSAGE_FILE = "mensagens.txt"

# Habilita a exibição de informações de depuração em caso de erros
cgitb.enable()

# Define o cabeçalho HTTP para exibir uma página HTML
print("Content-Type: text/html\n\n")

# Processa os dados enviados pelo formulário
form = cgi.FieldStorage()
autor = form.getvalue("autor")
mensagem = form.getvalue("mensagem")

# Se o autor e a mensagem forem definidos, armazena-os no arquivo de mensagens
if autor and mensagem:
    with open(MESSAGE_FILE, "a") as f:
        data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        f.write(f"{data} - {autor}: {mensagem}\n")
    print("<p>Mensagem enviada com sucesso!</p>")

# Exibe o formulário de envio de mensagens
print("""
<html>
  <head>
    <title>Meu blog</title>
  </head>
  <body style="background-color: black; color: white; font-size: 24px">
    <div style="display: flex; justify-content: center"; gap:"5px">
      <form method="post" action="/cgi-bin/blog.py">
        <h1>Meu blog</h1>
        <label for="autor">Autor:</label><br />
        <input type="text" id="autor" name="autor" /><br />
        <label for="mensagem">Mensagem:</label><br />
        <textarea id="mensagem" name="mensagem"></textarea><br />
        <button type="submit">Enviar</button>
      </form>
    </div>
    <h2>Mensagens</h2>
""")


linhas = []

# Exibe as mensagens armazenadas no arquivo de mensagens
if os.path.exists(MESSAGE_FILE):
    with open(MESSAGE_FILE, "r") as f:
        for linha in f:
            linhas.insert(0, f"<p>{linha.strip()}</p>")
            # print(f"<p>{linha.strip()}</p>")

for linha in linhas:
    print(linha)

print("""
  </body>
</html>
""")