#!/usr/bin/env python3

import socket

SERVER_ADDRESS= '127.0.0.1'
SERVER_PORT= 22224

def invia_comandi(sock_service):
         while True:
        primoNumero=input("Inserisci il primo numero. exit() per uscire")
        if primoNumero=="exit()":
            break
        primoNumero=float(primoNumero)
        operazione=input("Inserisci l'operazione (+,-,*,/,%)")
        secondoNumero=float(input("Inserisci il secondo numero"))
        messaggio={'primoNumero':primoNumero,
        'operazione':operazione,
        'secondoNumero':secondoNumero}
        messaggio=json.dumps(messaggio)
        s.sendall(messaggio.encode("UTF-8"))
        data=s.recv(1024)
        print("Risultato: ",data.decode())

def connessione_server(address, port):
    sock_service = socket.socket()
    sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
    print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
    invia_comandi(sock_service)

if __name__=='__main__':
    connessione_server(SERVER_ADDRESS, SERVER_PORT)
