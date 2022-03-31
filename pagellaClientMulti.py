import socket
import sys
import random
import os
import time
import threading
import multiprocessing
import json
import pprint

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
NUM_WORKERS=4

#Versione 1 
def genera_richieste1(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()

    #1. Generazione casuale:
    studenti=['Studente0', 'Studente1','Studente2', 'Studente3','Studente4',]
    materie=['Matematica','Italia','Inglese','Storia e Geografia']
    voto=random.randint(1,10)
    assenze=random.randint(1,5)
    materia=materie[random.randint(0,3)]
    studente=studente=studenti[random.randint(0,4)]

    #2. comporre il messaggio, inviarlo come json
    messaggio={
        'studente':studente,
        'materia':materia,
        'assenze':assenze,
        'voto':voto,
    }
    print(f"Dati inviati al server {messaggio}")
    messaggio=json.dumps(messaggio)
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    data=data.decode()
    data=json.loads(data)
    print(f"Dati ricevuti dal server {data}")

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        studente=data['studente']
        materia=data['materia']
        print(f"{threading.current_thread().name}: La valutazione di {data['studente']} in {data['materia']} è {data['valutazione']}")
    s.close()


#Versione 2 
def genera_richieste2(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"\n{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()


  #   1. Generazione casuale di uno studente(valori ammessi: 5 cognomi a caso scelti da una lista)
    studenti=['Studente0', 'Studente1','Studente2', 'Studente3','Studente4',]
    materie=['Matematica','Italia','Inglese','Storia e Geografia']
    studente=studenti[random.randint(0,4)]
    pagella=[]
    for m in materie:
        voto=random.randint(1,10)
        assenze=random.random(1,5)
        pagella.append((m, voto, assenze))



  #2. comporre il messaggio, inviarlo come json
    messaggio={
        'studente':studente,
        'pagella':pagella}
    print(f"Dati inviati al server {messaggio}")
    messaggio=json.dumps(messaggio)
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    data=data.decode()
    data=json.loads(data)
    print(f"Dati ricevuti dal server {data}")

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        print(f"{threading.current_thread().name}:Lo studente {data['studente']} ha una media di: {data['media']:.2f} e un totale di assenze: {data['assenze']} ")
    s.close()


#Versione 3
def genera_richieste3(num,address,port):
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} {num+1}) Connessione al server: {address}:{port}")
    except:
        print(f"\n{threading.current_thread().name} Qualcosa è andato storto, sto uscendo... \n")
        sys.exit()
    
    studenti=['Studente0', 'Studente1','Studente2', 'Studente3','Studente4',]
    materie=['Matematica','Italia','Inglese','Storia e Geografia']
    studente=studenti[random.randint(0,4)]
    tabellone={}
    for stud in studenti:
        pagella=[]
        for m in materie:
            voto=random.randint(1,10)
            assenze=random.random(1,5)
            pagella.append((m, voto, assenze))
        tabellone[stud]=pagella


    print("Dati inviati al server")
    pp=pprint.PrettyPrinter(indent=4)
    pp.pprint(tabellone)
    tabellone=json.dumps(tabellone)
    s.sendall(tabellone.encode("UTF-8"))
    data=s.recv(1024)
    data=data.encode()
    data=json.loads(data)
    print("Dati ricevuti dal server")
    pp.pprint(data)

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        for elemento in data:
            print(f"{threading.current_thread().name}:Lo studente {elemento['studente']} ha una media di: {elemento['media']:.2f} e un totale di assenze: {elemento['assenze']} ")
    s.close()


if __name__ == '__main__':
    start_time=time.time()
    # PUNTO A) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)
    # alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
     
    start_time=time.time()
    threads=[]
    # PUNTO B) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)  
    # tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i thread e attenderne la fine
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    process=[]
    # PUNTO C) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3) 
    # tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i processi e attenderne la fine
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)
    start_time=time.time()
    # PUNTO A) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)
    for i in range(NUM_WORKERS):
        genera_richieste1(i,SERVER_ADDRESS,SERVER_PORT)
    # alla quale passo i parametri (num,SERVER_ADDRESS, SERVER_PORT)
    end_time=time.time()
    print("Total SERIAL time=", end_time - start_time)
        
    start_time=time.time()
    threads=[]
    # PUNTO B) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3)  
    # tramite l'avvio di un thread al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i thread e attenderne la fine
    end_time=time.time()
    print("Total THREADS time= ", end_time - start_time)

    start_time=time.time()
    process=[]
    # PUNTO C) ciclo per chiamare NUM_WORKERS volte la funzione genera richieste (1,2,3) 
    # tramite l'avvio di un processo al quale passo i parametri args=(num,SERVER_ADDRESS, SERVER_PORT,)
    # avviare tutti i processi e attenderne la fine
    end_time=time.time()
    print("Total PROCESS time= ", end_time - start_time)