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

    
    #   di uno studente (valori ammessi: 5 cognomi a caso tra cui il tuo cognome)
    studenti = [['Rossi'],['Garavaglia'],['Grolla'],['Colombo'],['Bianchi']];
    print(studenti);
    for studente in studenti:
     print(studente);

    #   di una materia (valori ammessi: Matematica, Italiano, inglese, Storia e Geografia)
    materia  = [['Matematica'], ['Italiano'], ['Inglese'], ['Storia'], ['Geografia']];
    for materia in materia:
     print(materia);

    #   di un voto (valori ammessi 1 ..10)
     voto  = [['1'], ['1.5'], ['2'], ['2.5'], ['3'], ['3.5'], ['4'], ['4.5'], ['5'], ['5.5'], ['6'], ['6.5'], ['7'], ['7.5'], ['8'], ['8.5'], ['9'], ['9.5'], ['10']];
    for voti in voto:
     print(voto);

    #   delle assenze (valori ammessi 1..5)
     assenza = [['1'], ['2'], ['3'], ['4'], ['5']];
    for assenze in assenza:
     print(assenza);
    
    #2. comporre il messaggio, inviarlo come json
    #   esempio: {'studente': 'Studente4', 'materia': 'Italiano', 'voto': 2, 'assenze': 3}
    messaggio={
        'studente':studente,
        'materia':materia,
        'assenza':assenza,
        'voto':voto,
    }
    messaggio=json.dumps(messaggio)

    #3. ricevere il risultato come json: {'studente':'Studente4','materia':'italiano','valutazione':'Gravemente insufficiente'}

    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        #4 stampare la valutazione ricevuta esempio: La valutazione di Studente4 in italiano è Gravemente insufficiente
        print("La valutazione dello studente: " + studente, "in" + materia,  "è" + voto, data.decode())
        s.close()

#Versione 2 
def genera_richieste2(num,address,port):
  #....
  #   1. Generazione casuale di uno studente(valori ammessi: 5 cognomi a caso scelti da una lista)
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: pagella={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9.5,3), ("Storia",8,2), ("Geografia",8,1)]}
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

  #2. comporre il messaggio, inviarlo come json
    messaggio={
        'studente':studente,
        'materia':materia,
        'assenza':assenza,
        'voto':voto,
    }
    messaggio=json.dumps(messaggio)
  #3  ricevere il risultato come json {'studente': 'Cognome1', 'media': 8.0, 'assenze': 8}
    if not data:
        print(f"{threading.current_thread().name}: Server non risponde. Exit")
    else:
        print("Studente: " + 'studente: ' + studente, 'media: ' + voto/5, 'assenza: ' + assenza, data.decode())
        s.close()


#Versione 3
def genera_richieste3(num,address,port):
    pass
  #....
  #   1. Per ognuno degli studenti ammessi: 5 cognomi a caso scelti da una lista
  #   Per ognuna delle materie ammesse: Matematica, Italiano, inglese, Storia e Geografia)
  #   generazione di un voto (valori ammessi 1 ..10)
  #   e delle assenze (valori ammessi 1..5) 
  #   esempio: tabellone={"Cognome1":[("Matematica",8,1), ("Italiano",6,1), ("Inglese",9,3), ("Storia",8,2), ("Geografia",8,1)],
  #                       "Cognome2":[("Matematica",7,2), ("Italiano",5,3), ("Inglese",4,12), ("Storia",5,2), ("Geografia",4,1)],
  #                        .....}

  #2. comporre il messaggio, inviarlo come json


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