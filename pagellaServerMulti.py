import socket
from threading import Thread
import json


SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225

#Versione 1 
def ricevi_comandi1(sock_service,addr_client):
    while True:
        data=sock_service.recv(1024)
        if not data: 
                break
        data=data.decode()
        data=json.loads(data)     

        #1. recuperare dal json studente, materia, voto e assenze
        studente=data['studente']
        materia=data['materia']
        assenza=data['assenza']
        voto=data['voto']
        ris=""
       
        
        #2. restituire un messaggio in json contenente studente, materia e una valutazione testuale :
        # voto < 4 Gravemente insufficiente
        # voto [4..5] Insufficiente
        # voto = 6 Sufficiente
        # voto = 7 Discreto 
        # voto [8..9] Buono
        # voto = 10 Ottimo
    if voto <4:
         ris="Gravemente insufficiente"
         
    elif voto>=4 and voto<=5:
         ris="Insufficiente"

    elif voto==6:
         ris="Sufficiente"

    elif voto==7:
         ris="Discreto"

    elif voto>=8 and voto<=9:
         ris="Buono"

    else:
         ris="Ottimo"


    sock_service.sendall(messaggio.encode("UTF-8"))

    sock_service.close()

#Versione 2 
def ricevi_comandi2(sock_service,addr_client):
  #....
  #1.recuperare dal json studente e pagella
  studente=data['studente']
  pagella=data['pagella']

  #2. restituire studente, media dei voti e somma delle assenze :


#Versione 3
def ricevi_comandi3(sock_service,addr_client):
    pass
  #....
  #1.recuperare dal json il tabellone
  #2. restituire per ogni studente la media dei voti e somma delle assenze :
    studente=""
    studente=random.randint(0,5)
    if studente==0:
     studente="Rossi"

    elif studente==1:
        studente="Garavaglia"

    elif studente==2:
        studente="Grolla"

    elif studente==3:
        studente="Colombo"

    else:
        studente="Bianchi"

    materia=""
    materia=random.randint(0,5)
    if materia==0:
     materia="Matematica"

    elif materia==1:
        materia="Italiano"

    elif materia==2:
        materia="Inglese"

    elif materia==3:
        materia="Storia"

    else:
        materia="Geografia"
    
    voto=random.randint(1,10)
    assenza=random.randint(0,5)


def ricevi_connessioni(sock_listen):
        while True:
            sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da " + str(addr_client))
        print("\nCreo un thread per servire le richieste ")
        try:
            Thread(target=ricevi_comandi1,args=(sock_service,addr_client)).start()
        except:
            print("il thread non si avvia")
            sock_listen.close()
        
def avvia_server(SERVER_ADDRESS,SERVER_PORT):
    sock_listen=socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock_listen.bind((SERVER_ADDRESS,SERVER_PORT))
    sock_listen.listen(5)
    print("Server in ascolto su %s." %str((SERVER_ADDRESS,SERVER_PORT)))
    ricevi_connessioni(sock_listen)

if __name__=='__main__':
    avvia_server(SERVER_ADDRESS,SERVER_PORT)