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
s.bind((host, port))
s.listen(5)

from random import *
rdn = randint(1, 20)
tent = 3

print("[Aguardando por conexao...]")
c, addr = s.accept()
os.system("cls")
print("Conectado com:", addr)
while tent > 0:  
    while True:
        msg = c.recv(1024)

        if int(msg) > rdn:
                bytes_text = bytes('Errou, numero é menor!', 'utf-8')
                c.send(bytes_text)
        elif int(msg) < rdn:
                bytes_text = bytes('Errou, numero é maior!', 'utf-8')
                c.send(bytes_text)
        elif int(msg)  == rdn:             
                bytes_text = bytes('Parabéns! Você acertou!', 'utf-8')
                c.send(bytes_text)
        else:
                bytes_text = bytes('Digite um valor valido', 'utf-8')
                c.send(bytes_text)   
        if tent == 0:
                bytes_text = bytes('Que pena! Você perdeu! Mais sorte da próxima vez!', 'utf-8')
                c.send(bytes_text)
        tent = tent - 1
if (msg == 'cls') or (msg == 'CLS'):
        os.system("cls")
        print("Conectado com:", addr)
        q = input("[Jogo terminado, reinicie........:] ")
bytes_text = bytes(q, 'utf-8')
c.send(bytes_text)
