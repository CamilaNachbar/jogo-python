#!/usr/bin/python
#
# CODE BY: Camila Stefani Nachbar
# Fatec Carapicuiba - Desenvolvimento de Jogos Digitais
#
# Servidor de Mensagens: jogo adivinhe o número
# Módulo 2 - Redes
#
import socket
import os

s = socket.socket()
host = socket.gethostname()
port = 12221
s.connect((host, port))
os.system("cls")
print("Conectado com:", host)
print("Bem vindo ao jogo de adivinhe o numero! by: Camila Nachbar")
while True:
   
    q = input("[Digite um número........:] ")
    bytes_text = bytes(q, 'utf-8')
    s.send(bytes_text)
    msg = s.recv(1024)
    print("[Resposta.........]", msg.decode("utf-8"))


